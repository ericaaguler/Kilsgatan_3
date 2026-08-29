# STORA AUDITEN – kontrollpanel för hela Kilsgatan 3

**Status:** HUVUDLAGER  
**Funktion:** projektets kontrollpanel för bevisvärde, källkedja, juridisk funktion, luckor och extern användbarhet.  
**Primärnyckel:** `Bevis-ID` i `BEVISREGISTER.md`.

> **Detta är inte en sammanfattning.** STORA AUDITEN är kontrollagret ovanpå `BEVISREGISTER.md`, `TIDSLINJE.md` och samtliga sakspår. Varje uppgift ska kunna följas bakåt till källa och framåt till den juridiska fråga där den används.

---

## 1. Grundregel – tre nivåer får aldrig blandas ihop

1. **Vad källan faktiskt visar/säger.**
2. **Vad uppgiften juridiskt kan användas för.**
3. **Vad källan inte bevisar och vilken komplettering som saknas.**

Ett foto av en mörk beläggning bevisar exempelvis ett **synligt skick vid fotograferingstillfället**, men inte materialets kemiska eller biologiska identitet. Ett mejl där en part skriver att något är mögel bevisar att **uppgiften framfördes vid den tidpunkten**, men inte att materialet är tekniskt fastställt som mögel. En transkription är ett arbetsredskap tills ordalydelse och tidskod har kontrollerats mot originalinspelningen.

---

## 2. Datamodell – ingen dubbel sanning

För varje registrerad post B0001–B0464 gäller följande auditfält:

`Bevis-ID → datum → källa → faktisk uppgift → bevisklass → originalkontroll → juridisk funktion → vad den inte bevisar → saknad komplettering → relevant lag/princip → status i huvudtidslinjen/spåren`

**Datum, källa och faktisk uppgift hämtas kanoniskt från `BEVISREGISTER.md`.** De ska inte kopieras om i flera filer i onödan, eftersom dubblering skapar risk att två versioner senare skiljer sig åt. Auditmatrisen använder därför Bevis-ID som relationsnyckel och kompletterar den kanoniska posten med de fält som bevisregistret saknar.

Om datum/källa/faktisk uppgift ändras efter originalkontroll ska ändringen göras först i `BEVISREGISTER.md`; STORA AUDITEN ska därefter uppdateras.

---

## 3. Bevisklasser

| Klass | Betydelse | Typisk användning |
|---|---|---|
| **A1 – primär samtidshandling** | Ursprunglig eller nära ursprunglig handling från aktör/myndighet/entreprenör | Stark för att visa vad aktören meddelade, beslutade eller dokumenterade då |
| **A2 – primär bild/video/ljud** | Foto, video eller originalinspelning med verifierbar källa/tid | Stark för synligt/hörbart förhållande; kräver försiktighet om orsak/material |
| **B1 – samtida partsmeddelande** | E-post/SMS från Erica eller annan part | Stark för underrättelse, tidpunkt, vad som påtalats och partsuppgift; inte automatisk sanningsbevisning för sakpåståendet |
| **B2 – vittnesuppgift** | Namngiven tredje mans observation | Stöd för observerad händelse/symtom/lukt; värderas tillsammans med oberoende stöd |
| **C1 – myndighets-/bolagsbedömning** | Beslut, inspektionsrapport, svar eller tekniskt ställningstagande | Visar bedömningens innehåll och underlag; inte nödvändigtvis att sakfrågan är fullständigt utredd |
| **C2 – entreprenörs-/sakkunniguppgift** | Rapport, arbetsorder, service- eller skadeuppgift | Visar uppdrag, observation och åtgärd inom den omfattning uppdraget faktiskt hade |
| **D1 – partsinlaga/sammanställning** | PDF, egen sammanställning, analys eller argumentation | Visar vad som åberopats; bakomliggande fakta måste följas till ursprungskälla |
| **D2 – transkription/arbetsanalys** | Transkript, tidskodssammanställning, ChatGPT-analys | Endast arbetslager tills kontroll mot original |
| **H – hypotes/sökspår** | Möjligt samband eller minnesuppgift | Får styra utredning men inte presenteras externt som fastställt faktum |

---

## 4. ORIGINALKONTROLL – separat från gamla fältet ”Kontrollerat = Ja”

Det gamla bevisregistret har ett fält `Kontrollerat`. I STORA AUDITEN införs en **strängare extern-kvalitetsspärr**:

