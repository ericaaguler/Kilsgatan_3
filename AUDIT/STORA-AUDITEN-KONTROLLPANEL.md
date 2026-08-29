# STORA AUDITEN – KONTROLLPANEL

Detta är projektets huvudlager för beviskontroll. Det ersätter inte huvudtidslinjen utan styr vad som får användas som verifierat faktum.

## Obligatoriska fält per bevispost

**AUDIT-ID → datum → källa → faktisk uppgift → bevisklass → juridisk funktion → vad den inte bevisar → saknad komplettering → relevant lag/princip → status i huvudtidslinjen/spåren → source-lock-status**

## Statuskoder

- ✅ ORIGINAL KÄLLÅST
- 🟡 KÄLLA FINNS MEN ORIGINALKONTROLL KRÄVS FÖRE EXTERN ANVÄNDNING
- ⚠️ PARTS-/VITTNESUPPGIFT
- 🔴 SAKNAR ORIGINAL / EJ KÄLLÅST
- 🔵 ÖPPEN TEKNISK ELLER JURIDISK FRÅGA

## Bevisklasser

- A1 Officiell primärhandling
- A2 Motpartens egen primärhandling
- A3 Oberoende extern handling
- B1 Vittnesredogörelse som vittnet själv godkänt/lämnat
- B2 Samtida SMS/mejl om händelse eller upplevelse
- C1 Foto/film
- C2 Ljud/originalinspelning
- D Sammanställning, transkription eller inferens som måste tillbaka till original

---

# AUDITREGISTER

| Datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den inte bevisar | Saknad komplettering | Relevant lag/princip | Status |
|---|---|---|---|---|---|---|---|---|
| 2017-11-16 | Polis/SSBF | Dokumenterad brand-/rökhändelse på Kilsgatan 3. | A1 | Etablerar historisk händelse och motsäger påstående att ingen sådan händelse inträffat. | Bevisar inte att branden orsakar dagens besvär eller att sanering uteblev. | Full originalrapport och objektskoppling i bevisregistret. | Bevisvärdering; miljörättslig utredningsram. | ✅ Brandspår |
| 2018-11-30 | OVK 2018 | Objekt 0562 finns med: kök 10–27 l/s, bad 12 l/s. | A1 | Visar objektspecifik ventilationsdata och att viss äldre dokumentation finns. | Bevisar inte fullgod inomhusmiljö i alla avseenden 2025–2026. | Original-PDF och diariekoppling. | PBL/OVK. | ✅ OVK-spår |
| 2021-03-22–30 | Familjebostäders uppgift 15 jan 2026 | Vid uppgiven kanalrensning av fastigheten fick man inte tillträde till 562. | A2 | Visar enligt fastighetsägarens egen uppgift att 0562 inte omfattades av just den rensningen. | Bevisar inte att ingen annan rensning utförts. | Arbetsorder, entreprenörsrapport, avisering. | Egenkontroll; bevisvärdering. | ✅ Kanal/OVK |
| 2022-04-04 | OVK system 01 | 0562: kök 9–33, bad 15, sovrum 4 l/s. System 01 godkänt. Noteringar finns om ojämna flöden och läckage/otäthet på systemnivå. | A1 | Objektdata och systemnoteringar kan jämföras med senare mätningar. | Bevisar inte att 0562 hade formellt OVK-fel eller att systemnoteringarna orsakat senare besvär. | Eventuell åtgärdsredovisning. | PBL/OVK. | ✅ OVK |
| 2022-11-08 | OVK ombesiktning | Ombesiktningen omfattar endast system 02/bostäder 7–11; 0562 ingår inte. | A1 | Avgränsar dokumentets räckvidd. | Bevisar inte att system 01 saknade giltig kontroll. | Kontroll om separat senare system 01-handling finns. | PBL/OVK; bevisvärdering. | ✅ OVK |
| 2025-10-01 | Hyresförhållandet | Tillträde till lgh 1202/objekt 60020562. | A1/A2 beroende på kontraktskälla | Startpunkt för brukbarhets- och felkedjan. | Bevisar inte skick. | Hyresavtal/tillträdeshandling. | JB 12 kap. | ✅ Huvudtidslinje |
| 2025-10-02–08 | Foton + mejl/felanmälningar | Tidiga uppgifter om kök, ventilation, el och missfärgningar rapporteras. | C1+A2 | Visar tidig reklamation och kännedom. | Foto identifierar inte mögel, brandrest eller kemisk orsak. | Originalbilder med metadata och originalmejl. | JB 12 kap.; bevisning om reklamation. | 🟡 Foto/el/kök |
| 2025-11-04 | Ljudspår/sammanställning | Mätning/justering av ventilation och tilluft beskrivs; senare central jämförelse mot uppgift om 5 m kanalrensning. | C2/D | Potentiellt central för kanalrensningsmotsägelsen. | Transkription/sammanställning ensam bevisar inte exakt åtgärd. | Originalaudio + tidskoder + arbetsorder. | Bevisvärdering. | 🟡 MÅSTE TILL ORIGINAL LJUD |
| 2025-11-07–11 | SMS med Thomas på Torsbygatan | Thomas accepterar att följa med som stöd/vittne inför mötet 11 nov. | B2 | Styrker planerad vittnes-/stödroll och tidsanknytning. | Bevisar inte vad som sades på mötet. | Mötesaudio för mötesuttalanden. | Fri bevisprövning. | ✅ Vittnesspår |
| 2025-11-11 | Mötesaudio | Första större mötet; nuvarande transkript är ofullständigt. | C2/D | Kan styrka exakta uttalanden när source-lock är klar. | Ofullständigt transkript får inte användas som full bevisning. | Full genomlyssning av originalaudio och tidskoder. | Fri bevisprövning. | 🔴 MÅSTE TILL ORIGINAL |
| 2025-11-20 | Familjebostäder mejl | Kablar i köket beskrivs som ”feldragna” och ska demonteras/nymonteras fackmannamässigt. | A2 | Motpartens egen uppgift om konkret åtgärdsbehov. | Bevisar inte att installationen var olaglig eller vem som gjorde den. | Arbetsorder, utförare, egenkontroll. | JB 12 kap.; elsäkerhetsregler som teknisk ram. | ✅ Elspår |
| 2025-11-21 | SMS Peter | ”Nu är all el bortriven.” | A2 | Samtida bekräftelse att elåtgärd utförts. | Bevisar inte omfattning eller kvalitet. | Arbetsorder och egenkontroll. | JB 12 kap.; bevisvärdering. | ✅ Elspår |
| 2025-11-27 | Foto efter städning | Synlig mörk/brun beläggning/linje kvar vid köksbänk. | C1 | Visar synligt kvarstående skick efter rengöring. | Identifierar inte ämne eller orsak. | Originalfoto/metadata; ev. provtagning. | Bevisvärdering. | ✅ Städ/kök |
| 2025-12-02 | Jennifer/Familjebostäder | Kanalrensning beskrivs som något som ”kommer att ske”. | A2 | Central tidsmarkör mot senare uppgift att ca 5 m redan rensats. | Bevisar inte att rensningen senare genomfördes. | Beställning, arbetsorder, utförare. | Bevisvärdering. | ✅ Kanalspår |
| 2025-12-17 | Mötesaudio/sammanställning | Projektet innehåller uppgift om att ca 5 m kanalrensning redan skulle ha gjorts och att utlovade frågor inte genomgicks. | C2/D | Central motsägelse och frågehantering. | Får inte användas som verifierat citat utan originalkontroll. | Originalaudio + tidskoder + 12 dec-mejl. | Bevisvärdering. | 🟡 MÅSTE TILL ORIGINAL |
| 2026-01-09 | Miljöförvaltningen | MF frågar FB om senare OVK, kanalrensningens typ och vilket företag som utfört den. | A1 | Visar vilka kontrollfrågor myndigheten själv identifierade. | Bevisar inte att svaren senare verifierades. | MF:s kontroll/bedömning av svaren. | FL 23 §; MB 26 kap. | ✅ MF/kanal |
| 2026-01-15 | Jennifer till MF | Uppger 5 m kanalrensning i köket; 2021-rensningen saknade tillträde till 562; orsaken till hallukten är fortfarande oklar. | A2 | Stark motpartsuppgift och central motsägelse mellan åtgärd och kvarstående oklar orsak. | Bevisar inte själva utförandet av 5 m-rensningen. | Arbetsorder, datum, utförare, metod, rapport, efterkontroll. | MB 26 kap.; bevisvärdering. | ✅ Kanal/brukbarhet |
| 2026-03-11 | MF inspektion | Ingen avvikande lukt noterades. Flöden: kök 36, bad 4, sovrum 3, total 43 l/s; ca 8 Pa undertryck. | A1 | Officiell ögonblicksbild och ventilationsbedömning. | Bevisar inte orsaken till återkommande besvär eller material-/brandrelaterade frågor. | Metod/instrument och teknisk jämförelse vid behov. | MB 9 kap. 3 §; tillsyn. | ✅ MF/ventilation |
| 2026-03-26 | Erica till MF | Påtalar att eventuell brandpåverkan inte testats och att förhållanden förändrats före inspektionen. | Partsuppgift i primärhandling | Visar att invändningen fanns före beslutet. | Bevisar inte att brandpåverkan finns. | Teknisk provning/sakkunnig bedömning. | FL 23 §; MB tillsyn. | ✅ MF-process |
| 2026-04-04 | Thomas Duvsjö/Caroline | Godkänd vittnesredogörelse: snabb reaktion i 1202, tung luft/lukt, astmapåverkan/yrsel, förbättring i egen bostad i samma hus. | B1 | Förstahandsbevisning om upplevelse och kontrast mellan bostäder. | Bevisar inte medicinsk eller teknisk orsak. | Mejlad slutversion som primärbilaga. | Fri bevisprövning; MB 9 kap. 3 § sakfrågeram. | ✅ Vittnesspår |
| 2026-04-09 | MF | MF anger att konkreta indikationer för ytterligare brandtestning saknas. | A1 | Visar myndighetens avgränsning före beslut. | Bevisar inte att brandrelaterad påverkan tekniskt uteslutits. | Underlaget bakom avgränsningen. | FL 23 §; MB tillsyn. | ✅ MF/brand |
| 2026-04-13 | MF beslut 2026-5104 | Ärendet avslutas utan ytterligare åtgärd. | A1 | Huvudbeslutet i processkedjan. | Bevisar inte att alla tänkbara orsaker undersökts. | Full akt och beslutsunderlag. | FL 23 och 32 §§; MB. | ✅ Huvudtidslinje |
| 2026-04-14 | Aktinsynsbegäran | Begär bl.a. anteckningar, intern kommunikation och Stina Jurells anteckningar/roll. | A1/A2 | Visar att dokumentationsfrågan togs upp direkt efter beslutet. | Bevisar inte att handlingarna finns eller saknas. | Svar och aktförteckning. | TF 2 kap.; FL. | ✅ MF-process |
| 2026-05-18–19 | SMS Erica–Peter och Erica–Thomas Duvsjö | Erica ber om exakt tid p.g.a. symtom; Peter anger 09:30; Thomas försöker närvara. | B2+A2 | Styrker samtidiga uppgifter om symtom och FB:s kännedom. | Bevisar inte orsak. | Ljudfil från 19 maj. | Bevisning om reklamation/kännedom. | ✅ Peter/vittne |
| 2026-05-19 | Ljudspår 19 maj | Analysfil finns men är markerad NEED SOURCE LOCK. | C2/D | Kan bli viktig för exakta platsuttalanden. | Analysen får inte användas som verifierat ordagrant citat ännu. | Originalaudio + tidskoder + talare. | Fri bevisprövning. | 🔴 MÅSTE TILL ORIGINAL |
| 2026-05-24 | Erica till FB | Invänder mot att tidigare felärenden behandlas som avslutade och begär fortsatt utredning tills orsak dokumenterats. | A2 | Visar tydlig reklamation och kvarstående grundorsaksfråga. | Bevisar inte att intern status måste vara viss. | Full historik för 839920/846050. | JB 12 kap. | ✅ Felanmälningar |
| 2026-05-25 | Felanmälan 857001 | Dålig lukt; senare status ”Utförd”. | A2/systempost | Visar fortsatt felanmälan efter MF-beslut. | ”Utförd” bevisar inte att grundorsaken identifierats eller problemet upphört. | Arbetsorder, exakt åtgärd och resultat. | JB 12 kap.; bevisvärdering. | ✅ Felanmälningar |
| 2026-06-03 | Länsstyrelsen 21412-2026 | Överklagandet avslås. | A1 | Överinstansens prövning av MF-beslutet. | Bevisar inte att varje invändning analyserats uttryckligen. | Punkt-för-punkt-jämförelse mot överklagandet. | Förvaltningsprocess; motiveringsprincip. | ✅ Överinstans |
| 2026-06-14 | Felanmälan 864574 | Dålig lukt; senare ”Utförd”. | A2/systempost | Visar fortsatt problemrapportering. | ”Utförd” är inte bevis för löst grundorsak. | Arbetsorder/resultat. | JB 12 kap. | ✅ Felanmälningar |
| 2026-06-23 | SMS Erica–Peter | Erica skriver att hon har svårt att andas och är hjärntrött; väntar utanför. Peter kan komma om fem minuter. | B2+A2 | Samtida dokumentation av uppgivna symtom och husvärdens kännedom. | Bevisar inte medicinsk/teknisk orsak. | Koppla till ljud/anteckning från besöket. | JB 12 kap.; MB 9 kap. 3 § sakfrågeram. | ✅ Brukbarhet/Peter |
| 2026-06-24 | Felanmälan 867756 | Dålig lukt; senare ”Makulerad”. | A2/systempost | Visar ny felanmälan och senare administrativ makulering. | Makulering bevisar inte att problemet saknades eller löstes. | Makuleringsorsak och systemlogg. | JB 12 kap.; bevisvärdering. | ✅ Felanmälningar |
| 2026-07-02 | Felanmälan 870651 | Dålig lukt; först accepterad, senare makulerad. | A2/systempost | Visar statusförändring. | Bevisar inte varför den makulerades. | Full systemlogg. | JB 12 kap.; bevisvärdering. | ✅ Felanmälningar |
| 2026-07-09–10 | SMS Erica–Peter | Erica upprepar att hon får symtom och behöver framförhållning; 10 juli väntar hon utanför. | B2+A2 | Visar fortsatt kännedom hos husvärd. | Bevisar inte orsak. | Källås besöksljud/anteckning. | JB 12 kap. | ✅ Brukbarhet |
| 2026-07-10 | Marko – projektets ljud/transkriptspår | Uppgift finns om att Marko noterade någon form av doft. | C2/D | Potentiell personalobservation efter MF-beslutet. | Bevisar inte orsak eller hälsofara. | Originalaudio/video + tidskod. | Fri bevisprövning. | 🟡 MÅSTE TILL ORIGINAL |
| 2026-07-13 | Felanmälan 874860 | Objekt 60020562, dålig lukt; beställd/bokad; beskrivningen anger att ytterligare person blivit dålig 10 juli och att orsaken fortfarande inte utretts; senare makulerad. | A2/systempost | Stark samtidig intern FB-post om fortsatt problem. | Bevisar inte orsak eller skälet till makulering. | Makuleringslogg och arbetsorder. | JB 12 kap. | ✅ Felanmälningar |
| 2026-08-06 | SMS Thomas Duvsjö | Godkänner att hans redogörelser används i ärendet. | B2 | Stärker autenticitet och samtycke kring vittnesmaterialet. | Bevisar inte teknisk orsak. | Spara mejlade originalredogörelser. | Fri bevisprövning. | ✅ Vittnesspår |
| 2026-08-09–11 | MF-korrespondens | MF hänvisar till ”samma sakfråga”; 11 aug anges att nytt material registrerats men inte vidarebefordrats av MF till MMD. | A1 | Visar processhantering efter beslutet. | Bevisar inte att MF hade skyldighet att ompröva eller vidarebefordra allt. | Exakt e-postkedja/diarieföring. | FL/processregler. | ✅ MF/överinstans |
| 2026-08-10 | Stockholms Stadshus AB | Inga handlingar i det specifika fallet; hänvisning till S:t Erik. | A3 | Avgränsar dokumentkedjan. | Bevisar inte att FB saknar egna handlingar. | FB:s arkiv/gallringsspår. | Offentlighets-/dokumenthantering. | ✅ Brand/dokument |
| 2026-08-10/17 | S:t Erik Försäkring | FB var försäkrat 2017 men skadan anmäldes inte dit; inget skadeärende finns där. | A3 | Stark extern kontrollpunkt i försäkringskedjan. | Bevisar inte att ingen sanering eller intern hantering skedde. | FB:s interna skade-/beställningshandlingar. | Bevisvärdering. | ✅ Brand/försäkring |
| 2026-08-14/17 | Restvärderäddning | Ingen rapport hittas för händelsen. | A3 | Extern kontrollpunkt om avsaknad av RVR-rapport. | Bevisar inte att sanering aldrig utfördes. | Entreprenörs-/beställningsspår hos FB. | Bevisvärdering. | ✅ Brand/sanering |
| 2026-08-17 | Jennifer/Familjebostäder | FB bedömer bostaden brukbar sedan dag 1 och inomhusmiljön fullgod; hänvisar till luftflöden, OVK och MF. | A2 | Central motpartsposition som ska jämföras mot tidigare oklar orsak, fortsatta åtgärder och felanmälningar. | Bevisar inte att alla andra möjliga orsaker utretts. | Dokumentlista bakom slutsatsen ”fullgod”. | JB 12 kap.; MB 9 kap. 3 §; bevisvärdering. | ✅ Brukbarhet |
| 2026-08-17 | Erica till FB | Frågar varför tre felanmälningar makulerats och vad som faktiskt utförts i två andra. | A2 | Definierar konkreta kontrollfrågor. | Bevisar inte att statusarna är felaktiga. | Fullständigt svar + systemloggar. | JB 12 kap.; bevisvärdering. | ✅ Felanmälningar |
| 2026-08-17 | Jennifer svar | Identifierat svar redovisar inte varför de tre ärendena makulerades eller exakt vad ”Utförd” innebar i de två andra. | A2 | Visar ett svarsgap i den identifierade korrespondensen. | Bevisar inte att svar aldrig lämnats i annan kanal. | Sök hela ärende-/mejlhistoriken. | Bevisvärdering. | ✅ Felanmälningar |
| 2026-08-19 | Folkhälsomyndigheten, Malin Larsson | Generell vägledning: orsaken ska utredas vid konstaterade brister; målning för att stänga in eventuella problem är inte lämplig metod. | A3/officiell vägledning | Metodstöd för orsaksutredning. | Är inte beslut i det enskilda ärendet och bevisar inte mögel/fukt i 1202. | Länka FHM:s vägledning. | MB 9 kap. 3 §; FHM-vägledning. | ✅ Metod/juridik |
| 2026-08-19 | MMD M 5167-26 | Överklagandet avslås; domstolen återger bl.a. okänd orsak och vittnesuppgifter men har korta domskäl. | A1 | Central processhandling. | Bevisar inte att varje konkret motsägelse analyserats uttryckligen. | Punkt-för-punkt-audit av överklagande mot domskäl. | Förvaltningsprocess; motiveringsprincip. | ✅ Överinstans |
| 2026-08-20–25 | SBK-korrespondens | SBK anger bl.a. att varje lägenhet inte behöver redovisas i OVK-protokoll; objekt 60020562/system 01 efterfrågas specifikt. | A1 | Avgränsar vad OVK kan och inte kan visa. | Bevisar inte att lägenheten är ”PBL-godkänd” eller hälsofrisk. | Exakt aktuellt SBK-mejl ska source-lockas; klarlägg kontrollhandlingar efter brand. | PBL/OVK. | 🟡 SBK/OVK |
| 2026-08-25 | Samlad dokumentkontroll | Viss objektspecifik dokumentation finns, men en sammanhängande verifierad kontrollkedja för alla relevanta tekniska åtgärder före/efter brand och inför dagens inomhusmiljöbedömning har ännu inte kunnat byggas. | D | Definierar dokumentationsproblemet utan att påstå ”ingen dokumentation alls”. | Bevisar inte att en viss handling inte finns någonstans. | Fortsatt akt-/arkivsökning. | Egenkontroll; tillsynsutredning; bevisvärdering. | 🔵 Övergripande huvudfråga |

