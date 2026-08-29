# AUDITFYND OCH OMISSION REGISTER – 29 AUGUSTI 2026

**Status:** AKTIVT REGISTER  
**Hör ihop med:** `analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md`

Detta register ska innehålla identifierade fall där `TIDSLINJE.md` saknar, förkortar, blandar ihop eller otillräckligt källhänvisar en relevant händelse eller uppgift.

---

## FYND 001 – Thomas saknas i huvudtidlinjen 7–11 november 2025

**Status:** `SAKNAS I HUVUDTIDSLINJE` / `PERSON SAKNAS`

**Källa:** `bevis/2025-11-07--2025-11-11-sms-thomas-infor-mote.md`

Källan visar bland annat:

- 7 november: Erica ber Thomas följa med som **”stöd, vittne”** inför Familjebostäders möte.
- Thomas accepterar.
- 8 november: Erica tackar Thomas efter en genomgång och skriver att han ”hittade fler brister”.
- 10 november: de planerar att ses före mötet den 11 november kl. 14.
- 11 november kl. 13: Erica skriver att de ses snart och tackar honom för att han kommer med; därefter skriver hon att hon väntar utanför hans port.

**Avgränsning:** SMS-kedjan stöder starkt planerat och omedelbart förestående deltagande men exakt fysisk närvaro under hela mötet ska vid behov source-lockas med ytterligare möteskälla.

**Auditåtgärd:** Händelserna ska bedömas för införande i `TIDSLINJE.md` med korrekt bevisstatus och utan att överdriva vad SMS-källan ensam visar.

---

## FYND 002 – Själva Familjebostäders möte 11 november 2025 saknas som händelse

**Status:** `SAKNAS I HUVUDTIDSLINJE`

`TIDSLINJE.md` innehåller bokningskedjan 7 november och ett mejl 11 november kl. 08:02, men därefter går tidslinjen vidare till 12 november utan en särskild post för själva platsmötet den 11 november kl. 14.

Detta är en allvarlig strukturell lucka eftersom senare separata spår hänvisar till vad som sades eller föreslogs vid detta möte.

**Auditåtgärd:** Själva mötet ska source-lockas från befintliga möteskällor innan innehållsposter förs in. Deltagare, uttalanden, förslag, observationer och åtgärdsbesked ska därefter registreras som separata eller tydligt strukturerade händelseuppgifter.

---

## FYND 003 – Jennifer Ehlins besked 12 december 2025 är materiellt underrepresenterat

**Status:** `FINNS MEN ÄR FÖR KORTFATTAD` / `ORDALYDELSE SAKNAS`

**Bevis-ID:** B0174  
**Källa:** `korrespondens/familjebostader/2025-12-12_1013_B0174_jennifer-ehlin_sv-kilsgatan-3-123-44-farsta-lgh-nr-1202.md`

`TIDSLINJE.md` beskriver i nuläget posten i huvudsak som att Jennifer skickade ett mejl med visst ämne.

Originalkällan innehåller däremot det materiellt viktiga beskedet:

> ”Vi ses den 17/12 kl 09:00. Jag tar med mig husvärd Peter.”
>
> ”Vi går igenom dina kvarvarande frågor då.”

Den citerade underliggande tråden visar dessutom att de kvarvarande frågorna omfattade brandhistorik, motstridiga uppgifter om brand, saneringsdokumentation och andra kvarstående brister.

**Auditåtgärd:** Huvudtidlinjen ska återge sakinnebörden och den centrala exakta formuleringen, inte bara mejlets existens/ämnesrad.

---

## FYND 004 – Mötet 17 december 2025 saknas som egen händelse i huvudtidlinjen

**Status:** `SAKNAS I HUVUDTIDSLINJE`

`TIDSLINJE.md` innehåller e-postposter 17 december men ingen tydlig egen post som registrerar Familjebostäders platsmöte i lägenheten som Jennifer bokade i B0174.

Detta är särskilt relevant eftersom Jennifer den 12 december uttryckligen skrev att de kvarvarande frågorna skulle gås igenom då. Om dessa frågor inte togs upp/besvarades under mötet är det en separat relevant händelse i dokumentations- och svarskedjan.

**Auditåtgärd:** Source-locka mötet 17 december och kontrollera exakt:

1. vilka som deltog,
2. vilka frågor som faktiskt behandlades,
3. vilka av de uttryckligen kvarvarande frågorna som inte behandlades,
4. vad som senare skrevs om det som inte hanns med,
5. vilka sakspår detta hör till, särskilt brand/sanering/dokumentation.

---

## FYND 005 – Huvudtidlinjens nuvarande princip riskerar att tappa bevisad sakinnebörd

**Status:** `STRUKTURELL AUDITBRIST`

`TIDSLINJE.md` anger att endast källbelagda händelser ska läggas in. Det är korrekt som huvudprincip, men flera källbelagda mejlposter är i nuläget automatiskt formulerade som endast:

> ”[Person] skickade e-post ... med ämnet ...”

Detta gör att juridiskt/faktiskt betydelsefull saktext kan finnas i originalbeviset men inte vara synlig i huvudtidlinjen.

**Auditåtgärd:** Vid PASS B ska varje mejl som rör ett relevant bevistema granskas för sakinnebörd. Ämnesrad räcker inte när meddelandet innehåller löfte, besked, fråga, svar, uteblivet svar, motsägelse, kännedom, planerad åtgärd eller dokumentationsuppgift.

---

## Nästa kontrollblock

Efter dessa initiala fynd ska auditten fortsätta systematiskt med:

- `BEVISREGISTER.md` ↔ `TIDSLINJE.md`,
- samtliga tidslinjekompletteringar ↔ `TIDSLINJE.md`,
- personkontroll,
- exakta formuleringar,
- uteblivna svar,
- brandspåret ↔ hela huvudmaterialet,
- därefter användarens nya anteckningar från 29 augusti 2026.