| Kod | Status |
|---|---|
| **O1 – original låst** | Native/originalfil finns och relevanta metadata/citat/tidskoder är kontrollerade. Kan normalt användas externt för exakt det källan visar. |
| **O2 – export/återgivning** | Outlook-export, PDF-utskrift eller skärmbild återger källan. Bra arbetsbevis, men kritiska citat/bilagor bör vid behov kontrolleras mot mailbox/native original. |
| **O3 – derivat** | Sammanställning, transkription eller analys. Måste tillbaka till original innan ordalydelse eller underliggande sakuppgift används externt. |
| **O4 – partsuppgift/hypotes** | Bevisar att uppgiften framförts men inte att den objektiva omständigheten är sann. Kräver oberoende stöd när sanningshalten är avgörande. |
| **OX – original saknas/ej lokaliserat** | Uppgiften får inte presenteras som direktbevis förrän originalet har lokaliserats. |

**Viktig regel:** `Kontrollerat = Ja` i BEVISREGISTER betyder inte automatiskt `O1`. Exempelvis en korrekt registrerad partsinlaga kan vara kontrollerad som fil men fortfarande vara `O4` beträffande de bakomliggande sakpåståendena.

---

## 5. Juridiska rättstaggar

Rättstaggarna anger **möjlig juridisk funktion**, inte att en viss rättsföljd redan är bevisad.

| Tagg | Lag/princip |
|---|---|
| **JB12:9** | 12 kap. 9 § jordabalken – fullt brukbart skick på tillträdesdagen |
| **JB12:15** | 12 kap. 15 § jordabalken – hyresvärdens skyldighet att hålla lägenheten i motsvarande skick under hyrestiden |
| **JB12:16** | 12 kap. 16 § jordabalken – skada, hinder/men och möjlig åtgärdsfunktion under hyrestiden |
| **MB9:3** | 9 kap. 3 § miljöbalken – definition av olägenhet för människors hälsa |
| **MB26:19** | 26 kap. 19 § miljöbalken – fortlöpande kontroll/egenkontroll för verksamhet som kan medföra olägenheter |
| **FL23** | 23 § förvaltningslagen – myndigheten ska utreda ärendet i den omfattning dess beskaffenhet kräver |
| **PBL-OVK** | PBL 8 kap. 25 §, PBF 5 kap. 1 § och OVK-regler – byggnadsägarens ansvar för obligatorisk funktionskontroll av ventilation |
| **KÄLLA** | Allmän bevis-/källkritisk princip: skilj original från derivat, samtidighet från efterhandsuppgift och observation från slutsats |
| **UNDERRÄTTELSE** | Bevisfunktion: visar när motpart/myndighet fick kännedom om en uppgift |
| **SPÅRBARHET** | Dokumentations-/processprincip: arbetsorder, statusändring, avvikelse och återrapportering ska kunna följas i källkedjan |
| **DUBBELRÄKNING** | En PDF-utskrift eller sammanställning som återger ett redan registrerat mejl är inte ett nytt oberoende sakbevis |

---

## 6. Övergripande auditstatus

| Kontrollområde | Status | Huvudrisk |
|---|---|---|
| Registrerade Bevis-ID | **B0001–B0464 finns i BEVISREGISTER** | Klassificering/originalberedskap behöver hållas separat från `Kontrollerat` |
| Huvudtidslinje | **Finns** | Nya visuella bevis från chatten är delvis analyserade men saknar egna B-ID och ska inte osynligt blandas in |
| E-post | **Omfattande** | Många poster är Outlook-återgivningar; kritiska citat och bilagor måste kunna gå tillbaka till mailbox/original |
| Ljud | **KARANTÄN för ej låsta citat** | Jennifer/Peter ”trasa” får inte citeras som verifierat innan originalfil + tidskod är låsta |
| Bilder/video | **Flera starka samtidiga visuella spår** | Bilden visar skick – inte materialidentitet, orsak eller ansvar |
| Brand 2017 | **Händelse styrkt på händelsenivå genom B0464** | Samband mellan 2017 års brand och senare material-/luktproblem är inte bevisat utan skade-/saneringskedja |
| Golvbyte 1 dec 2025 | **Visuellt öppet underlag dokumenterat av Erica** | Familjebostäder var enligt partsuppgift inte på plats; entreprenörens arbetsorder/avvikelserapport saknas |
| Städning | **Beställning/datum delvis styrkta genom SMS/mejl** | Exakt omfattning, instruktioner och återrapportering från entreprenören saknas |
| Ventilation | **Synligt avvikande skick dokumenterat** | Beläggningens identitet och exakt omfattning av ”5 meter kanalrensning” är inte tekniskt låsta |
| Miljöförvaltningens tillsyn | **Platsbesök/beslut finns i spåret** | Vad som faktiskt observerades, dokumenterades och vägdes in behöver jämföras mot originalanteckningar/foton |
| OVK 0562/system 01 | **Öppet kontrollspår** | Lägenhetsspecifikt/systemspecifikt underlag behöver fortfarande identifieras |
| Felanmälningar | **Flera statusspår** | Full audit trail, makuleringar/försvunna poster och teknisk återrapportering saknas |

