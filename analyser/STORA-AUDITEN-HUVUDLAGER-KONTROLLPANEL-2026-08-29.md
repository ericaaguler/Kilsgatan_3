# STORA AUDITEN – HUVUDLAGER / KONTROLLPANEL

**Projekt:** Kilsgatan 3, lgh 1202 / objekt 60020562 / 0562  
**Datum:** 29 augusti 2026  
**Status:** STYRANDE HUVUDLAGER  
**Funktion:** Kontrollpanel ovanför `TIDSLINJE.md`, `BEVISREGISTER.md`, sakspåren, processanalysen, MÖD-spåret, ansvarskartan, remedymatrisen och juristbriefen.

---

## 0. Vad detta lager är

Detta är **inte ännu en sammanfattning**. Det är projektets styrande auditlager.

Varje bevispost som tas upp här ska följas genom samma kedja:

`datum → källa → faktisk uppgift → bevisklass → juridisk funktion → vad den inte bevisar → saknad komplettering → relevant lag/princip → status i huvudtidslinjen/spåren`

Syftet är att förhindra tre fel:

1. att en sekundär sammanställning behandlas som primärbevis,
2. att en faktisk uppgift ges större bevisräckvidd än källan medger,
3. att ett juridiskt argument används innan både beviset och den aktuella rättsregeln är kontrollerade.

**Denna fil ersätter inte originalbevis.** Vid konflikt gäller alltid:

1. originalfil/primärhandling,
2. verifierad transkription eller dokumenterad förstahandsuppgift,
3. källåst post i `TIDSLINJE.md` / `BEVISREGISTER.md`,
4. denna audit,
5. annan analys/sammanställning.

---

# 1. Statuskoder

### Bevisklass

- **P1 – Primärhandling:** originalmejl, myndighetsbeslut, teknisk rapport, fotografi med verifierbar metadata, original arbetsorder, officiell händelserapport.
- **P2 – Primär närtidsuppgift:** samtida partsmejl där en händelse/ett uttalande återges kort efter att det inträffat.
- **P3 – Verifierad transkription/ljud:** direkt ljudkälla eller kontrollerad transkription.
- **S1 – Sekundär sammanställning:** senare partsinlaga, mastertidslinje, analys, återgivning av tidigare material.
- **V1 – Vittnesuppgift:** förstahandsobservation från annan person.
- **A1 – Analytisk inferens:** slutsats byggd av flera källor; aldrig självständigt bevis.

### Source-lock-status

- `VERIFIERAT I PRIMÄRKÄLLA`
- `STARKT STÖD`
- `SOURCE-LOCK KRÄVS`
- `KAN INTE FASTSTÄLLAS`
- `JURIDISK KONTROLL KRÄVS`
- `TEKNISK SAKKUNNIG KRÄVS`

### Spårstatus

- `HT` = källbelagd huvudtidslinje
- `BR` = bevisregister
- `MF` = Miljöförvaltningens handläggning
- `MÖD` = överklagande/process
- `FB` = Familjebostäder/ansvar/kunskapskedja
- `VENT` = ventilation/OVK
- `KANAL` = kanalrensning
- `BRAND` = brand/sanering/återställning
- `STÄD` = städning/mögelinriktade rengöringsmedel
- `VITTNE` = vittnen/förstahandsreaktioner
- `HYRA` = hyresrätt/brukbarhet/remedy
- `OFF` = offentlighet/akt
- `SBK` = Stadsbyggnadskontoret/PBL

---

# 2. AUDITREGISTER – KRITISKA BEVISPOSTER

> **Arbetsregel:** Extern användning får aldrig bygga på audittexten ensam. Kontrollera alltid den angivna källan/originalet.

