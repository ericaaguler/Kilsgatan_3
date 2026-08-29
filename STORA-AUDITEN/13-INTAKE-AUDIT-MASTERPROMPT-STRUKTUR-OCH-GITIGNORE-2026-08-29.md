# 13. INTAKE-AUDIT – MASTERPROMPT, STRUKTUR OCH `.gitignore`

**Datum:** 29 augusti 2026  
**Status:** GENOMFÖRD INTAKE-AUDIT  
**Syfte:** kontrollera vad som tillkommit i arbetschatten men ännu inte varit fullt representerat i GitHub-strukturen och säkerställa att det inte kan tappas bort.

## 1. Resultat

### A. Ny masterprompt saknades helt som styrfil

**Fynd:** Den nya `MASTERPROMPT – JURIDISK AI-ANALYS MED KÄLLKONTROLL` fanns inte tidigare som separat styrande fil i repositoryt.

**Åtgärd:** skapad som:

`styrning/MASTERPROMPT-JURIDISK-AI-ANALYS-MED-KALLKONTROLL.md`

Den inför obligatoriskt:

- rättskällehierarki,
- aktualitetskontroll,
- strikt fakta/rättskälla/juridisk-bedömning-separation,
- source-lock GRÖN/GUL/RÖD,
- juridisk styrkegrad,
- motargumentstest,
- praxiskontroll,
- extern användbarhet,
- slutkontroll `Säkert belagt / Juridiskt starkast / Osäkert / Får inte användas ännu / Nästa viktigaste komplettering`.

### B. Befintlig STORA AUDITEN var stark men saknade vissa uttryckliga fält

**Fynd:** STORA AUDITEN hade redan datum, källa, faktisk uppgift, bevisklass, juridisk funktion, vad beviset inte visar, saknad komplettering, originalkontroll och extern användbarhet.

**Saknade uttryckliga globala fält:**

- rättskälletyp,
- aktualitetsstatus,
- source-lock-färg GRÖN/GUL/RÖD,
- juridisk styrkegrad,
- standardiserat motargumentstest.

**Åtgärd:** dessa ligger nu i `styrning/README.md` och masterprompten och ska tillämpas på alla nya större juridiska audits.

### C. `.gitignore` skyddade inte uttryckligen alla nya huvudlager

**Fynd:** `.gitignore` skyddade anteckningar, analyser, bevis, handlingar, korrespondens, inspelningar och transkriptioner, men saknade uttryckliga negationer för:

- `STORA-AUDITEN/`
- `juridik/`
- `audit/`
- `styrning/`

**Åtgärd:** samtliga fyra lager är nu uttryckligen skyddade med `!mapp/` och `!mapp/**`. Masterprompten är också särskilt skyddad.

### D. Sex nya juridiska böcker – redan representerade, men binärfilerna är inte samma sak som registerpost

Följande sex uppladdade böcker ingår i arbetsunderlaget:

1. Håkan Strömberg/Bengt Lundell – `Allmän förvaltningsrätt`, 23 uppl., 2006.
2. Jesper Blomberg/Patrik Södergren – `Förvaltningsprocesslagen – En kommentar`, 2020.
3. Mattias Nilsson – `Juridiken – en introduktion till rättsvetenskapen`, 3 uppl., 2011.
4. Charlotte Andersson/Emil Andersson – `Lägenhetsbyten och andrahandsuthyrning`, 4 uppl., 2021.
5. `Myndigheternas skrivregler`, Ds 2004:45.
6. Språkrådet – `Myndigheternas skrivregler`, 8 uppl., 2014.

**GitHub-status:** böckerna är redan registrerade och analyserade i:

- `juridik/KALLREGISTER-JURIDISKA-BOKER-2026-08-29.md`
- `STORA-AUDITEN/12-SEXBOKS-AUDIT-NYA-RATTSSPAR-OCH-OVERKLAGANDE-FORBATTRINGAR-2026-08-29.md`

**Viktig spärr:** en registerpost eller bok-audit är inte detsamma som att den ursprungliga PDF-filen är versionshanterad i GitHub. Externa hänvisningar till bokinnehåll ska kunna gå tillbaka till den faktiska uppladdade PDF:n/originalet eller annan verifierbar utgåva.

### E. Nya rättsspår från sexboks-auditen är bevarade

Redan infört:

- FL 27 → 10 → 25 → 32: dokumentationskedjan från tillsynen.
- teknisk informationsasymmetri och utredningsansvar.
- återförvisning som processuell lösning.
- `samma sak` kontra senare faktiska omständigheter.
- saklighets-/relevanskontroll.
- separat JO-/klarspråksspår.

### F. `Överklagan kanske Erica` får inte tyst ersättas

Den nuvarande arbetsversionen och V2-förbättringslagret ska båda bevaras. V2-fynd får endast föras in i nästa fullversion efter source-lock och aktuell rättskontroll.

## 2. Ny styrkedja

Från och med denna audit gäller:

`originalkälla → source-lock → BEVISREGISTER → STORA AUDITEN → rättskällekontroll/aktualitet → styrkegrad/motargument → TIDSLINJE/spår → extern text`

## 3. Nya hårda statusmarkeringar

- **INTE VERIFIERAT**
- **JURIDISK BEDÖMNING – INTE FASTSLAGET FAKTUM**
- **GRÖN / GUL / RÖD source-lock**
- **MYCKET STARKT STÖD / STARKT ARGUMENT / MÖJLIGT ARGUMENT / SVAGT ARGUMENT / BÖR INTE ANVÄNDAS**

## 4. Vad som fortfarande INTE är färdigt bara genom denna audit

- Native original för samtliga viktiga mejl/ljud/bilder är inte automatiskt source-lockade.
- MF:s eventuella fält-/tjänsteanteckningar från tillsynen är inte härmed verifierade.
- Att en uppgift inte syns i en kontrollrapport bevisar inte automatiskt att dokumentationsskyldighet åsidosatts.
- Äldre doktrin får inte användas med gamla paragrafnummer.
- FPL 8 § är inte automatiskt direkt processregel i ett överklagat miljöbalksmål i MMD/MÖD.

## 5. Slutstatus

**Säkert belagt:** masterprompten saknades som styrfil; `.gitignore` saknade explicit skydd för fyra nya huvudlager; sexboks-auditen och V2-lagret fanns redan i GitHub.

**Juridiskt starkast:** den nya standarden förstärker källkontrollen och hindrar att äldre doktrin, transkriptioner eller sannolika slutsatser behandlas som primär eller gällande rätt.

**Osäkert:** postspecifika sakuppgifter som ännu inte kontrollerats mot native original.

**Får inte användas ännu:** direkta citat/talaridentiteter/datum eller rättsfall som inte source-lockats.

**Nästa viktigaste komplettering:** tillämpa masterprompten på den potentiella MÖD-överklagandets samtliga rättsliga huvudargument och verifiera varje direkt lagrum mot aktuell SFS.
