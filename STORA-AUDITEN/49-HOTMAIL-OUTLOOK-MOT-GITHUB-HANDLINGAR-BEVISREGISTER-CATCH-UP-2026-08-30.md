# 49 – HOTMAIL/OUTLOOK MOT GITHUB: HANDLINGAR + BEVISREGISTER + KORRESPONDENS

Datum: 2026-08-30

Status: **CATCH-UP AUDIT – STRUKTURKLAR, EFTERIMPORT 19–30 AUGUSTI ÅTERSTÅR**

## 0. Syfte

Denna rapport kontrollerar projektets Hotmail/Outlook-korrespondens mot GitHub-strukturen. Fokus är juridiskt relevant material om Kilsgatan 3 och särskilt Spår 5, men strukturen gäller samtliga spår.

Grundregel:

**Native e-post ska i första hand ligga i `korrespondens/...` med eget Bevis-ID och registreras i `BEVISREGISTER.md`. `handlingar/` är inte huvudarkivet för all e-post.**

---

# 1. HUVUDFYND – `handlingar/` ÄR INTE HELA MAILARKIVET

`handlingar/README.md` beskriver uttryckligen katalogen som de 16 filer som laddades upp den 18 augusti 2026. Där finns partsinlagor, fyra PDF-utskrifter av Outlook-mail och en skärmbild av brandhändelsen.

De fyra Outlook-PDF:erna B0457–B0462 är dubblettformat av redan registrerade mailhändelser, exempelvis B0457 = samma mejlhändelse som B0207 och B0460 = samma mejlhändelse som B0171.

### Slutsats

Det vore fel att försöka lägga alla Hotmail-mail i `handlingar/`.

Projektets riktiga mailstruktur är:

`HOTMAIL/OUTLOOK → korrespondens/<aktör>/YYYY-MM-DD_Bxxxx...md → BEVISREGISTER.md → tidslinje/spår/audit`

`handlingar/` ska fortsätta vara uppladdade fristående filer/originalutskrifter, inte ett parallellt komplett e-postarkiv.

---

# 2. VAD SOM REDAN FINNS I GITHUB

`BEVISREGISTER.md` visar att native/Outlook-återgiven korrespondens redan har registrerats löpande från B0001 och framåt.

Exempel:

- B0006–B0011 = Jennifer/Erica november 2025.
- B0092–B0098 = Gaby/Erica om OKAB, brister och åtgärder.
- B0119–B0125 = Gaby/Erica 24–25 november 2025 i den centrala Kilsgatan-tråden.
- B0149 = 1 december 2025 till Miljöförvaltningen.
- B0171 = 11 december 2025 till Miljöförvaltningen.
- B0180 = 15 december 2025 till Jennifer.
- B0189 = 17 december 2025 till Miljöförvaltningen.
- B0207 = 12 januari 2026 Erica → Familjebostäder.
- B0223 = 17 januari 2026 felanmälan lukt i porten.
- B0433 = Bostadsförmedlingen/Maria Lundqvist 13 augusti 2026.
- B0434–B0440 = brandförsvar/restvärderäddning.
- B0441–B0447 = Familjebostäder 17 augusti 2026, inklusive Jennifer.
- B0448 = Hyresgästföreningen/Emma Sega 18 augusti 2026.

Därefter ligger B0449–B0464 som de 16 uppladdade filerna i `handlingar/`.

### Strukturstatus

**GRÖN:** äldre Outlook-material är redan omfattande importerat och behöver inte dubbleras som nya `handlingar`.

---

# 3. SPÅR 5 – GABY 24–25 NOVEMBER ÄR REDAN I ORIGINALSTRUKTUREN

Tidigare osäkerhet om huruvida Gabys brandbesked verkligen fanns i GitHub är nu undanröjd.

## B0119 – 24 november 2025

- Avsändare: Gaby Khalaf
- native Outlook-metadata sparad
- `Kontrollerat mot Outlook: Ja, den 18 augusti 2026`
- hör till Tråd 028.

Status: **GRÖN för att meddelandet existerar, avsändare, tid och tråd.**

## B0124 – 25 november 2025 11:14

Fulltexten är registrerad och source-lockad i:

`korrespondens/familjebostader/2025-11-25_1114_B0124_gaby-khalaf_sv-kilsgatan-3-123-44-farsta-lgh-nr-1202.md`

Gaby skriver ordagrant:

> "Jag ser inte heller att det har funnits någon brand i denna lägenhet, så vet inte vart du har fått detta ifrån..."

### Juridisk funktion

**GRÖN – direkt partsuppgift från Familjebostäders företrädare.**

Den visar vad Gaby uppgav den 25 november 2025.

Den bevisar INTE att:

- branden inte inträffade,
- Gaby hade gjort en uttömmande arkivsökning,
- Familjebostäder som organisation saknade kännedom 2017 eller 2025,
- någon avsiktligt lämnade en felaktig uppgift.

### Ny kontrollfråga

**Vilket system, vilka arkiv eller vilka interna källor hade Gaby faktiskt kontrollerat innan han skrev att han inte såg att någon brand funnits?**

---

# 4. JENNIFER – SAMMA ORGANISATION, ANNAN SENARE FÖRKLARING

Den source-lockade Jennifer-kedjan ligger kvar:

- 28 november 2025: hon föreslår nytt platsmöte i stället för att besvara brand-/saneringsfrågan skriftligt.
- 30 november: Erica ställer uttrycklig fråga om sanering efter branden.
- 2 december: Jennifer uppger att lägenheten "självklart" sanerats efter en eventuell brand, men skriver samtidigt att hon inte har dokumentation eftersom händelsen ligger nästan nio år tillbaka och att fastighetssystemet inte innehåller så gammal information.
- 12 december: kvarvarande frågor skjuts till mötet den 17 december.

### Juridisk funktion

Detta är **inte ett bevis för lögn eller svek**.

Det är däremot en **GRÖN organisatorisk diskrepans i uppgifter**:

Gaby: ser inte att brand funnits.

Jennifer: utgår senare från att brand/sanering kan ha ägt rum och gör ett positivt påstående om sanering.

Det öppnar två mycket starka verifieringsfrågor:

1. Vilken informationskälla använde Jennifer för påståendet om sanering?
2. Varför gav Gaby och Jennifer olika besked om samma historiska händelse?

---

# 5. HOTMAIL-AUDIT – VAD SOM KONTROLLERATS NU

Outlook har nu sökts brett för projektmaterial från 2025-08 och framåt med `Kilsgatan`, vilket gav mer än 200 träffar och täckte tre resultatsidor.

Därutöver har riktade kontroller gjorts mot centrala avsändare efter den senaste registrerade Outlook-importen:

- Jennifer Ehlin
- Gaby Khalaf
- Emma Sega / Hyresgästföreningen
- Maria Lundqvist / Bostadsförmedlingen
- Miriam Adolfsson / Miljöförvaltningen

Den breda sökningen visar att det finns ett betydande antal mail efter 18 augusti 2026 som ännu inte finns i det nuvarande BEVISREGISTER, eftersom registret därefter går över till de 16 uppladdade handlingarna B0449–B0464.

### Exempel på efterimport som måste hanteras

- 26 augusti 2026 – Erica → Jennifer, frågor i felanmälan fortfarande obesvarade.
- 27 augusti 2026 – Jennifer → Erica, nytt besked om planerat besök/egna tidigare observationer.
- 27 augusti 2026 – Erica → Jennifer, väntar på svar om arbetsordrar.
- 26 augusti 2026 – Erica → Miriam/Miljöförvaltningen, uppföljning av de tre frågorna om "samma sakfråga".
- senare SBK/OVK-korrespondens i samma period.

### Status

**GUL – materialet finns i native Hotmail/Outlook men är ännu inte infört som nya Bevis-ID efter B0464.**

---

# 6. VIKTIG STRUKTURKORRIGERING

Det finns tre olika saker som inte får blandas ihop:

### A. Native Outlook-bevis
Direkt meddelande med metadata och full meddelandetext.

**Primärt bevisformat i projektets korrespondenslager.**

### B. PDF-Outlook-utskrift
Kan vara bra som visuell originalnära handling men får inte räknas som en ny separat händelse när samma mejl redan har eget Bevis-ID.

### C. Partsinlaga/sammanställning
Visar vad Erica senare har sammanställt eller gjort gällande. Sakuppgifter i dokumentet måste fortfarande knytas tillbaka till primärkällorna.

---

# 7. SPÅR 5 – VILKA MAILGRUPPER SOM SKA PRIORITERAS I NÄSTA IMPORTPASS

## PRIORITET A – AVGÖRANDE

1. Gaby 24–25 november 2025 om branden – redan registrerade B0119–B0125, men exact quote audit ska kompletteras för samtliga relevanta meddelanden.
2. Jennifer 28 november–12 december 2025 om brand/sanering – redan i korrespondenslagret; ska länkas hårdare till Spår 5-matrisen.
3. Mail där Erica uttrycker att hon aldrig skulle ha accepterat/tackat ja om informationen varit känd – flera source-lockade förekomster till Hyresgästföreningen; ska få en egen kausalitets-/betydelsematris, inte räknas dubbelt genom citerade trådar.
4. Bostadsförmedlingens mail om vilken information som lämnas/kontrolleras i förmedlingsledet.
5. Miljöförvaltningens mail där brand-/saneringshypotesen eller beslutsunderlaget uttryckligen berörs.