---

# 7. HÖGPRIORITERADE POSTER – full juridisk audit

Detta är poster som redan nu bär flera centrala funktioner i ärendet. De ska alltid läsas tillsammans med den kanoniska raden i `BEVISREGISTER.md`.

| Datum | Källa | Faktisk uppgift | Bevisklass / original | Juridisk funktion | Vad den **inte** bevisar | Saknad komplettering | Lag/princip | Status huvudtidslinje/spår |
|---|---|---|---|---|---|---|---|---|
| 2017-11-16 19:50 | **B0464**, skärmbild av polisens händelseinformation | Larm om rök från lägenhet på Kilsgatan; torrkokning med kraftig rökutveckling; person kontrollerades av sjukvård | A1/B-officiell återgivning, **O2** | Styrker att brand-/rökhändelse inträffade; öppnar skade- och saneringsspår | Bevisar inte omfattningen av skador, vilka byggnadsdelar som påverkades eller att senare avvikelser kommer från branden | Original händelserapport/räddningstjänstrapport, skadeakt, sanerings- och återställningshandlingar | KÄLLA; skadehistorik; ev. JB12 | **TL: JA. Spår: BRAND** |
| 2025-10-01 14:41 | Originalvideo ”H 1 oktober 2025 kl 14.41” – analys i `analyser/2025-10-01_videoanalys_forsta-besok_kok-golv-radiator.md` | Visuella avvikelser syns redan vid första besöket efter nyckelhämtning | A2, originalvideo uppges finnas; **B-ID SAKNAS** | Ursprungsläge/alternativ orsak: visar att skicket föregår eget boende och senare åtgärder | Bevisar inte materialidentitet, orsak, hälsorisk eller vem som orsakat skicket | Registrera originalvideo med B-ID; lås filmetadata/hash; koppla till tillträdes-/besiktningshandling | JB12:9; KÄLLA | **TL: bör vara JA. Spår: TILLTRÄDE/KÖK. REGISTRERING KRÄVS** |
| 2025-10-08 08:32 | **B0027**, Erica → Familjebostäder, fotodokumentation köket | Familjebostäder mottog ett mejl med uttryckligt ämne om fotodokumentation av köket | B1, O2 | **Underrättelse/kännedom** före första samlade platsmötet; visar tidig dokumentationskedja | Bevisar inte i sig att varje bifogad bild granskades eller att sakpåståendena var riktiga | Kontrollera originalmejl + samtliga bilagor/OneDrive-länkar; fastställ exakt bildinnehåll | UNDERRÄTTELSE; JB12:9/15; KÄLLA | **TL: JA/bör vara JA. Spår: MAILFORENSIK/KÖK** |
| 2025-10-20 17:12 | **B0043**, Erica → Familjebostäder | Förtydligande frågor om OCAB:s analys, felanmälningar och åtgärder i köket skickades | B1, O2 | Underrättelse; visar att metod/omfattning, felanmälningar och köksåtgärder efterfrågades tidigt | Bevisar inte svaret på de tekniska frågorna | Originalmejl + bilagor; OCAB:s beställning och rårapport | UNDERRÄTTELSE; MB26:19; JB12:15 | **TL: JA/bör vara JA. Spår: OCAB/KÖK** |
| 2025-10-27 07:45 | SMS med Eds städfirma, uppladdad skärmbild i chatten | Erica frågar/bekräftar att städfirman ska komma till Kilsgatan 3 kl. 07.30 den 27 oktober | B1/A1 kommunikation, **B-ID SAKNAS** | Tidsfäster första professionella städningen; stöd för entreprenörskedja | Bevisar inte exakt beställningsomfattning eller resultat | Native SMS-export/skärmbild med hela tråden; Familjebostäders beställning/arbetsorder/faktura | KÄLLA; SPÅRBARHET | **TL: städspår; REGISTRERING KRÄVS** |
| 2025-11-06 | SMS med Eds städfirma | Eds uppger att de fått en beställning och behöver boka tid; Erica frågar vad Familjebostäder beställt och om hela köket städats 27 oktober | B1/A1 kommunikation, **B-ID SAKNAS** | Styrker entreprenörens uppgift om beställning samt tidig invändning mot städningens omfattning/effekt | Ericas ord ”mögel” i SMS bevisar inte tekniskt konstaterat mögel | Full SMS-tråd, beställning, arbetsbeskrivning, rapportering efter 27/10 | UNDERRÄTTELSE; SPÅRBARHET; KÄLLA | **Spår: STÄDNING. REGISTRERING KRÄVS** |
| 2025-11-06 10:49–11:37 | **B0092–B0093**, Gaby/Erica | Korrespondens om OCAB, städning, ventilation och kvarstående problem; Erica hänvisar till fotodokumentation efter städning | B1/C1, O2 | Kännedom och beslutsunderlag före första samlade mötet | Bevisar inte att Familjebostäder själva tekniskt kontrollerat varje bildpåstående | Lås full mejltråd och bilagor; kartlägg vilka interna arbetsordrar/beslut som fanns före 11/11 | UNDERRÄTTELSE; JB12:15; MB26:19 | **TL: MAILFORENSIK** |
| 2025-11-06 12:24 | **B0006**, Jennifer Ehlin | Jennifer föreslår att hon och husvärd ska gå igenom Ericas punkter på plats | C1/A1 e-post, O2 | Visar att ansvarig förvaltares samlade platsgenomgång ännu låg framför dem | Bevisar inte att ingen annan FB-anställd eller entreprenör tidigare varit i lägenheten | Interna besöks-/arbetsorderloggar före 6/11 | KÄLLA; SPÅRBARHET | **TL: JA. Spår: FÖRVALTNING/MAILFORENSIK** |
| 2025-11-07 10:57 | **B0007**, Erica → Jennifer | Erica klargör att saken inte bara gäller städning, beskriver brister/hälsopåverkan och ber Jennifer läsa bifogat underlag före mötet | B1, O2/O4 för sakpåståenden | Starkt underrättelsebevis: ansvarig förvaltare fick frågorna före mötet | Bevisar inte att bilagan faktiskt lästes eller att alla påståenden var tekniskt riktiga | Originalmejl/bilaga; intern vidarebefordran/läs-/ärendehistorik om sådan finns | UNDERRÄTTELSE; JB12:15; MB26:19 | **TL: JA. Spår: MAILFORENSIK** |
| 2025-11-10 15:15 | **B0098**, Gaby | Gaby skriver att ”vi tar allting på plats imorgon” och går igenom samtliga avvikelser samt tidsplan | C1, O2 | Tidsfäster att den samlade platsgenomgången fortfarande skulle ske 11/11 | Bevisar inte att ingen tidigare separat kontroll skett | Arbetsorder/inspektionsanteckningar före 11/11; protokoll från mötet 11/11 | KÄLLA; SPÅRBARHET | **TL: JA/bör vara JA. Spår: FÖRVALTNING** |
| 2025-11-11 14:00 | Första samlade mötet i lägenheten; ljudspår finns enligt projektet | Jennifer/Gaby/Micke m.fl. på plats; kanalrensning diskuteras enligt arbetsanalys | A2 om originalinspelning låses, annars D2/O3 | Direkt källa till vad som faktiskt sades och observerades på första samlade mötet | Arbetsanalys/transkript bevisar inte exakt ordalydelse utan kontroll mot ljud | Original ljudfil, full ordagrann transkription, tidskoder och deltagarlista | KÄLLA; SPÅRBARHET | **TL: JA. Spår: LJUD/VENTILATION. ORIGINALKONTROLL KRÄVS för citat** |
| 2025-11-27 | Professionell städning nr 3 + video av golv/sockel enligt projektmaterial | Visuellt avvikande/mörka områden dokumenteras samma dag som tredje städningen | A2 video + entreprenörsspår; **B-ID för video saknas** | Effekt-/resultatbevis: kvarstående visuellt skick efter upprepade städningar | Bevisar inte vad materialet är eller att alla synliga ytor ingick i städuppdraget | Originalvideo B-ID; städfirmans rapport 27/11; beställning och återrapportering | JB12:15; SPÅRBARHET; KÄLLA | **Spår: STÄDNING/KÖK. REGISTRERING KRÄVS** |
| 2025-12-01 | Bildserie från köksgolvbyte, fotograferad av Erica | Golvet är öppnat och underlaget/anslutningar syns; flera visuellt avvikande/mörka områden och löst material dokumenteras | A2 foto, **B-ID SAKNAS** | Visar ett konkret kontrolltillfälle när normalt dolda delar var åtkomliga; relevant för entreprenörens avvikelserapportering | Bevisar inte fukt, mögel, sot eller att Familjebostäder själva såg förhållandena. FB var enligt Erica inte på plats | Originalbilder + metadata/B-ID; arbetsorder; entreprenör; fuktmätning; egenkontroll; avvikelserapport; återrapportering till FB | JB12:15; MB26:19; SPÅRBARHET | **Spår: GOLVBYTE. REGISTRERING KRÄVS** |
| 2025-12-12 10:13 | **B0174**, Jennifer | E-post inför möte 17/12 finns registrerat | C1, O2 | Kan visa vilka frågor/åtaganden som skulle hanteras vid mötet | En registerrad med ämne bevisar inte exakt innehåll om fulltext inte läses | Läs/lås full originalmejl; extrahera exakt vilka frågor Jennifer lovade gå igenom | UNDERRÄTTELSE; SPÅRBARHET | **Spår: 17 DEC. FÖRDJUPNING KRÄVS** |
| 2025-12-17 | Original ljudinspelning från mötet | Arbetsanalys identifierar sekvens ca 16:31–18:12 om femmeters kanalrensning och att smuts i ventilation kan rengöras löpande | A2 endast efter originalkontroll; idag **D2/O3 för arbetsanalysen** | Kan bli direktbevis om åtgärdslogik och hur ventilationens synliga skick bedömdes | **Inte verifierat** att Jennifer exakt säger ”Peter” eller ”trasa” | Lokalisera originalfil, verifiera ordalydelse/tidskod, skapa ordagrann transkription med kontrollmarkering | KÄLLA; SPÅRBARHET | **Spår: LJUD/VENTILATION. KARANTÄN för ”Peter/trasa”** |
| 2026-01-05 20:18:42 | Originalvideo kök, analys `analyser/2026-01-05_videoanalys_kok-under-inredning.md` | Svårtillgängliga delar i/under köksinredning visar omfattande mörkbruna/svarta beläggningar, missfärgningar och ansamlingar | A2, originalvideo uppges verifierad; **B-ID SAKNAS** | Visar kvarstående visuellt avvikande skick efter städningar och golvåtgärd; relevant för omfattningen av tidigare undersökning/rengöring | Bevisar inte mögel, sot, mikrobiell tillväxt eller fuktorsak | Registrera originalfil/B-ID; teknisk provtagning/byggteknisk bedömning; jämför med arbetsorder | JB12:15; MB9:3; MB26:19; KÄLLA | **Spår: KÖKSSTOMME. REGISTRERING KRÄVS** |
| 2026-01-20 | Video ventilation | Synliga delar kring/inne i ventilationsöppning visar omfattande mörka beläggningar och nedsmutsning | A2; **B-ID/path ska låsas** | Visar visuellt skick efter tidigare ventilationsåtgärder och skapar kontrollfråga mot 5 m kanalrensning | Bevisar inte beläggningens material eller att samma del faktiskt skulle ha ingått i kanalrensningen | Originalvideo/B-ID; arbetsorder för kanalrensning; metod, sträcka, före/efter-dokumentation | PBL-OVK; JB12:15; MB26:19; KÄLLA | **Spår: VENTILATION. REGISTRERING/ORIGINALKOPPLING KRÄVS** |
| 2026-03-11 | Miljöförvaltningens platsbesök, ärende 2025-23696 | Platsbesök och ventilationskontroller ingår i tillsynsspåret; Erica uppger att synlig ventilation såg ut som januari-bilderna | C1 för myndighetshandlingar + O4 för Ericas likhetsuppgift | Prövning av tillsynens omfattning och underlag; vad såg myndigheten och vad utreddes? | Ericas efterhandsuppgift bevisar inte ensam exakt vad inspektörerna såg/noterade | Myndighetens originalfoton, fältanteckningar, mätprotokoll, frågeställning/metod och eventuell kommunicering med FB | MB9:3; FL23; KÄLLA | **TL: JA. Spår: MILJÖFÖRVALTNINGEN/VENTILATION** |
| 2026-04-13/15 | Miljöförvaltningens beslutsspår, bl.a. B0302 och handlingar i ärende 2025-23696/2026-9758 | Beslut/kommunikation finns registrerade och tillsynen avslutades enligt projektets ärendehistorik | C1, O1/O2 beroende på originalhandling | Visar myndighetens rättsliga/tekniska bedömning och vad som ansågs tillräckligt utrett | Ett beslut bevisar inte att en viss fysisk orsak faktiskt är identifierad om orsaksfrågan inte ingick i undersökningen | Originalbeslut + komplett akt + tjänsteanteckningar + vilka underlag som faktiskt låg före beslutet | FL23; MB9:3; KÄLLA | **TL: JA. Spår: MF/BESLUT** |
| 2026-05-26 15:39 | Video köksstomme | Senare video visar fortsatt visuellt avvikande mörkt/brunt/skadat material i konstruktionen | A2, **B-ID SAKNAS** | Tidsserie: jämförbar med 5 januari och tidigare öppna konstruktioner; relevant för om bakomliggande problem utretts/åtgärdats | Bevisar inte identitet, orsak eller att exakt samma punkt är oförändrad utan bildmatchning | Originalvideo/B-ID; positionsmatchning; teknisk undersökning/provtagning | JB12:15; MB9:3; MB26:19; KÄLLA | **Spår: KÖKSSTOMME. REGISTRERING KRÄVS** |
| 2026-06-23 | Samtal med Peter, ljudspår att lokalisera | Erica uppger att Peter uttalar sig om att man gjort vad man kan/att orsaken inte tagits reda på samt separat möjligt ”trasa”-spår | A2 om original låses; idag H/D2/OX för ej verifierad exakt ordalydelse | Kan bli viktigt för Familjebostäders egen kunskap om utredningens begränsning | Minnesbild/arbetsnotering bevisar inte exakt citat | Originalinspelning 23/6; tidskod; ordagrann kontrolltranskription | KÄLLA; SPÅRBARHET | **Spår: LJUD/PETER. ORIGINAL MÅSTE LÅSAS** |
| 2026-07-10 | Marko platsbesök enligt projektspår | Arbetsuppgift: Marko uppges ha känt ”någon form av doft”/”något” | A2 om ljud/video finns; annars O4 | Sen förstahandsobservation från FB-representant kan vara relevant för kvarstående problem efter MF-beslut | Arbetscitat bevisar inte exakt ordalydelse eller orsak | Originalinspelning/anteckning, deltagare, tidskod | KÄLLA; JB12:15 | **Spår: FB SENARE OBSERVATION. ORIGINALKONTROLL** |
| 2026-08-25 | Badrumsbild enligt projektmaterial | Mörka/missfärgade fogar är visuellt dokumenterade; Erica betecknar dem som mögel | A2 för bild, O4 för ordet ”mögel”; **B-ID SAKNAS** | Visar kvarstående synlig avvikelse sent i tidslinjen | Bilden ensam fastställer inte mögel/mikroorganismer | Originalbild/metadata/B-ID; teknisk bedömning/prov om materialidentitet ska åberopas | JB12:15; MB9:3; KÄLLA | **Spår: BADRUM. REGISTRERING KRÄVS** |

