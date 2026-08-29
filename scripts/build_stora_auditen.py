#!/usr/bin/env python3
"""Bygger STORA AUDITEN från BEVISREGISTER.md och TIDSLINJE.md.

Målet är inte att ersätta källgranskning utan att ge varje identifierad bevispost
samma obligatoriska kontrollfält. Poster som bara är metadata-/Outlook-återgivning
markeras för source-lock innan extern användning när sakuppgiften är omstridd.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "BEVISREGISTER.md"
TIMELINE = ROOT / "TIDSLINJE.md"
OVERRIDES = ROOT / "STORA-AUDITEN" / "OVERRIDES.json"
OUT = ROOT / "STORA-AUDITEN" / "01-BEVISPOSTER-KONTROLLPANEL.md"

ROW_RE = re.compile(
    r"^\|\s*(B\d{4})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$"
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\n", " ")).strip()


def actor_kind(actor: str, path: str) -> str:
    a = actor.lower()
    p = path.lower()
    if "miljoförvalt" in a or "miljoforvalt" in a or "miljoforvaltningen" in p:
        return "myndighet_miljo"
    if "stadsbygg" in a or "stadsbygg" in p:
        return "myndighet_pbl"
    if "länssty" in a or "lanssty" in a or "lanssty" in p:
        return "myndighet_overprovning"
    if "domstol" in a or "domstol" in p:
        return "domstol"
    if "familjebost" in a or "familjebost" in p or "gaby khalaf" in a or "jennifer ehlin" in a:
        return "hyresvard"
    if "hyresgastforeningen" in p or "hyresgästfören" in a or "hyresgastforen" in a:
        return "hgf"
    if "vittnen" in p:
        return "vittne"
    if "sakkunniga" in p or "entrepren" in p:
        return "sakkunnig"
    if "bostadsformed" in p or "bostad.stockholm" in a:
        return "bostadsformedling"
    if "erica" in a:
        return "part"
    return "ovrig"


def classify(typ: str, actor: str, path: str, fact: str) -> tuple[str, str]:
    t = typ.lower()
    f = fact.lower()
    k = actor_kind(actor, path)
    if any(x in t for x in ["foto", "bild", "ljud", "video", "rapport", "beslut", "protokoll", "handling"]):
        return "A/B", "PRIMÄR/KÄLLNÄRA – kontrollera filens originalstatus och metadata"
    if "outlook-export" in t:
        return "B", "KÄLLNÄRA OUTLOOK-EXPORT – kontrollerad återgivning; rå MIME/EML saknas normalt"
    if "outlook-återgivning" in t or "outlook-atergivning" in t:
        if k == "vittne":
            return "C", "SAMTIDA FÖRSTAHANDSUPPGIFT I E-POST – originalmejl bör source-lockas vid tvist"
        return "B/C", "KÄLLNÄRA E-POSTÅTERGIVNING – visar säkert kommunikationen, inte automatiskt sakförhållandets objektiva riktighet"
    if "sammanställ" in t or "transkript" in t:
        return "D", "SEKUNDÄR SAMMANSTÄLLNING/TRANSKRIPTION – ORIGINALKARANTÄN tills originalet är låst"
    if k == "vittne":
        return "C", "VITTNESUPPGIFT – förstahandsiakttagelse om det uttryckligen framgår"
    return "B/C", "KÄLLSTATUS BEHÖVER PRECISERAS MOT ORIGINAL"


def legal_and_function(kind: str, subject: str, fact: str, path: str) -> tuple[str, str]:
    text = f"{subject} {fact} {path}".lower()
    if kind == "myndighet_miljo":
        return (
            "MB 9 kap. 3 §; MB 26 kap. 19, 21–22 §§; FL 23, 25, 27, 32 §§ efter relevans",
            "Visar tillsynsärendets omfattning, myndighetens kunskap, utredningssteg, kommunicering eller beslut. Kan användas för att pröva om sakfrågan utretts i den omfattning ärendets beskaffenhet krävt.",
        )
    if kind == "myndighet_pbl":
        return (
            "PBL 8 kap. 25 §; PBF 5 kap. 1–7 §§; FL 23, 25, 27, 32 §§ efter relevans",
            "Visar PBL/OVK-tillsyn, vilka ventilationsuppgifter som finns registrerade och vad byggnadsnämnden faktiskt kontrollerat eller efterfrågat.",
        )
    if kind == "myndighet_overprovning":
        return (
            "Miljöbalkens överprövningsregler + FL:s rättssäkerhetsprinciper; exakt lagrum kontrolleras per beslut",
            "Visar vad som getts in till eller bedömts av överprövande myndighet samt processuell kunskapstidpunkt.",
        )
    if kind == "domstol":
        return (
            "Processuell bevisning och fri bevisvärdering; materiell rätt enligt MB/JB/PBL beroende på frågan",
            "Visar vad som faktiskt åberopats, kommunicerats eller beslutats i domstolsprocessen.",
        )
    if kind == "hyresvard":
        law = "JB 12 kap. 9 och 15 §§; vid påstådd brist även 12 kap. 11 och 16 §§ efter situation; MB 2 kap. 2–3 §§ och 26 kap. 19 § när miljöpåverkan är relevant"
        if any(w in text for w in ["ventilation", "ovk", "kanal", "luftflöde", "luftflode"]):
            law += "; PBL 8 kap. 25 § och PBF 5 kap. 1–7 §§ för OVK/funktionskontroll"
        return (
            law,
            "Visar hyresvärdens kunskap, ställningstagande, utfästelser, beställningar eller hänvisningar. Kan användas för att bedöma när brist påtalats och vilka åtgärder/underlag hyresvärden faktiskt redovisat.",
        )
    if kind == "part":
        return (
            "JB 12 kap. 9, 15 och 16 §§ efter situation; MB 9 kap. 3 § och tillsyn enligt 26 kap. MB när klagomålet gäller inomhusmiljö",
            "Visar när och hur klagomål, frågor, symtomuppgifter, begäran om handlingar eller invändningar framfördes. Är särskilt relevant för kunskapstidpunkt och om frågor lämnats obesvarade.",
        )
    if kind == "vittne":
        return (
            "Allmän bevisvärdering; materiell koppling främst JB 12 kap. och MB 9 kap. 3 § beroende på bevistema",
            "Kan styrka förstahandsiakttagelser om lukt, luft, synliga förhållanden, reaktioner och jämförelser. Flera oberoende uppgifter kan ge korroboration.",
        )
    if kind == "sakkunnig":
        return (
            "Beror på uppdraget; teknisk bevisning kan knytas till JB 12 kap., MB 9 kap./26 kap. och PBL/PBF",
            "Visar sakkunnigs/entreprenörs uppdrag, metod, observationer eller rekommendationer i den utsträckning detta faktiskt framgår av originalet.",
        )
    if kind == "hgf":
        return (
            "JB 12 kap. som materiell bakgrund; HGF-korrespondens är inte myndighetsbeslut",
            "Visar rådgivning, partsstöd och vad som kommunicerats via Hyresgästföreningen. Kan vara relevant för kronologi men har inte myndighetsstatus.",
        )
    if kind == "bostadsformedling":
        return (
            "Avtals-/informationsfrågor; exakt rättslig ram kontrolleras per bevistema",
            "Visar vilken information som efterfrågats eller lämnats om förmedling, besiktningsunderlag och transparens. Bevisar inte bostadens tekniska skick.",
        )
    return ("JURIDISK KONTROLL KRÄVS", "Kronologi/kommunikation. Juridisk funktion måste låsas mot bevistemat.")


def not_proves(kind: str, typ: str, fact: str) -> str:
    if kind == "part":
        return "Bevisar inte i sig att den tekniska orsaken eller den historiska sakuppgiften är objektivt fastställd; visar främst att uppgiften framfördes vid denna tidpunkt."
    if kind == "vittne":
        return "Bevisar inte ensam teknisk orsak, medicinsk diagnos eller exakt källa till lukt/luftpåverkan."
    if kind == "hyresvard":
        return "Bevisar inte att en teknisk uppgift är korrekt eller att en åtgärd faktiskt utförts fackmässigt om arbetsorder, utföranderapport eller mätdata saknas."
    if kind.startswith("myndighet"):
        return "Bevisar inte mer än vad myndigheten faktiskt undersökte, observerade eller beslutade. Ett begränsat tillsynstillfälle utesluter inte automatiskt andra/intermittenta förhållanden."
    if kind == "sakkunnig":
        return "Bevisar inte frågor utanför uppdragets omfattning och ska inte ges bredare räckvidd än metod, provtagning och slutsats medger."
    if kind == "hgf":
        return "Bevisar inte tekniskt skick eller myndighetsbedömning; rådgivning och partsstöd är inte ett oberoende tillsynsbeslut."
    if kind == "domstol":
        return "Att något getts in bevisar inte att domstolen har godtagit sakuppgiften som riktig."
    return "Bevisar inte automatiskt den bakomliggande sakuppgiftens objektiva riktighet eller tekniska orsak."


def missing(kind: str, typ: str, fact: str, path: str) -> str:
    t = typ.lower()
    text = f"{fact} {path}".lower()
    needs = []
    if "outlook" in t:
        needs.append("originalmejl/rå MIME eller ny kontroll i originalpostlådan vid omstritt citat")
    if any(w in text for w in ["kanalrens", "rensning", "utförd", "utford", "arbete", "åtgärd", "atgard"]):
        needs.append("beställning/arbetsorder/utföranderapport och effektkontroll")
    if any(w in text for w in ["ventilation", "ovk", "luftflöde", "luftflode"]):
        needs.append("originalprotokoll/mätblad, systemidentitet och metod/utförare")
    if any(w in text for w in ["brand", "sanering"]):
        needs.append("primär brand-/skade-/saneringsdokumentation och återställningskedja")
    if any(w in text for w in ["mögel", "mogel", "mikro", "fukt"]):
        needs.append("riktad teknisk undersökning/provtagning om slutsatsen ska gå längre än okulär observation")
    if kind == "vittne":
        needs.append("originalmejl/undertecknad redogörelse samt exakt besöksdatum; teknisk orsak kräver separat sakkunnigbevisning")
    if not needs:
        needs.append("sakgranska fulltexten och lås relevanta bilagor/svarskedjor innan extern användning")
    return "; ".join(dict.fromkeys(needs))


def track(subject: str, fact: str, path: str) -> str:
    text = f"{subject} {fact} {path}".lower()
    tracks = []
    rules = [
        (["brand", "sanering", "rök", "rok"], "1 Brand/sanering/återställning 2017"),
        (["ocab", "okab", "fukt", "missfärg", "golv", "kök", "kok"], "2 Tillträde/skick/OCAB/fukt"),
        (["lukt", "hälsa", "halsa", "andning", "huvudvärk", "inomhusmiljö", "inomhusmiljo"], "3 Inomhusmiljö/lukt/hälsoreaktioner"),
        (["ventilation", "ovk", "kanal", "luftflöde", "luftflode", "system 01", "60020562"], "4 Ventilation/kanalrensning/OVK"),
        (["familjebost", "gaby", "jennifer", "peter", "marko", "husvärd", "husvard"], "5 Familjebostäders kunskap/felsökning/åtgärder"),
        (["2025-23696", "miljoforvalt"], "6 Miljöförvaltningens tillsyn"),
        (["länssty", "lanssty"], "7 Länsstyrelsen"),
        (["m 5167-26", "domstol"], "8 Mark- och miljödomstolen"),
        (["2026-06369", "stadsbygg", "pbl"], "9 Stadsbyggnadskontoret/PBL"),
        (["diarie", "handling", "registr", "kommunic", "beslut", "fråga", "fraga"], "10 Dokumentation/diarieföring/process"),
        (["vittne", "thomas", "jimmy", "karolin"], "11 Vittneskedjan"),
        (["foto", "bild", "ljud", "video", "transkript"], "12 Foto/video/ljud/tekniska original"),
    ]
    for keys, name in rules:
        if any(k in text for k in keys):
            tracks.append(name)
    return "; ".join(dict.fromkeys(tracks)) if tracks else "10 Dokumentation/process – SAKSPÅR BEHÖVER PRECISERAS"


def timeline_status(bevis_id: str, timeline_text: str) -> str:
    return "HUVUDTIDSLINJE: JA" if bevis_id in timeline_text else "HUVUDTIDSLINJE: NEJ/INTE IDENTIFIERAD"


def external_status(typ: str, kind: str, fact: str) -> str:
    t = typ.lower()
    if "sammanställ" in t or "transkript" in t:
        return "ORIGINALKARANTÄN – EJ FÖR EXTERN ANVÄNDNING SOM ORIGINAL"
    if "outlook" in t:
        return "INTERN/KÄLLNÄRA – source-lock original vid omstritt ordagrant citat"
    if kind == "vittne":
        return "KAN ÅBEROPAS SOM VITTNESUPPGIFT; teknisk orsak kräver separat stöd"
    return "SAKGRANSKA ORIGINAL OCH RÄCKVIDD FÖRE EXTERN ANVÄNDNING"


def load_overrides() -> dict:
    if not OVERRIDES.exists():
        return {}
    return json.loads(OVERRIDES.read_text(encoding="utf-8"))


def main() -> None:
    reg_text = REGISTER.read_text(encoding="utf-8")
    timeline_text = TIMELINE.read_text(encoding="utf-8") if TIMELINE.exists() else ""
    overrides = load_overrides()

    rows = []
    for raw in reg_text.splitlines():
        m = ROW_RE.match(raw)
        if not m:
            continue
        bid, date, actor, typ, original, fact, checked = map(clean, m.groups())
        lm = LINK_RE.search(original)
        source_name = lm.group(1) if lm else original
        source_path = lm.group(2) if lm else ""
        kind = actor_kind(actor, source_path)
        bclass, source_status = classify(typ, actor, source_path, fact)
        law, function = legal_and_function(kind, source_name, fact, source_path)
        np = not_proves(kind, typ, fact)
        miss = missing(kind, typ, fact, source_path)
        tr = track(source_name, fact, source_path)
        tl = timeline_status(bid, timeline_text)
        ext = external_status(typ, kind, fact)

        row = {
            "id": bid,
            "datum": date,
            "källa": f"[{source_name}]({source_path})" if source_path else source_name,
            "faktisk uppgift": fact,
            "bevisklass": bclass,
            "juridisk funktion": function,
            "vad den inte bevisar": np,
            "saknad komplettering": miss,
            "relevant lag/princip": law,
            "status i huvudtidslinjen/spåren": f"{tl}; {tr}",
            "source-lock/extern status": f"{source_status}; {ext}; registerkontroll={checked}",
        }
        if bid in overrides:
            for k, v in overrides[bid].items():
                if v:
                    row[k] = v
        rows.append(row)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = """# STORA AUDITEN – BEVISPOSTER / KONTROLLPANEL\n\n**Genererad från:** `BEVISREGISTER.md` + `TIDSLINJE.md` + `STORA-AUDITEN/OVERRIDES.json`  \n**Styrning:** `00-HUVUDLAGER-STYRNING-OCH-BEVISSTANDARD.md`  \n\nDetta är **inte en sammanfattning**. Varje rad är en kontrollpost. Automatiskt genererade juridiska funktioner och kompletteringsbehov är arbetsklassningar och ska preciseras när originalfilen sakgranskas. En post med Outlook-återgivning visar kommunikationens existens och innehåll enligt den källnära exporten, men om ett ordagrant citat eller en omstridd sakuppgift ska användas externt ska originalet source-lockas.\n\n**Obligatorisk kedja:** datum → källa → faktisk uppgift → bevisklass → juridisk funktion → vad den inte bevisar → saknad komplettering → relevant lag/princip → status i huvudtidslinjen/spåren.\n\n"""
    cols = [
        "ID", "Datum", "Källa", "Faktisk uppgift", "Bevisklass", "Juridisk funktion",
        "Vad den inte bevisar", "Saknad komplettering", "Relevant lag/princip",
        "Status i huvudtidslinjen/spåren", "Source-lock / extern status"
    ]
    out = [header, "| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in rows:
        vals = [
            r["id"], r["datum"], r["källa"], r["faktisk uppgift"], r["bevisklass"],
            r["juridisk funktion"], r["vad den inte bevisar"], r["saknad komplettering"],
            r["relevant lag/princip"], r["status i huvudtidslinjen/spåren"], r["source-lock/extern status"],
        ]
        vals = [str(v).replace("|", "\\|").replace("\n", " ") for v in vals]
        out.append("| " + " | ".join(vals) + " |")

    out.append(f"\n**Antal identifierade bevisposter i kontrollpanelen: {len(rows)}.**\n")
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT} with {len(rows)} rows")


if __name__ == "__main__":
    main()