| ID | Datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den inte bevisar | Saknad komplettering | Relevant lag/princip | Status/spår |
|---|---|---|---|---|---|---|---|---|---|
| AUD-001 | 2017-11-16 | Polis-/brandhändelse; SSBF-spår | Brand/rök-händelse i lägenheten är dokumenterad; torrkokning/kraftig rökutveckling finns i officiellt material. | P1 | Fastställer att brandhistoriken är verklig och relevant historisk faktor. | Bevisar inte dagens orsak, saneringsbehov eller kvarvarande förorening. | Full SSBF-händelserapport, överlämnande till fastighetsägaren, skade-/sanerings-/återställningskedja. | Bevisvärdering; MB 9 kap. endast om aktuell påverkan kan knytas; fastighetsägaransvar separat. | HT/BR/BRAND – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-002 | 2017-11-16 | SSBF uppgift om kontakt/ansvarsövergång | Arbetsmaterial anger att Familjebostäder kontaktades under insatsen och att ansvar efter avslutad räddningsinsats övergår till fastighetsägaren. | P1/S1 beroende på exakt handling | Kunskaps- och ansvarskedja efter brand. | Bevisar inte vilka åtgärder FB faktiskt utförde. | Source-lock exakt SSBF-formulering och eventuell kontaktlogg. | LSO/fastighetsägaransvar – `JURIDISK KONTROLL KRÄVS` för exakt rättslig funktion. | BRAND/FB – `SOURCE-LOCK KRÄVS` för exakt citat |
| AUD-003 | 2025-10-01 | Tillträdeshandling/hyresavtal + samtida dokumentation | Erica får tillträde till bostaden. | P1 | Startpunkt för brukbarhets-, fel- och kunskapstidslinjen. | Bevisar inte att bostaden redan då juridiskt var bristfällig. | Originalhyresavtal/tillträdesbevis vid extern användning. | JB 12 kap. 9, 15, 16 §§ – aktuell lydelse måste kontrolleras. | HT/HYRA – `STARKT STÖD` |
| AUD-004 | 2025-10-02 | Videodokumentation/senare skrivelse | Lukt uppmärksammas i direkt anslutning till tillträdet; Peter uppges också ha upplevt lukt och vädrat. | P2/S1 tills video kontrollerats | Tidig kunskap hos FB och tidig problemrapport före senare åtgärder. | Bevisar inte luktkälla eller hälsorisk. | Originalvideo + exakt uttalande. | JB brukbarhet/underhåll; MB 9:3 som tillsynsfråga. | FB/HYRA/MF – `SOURCE-LOCK KRÄVS` |
| AUD-005 | 2025-10-08 | Mejl/fotodokumentation till FB | Fotodokumentation om kök/ventilation skickas till Familjebostäder. | P1 | Visar tidig underrättelse och kunskap om påtalade brister. | Bevisar inte teknisk diagnos av bilderna. | Originalbilder och mejlbilagor måste kopplas ihop. | Kunskapskedja; JB 12:15–16; bevisprincip. | HT/BR/FB – delvis källåst |
| AUD-006 | 2025-10-15–18 | OCAB 716247 | OCAB tillkallas efter missfärgningar; fuktskada/fuktfråga undersöks; rapporten har begränsat uppdrag. | P1 | Avgränsar vad som faktiskt undersöktes före senare städningar. | Utesluter inte mögel, luktorsak, VOC, dolda konstruktioner eller total inomhusmiljö om detta inte ingick i uppdraget. | Originalrapport + uppdragsbeställning + metod/scope. | Bevisräckvidd; MB 26:21–22 i senare tillsyn; JB separat. | HT/BR/MF/STÄD – `VERIFIERAT` rapport, scope ska hållas exakt |
| AUD-007 | 2025-10-20 | Ericas fråga om OCAB | Erica frågar om OCAB bara gjort fuktmätning eller också mikrobiologisk/mögelanalys och efterfrågar ytterligare undersökning. | P1 | Visar att utredningens begränsning ifrågasattes tidigt. | Bevisar inte att ytterligare utredning rättsligt måste göras på exakt begärt sätt. | Originalmejl och svar från FB. | JB/MB utredningsfråga; senare FL 23 § för myndighetsärendet. | HT/FB/MF – `STARKT STÖD` |
| AUD-008 | 2025-10-27 | Första professionella städningen | Första städningen genomförs; symtomrapport uppges ha uppstått före städarnas ankomst när lägenheten var stängd. | P2/S1 tills originalmaterial låsts | Skiljer rapporterade besvär från själva rengöringsmedlen/städningen. | Bevisar inte orsaken till symtomen. | Originalmejl/felanmälningslogg/ev. vittne. | MB 9:3; bevisning om tidsmönster; JB brukbarhet. | STÄD/VITTNE/HYRA – `SOURCE-LOCK KRÄVS` |
| AUD-009 | 2025-10-29 | Leonard Thörnfeldt mejl | Platsbesök för lukt samt kontroll/rengöring av ventilation anges/beställs enligt tidigare material. | P1 när originalet används | Kunskaps- och åtgärdskedja. | Bevisar inte att orsaken utreddes eller att åtgärden lyckades. | Originalmejl/arbetsorder. | JB underhåll; senare MB 26:19/21 som utredningsunderlag. | FB/VENT – `SOURCE-LOCK KRÄVS` på exakt lydelse |
| AUD-010 | 2025-11-04 | Caroline Blomberg driftanteckning | Luftflöden justeras; anteckningen innehåller bl.a. 7,4→10,2 l/s, badrum ca 10→15,4, sovrum ned mot projekterat värde och formuleringen “rensningen av kanal” kopplad till forcerat flöde. | P1 | Teknisk åtgärd/mätning; central för ventilations- och kanalrensningskedjan. | Visar inte ensam 5 m, exakt kanalsträcka, metod eller att total inomhusmiljö var godtagbar. | Original driftanteckning/arbetsorder, instrument/metod, vilken kanal/åtkomstpunkt. | PBL/OVK endast i rätt räckvidd; MB 26:21–22; teknisk sakkunnig. | VENT/KANAL – `VERIFIERAT` delar; `TEKNISK SAKKUNNIG KRÄVS` |
| AUD-011 | 2025-11-05 | HGF bristunderlag CAS-133640-Q5D1C8, 28 sidor | Mycket detaljerad samtida beskrivning av 4 nov-besöket; blockerad friskluft, ventiler/öppningar och filter diskuteras. Ingen träff på “kanalrensning/rensning” i dokumentet. | P1/P2 | Samtida kunskaps-/kommunikationsbevis och negativ bevisomständighet. | Bevisar inte att teknisk kanalrensning inte skedde. | Original PDF finns; vid extern användning citera relevanta sidor, inte senare sammanfattning. | Bevisvärdering; ingen särskild lagregel. | BR/VENT/KANAL – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-012 | 2025-11-06 | Gaby-mejl | Gaby skriver enligt source-lockat spår att “här ska vi felsöka vad problemet är” och att det är komplext eftersom det gäller just lägenheten. | P1 | Direkt kunskaps-/positionsmarkör: problemet beskrevs ännu som något som behövde förstås/felsökas. | Bevisar inte att viss felsökningsmetod juridiskt krävdes eller att FB erkände viss teknisk brist. | Originalmejl ska anges exakt. | JB 12:15–16; MB 26:19 som eventuell senare tillsynsrelevans; ansvarskedja. | FB/HYRA/MF – `VERIFIERAT` enligt projektets tidigare source-lock |
| AUD-013 | 2025-11-06/07 | Jennifer initialt mejl + Ericas svar | Jennifer beskriver frågan som missnöje med “städning och skick”. Erica korrigerar före mötet och anger att frågan gäller inomhusmiljö, hälsa, ventilation, lukt m.m. och ber Jennifer läsa underlaget. | P1 | Visar vad ansvarig förvaltare fick skriftlig information om före platsmötet. | Bevisar inte tekniska orsaker eller att varje påstående i bilagan var korrekt. | Originalbilaga/checklista knyts till mejlet. | Kunskapskedja; JB; bevisning. | HT/BR/FB – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-014 | 2025-11-11 | Mötesbokning + ljud | Första större platsmötet äger rum 11 nov. Deltagare enligt projektets aktuella källbild: Jennifer, Gaby, Micke samt Thomas från Torsbygatan-spåret; Thomas Duvsjö är en annan person. | P1/P3 | Låser datum och persondistinktion; central för kunskap/åtgärder. | Bevisar inte innehållet i mötet utan ljud/source-lock. | Full ljudgenomgång + verifierad transkription med talaridentifikation. | Bevisvärdering, ansvarskedja. | HT/FB/KANAL/STÄD – datum verifierat; innehåll `SOURCE-LOCK KRÄVS` |
| AUD-015 | 2025-11-12 | Erica till Jennifer efter mötet | “Vi hann inte toucha på ämnet huvudvärken - luften - jag tror rengöring i kanal samt få in luft i klädkammaren är smart början.” | P1/P2 | Samtida markör att huvudvärk/luftfrågan enligt Erica inte hann behandlas fullt och att kanalrengöring sågs som möjlig nästa åtgärd. | Bevisar inte vad övriga deltagare ansåg eller om viss kanalåtgärd redan hade gjorts. | Originalmejl finns; koppla till 11 nov-ljud. | Bevisning; JB/MB senare utredningsfråga. | FB/KANAL/MF – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-016 | 2025-11-18 | Gaby mejl | Gaby skriver att städningen är bokad enligt tidsbokning mellan Erica och städfirman. | P1 | Visar FB:s kännedom om ny städning inför 20 nov. | Visar inte vem som formulerade själva arbetsordern eller vad som beställdes. | Beställning/arbetsorder/reklamation till städfirman. | Bevisning/ansvarskedja. | STÄD/FB – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-017 | 2025-11-20 09:49 | Foto | Foto visar Diversey TASKI Sani MouldOut tillsammans med rengöringsmedel vid andra städningen. | P1 | Visar att mögelinriktat rengöringsmedel fanns/användes enligt kompletterande material vid andra städningen. | Bevisar inte att mögel diagnostiserats, varför produkten valdes eller vem som beställde den. | Städfirmans arbetsorder, arbetsrapport, produktval, utförare/vittnesuppgift. | Bevisvärdering; MB 26:21–22 för myndighetens möjliga kompletteringsbehov. | STÄD/MF – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-018 | 2025-11-20 20:08 | Erica till Gaby | Samma kväll skriver Erica att ingrodd smuts/mögelliknande påverkan inte gått bort och återger att “städarna säger det inte går bort”. Hon skiljer också vanlig städreklamation från sådant som enligt henne kräver annan lösning. | P1/P2 | Samtida rapport till FB om begränsad effekt och städarnas uppgivna observation. | Är inte direkt vittnesutsaga från städarna och bevisar inte mögel. | Direkt uttalande från städfirman, arbetsrapport eller ljud/vittne. | Kunskapskedja; JB; senare MB/FL utredningsrelevans. | STÄD/FB/MF – `VERIFIERAT` att mejlet skickats; städarnas ord är P2 |
| AUD-019 | 2025-11-27 | Foto/komplettering | Tredje städning; produkt benämnd “Mögel bort” dokumenteras. | P1/S1 beroende på foto | Visar ytterligare riktad rengöringsinsats. | Bevisar inte diagnos eller orsak. | Arbetsorder/rapport och vilka ytor som behandlades. | MB 26:21–22 som möjlig tillsynsfråga; bevisning. | STÄD/MF – foto/source-lock ska kopplas |
| AUD-020 | 2025-12-02 | Jennifer mejl | Enligt arbetsmaterial beskriver Jennifer kanalrensning som något som “kommer att ske”. | P1 när originalet låses | Kritisk tidsmarkör i kanalrensningskedjan. | Bevisar inte att detta avser samma rensning som 4 nov eller senare 5 m-uppgift. | Originalmejl med exakt tempus, objekt, rum/system. | Bevisning; MB 26:21; PBL endast teknisk räckvidd. | KANAL/FB – `SOURCE-LOCK KRÄVS` |
| AUD-021 | 2025-12-02 | Jennifer mejl om brand | Jennifer uppger att lägenheten “självklart” sanerats efter eventuell brand men att hon inte har dokumentation från den tiden. | P1 när originalet används | Visar FB-representants uppgift om sanering och samtidigt dokumentationslucka. | Bevisar inte att sanering faktiskt genomfördes eller hur. | Originalmejl + skade-/sanerings-/återställningshandling. | Bevisvärdering; JB/MB endast efter rättslig koppling. | BRAND/FB – `STARKT STÖD`, exact source-lock |
| AUD-022 | 2025-12-17 | Ljud/transkription | Vid andra mötet förekommer enligt arbetsmaterial uppgift om ca 5 m kanalrensning samt diskussion om lukt/provtagning/åtgärder. | P3/S1 tills ljud låsts | Kan bli centralt direktbevis om vad FB uppgav. | Ingen säker slutsats om exakt ordalydelse, talare, datum för utförande eller teknik före ljudkontroll. | Full ljudanalys och talar-ID. | Bevisning; MB/FL senare relevans; teknisk sakkunnig. | KANAL/FB/MF – `SOURCE-LOCK KRÄVS` |
| AUD-023 | 2026-01-15 | FB uppgift till MF | Arbetsmaterial anger senare uppgift om “kanalrensning i köket 5 m upp” eller motsvarande. | P1 när MF-handlingen låsts | Binder senare femmetersuppgift till myndighetsakten. | Bevisar inte själva utförandet utan bakomliggande arbetsorder/rapport. | Original MF-handling, vem som lämnat uppgiften, arbetsorder. | FL 23; MB 26:21–22; bevisvärdering. | MF/KANAL – `SOURCE-LOCK KRÄVS` |
| AUD-024 | 2026-03-11 | MF inspektion/rapport | Okulär kontroll och ventilationsmätningar; arbetsmaterial anger ca kök 36, badrum 4, sovrum 3, totalt 43 l/s; undertryck omkring 8 Pa. | P1 | Visar vad som faktiskt mättes/observerades vid tillsynstillfället. | Utesluter inte automatiskt mikrobiell påverkan, emissioner, dolda konstruktioner eller annan orsak som metoden inte undersökte. | Originalrapport, instrument/metod, andra inspektörens anteckningar, exakt ventilationsläge. | FL 23; MB 9:3, 26:21–22; teknisk sakkunnig. | HT/BR/MF/VENT – `VERIFIERAT` huvudsak; räckvidd måste hållas exakt |
| AUD-025 | 2026-03-11 | Uppgift om ventiler i angränsande lägenheter | Arbetsmaterial anger att blockerande material togs bort även i lägenheter över/under. | P1/S1 beroende på original | Relevant för om ventilationsfrågan var lägenhetsisolering eller del av större systembild. | Bevisar inte systemfel eller kausalitet. | Arbetsorder/fastighetsskötaranteckning, vilka lägenheter/system. | PBL/OVK och MB; teknisk sakkunnig. | VENT/SBK/MF – `SOURCE-LOCK KRÄVS` |
| AUD-026 | 2026-03-11–04-03 | Ericas dokumentation + vittnen | Lägenheten vädras kontinuerligt i ca 23 dygn; därefter rapporteras återkommande besvär när den stängs. | P2/V1/S1 | Fenomen-/tidsmönster och effekt av ett praktiskt försök. | Bevisar inte att ventilation “uteslutits” eller vilken teknisk orsak som finns. | Original tidsdokumentation + vittnesuppgifter. | MB 9:3; bevisning. | VITTNE/MF/HYRA – `STARKT STÖD`; kausalitet inte visad |
| AUD-027 | 2026-04-04 | Thomas Duvsjö m.fl. | Flera personer uppges reagera vid vistelse; Thomas Duvsjö är separat från Thomas i 11 nov-spåret. | V1/S1 tills originalvittnesuppgifter låsts | Stöd för återkommande fenomen hos fler än en individ. | Bevisar inte teknisk eller medicinsk orsak. | Originalvittnesuppgifter, datum, exponeringstid, symtom, jämförelsebostad. | MB 9:3; bevisvärdering. | VITTNE/MF/MÖD – `SOURCE-LOCK KRÄVS` för varje individ |
| AUD-028 | 2026-04-03–09 | Komplettering 2025-23696-97 | Erica lämnar omfattande komplettering efter tillsyn: återkommande besvär, tre städningar, MouldOut/Mögel bort, vittnen, 23 dygn vädring, konstruktionsfrågor och begäran om fortsatt utredning. | P1 som partsinlaga | Visar exakt vad MF hade fått kännedom om före beslutet och vilka frågor som uttryckligen lyftes. | Bevisar inte sanningshalten i varje tekniskt påstående i inlagan. | Registreringsdatum, bilagelista, diarielogg, vilka delar som kommunicerades till FB och bedömdes. | FL 23, 25, 27, 32 §§ beroende på tillämplighet; MB 26:21–22. | MF/MÖD – `VERIFIERAT I PRIMÄRKÄLLA` att inlagan finns; handläggning behöver audit |
| AUD-029 | 2026-04-03–09 | Foto 2025-23696-98 | Foto från 20 nov med Sani MouldOut ges in till MF. | P1 | Gör produktvalet konkret och visuellt verifierbart i myndighetsakten. | Bevisar inte varför medlet valdes eller att mögel fanns. | Aktlogg: mottagande, intern bedömning, eventuell kompletteringsfråga till FB. | FL 23/32; MB 26:21–22. | MF/STÄD/MÖD – `VERIFIERAT` foto; bedömning `ÖPPEN` |
| AUD-030 | 2026-04-13 | MF beslut | Miljöförvaltningen avslutar tillsynsärendet. | P1 | Processuell slutpunkt i underinstansen. | Bevisar inte att lägenheten objektivt saknar brist eller att teknisk orsak är klarlagd. | Exakt beslutsskäl, aktkedja, kommunicering, vilka kompletteringar som bedömts. | FL 23/25/27/32; MB 9:3 och 26 kap.; processuell kontroll. | HT/BR/MF/MÖD – `VERIFIERAT I PRIMÄRKÄLLA` |
| AUD-031 | 2026-05-19 | Thomas Duvsjö / FB-representant | Senare förstahandsuppgift om kvarstående fenomen vid nytt besök. | V1/S1 tills original låsts | Visar att rapporterat fenomen inte bara hänförs till mars/april. | Bevisar inte teknisk orsak. | Exakt vittnesuppgift, FB-personens identitet, eventuell anteckning. | Bevisvärdering; MB/JB beroende forum. | VITTNE/FB/MÖD – `SOURCE-LOCK KRÄVS` |
| AUD-032 | 2026-06-03 | Länsstyrelsen beslut | Länsstyrelsen avslår/ger inte ändring av MF:s avslut. | P1 | Processuell överprövning och domstolskedja. | Bevisar inte att varje bakomliggande sakfråga är tekniskt utredd. | Originalbeslut och skäl. | Specialprocess + FPL där tillämpligt. | MÖD – `VERIFIERAT` |
| AUD-033 | 2026-07-10 | Marko/Björn-besök | Arbetsmaterial anger att FB-husvärd Marko upplevde någon form av doft/“något”. | P3/P2/S1 beroende på källa | Potentiellt senare FB-förstahandsbevis om avvikelse efter avslutad MF-tillsyn. | Bevisar inte orsak eller olägenhet i miljöbalkens mening. | Original ljud/mejl och rätt personidentitet. | Bevisvärdering; ny omständighet efter 13 april. | FB/MF-post13/MÖD – `SOURCE-LOCK KRÄVS` |
| AUD-034 | 2026-08-16 | Ny vistelse/felanmälningsspår | Återkommande besvär rapporteras på nytt. | P2 | Visar fortsatt upplevt fenomen efter tidigare beslut. | Bevisar inte orsak. | Original felanmälan och eventuell extern observation. | JB/MB ny tillsyn/remedy. | FB/MF-post13 – `SOURCE-LOCK KRÄVS` |
| AUD-035 | 2026-08-17 | Ny felanmälan + Jennifer | Ny anmälan; Jennifer föreslår längre personligt besök för att själv uppleva inomhusmiljön. | P1 | Visar att FB fortfarande hanterar ny rapport och att föreslaget underlag initialt är personlig observation. | En förvaltares egen symtomupplevelse är inte objektiv teknisk undersökning. | Exakt mejlkedja och om mätning/teknisk metod alls planerades. | JB 12:15–16; MB självkontroll/tillsyn som argument; bevisprincip. | FB/HYRA/MF-post13 – `VERIFIERAT` mejlspår |
| AUD-036 | 2026-08-19 | MMD dom M 5167-26 | MMD avslår/ändrar inte och använder enligt arbetsmaterial formulering om att utredning/åtgärder motsvarat ärendets beskaffenhet. | P1 när domen source-lockats | Direkt mål för prövningstillstånds-/granskningsargumentet. | Bevisar inte att varje identifierad kompletteringsfråga faktiskt kan följas i akten. | Originaldom, exakt domskäl, fullföljdshänvisning. | LOMMD + lagen om domstolsärenden för PT; FPL-kommentar metodiskt. | MÖD – `SOURCE-LOCK KRÄVS` exakt ordalydelse/frist |
| AUD-037 | 2026-08-20–28 | SBK OVK/tillsyn | SBK uppger bl.a. att varje lägenhet inte måste redovisas individuellt i OVK och att ärende 2026-06369 handläggs; fokus måste vara faktisk räckvidd för objekt 0562/system 01. | P1 | Avgränsar PBL/OVK-spåret och förhindrar felargument om formellt krav på varje lägenhet i protokoll. | Bevisar inte att just 0562/system 01 faktiskt var kontrollerat eller tekniskt korrekt vid relevant tidpunkt. | Original OVK för system 01/02, objektkoppling, SBK handlingar. | PBL/PBF/OVK-regler – aktuell lag/föreskrift. | SBK/VENT – `STARKT STÖD`, objektfråga öppen |
| AUD-038 | 2026-08-24–29 | OVK 2022 ombesiktning | Identifierad handling anger system 02, bostäder 7–11, godkänd 2022-11-08; fråga kvarstår om Kilsgatan 3/0562 tillhör annat system. | P1 | Kan visa räckviddsproblem i den handling som använts som “godkänd OVK”. | Bevisar inte automatiskt att 0562 saknade giltig kontroll. | Original system 01 handling, byggnads-/systemmatris. | PBL/PBF/OVK; teknisk dokumenträckvidd. | SBK/VENT/MÖD – `SOURCE-LOCK KRÄVS` innan extern slutsats |
| AUD-039 | 2026-08 | SSBF/RVR/S:t Erik | SSBF har brandhändelse; RVR har ingen rapport; S:t Erik uppges inte ha skadeanmälan för Kilsgatan 3 i den egna försäkringsakten. | P1 när respektive svar används | Kartlägger dokumentationskedjan och luckor. | Frånvaro hos RVR/S:t Erik bevisar inte att ingen sanering eller annan försäkringslösning förekom. | Exakta originalbesked, andra möjliga försäkringsgivare/entreprenörer, FB intern skadeakt. | Bevisvärdering; offentlighet/bolagsdokumentation separat. | BRAND/OFF – delvis `VERIFIERAT`, inferens förbjuden |
| AUD-040 | 2026-08-27/28 | Jennifer om SBK + besök | Jennifer uppger att hon fått en tillsynsanmälan från SBK som hon ska svara på och att hennes planerade besök var för att själv uppleva det Erica beskriver. | P1 | Ny kunskapsmarkör och framtida källa: FB:s svar till SBK kan visa deras aktuella tekniska/faktiska position. | Bevisar inte vad FB kommer att svara eller att personlig observation ersätter utredning. | Begär in/inhämta FB:s yttrande till SBK. | PBL-tillsyn; bevisning; JB/MB endast indirekt. | SBK/FB – `VERIFIERAT` mejl, yttrande väntas |

