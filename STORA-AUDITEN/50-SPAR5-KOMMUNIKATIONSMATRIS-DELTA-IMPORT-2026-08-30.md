# 50 – SPÅR 5 KOMMUNIKATIONSMATRIS + DELTA-IMPORT 19–30 AUGUSTI 2026

Datum: 2026-08-30

Status: **DELTA-IMPORT BATCH 1 SOURCE-LOCKAD – PERIODEN ÄR INTE ÄNNU EXHAUSTIVT STÄNGD**

## 0. Syfte

Detta lager följer projektets kommunikations-masterprompt och gör två saker:

1. fortsätter den stabila Bevis-ID-serien efter B0464,
2. bygger en exakt Spår 5-kommunikationsmatris med strukturen:

`datum → avsändare → fråga → svar → uteblivet svar → Bevis-ID → juridisk funktion`

Endast native Outlook-meddelanden med kontrollerad metadata får få nytt Bevis-ID.

---

# 1. DELTA-IMPORT – NYA BEVIS-ID

| Bevis-ID | Lokal tid | Avsändare → mottagare | Ämne | Importstatus | Primär funktion |
|---|---|---|---|---|---|
| **B0465** | 20 aug 2026 19:45 CEST | Erica → SBK/Jenny Hamrin | ärendenummer är 2026KC299053 | **IMPORTERAD / GRÖN** | OVK + brand-/dokumentkedja |
| **B0466** | 26 aug 2026 21:36 CEST | Erica → Jennifer Ehlin | Sv: Ny felanmälan & klagomål | **IMPORTERAD / GRÖN** | obesvarade frågor; kanalrensning; AO; post-brand |
| **B0467** | 26 aug 2026 22:00 CEST | Erica → Miriam Adolfsson | Sv: Vad menar MF med samma sakfråga? | **IMPORTERAD / GRÖN** | Spår 4: beslutsunderlag/later material |
| **B0468** | 27 aug 2026 10:27 CEST | Jennifer Ehlin → Erica | Sv: Ny felanmälan & klagomål | **IMPORTERAD / GRÖN** | delbesked; syfte med besök; AO-löfte; SBK-kännedom |
| **B0469** | 27 aug 2026 21:32 CEST | Erica → Jennifer Ehlin | Sv: Ny felanmälan & klagomål | **IMPORTERAD / GRÖN** | uppföljning AO + post-brand-dokumentation |
| **B0470** | 28 aug 2026 11:41 CEST | Jenny Hamrin → Erica | Dnr 2026-06369, Återkoppling efter frågor | **IMPORTERAD / GRÖN** | PBL-scope; OVK; brandhandlingar; pågående tillsyn |

### Nyckelregel

Dessa sex är faktiska nya Bevis-ID-poster i `korrespondens/...`.

**B0471 och framåt får inte användas förrän nästa native Outlook-meddelande är fullständigt kontrollerat.**

---

# 2. SPÅR 5 – KOMMUNIKATIONSMATRIS

Spår 5 avser information/kunskap före avtal och senare kommunikation som kan identifiera källor, ändrade förklaringar eller dokumentkedjor. Senare mejl får aldrig flyttas bakåt och användas som direkt bevis för vad Familjebostäder visste före avtalet 2025 utan särskild länk.