---

# 8. SYSTEMAUDIT AV REGISTRERADE B0001–B0464

Den fulla ID-matrisen finns i:

- [`audit/AUDIT-MATRIS-B0001-B0464.md`](audit/AUDIT-MATRIS-B0001-B0464.md)
- [`audit/OREGISTRERADE-BEVIS-OCH-ORIGINALKARANTAN.md`](audit/OREGISTRERADE-BEVIS-OCH-ORIGINALKARANTAN.md)

### Grundklassning för de 464 registrerade posterna

- **B0001–B0011:** e-postexporter; normalt B1/C1 beroende på avsändare, extern kvalitet O2 om inte native original separat har låsts.
- **B0012–B0448:** huvudsakligen `E-post (Outlook-återgivning)`. Dessa är registrerade och daterade men kritisk extern citering ska kunna gå tillbaka till mailbox/native original. Partens egna sakpåståenden är O4 i sanningsfrågan även när själva mejlet är autentiskt.
- **B0449–B0456:** egna partsinlagor/sammanställningar. **D1/O3–O4.** De visar vad som åberopats; varje underliggande sakuppgift måste följas till sin primärkälla.
- **B0457–B0462:** PDF-utskrifter av redan registrerade Outlook-mejl. **O2 + DUBBELRÄKNING.** De ska inte räknas som sex nya oberoende sakbevis när de återger B0207, B0223, B0149, B0171, B0189 och B0180.
- **B0463:** partsinlaga om hyresåterbetalning. **D1/O4.** Bevisar yrkande och åberopade grunder, inte automatiskt de bakomliggande sakförhållandena.
- **B0464:** skärmbild av brandhändelseinformation. **A1/O2.** Starkt stöd för att händelsen inträffade men bör kompletteras med original händelserapport/skadeakt för skadeomfattning och sanering.