---

# 3. PROCESSAUDIT – MILJÖFÖRVALTNINGEN

Detta lager ska nu kontrollera MF enligt följande kedja för **varje materiell fråga**:

`fråga identifierad → uppgift begärd → svar inkom → svar kommunicerat → svar värderat → skäl synligt före beslut`

## 3.1 Prioriterade kontrollfrågor

| Fråga | Vad fanns före 13 april? | Vad måste hittas i akten? | Nuvarande status |
|---|---|---|---|
| Orsaken till återkommande reaktioner | Återkommande partsuppgifter, flera åtgärder, vittnen, 23-dygns vädring | Vilken undersökning ansågs faktiskt besvara orsaks-/olägenhetsfrågan? | **ÖPPEN / HUVUDFRÅGA** |
| OCAB:s räckvidd | OCAB fukt-/missfärgningsrapport + tidig fråga om dess scope | Varför fick rapporten den betydelse den fick? | **ÖPPEN** |
| Tre städningar / MouldOut / Mögel bort | 2025-23696-97 + foto 98 | Bedömning av varför dessa medel användes, vad som beställts och utebliven effekt | **INGEN BEDÖMNING IDENTIFIERAD ÄNNU** |
| Kanalrensning / 5 m | FB-uppgift i MF-spåret | Vilken primär utförandehandling verifierade åtgärden? | **SOURCE-LOCK / ÖPPEN** |
| Ventilationens rumsfördelning | 4 nov-data + 11 mars-data | Teknisk bedömning av metod/status och betydelse | **TEKNISK SAKKUNNIG KRÄVS** |
| Vittnesuppgifter | Inlämnade före beslut enligt arbetsmaterial | Hur värderades de som fenomenbevis? | **SOURCE-LOCK AKT** |
| Andra inspektörens observationer | Erica har redovisat uppgifter om sötare lukt/ättika m.m. | Tjänsteanteckning eller annan dokumentation från personen | **SOURCE-LOCK KRÄVS** |
| 9 april-kompletteringen | Omfattande inlaga/bilagor | Registrering, genomgång, kommunicering, bedömning före 13 april | **HÖGSTA PROCESSPRIORITET** |

