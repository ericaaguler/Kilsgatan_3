# NORSTEDTS AI-RAPPORT 2025 – RELEVANS FÖR KILSGATAN 3 OCH MÖD-ÖVERKLAGANDE

**Datum:** 30 augusti 2026  
**Status:** METOD- OCH ARBETSFLÖDESSTÖD – INTE RÄTTSKÄLLA I SAKFRÅGAN

## 1. Slutsats

Norstedts Juridiks rapport `AI i juridiken – Möjligheter, risker och vägen framåt` är **relevant för projektets arbetsmetod**, men den är **inte rättsligt stöd för sakfrågorna i Kilsgatan 3** och ska inte åberopas i MÖD som lag, praxis eller doktrin om bostad, tillsyn, miljöbalk eller processrätt.

Rapportens praktiska värde ligger i att den beskriver hur jurister använder AI för:

- juridisk research,
- dokumentgranskning,
- informationsinsamling och sammanställning,
- textproduktion och struktur,
- argumentationsstöd,
- kvalitetssäkring,
- spårbarhet och mänsklig kontroll.

Rapporten varnar samtidigt för:

- faktafel,
- bias,
- bristande transparens,
- överdriven tilltro till AI,
- otillräcklig källförankring,
- bristande mänsklig granskning.

Detta ligger mycket nära projektets befintliga MASTERPROMPT och STORA AUDITEN.

## 2. Vad rapporten tillför vårt arbetssätt

### 2.1 Research
AI ska användas för att snabbt hitta relevanta rättskällor och skapa överblick, men varje rättsligt påstående ska verifieras mot aktuell primärkälla innan extern användning.

### 2.2 Dokumentgranskning
AI kan användas för att gå igenom stora dokumentmängder, hitta avvikelser och sammanställa material. I Kilsgatan 3 ska detta fortsatt ske dokument-för-dokument med source-lock, scope och bevisklass.

### 2.3 Textproduktion
AI får användas för att strukturera och skriva utkast till överklagandet, men får aldrig uppgradera en hypotes, användaruppgift, transkription eller sammanställning till verifierat faktum.

### 2.4 Human-in-the-loop
Varje slutlig juridisk slutsats ska bygga på:

`källa → aktuell rättsregel → rekvisit → verifierat faktum → tillämpning → slutsats`

Om länken inte kan följas ska slutsatsen markeras osäker.

### 2.5 Spårbarhet
För varje påstående i en extern inlaga ska det gå att svara på:

1. Varifrån kommer uppgiften?
2. Är originalkällan verifierad?
3. Vilken rättskälla stöder den juridiska regeln?
4. Är rättskällan aktuell och direkt tillämplig?
5. Vilken slutsats medger källan faktiskt?
6. Vad bevisar den inte?

## 3. Vad rapporten INTE får användas till

- Den får inte citeras som stöd för att Familjebostäder brutit mot jordabalken eller miljöbalken.
- Den får inte användas som stöd för prövningstillstånd i sig.
- Den får inte ersätta kontroll av lag, förordning, föreskrift, praxis eller förarbeten.
- Den får inte användas för att säga att en AI-bedömning är juridiskt korrekt därför att jurister använder AI.

## 4. Hur detta förbättrar “Överklagan kanske Erica”

Överklagandet ska genomgå fem separata kvalitetskontroller:

### Kontroll A – faktapåstående
För varje mening som beskriver vad som hände:
- ange primärkälla,
- verifiera datum,
- verifiera talare/avsändare,
- ange vad källan faktiskt visar,
- markera GRÖN/GUL/RÖD.

### Kontroll B – rättsregel
För varje lagpåstående:
- kontrollera aktuell SFS,
- kontrollera direkt tillämplighet,
- skilj lag från doktrin/vägledning,
- kontrollera om senare ändring/praxis påverkar regeln.

### Kontroll C – bevisräckvidd
För varje teknisk rapport, foto, mätning, vittnesuppgift eller e-post:
- vilket uppdrag/scope hade källan?
- vilken fråga kunde den besvara?
- vilken fråga kunde den inte besvara?
- används den bredare än metoden tillåter?