| Datum | Avsändare | Fråga / uppgift | Svar | Uteblivet/delsvar | Bevis-ID | Juridisk/bevismässig funktion |
|---|---|---|---|---|---|---|
| 24 nov 2025 | Gaby Khalaf | uppger att ingen brandsituation finns dokumenterad från FB:s sida och drar slutsats att något sådant inte inträffat | Erica invänder och hänvisar senare till extern händelseinformation | intern sökkälla fortfarande okänd | B0119–B0124-kedjan | organisationskunskap; källa bakom beskedet måste identifieras |
| 25 nov 2025 | Gaby Khalaf | `Jag ser inte heller att det har funnits någon brand i denna lägenhet...` | Erica fortsätter ifrågasätta och begära dokumentation | vilket system Gaby kontrollerade är obesvarat | **B0124** | GRÖN partsuppgift; inte bevis att brand saknas |
| 28–30 nov 2025 | Erica → Jennifer/Gaby | frågar om lägenheten någonsin sanerats efter branden | Jennifer besvarar 2 dec | initialt ej sakligt svar 28 nov; sedan svar | befintliga Bevis-ID i tråd | visar att saneringsfrågan var uttryckligen ställd |
| 2 dec 2025 | Jennifer Ehlin | uppger att lägenheten `självklart` sanerats efter eventuell brand men att hon saknar dokumentation och systemet inte innehåller så gammal information | Erica begär senare korrekt version/källa | **källan bakom saneringsuppgiften är fortfarande inte identifierad** | befintligt Jennifer-bevis | positiv partsuppgift + dokumentationsläge; central Spår 5-källfråga |
| 10–12 dec 2025 | Erica → Jennifer | ställer Gaby/Jennifer-beskeden mot varandra och begär skriftlig korrekt version | Jennifer hänvisar kvarvarande frågor till möte 17 dec | skriftligt sakbesked om källan uteblir i denna sekvens | befintliga Bevis-ID | fråga→svar-gap; inte medgivande |
| 20 aug 2026 | Erica → SBK/Jenny | vilka OVK- och post-brand-handlingar finns för 0562? | SBK svarar senare 28 aug | mellanliggande svar/OVK-tråd måste läsas separat | **B0465** | senare verifieringsarbete; inte pre-contract-knowledge |
| 26 aug 2026 | Erica → Jennifer | vad var scope/metod för besöket; när/hur gjordes 5 m kanalrensning; AO; makulerade felanmälningar; vad gjordes efter branden? | Jennifer 27 aug förklarar besökets syfte, lovar AO-svar och säger att SBK-tillsyn mottagits | kanalrensning/post-brand-frågor fullt sakbesvaras inte i B0468 | **B0466 → B0468** | senare konsistens-/källspår; tydligt DELSVAR |
| 27 aug 2026 | Jennifer → Erica | besök syftade till att hon själv skulle uppleva miljön; hon har inte upplevt Ericas symtom vid tidigare besök; AO-svar ska komma; SBK-tillsyn ska besvaras | Erica följer upp samma dag | AO fortfarande utlovat i denna punkt | **B0468** | senare partsuppgift, observation, löfte, PBL-kännedom |
| 27 aug 2026 | Erica → Jennifer | inväntar utlovat AO-svar och vill se FB:s kommande SBK-svar om brandinformation/åtgärder | senare svar måste kontrolleras | **STATUS ÖPPEN** | **B0469** | fråge-/löfteuppföljning; får inte kallas slutligt obesvarad innan senare mail audit |
| 28 aug 2026 | Jenny Hamrin/SBK | tillsynen har börjat; scope avgränsas; inga generella post-brand-intyg krävs in till SBK; FB-svar inväntas till 20 sep | — | tillsynen är uttryckligen inte slutligt avgjord | **B0470** | visar myndighetens aktuella scope och att avsaknad hos SBK ≠ avsaknad hos FB |

---

# 3. FRÅGA → SVAR – CENTRALA ÖPPNA SPÅR 5-FRÅGOR

| Fråga | Första verifierade fråga | Senaste kontrollerade uppföljning | Besvarad? | Juridisk funktion |
|---|---|---|---|---|
| Vilket system/källa kontrollerade Gaby när han skrev att han inte såg någon brand? | nov 2025 | fortfarande öppen i nuvarande audit | **INTE SOURCE-LOCKAT SVAR** | avgör styrkan i kunskaps-/informationskedjan |
| Vilken faktisk källa låg bakom Jennifers positiva uppgift att sanering `självklart` skett? | dec 2025 | senare externa dokumentationssökningar 2026 | **INTE SOURCE-LOCKAT SVAR** | kärnfråga om faktapåstående vs antagande/intern information |
| Finns saneringsrapport/intyg/arbetsorder/entreprenörskedja? | nov–dec 2025 | B0465 och B0469 visar fortsatt efterfrågan | **INGEN SÅDAN HANDLING SOURCE-LOCKAD I NUVARANDE LAGER** | dokumentationslucka; bevisar inte utebliven sanering |
| Vad gjorde FB efter SSBF:s insats 16 nov 2017? | uttryckligen i senare skriftlig kedja | B0466/B0469 | **ÖPPEN I DENNA DELTA-AUDIT** | kan identifiera ursprunglig återställningskälla och organisationskunskap |
| Vilka arbetsordrar stödjer kanalrensning/femmetersuppgift och andra åtgärder? | tidigare 2025/2026 | B0466 → Jennifer lovar svar B0468 → B0469 påminner | **DELSVAR/ÖPPEN** | source-lock av utförande vs muntlig/senare uppgift |

---