---

# 4. KANALRENSNING – DELAUDIT

Nuvarande verifieringskedja:

`4 nov teknisk anteckning “rensningen av kanal” → 5 nov detaljerad partsredogörelse utan rensningsbegrepp → 6 nov “rengjorde ventilkanalerna” i Ericas kommunikation → 11 nov möte → 12 nov “rengöring i kanal ... smart början” → 2 dec Jennifer framtidsform → 17 dec ca 5 m enligt arbetsmaterial → 15 jan “5 m upp” enligt MF-spår`

### Styrande fråga

> **Är dessa uppgifter olika beskrivningar av samma åtgärd eller flera separata åtgärder?**

Ingen materiell motsägelse får påstås förrän följande är source-lockat:

- 4 nov driftanteckning,
- 11 nov ljud,
- 2 dec originalmejl,
- 17 dec ljud,
- 15 jan originalhandling,
- arbetsorder/utföranderapport.

---

# 5. STÄDNING / MÖGELINRIKTADE MEDEL – DELAUDIT

Verifierad kronologi:

- **27 okt** – första professionella städningen.
- **20 nov** – andra städningen; foto visar `TASKI Sani MouldOut`.
- **20 nov kväll** – Erica skriver till Gaby att städarna uppgett att viss ingrodd påverkan inte går bort.
- **27 nov** – tredje städningen; `Mögel bort` dokumenteras i inlämnat material.