---

# MATERIAL SOM MÅSTE TILLBAKA TILL ORIGINAL FÖRE EXTERN ANVÄNDNING

| Post | Nuvarande läge | Krav |
|---|---|---|
| 11 nov 2025 – kanalrensningssamtal | Ofullständigt transkript/sammanställning | Originalaudio, exakt tidskod, talare och kontext |
| 17 dec 2025 – 5 m kanalrensning/frågor | Sammanställning + ljud finns | Originalaudio + tidskod + 12 dec-mejl |
| 19 maj 2026 – Peter/Thomas | Analysfil, NEED SOURCE LOCK | Originalaudio + tidskoder + talaridentifiering |
| 10 juli 2026 – Markos observation | Projektanteckning/transkript | Originalaudio/video + tidskod |
| ”5 m kanalrensning” som faktiskt utförd teknisk åtgärd | Partsuppgift finns | Arbetsorder, datum, utförare, metod, rapport och efterkontroll |
| Foto som påstås visa mögel/mikrobiell tillväxt | Foto/användartext | Beskriv endast synligt skick tills prov/sakkunnig finns |
| Brand 2017 → dagens symtom | Historik + symtom | Teknisk kausalitetsutredning krävs |
| ”Ingen sanering skedde” | Inga hittade rapporter hos flera aktörer | Frånvaro av dokument får inte likställas med bevis att åtgärd aldrig skedde |
| ”Ventilationen är felaktig” generellt | OVK + mätningar | Beskriv exakta värden/noteringar; system 01 var formellt godkänt |
| ”Lägenheten saknar dokumentation” | För stark formulering | Använd: sammanhängande objektspecifik kontrollkedja har inte kunnat verifieras |
| ”Lagbrott” | Juridisk hypotes | Rekvisit, faktum, ansvar och regel måste prövas innan etiketten används |