## PRIORITET B – STÖDBEVISNING

- SSBF / Max Ekberg
- S:t Erik Försäkring
- Restvärderäddning
- Folkhälsomyndigheten
- SBK/OVK

Dessa kan styrka historik, dokumentationskedja eller senare utredningsrelevans, men de bevisar inte i sig vad Familjebostäder upplyste om före avtalet.

---

# 8. GRÖN / GUL / RÖD

| Post | Status | Juridisk funktion | Lucka / nästa kontroll |
|---|---|---|---|
| `handlingar/` som katalog över 16 uppladdade filer | **GRÖN** | originalfilslager | ska inte expanderas till komplett mailarkiv |
| `BEVISREGISTER.md` B0001–B0448 | **GRÖN struktur** | index till Outlook-korrespondens | kvalitetsvärdet i varje enskild post måste bedömas efter innehåll |
| B0457–B0462 Outlook-PDF | **GRÖN dubblettkoppling** | visuell stödhandling | får inte räknas som nya händelser |
| B0119/B0124 Gaby brandkedja | **GRÖN** | partsuppgift/organisatoriskt informationsläge | exakt kontroll av samtliga 24 nov-formuleringar återstår |
| Jennifer 2 dec om sanering | **GRÖN** | positiv partsuppgift + dokumentationsläge | källan bakom hennes slutsats om sanering saknas |
| Mail efter 18 aug 2026 | **GUL** | ny bevisning/processhistorik | behöver nya Bevis-ID och repoimport |
| "Gaby ljög" | **RÖD** | otillåten slutsats | kräver kunskap/uppsåt som inte visats |
| "Sanering skedde aldrig" | **RÖD** | otillåten slutsats | dokumentationslucka bevisar inte utebliven åtgärd |
| "FB hade noll kunskap om branden" | **RÖD** | motsägs av senare extern dokumentation om kontakt 2017 | organisatorisk kunskapskedja måste analyseras separat |

---

# 9. NÄSTA TEKNISKT/JURIDISKT KORREKTA STEG

Nästa steg ska INTE vara att dumpa fler filer i `handlingar/`.

Nästa steg är en **delta-import från Hotmail/Outlook efter senaste native mailposten B0448 (18 augusti 2026)**:

1. inventera samtliga projektmail efter 18 augusti,
2. rensa bort privata/irrelevanta träffar och rena citerade dubbletter,
3. skapa nya stabila Bevis-ID från B0465 och framåt,
4. spara varje native mail i rätt `korrespondens/<aktör>/`,
5. uppdatera `BEVISREGISTER.md`,
6. koppla endast juridiskt relevanta mail till Spår 1–5 och huvudtidslinjer,
7. markera dubbletter uttryckligen i stället för att räkna dem som nya bevis.

---

# 10. HUVUDSLUTSATS

GitHub saknar **inte** hela den äldre Hotmail-korrespondensen. Tvärtom finns ett omfattande Outlook-baserat korrespondenslager redan registrerat med Bevis-ID.

Den verkliga luckan är tidsmässig:

> **native mailimporten är i praktiken source-lockad till och med 18 augusti 2026, medan flera projektmail från 19–30 augusti fortfarande bara finns i Hotmail/Outlook och ännu inte har fått Bevis-ID i GitHub.**

För Spår 5 är dessutom Gaby-kedjan 24–25 november redan betydligt bättre source-lockad än tidigare arbetsanteckningar gav intryck av.

## Säkert belagt

- `handlingar/` = 16 uppladdade filer, inte komplett mailarkiv.
- äldre native Outlook-material finns i `korrespondens/...` och `BEVISREGISTER.md`.
- B0124 innehåller Gabys ordagranna uppgift att han inte ser att det funnits någon brand i lägenheten.
- Jennifer och Gaby lämnar senare olika typer av besked om brand-/saneringshistoriken.

## Juridiskt starkast

**Organisatoriskt informationsläge och källan bakom respektive besked**, inte anklagelsen att någon ljög.

## Osäkert

Vilka interna system/arkiv Gaby faktiskt kontrollerade och vilken källa Jennifer använde för saneringspåståendet.

## Får inte användas ännu

- att sanering aldrig skedde,
- att Gaby medvetet lämnade felaktiga uppgifter,
- att den interna informationsdiskrepansen ensam bevisar svek före avtalet.

## Nästa viktigaste komplettering

**Delta-import och Bevis-ID-sättning av projektmail 19–30 augusti 2026, följt av en exakt Spår 5-matris över Gaby/Jennifer/Erica/Bostadsförmedlingen/Hyresgästföreningen/Miljöförvaltningen.**