### Vad detta juridiskt kan användas till

Inte som bevis för att mögel är konstaterat.

Det kan användas för att fråga:

1. vad beställde Familjebostäder,
2. varför valdes dessa produkter,
3. vilka ytor behandlades,
4. vad observerade städfirman,
5. vilken effekt fick behandlingen,
6. hur värderade MF att ytorna redan behandlats flera gånger före tillsynen 11 mars.

**Högprioriterad source-lock:** arbetsorder/reklamation inför 20 november och 27 november.

---

# 6. BRAND / SANERING – DELAUDIT

Styrande kedja:

`brand 16 nov 2017 → räddningstjänstens information till FB → skaderegistrering → skadebedömning → sanering → återställning → slutkontroll → senare dokumentation`

### Nuvarande status

- branden: **verifierad historisk händelse**,
- uppgift att sanering skett: **FB-uppgift, inte självverifierande**,
- sammanhängande sanerings-/återställningskedja: **inte identifierad**,
- RVR/S:t Erik-frånvaro: **dokumentationsinformation, inte bevis för att sanering saknades**,
- teknisk koppling från 2017 till dagens besvär: **KAN INTE FASTSTÄLLAS**.

---

# 7. VENTILATION / OVK – DELAUDIT

### Separera alltid

1. **luftflöde vid ett mättillfälle**,
2. **ventilationssystemets tekniska funktion över tid**,
3. **lägenhetens totala inomhusmiljö**,
4. **orsaken till rapporterade reaktioner**.