---

# 9. EXTERN ANVÄNDNING – hård spärr

En uppgift får märkas **EXTERN-KLAR** endast om följande kan besvaras JA:

1. Är rätt original/ursprungskälla identifierad?
2. Är datum/tid och avsändare/deltagare verifierade?
3. Om citat används: är ordalydelsen kontrollerad mot originalet?
4. Om ljud/video: finns tidskod?
5. Om bild: beskriver texten bara det som faktiskt kan ses?
6. Om parten använder ord som mögel/sot/fuktskada: finns teknisk källa som fastställer just detta, annars har ordet tydligt märkts som partsuppgift/hypotes?
7. Om samma sak finns i flera PDF/mejl/sammanställningar: har dubbelräkning undvikits?
8. Är det klart vad beviset **inte** visar?
9. Är den juridiska funktionen relevant för den fråga där beviset används?
10. Är posten införd eller korrekt länkad i huvudtidslinjen/sakspåret?

Om någon punkt är NEJ ska posten vara **ARBETSMATERIAL / KOMPLETTERA**, inte ”bevisat faktum” i extern text.

---

# 10. KRITISKA ORIGINAL SOM SKA HÄMTAS/LÅSAS FÖRST

1. Original ljudfil 17 december 2025 – exakt sekvens om femmeters kanalrensning/rengöring; separat kontroll av ”Peter” och ”trasa”.
2. Originala Peter-inspelningar 13 januari, 19 maj och 23 juni – lokalisera rätt sekvens och tidskod.
3. Familjebostäders beställningar/arbetsorder och Eds städfirmas återrapportering 27 okt, 20 nov, 27 nov.
4. Arbetsorder/entreprenörsrapport/fuktmätning/egenkontroll från golvbytet 1 december 2025.
5. Originalbilder/video från tillträdet och senare konstruktion/ventilation som ännu saknar B-ID.
6. Miljöförvaltningens egna foton, fältanteckningar och råmätningar från 11 mars 2026.
7. Komplett OCAB-beställning, uppdragsavgränsning, rådata och eventuell avvikelserapport.
8. Brand-/skade-/sanerings-/försäkringskedjan efter 16 november 2017.
9. OVK-underlag som uttryckligen kan knytas till objekt 60020562/0562 och system 01.
10. Familjebostäders fulla systemlogg för felanmälningar: skapad, ändrad, makulerad/utförd/avslutad, användare, tid och teknisk återrapportering – inklusive fönsterbrädan.

---

# 11. Huvudfrågan auditlagret ska kunna besvara

> **Vilket dokumenterat tekniskt underlag visar att orsaken till de återkommande problemen i just objekt 60020562 faktiskt har identifierats, avgränsats och åtgärdats – och vilka delar av den slutsatsen bygger i stället på begränsade kontroller, partsuppgifter, sekundära sammanställningar eller antaganden?**

STORA AUDITEN ska inte besvara den frågan genom retorik. Den ska göra det möjligt att se **rad för rad** vilken källa som bär vilken del av bevisningen och exakt var kedjan fortfarande saknar en länk.