---

# MASTER QUEUE – SAKNAD KOMPLETTERING

## Familjebostäder
- Arbetsorder/rapport för påstådd 5 m kanalrensning.
- Full historik för 839920, 846050, 857001, 864574, 867756, 870651, 874860 inklusive statuslogg och makuleringsorsak.
- Arbetsorder/egenkontroll för elåtgärden.
- Brandrelaterad sanerings-/återställningsdokumentation 2017 om sådan finns.
- Objektspecifik egenkontroll-/underhållshistorik.
- Underlaget bakom slutsatsen 17 aug 2026 att bostaden varit brukbar sedan dag 1 och att inomhusmiljön är fullgod.

## Miljöförvaltningen
- Stina Jurells egna anteckningar/roll.
- Dokumenterad värdering av uppgiften om kanalrensning.
- Full akt före 13 april inklusive tillgängliga interna anteckningar.
- Kartläggning av vilka orsaker som faktiskt bedömdes, tekniskt uteslöts eller lämnades öppna.

## Stadsbyggnadskontoret / OVK
- Full objektsökning för 60020562/0562, system 01.
- Eventuella separata kontroller/åtgärdsredovisningar efter OVK 2022.
- Exakt vilka brand-/kontrollhandlingar som finns respektive inte finns registrerade.