De är inte samma bevistema.

### Prioriterade luckor

- objekt 0562/system 01 – exakt dokumenträckvidd,
- system 02 / bostäder 7–11 får inte användas som automatisk verifiering av 0562,
- teknisk jämförelse 2018/2022/4 nov 2025/11 mars 2026 kräver metod- och statuskontroll,
- kanalrensningens faktiska utförande måste skiljas från luftflödesjustering.

---

# 8. BEVISKLASSNING – VAD FÅR INTE GÖRAS

Följande formuleringar är förbjudna externt tills bevisningen räcker:

- “Det var mögel” enbart från bilder eller produktnamn.
- “Branden orsakar dagens besvär” utan teknisk kausalitetsutredning.
- “Ingen sanering skedde” enbart därför att dokument inte hittats.
- “Ingen kanalrensning skedde” enbart därför att Erica inte nämnde den 5 november.
- “Jennifer/Gaby ljög” på grund av olika uppgifter utan full source-lock och alternativförklaring.
- “OVK var ogiltig för fastigheten” innan korrekt system-/objekträckvidd är klar.
- “MF ignorerade materialet” innan hela akten visar att materialet inte bedömdes.

Använd i stället:

> **Materialet fanns tillgängligt, men dess bedömning har ännu inte kunnat identifieras i den kända akten/beslutsmotiveringen.**