### Kontroll D – motpartsattack
För varje huvudargument:
- vad skulle FB/MF/LST/MMD invända?
- vilket motbevis finns?
- vilken del är inferens?
- vilken komplettering skulle göra argumentet starkare?

### Kontroll E – MÖD-relevans
Varje stycke i slutversionen ska märkas internt med minst en funktion:
- PT 39 § 1 – anledning att betvivla riktigheten,
- PT 39 § 2 – riktigheten kan inte bedömas utan prövning,
- återförvisningsskäl,
- konkret utredningslucka,
- processuell dokumentations-/kommuniceringsfråga,
- relevant bakgrund.

Om ett stycke inte fyller någon funktion ska det kortas eller tas bort.

---

# 5. ARBETSPROMPT – MÖD-ÖVERKLAGANDE KILSGATAN 3

Använd följande prompt som ett särskilt kvalitetslager när `Överklagan kanske Erica` granskas eller skrivs om.

```text
UPPGIFT

Du ska agera som en senior juridisk granskningsassistent inför ett överklagande till Mark- och miljööverdomstolen i mål M 5167-26.

Målet är INTE att skriva den mest dramatiska texten. Målet är att skriva den mest rättsligt träffsäkra, verifierbara och processuellt användbara överklagan som materialet medger.

HUVUDPRINCIP

AI är endast ett analys- och strukturstöd. Ingen juridisk slutsats får användas externt utan att den går att följa genom:

KÄLLA → RÄTTSREGEL → REKVISIT → VERIFIERAT FAKTUM → TILLÄMPNING → SLUTSATS.

Om kedjan brister ska påståendet markeras INTE VERIFIERAT eller JURIDISK BEDÖMNING – INTE FASTSLAGET FAKTUM.

1. BÖRJA MED PRÖVNINGSTILLSTÅNDET

Analysera varje huvudargument mot 39 § lagen om domstolsärenden.

Pröva särskilt:

A. 39 § 1 – finns konkret anledning att betvivla riktigheten av MMD:s slut?
B. 39 § 2 – går riktigheten verkligen att bedöma utan närmare prövning?

Knyt inte PT till allmän kritik. Knyt varje PT-grund till en konkret verifierad utrednings-, metod-, dokumentations- eller processlucka.

2. TESTA MMD:S BÄRANDE SLUTSATS

Utgå från domstolens slutsats att nämnden företagit den utredning och vidtagit de åtgärder som ärendets beskaffenhet har krävt.

Bygg en kontrollkedja:

PÅTALAT PROBLEM
→ VILKA UTREDNINGSFRÅGOR IDENTIFIERADES?
→ VILKA METODER ANVÄNDES?
→ VAD KUNDE METODERNA FAKTISKT BESVARA?
→ VAD VISAR RESULTATEN?
→ VILKA RELEVANTA FRÅGOR ÅTERSTOD?
→ VILKET KONKRET UNDERLAG GJORDE YTTERLIGARE TILLSYN OBEHÖVLIG?

Om en länk saknas ska du identifiera exakt vilken handling eller utredning som saknas.

3. HÅLL ISÄR ORSAK OCH UTREDNING

Överklagandet ska inte behöva bevisa att brand, VOC, mögel, ventilation eller någon annan teori är den faktiska orsaken.

Frågan är om det fanns ett tillräckligt underlag för att avsluta tillsynen trots att den tekniska orsaken inte var klarlagd.

Använd aldrig:
"denna omständighet bevisar att X orsakar besvären"
om underlaget bara visar att X är ett relevant utredningsspår.

4. GRANSKA VARJE KÄLLAS SCOPE

För varje:
- OCAB-rapport,
- ventilationsmätning,
- OVK,
- kontrollrapport,
- fotografi,
- vittnesuppgift,
- ljud/video,
- brandrapport,
- försäkringsuppgift,
- arbetsorder,

ska du ange:

A. Vad undersöktes?
B. Vad visades?
C. Vad undersöktes inte?
D. Vilken slutsats får källan bära?
E. Vilken bredare slutsats får den INTE bära?

5. GRANSKA FAMILJEBOSTÄDERS EGEN UTREDNINGSKEDJA

Familjebostäder uppgav att problemet skulle felsökas.

Identifiera därför:
- vilket uppdrag som kallades felsökning,
- vem som fick uppdraget,
- vilken fråga uppdraget skulle besvara,
- vilka orsaker som prövades,
- vilka resultat som dokumenterades,
- hur genomförda åtgärder följdes upp,
- och på vilket underlag problemet ansågs avhjälpt eller färdigutrett.

Skilj alltid mellan ÅTGÄRD och ORSAKSUTREDNING.

6. GRANSKA MF:S BESLUTSKEDJA

Kontrollera:
- FL 23 – utredningens omfattning,
- FL 27 – beslutsrelevanta muntliga uppgifter/observationer och dokumentation,
- FL 10 – partsinsyn,
- FL 25 – kommunicering,
- FL 32 – motivering,
- MB 26:21–22 – tillgängliga utredningsverktyg,
- MB 2:1–3 – bevisbörda/kunskap/försiktighet inom rätt regelkontext.

Påstå inte ett handläggningsfel förrän rekvisiten är verifierade.

7. BRAND- OCH SANERINGSSPÅRET

Håll följande isär:

VERIFIERAT:
- brandhändelsen,
- den information respektive aktör faktiskt har,
- vilka dokument som finns eller uttryckligen uppges saknas.

INTE AUTOMATISKT VERIFIERAT:
- att sanering inte genomfördes,
- att branden orsakar dagens problem,
- att dokument medvetet raderats.

Ställ i stället den dokumentbaserade frågan:
Vilken primär dokumentationskedja visar vad fastighetsägaren gjorde efter branden, med vilken metod och med vilket verifierat resultat?

8. TESTA MOTARGUMENT

För varje argument, skriv internt:
- starkaste motargumentet,
- svagheten i vårt underlag,
- motbevis,
- vilken handling som skulle lösa osäkerheten,
- om argumentet fortfarande bör vara med.

9. KAPA ALLT SOM INTE HJÄLPER MÖD

Varje avsnitt ska fylla minst en av följande funktioner:
- PT enligt 39 § 1,
- PT enligt 39 § 2,
- återförvisning,
- konkret utredningslucka,
- processuell brist,
- nödvändig bakgrund.

Om inte: korta eller stryk.

10. SLUTLIG RELEASE-GATE

Innan texten får kallas slutversion:
- verifiera alla citat mot original,
- verifiera alla datum,
- kontrollera samtliga lagrum mot aktuell SFS,
- kontrollera att rätt processlag används,
- separera händelser före och efter MF:s beslut 13 april,
- kontrollera att senare bevis inte tillskrivs myndigheten retroaktivt,
- kontrollera att tekniska slutsatser inte överstiger källans scope,
- markera varje huvudargument MYCKET STARKT / STARKT / MÖJLIGT / SVAGT / BÖR INTE ANVÄNDAS.

SLUTOUTPUT

Leverera:

A. Vilka 3–5 argument som är starkast för prövningstillstånd.
B. Vilka delar av nuvarande överklagande som ska strykas eller kortas.
C. Vilka formuleringar som överdriver bevisningen.
D. Vilka konkreta källor/bilagor som ska kopplas till varje huvudargument.
E. Vilka bevisluckor som fortfarande måste fyllas.
F. En reviderad överklagandeversion där varje stycke tjänar en tydlig processuell funktion.
```

---

# 6. Styrkegrad

**MYCKET STARKT METODSTÖD:** source-lock, mänsklig kontroll, källhänvisning, spårbarhet, dokumentgranskning och kvalitetssäkring.

**STARKT METODSTÖD:** använda AI för att hitta avvikelser, strukturera juridisk research och testa argument.

**BÖR INTE ANVÄNDAS SOM RÄTTSKÄLLA:** rapportens opinionsdata eller rekommendationer får inte föras in som stöd för att underinstanserna gjort rätt/fel i Kilsgatan 3.

## 7. Slutsats

Rapportens verkliga värde för Kilsgatan 3 är att den bekräftar en professionell arbetsprincip som projektet redan bör följa: AI kan göra stora mängder juridiskt material hanterbara, men slutprodukten måste vara källspårbar, transparent, kritiskt granskad och underställd mänskligt juridiskt omdöme.