# 4. DELTA-PERIOD 19–30 AUGUSTI – KVAR ATT KONTROLLERA INNAN PERIODEN KAN STÄNGAS

Den breda Outlook-sökningen visar ytterligare relevanta kandidater som ännu inte fått nytt Bevis-ID i denna batch. De får inte räknas som importerade förrän full metadata/body/dubblettstatus kontrollerats.

Prioriterade kandidater:

- 25 aug – Erica → Folkhälsomyndigheten/Malin, följdfrågor efter ny dokumentation,
- SBK/Sheida-tråden om objekt 0562/system 01 och varför underlag saknas,
- eventuella 28–30 aug-svar från MF, HGF, Bostadsförmedlingen eller FB,
- automatiska service-/reparatörsmeddelanden endast om de förändrar relevant bevistema,
- eventuellt material som skickades/vidarebefordrades till MMD under perioden.

**Status för hela perioden 19–30 augusti:** **GUL – DELTAIMPORT PÅBÖRJAD, INTE EXHAUSTIVT STÄNGD.**

Detta är medvetet: projektets regel `smartare data, inte mer data` innebär att privata, administrativa och rena tråddubbletter inte ska importeras bara för att de träffar på `Kilsgatan`.

---

# 5. KOPPLING TILL SPÅR 5 – VAD SENARE MEJL KAN OCH INTE KAN GÖRA

### Kan göra

- identifiera källan bakom äldre faktapåståenden,
- visa hur FB senare beskriver historiken,
- visa vilka frågor som ställts och om de besvarats,
- visa ändrade förklaringar eller nytillkommen information,
- lokalisera arbetsorder, system, rapporter, entreprenörer och andra primärkällor.

### Kan inte automatiskt göra

- bevisa att FB före avtalet 2025 kände till dagens påstådda problem,
- bevisa att sanering inte utfördes,
- bevisa svek/förtigande,
- flytta 2026 års kunskap till 12 augusti 2025.

---

# 6. SOURCE-LOCK / KVALITET

| Påstående | Status |
|---|---|
| B0465–B0470 finns som nya native Outlook-baserade bevisposter | **GRÖN** |
| Perioden 19–30 augusti är fullständigt importerad | **RÖD – FÅR INTE SÄGAS ÄNNU** |
| Jennifer lovade 27 aug att återkomma om AO | **GRÖN – B0468** |
| Erica påminde samma dag om AO | **GRÖN – B0469** |
| SBK hade 28 aug börjat PBL-tillsyn och väntar FB-svar till 20 sep | **GRÖN – B0470** |
| Avsaknad av post-brand-handlingar hos SBK betyder att FB saknar dem | **RÖD** |
| Gaby-källan och Jennifer-saneringkällan är identifierade | **RÖD / INTE VERIFIERAT** |

---

# 7. NÄSTA DELTAIMPORT

Fortsätt från **B0471** först efter full kontroll av nästa materiellt relevanta native Outlook-mail.

Prioritetsordning:

1. 25 aug Folkhälsomyndigheten-tråden,
2. Sheida/SBK 0562/system 01,
3. MF 26–30 aug eventuella svar,
4. FB/Jennifer/Gaby efter B0469,
5. HGF/Bostadsförmedlingen endast om deras mail tillför ett relevant Spår 5-bevistema,
6. MMD-vidarebefordran/nytt material om sådan faktisk kommunikation finns.

---

# 8. SLUTSTATUS

## Säkert belagt

Sex nya native Outlook-mail har source-lockats och importerats som B0465–B0470.

## Juridiskt starkast

Spår 5-matrisen visar att kärnfrågorna fortfarande inte är `fanns brand?` utan:

1. vilken källa använde Gaby,
2. vilken källa använde Jennifer,
3. vilken återställnings-/saneringsdokumentation kan faktiskt identifieras,
4. vad visste FB före avtalet och vad upplystes om då.

## Osäkert

Perioden 19–30 augusti är ännu inte komplett importerad; ytterligare mailkandidater måste dubblett- och relevanskontrolleras.

## Får inte användas ännu

- `hela perioden är färdigimporterad`,
- `alla Jennifer-frågor är fortfarande obesvarade`,
- `FB saknar dokumentation bara för att SBK saknar den`,
- `senare dokumentationsbrist bevisar svek före avtalet`.

## Nästa viktigaste komplettering

**Fortsätt delta-importen från B0471 och source-locka därefter den interna källan bakom Jennifers saneringsuppgift.**