---

# 9. JURIDISK FUNKTIONSKARTA

| Spår | Huvudfråga | Relevant rätt | Bevis som primärt behövs |
|---|---|---|---|
| MF/MÖD | Var utredningen tillräcklig och kontrollerbar? | FL 23, 25, 27, 32 §§ där tillämpliga; MB 26:21–22; specialprocess för MÖD | Aktkedja + originalfrågor/svar/kommunicering/beslut |
| Olägenhet | Finns en störning som enligt medicinsk/hygienisk bedömning kan påverka hälsan? | MB 9:3, 9:9, försiktighets-/kunskapsregler där tillämpliga | fenomenbevis + teknisk/medicinsk utredning |
| Hyresrätt | Är bostaden brukbar och finns brist/hinder/men? | JB 12:9, 15, 16 och eventuella påföljdsregler | konkret brist, användbarhet, åtgärdsbehov, tid |
| Ventilation/OVK | Vilken kontroll gällde just system/objekt och vad visar den? | PBL/PBF/OVK-föreskrifter | originalprotokoll, systemmatris, sakkunnig |
| Brand | Vad skedde efter branden och vad kan verifieras? | ansvar/MB/JB beroende konkret fråga | SSBF + FB skadeakt + sanering + slutkontroll |
| Offentlighet | Vilka handlingar finns och hur har utlämnandefrågor hanterats? | TF 2 kap., OSL 6:3 m.fl. | diarier, formella beslut, utlämnandebegäranden |

**Aktuell lagtext och senare praxis ska alltid kontrolleras före extern juridisk slutversion.**

---

# 10. SOURCE-LOCK-KÖ – PRIORITERING

## PRIORITET A – påverkar MÖD / utredningsfrågan direkt

1. MMD-dom 19 augusti – exakt domskäl och fullföljdshänvisning.
2. MF:s kompletta kedja 11/12 mars → kompletteringsfrågor → FB-svar → 9 april → 13 april.
3. Aktlogg för `2025-23696-97` och `2025-23696-98` + intern bedömning.
4. 11 november-ljud – full talaridentifiering och kanalrensnings-/orsaksdiskussion.
5. 17 december-ljud – exakt 5 m-uppgift, provtagning, lukt och åtgärder.
6. 2 december Jennifer – exakt kanalrensningstempus och brand/saneringsuppgift.
7. 15 januari FB→MF – exakt femmetersuppgift.