## Originalmedia
- 11 nov audio.
- 17 dec audio.
- 19 maj audio.
- 10 juli audio/video.
- Originalfoton med metadata för tillträde, kök, ventilation, städning och badrum.

---

# JURIDISK FUNKTIONSKARTA

Den juridiska kolumnen anger **vilken rättslig funktion bevisposten kan få**, inte att ett lagbrott är fastställt.

- **JB 12 kap.** – brukbarhet, brist, reklamation och hyresrättsliga påföljder.
- **MB 9 kap. 3 §** – ram för olägenhet för människors hälsa.
- **MB 26 kap.** – tillsyn och underlag/utredning.
- **FL 23 §** – myndighetens utredningsansvar.
- **FL 32 §** – motivering av beslut där tillämpligt.
- **PBL/OVK** – ventilationskontroll och byggnadstillsyn; inte ett generellt friskintyg för en lägenhet.
- **TF 2 kap.** – allmänna handlingar hos myndigheter/organ som omfattas.
- **Fri bevisprövning** – SMS, vittnen, ljud och foton bedöms efter vad de faktiskt kan styrka.

---

# STYRREGEL FÖR HELA PROJEKTET

Varje ny bevispost ska först in här och få full klassning innan den används i externa skrivelser. En post får inte markeras ”extern användning klar” om den bara bygger på sammanställning, användarens återberättande, transkription utan originalkontroll, teknisk diagnos från foto eller slutsats från att en handling ännu inte hittats.

Detta är kontrollpanelen för huvudtidslinjen och samtliga mikrotidslinjer.