## PRIORITET B – teknisk kedja

8. arbetsorder/utföranderapport 4 nov och eventuell separat kanalrensning,
9. arbetsorder/reklamation städning 20 och 27 nov,
10. OVK system 01 / objekt 0562 samt systemmatris,
11. OCAB:s beställning/scope och full rapport,
12. teknisk sakkunnig om betydelsen av flödesförändringar, don, kanal, tryck och system.

## PRIORITET C – kunskap/ansvar

13. Gaby/FB beställningskedja till städfirman,
14. FB:s skade-/saneringsakt 2017,
15. FB:s kommande yttrande till SBK,
16. Marko 10 juli – exakt uttalande/personroll,
17. Peter/andra senare förstahandsuppgifter.

---

# 11. STATUS I HUVUDTIDSLINJEN

## Får gå in i `TIDSLINJE.md`

Endast poster där originalkälla är identifierad och faktum kan formuleras utan inferens.

Exempel:

- officiell brandhändelse 16 nov 2017,
- verifierade mejldatum och vad mejlet faktiskt säger,
- mötesdatum 11 nov verifierat genom bokning/efterföljande mejl,
- foto 20 nov med Sani MouldOut,
- MF-inspektion och beslut,
- Länsstyrelse/MMD-beslut när original finns.

## Får INTE gå in som faktum ännu

- att “5 m kanalrensning faktiskt utfördes” utan utförandehandling,
- att en viss person “förnekade branden” utan originalcitat,
- att viss biologisk tillväxt är mögel utan sakkunnig analys,
- att branden orsakar dagens besvär,
- att MF avsiktligt ignorerade material,
- att FB avsiktligt dolt eller undanhållit information.

---

# 12. KONTROLLPANEL – NUVARANDE HUVUDSTATUS

| Huvudområde | Styrka idag | Största öppna fråga | Nästa bevis |
|---|---|---|---|
| Återkommande rapporterat fenomen | **STARKT som fenomen/tidsmönster** | teknisk/medicinsk orsak | oberoende sakkunnig + source-lock vittnen |
| FB:s kunskap | **STARK** | vad gjordes efter varje ny uppgift? | kunskaps-/AO-logg |
| MF:s utredningskedja | **CENTRAL MEN OFULLSTÄNDIG** | vilka frågor följdes till verifierbart svar och bedömning? | full akt/source-lock |
| Kanalrensning | **DOKUMENTATIONSGLAPP** | en eller flera åtgärder, när, var, hur? | arbetsorder + 11/17 dec ljud |
| Städning/MouldOut | **STARKT DOKUMENTERAT ÅTGÄRDSVAL** | varför användes medlen och vad beställdes? | städfirmans order/rapport |
| Brand | **BRAND VERIFIERAD, EFTERKEDJA ÖPPEN** | skade/sanering/slutkontroll | FB skadeakt + entreprenör |
| OVK/ventilation | **TEKNISKT RELEVANT MEN RÄCKVIDDSKÄNSLIGT** | objekt 0562/system 01 | rätt OVK + sakkunnig |
| Hyresrätt/brukbarhet | **MÖJLIGT STARKT REMEDYSPÅR** | konkret brist/åtgärd som kan föreläggas | teknisk utredning |
| MÖD/PT | **PROCESSUELLT HUVUDSPÅR** | går MMD:s slutsats att kontrollera mot källkedjan? | source-lock dom + MF-akt |

---

# 13. Styrande kärna

> **Caset ska inte byggas på att den tekniska orsaken redan är bevisad. Caset ska byggas på vad som faktiskt kan visas om återkommande fenomen, faktisk användbarhet, Familjebostäders kunskap och åtgärdsval, undersökningarnas verkliga räckvidd, dokumentationsluckor och den processuella frågan om hur relevanta frågor följdes från identifiering till svar, kommunicering och uttrycklig bedömning.**

Och för varje ny bevispost ska STORA AUDITEN uppdateras före extern användning:

`ny källa → klassificera → source-lock → direkt bevisvärde → begränsning → juridisk funktion → lagkontroll → spårstatus → extern användbarhet`.

---

# 14. Arbetsregel för framtida material

När Erica skriver **`@GitHub audit denna`**, **`@GitHub STORA AUDITEN`** eller laddar upp ny information som ska in i huvudlagret ska följande göras:

1. läs originalet i sin helhet,
2. skapa/uppdatera en AUD-post,
3. ange datum och exakt källa,
4. klassificera P1/P2/P3/S1/V1/A1,
5. skriv endast den faktiska uppgiften – ingen dold inferens,
6. ange juridisk funktion,
7. ange uttryckligen vad beviset **inte** visar,
8. ange source-lock/komplettering,
9. koppla till relevant lag/princip och markera om aktuell lagkontroll krävs,
10. ange HT/BR/MF/MÖD/FB/VENT/KANAL/BRAND/STÄD/VITTNE/HYRA/OFF/SBK,
11. kontrollera om `TIDSLINJE.md` och `BEVISREGISTER.md` ska uppdateras,
12. håll sammanställningar/transkriptioner markerade som sådana tills originalfilen är verifierad.

**STORA AUDITEN är från och med 29 augusti 2026 projektets kontrollpanel för bevisdisciplin och källstatus.**