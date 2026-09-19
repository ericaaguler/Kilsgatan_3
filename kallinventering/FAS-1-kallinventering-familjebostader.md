# FAS 1 – Källinventering för Familjebostäders påståendekatalog

**Ärende:** Kilsgatan 3, lägenhet 1202  
**Inventeringsdatum:** 2026-08-18  
**Inventerad version:** `main` vid commit `2fb1ebd837b7562b68f8cf303b3699c1ad6b1b1f`

## 1. Syfte och avgränsning

Detta dokument inventerar de källor i projektet som kan behövas för en fullständig katalog över vad AB Familjebostäder har sagt i ärendet.

FAS 1 avgör inte:

- om ett påstående är sant eller falskt,
- om två uppgifter motsäger varandra,
- om en undersökning är tillräcklig,
- eller vilken juridisk betydelse en uppgift har.

Den anger i stället:

1. vilka källor som faktiskt finns i repositoryt,
2. vilka källor som endast är registrerade som Outlook-bilagor eller återges i andra handlingar,
3. vilka efterfrågade källor som ännu saknas som självständiga originalfiler,
4. och vilket material som ska föras vidare till FAS 2 och FAS 3.

## 2. Källnivåer som ska hållas isär

| Nivå | Källtyp | Behandling i senare faser |
|---|---|---|
| K1 | Direkt meddelande från Familjebostäder, med metadata och fullständig text från Outlook-anslutningen | Primär källa till vad avsändaren skrev vid den tidpunkten |
| K2 | Självständig bilaga eller handling som finns som faktisk fil i repositoryt | Primär källa till handlingens eget innehåll |
| K3 | Bilaga registrerad i ett mejl med namn och Outlook-ID men inte uppladdad som fil | Känd men ännu inte innehållsverifierad; `UNDERLAG SAKNAS` tills filen hämtats |
| K4 | Äldre text som citeras i en mejltråd | Använd separat originalmejl om det finns; annars endast sekundär återgivning |
| K5 | Ericas, ett vittnes eller en tredje parts uppgift om vad Familjebostäder muntligen ska ha sagt | Parts-, vittnes- eller minnesuppgift; inte ett direkt Familjebostäder-uttalande |
| K6 | Tidslinje, bevisregister, trådindex eller tidigare sammanfattning | Endast index och navigationshjälp; inte bevis för sakpåståendet |

Outlook-filerna är direkta återgivningar från Outlook-anslutningen och innehåller Outlook-ID, datum, avsändare, mottagare och fullständig meddelandetext. De är inte råa MIME-/EML-exporter.

## 3. Repositoryts samlade bestånd

| Bestånd | Antal | Anmärkning |
|---|---:|---|
| Samtliga filer | 635 | Inventerat rekursivt på angiven commit |
| Markdownfiler | 616 | Mejl, trådindex, register, tidslinje och instruktioner |
| PDF-filer | 18 | 15 av de 16 uppladdade handlingarna samt 3 separat sparade mejlbilagor |
| PNG-filer | 1 | B0464, skärmbild av brandhändelseinformation |
| Individuella Outlook-mejl | 448 | B0001–B0448 |
| Trådar/vidarebefordrade grenar | 148 | Tråd 001–148 |
| Uppladdade handlingar 2026-08-18 | 16 | B0449–B0464 |
| Faktiska separat sparade mejlbilagor | 3 | B0003, B0007 och B0011 |
| Originalinspelningar | 0 | Endast README/instruktion finns |
| Transkriptioner | 0 | Endast README/instruktion finns |

De 16 uppladdade handlingarna består av:

- 9 partsinlagor från Erica: B0449–B0456 och B0463,
- 6 PDF-utskrifter av mejl som också finns som separata Outlook-bevis: B0457–B0462,
- 1 skärmbild av händelseinformation: B0464.

Partsinlagorna visar vad Erica skrev, uppgav eller yrkade. De verifierar inte automatiskt varje sakpåstående i texten.

## 4. Direkt korrespondens mellan Erica och Familjebostäder

Mappen `korrespondens/familjebostader/` innehåller 173 individuella mejl från 2025-09-24 till 2026-08-17:

- 85 mejl där Erica står som avsändare,
- 88 kandidatmejl där Familjebostäder, en anställd eller en funktionsbrevlåda står som avsändare.

De 88 kandidatmejlen är bruttomängden. Autosvar, nyhetsbrev, rena bokningar och tekniska systemnotiser ska granskas och vid behov sorteras bort från själva påståendekatalogen i FAS 2, men de bevaras i källinventeringen.

### 4.1 Familjebostäders avsändare

| Avsändare/funktion | Antal | Datumintervall | Bevis-ID |
|---|---:|---|---|
| Jennifer Ehlin | 11 | 2025-11-06–2026-08-17 | B0006, B0008, B0010, B0140, B0152, B0174, B0283, B0298, B0299, B0442, B0447 |
| Gaby Khalaf | 26 | 2025-11-06–2026-07-09 | B0092, B0095, B0098, B0101, B0106, B0107, B0109, B0117, B0119, B0120, B0121, B0124, B0125, B0131, B0132, B0135, B0138, B0156, B0163, B0172, B0188, B0206, B0366, B0368, B0372, B0375 |
| Leonard Thörnfeldt | 2 | 2025-10-29–2025-10-30 | B0076, B0079 |
| Anna Smed | 4 | 2025-10-30–2025-11-03 | B0080, B0082, B0083, B0086 |
| Ayub Mannai | 1 | 2025-09-24 | B0001 |
| Familjebostäder, namngiven/central avsändare | 3 | 2025-09-25–2026-02-26 | B0003, B0103, B0253 |
| FB Intresseanmälningar | 9 | 2025-10-06–2025-11-03 | B0013, B0015, B0018, B0019, B0026, B0059, B0064, B0085, B0088 |
| Info Kontakt Familjebostäder | 24 | 2025-10-07–2026-08-06 | B0023, B0025, B0030, B0031, B0034, B0044, B0048, B0049, B0055, B0060, B0071, B0073, B0077, B0091, B0126, B0127, B0226, B0333, B0342, B0345, B0373, B0390, B0392, B0394 |
| AB Familjebostäder/systemutskick | 7 | 2025-10-10–2026-07-15 | B0032, B0035, B0319, B0332, B0362, B0376, B0380 |
| GDPR-support | 1 | 2026-08-07 | B0398 |

### 4.2 Inledande bedömning av källkaraktär

- Jennifers och Gabys mejl utgör huvudkällor till deras skriftliga påståenden och bedömningar.
- Leonard Thörnfeldts mejl är särskilt relevanta för OCAB-/besiktningsunderlag eftersom bilagor registrerats.
- Funktionsbrevlådornas mejl kan innehålla både sakbesked och rena vidarebefordringar eller mottagningsbekräftelser. Varje meddelande måste därför granskas individuellt.
- Systemutskick om exempelvis reparatör på väg kan styrka att en bokning eller arbetskontakt fanns, men visar inte i sig att arbetet slutfördes eller vilken effekt det fick.
- Ericas 85 mejl är primärkällor till vad Familjebostäder fick information om och när. De är däremot inte Familjebostäders egna påståenden.

## 5. Separat Jennifer-bestånd

Jennifers 11 meddelanden är fullständigt identifierade ovan. Ett av dem, B0283, är ett autosvar och behöver normalt inte ge upphov till ett materiellt påstående.

Följande meddelanden ska prioriteras i FAS 2:

| Bevis-ID | Datum | Orsak till prioritering |
|---|---|---|
| B0006 | 2025-11-06 | Inledning av mötes-/utredningsspåret |
| B0140 | 2025-11-28 | Fortsatt handläggning och förslag om nytt platsmöte |
| B0152 | 2025-12-02 | Direkt besked efter den tidiga handläggningen |
| B0174 | 2025-12-12 | Direkt sakbesked i den längre Kilsgatan-tråden |
| B0298 | 2026-04-14 | Besked efter Miljöförvaltningens beslut |
| B0299 | 2026-04-14 | Ytterligare besked samma dag |
| B0442 | 2026-08-17 | Samlat svar om brukbarhet, inomhusmiljö, orsaksutredning, ventilation och astma-/allergianpassad bostad |
| B0447 | 2026-08-17 | Vidarebefordran av ny felanmälan/klagomål |

Detta är endast en prioriteringslista. Exakta påståenden och deras status registreras först i FAS 2–3.

## 6. Övriga kontrollkällor i Outlook-arkivet

Dessa mappar innehåller både externa primärkällor, Ericas egna mejl, autosvar och vidarebefordringar. Antalen är därför källbestånd, inte antal oberoende kontrollhandlingar.

| Källa/mapp | Antal mejl | Datumintervall | Funktion i senare kontroll |
|---|---:|---|---|
| Miljöförvaltningen | 41 | 2025-10-21–2026-08-11 | Kontrollera vad myndigheten faktiskt skrev och skilja det från Familjebostäders tolkning |
| Brand och försäkring | 13 | 2026-08-09–2026-08-17 | Kontroll av brandhändelse, överlämnande, restvärderäddning och försäkringsspår |
| Bostadsförmedlingen | 19 | 2026-01-13–2026-08-13 | Kontroll av uthyrningsinformation och senare besked |
| Sakkunniga och entreprenörer | 10 | 2025-09-26–2026-04-15 | Kontroll av uppdrag, tekniska bedömningar och möjlig provtagning |
| Vittnen | 11 | 2026-04-04–2026-08-17 | Kontroll av förstahandsuppgifter om reaktioner; inte teknisk orsaksbevisning |
| Myndigheter och stadsbolag | 46 | 2026-03-11–2026-08-17 | PBL-, diarieförings-, försäkrings- och ägarstyrningsspår |
| Domstol | 11 | 2026-03-11–2026-08-10 | Vad som skickats till eller kommit från domstol |
| Hyresgästföreningen | 118 | 2025-10-20–2026-08-18 | Rådgivning och vidarebefordrade uppgifter; måste hållas isär från FB-original |
| Övriga aktörer | 2 | 2025-10-06–2025-10-27 | Tidiga externa kontakter |
| Media | 4 | 2026-03-11 | Ericas partsuppgifter till medier; inte oberoende verifiering |

## 7. Efterfrågade källslag – tillgänglighet

| Efterfrågad källa | Tillgänglighet i repositoryt | Källstatus efter FAS 1 |
|---|---|---|
| Familjebostäders originalmejl | Ja, 88 kandidatmejl från FB-sidan | K1, med begränsningen att materialet är Outlook-återgivning och inte EML |
| Jennifers mejl | Ja, 11 | K1 |
| Gabys mejl | Ja, 26 | K1 |
| Markos dokumenterade uttalanden | Ingen direkt fil med Marko som avsändare och ingen inspelning/transkription | Endast eventuella K5-återgivningar tills direkt källa hittas |
| Inspelningar | Nej | UNDERLAG SAKNAS |
| Transkriptioner | Nej | UNDERLAG SAKNAS |
| Familjebostäders yttranden till myndigheter | Inte identifierade som självständigt uppladdade originalfiler | BEHÖVER LOKALISERAS i bilagor/diariehandlingar |
| Felanmälningar och svar | Delvis som mejl, ärendenummer och systemmeddelanden | K1 för meddelandena; interna ärendeposter/hela statusloggen saknas |
| Arbetsorder/beställningar | Inte uppladdade som självständiga arbetsorder | UNDERLAG SAKNAS |
| Driftteknikerns anteckningar | Registrerad som bilaga till B0442 men inte uppladdad | K3; UNDERLAG SAKNAS |
| OCAB-rapporten | `Rapport 716247-2025-10-18-161913.pdf` registrerad som bilaga till B0076 men inte uppladdad | K3; UNDERLAG SAKNAS |
| OVK | `1_2022-11-08.pdf` registrerad som bilaga till B0442 men inte uppladdad | K3; UNDERLAG SAKNAS |
| Miljöförvaltningens huvudhandling/beslut i 2025-23696 | `Ärende 2025-23696 Klagomål.pdf` registrerad som bilaga till B0442 men inte uppladdad | K3; UNDERLAG SAKNAS |
| Brandförsvarets händelserapport | `2017010144_Kilsgatan 3_2017-11-16.pdf` registrerad som bilaga till B0434 men inte uppladdad | K3; B0464 är endast en skärmbild av händelseinformation |
| Handlingar om sanering | Ingen självständig saneringsrapport, arbetsorder eller intyg lokaliserad | UNDERLAG SAKNAS; detta bevisar inte att sanering aldrig skedde |
| Bostadsförmedlingens handlingar | 19 mejl finns; ingen separat teknisk besiktning/uthyrningsakt lokaliserad | K1 för mejlen; övrigt BEHÖVER PRECISERAS |

## 8. Kända centrala bilagor som inte är materialiserade som filer

Följande bilagor är registrerade med namn och Outlook-bilage-ID men finns inte som självständiga filer i repositoryt:

| Bärande mejl | Bilaga | Varför central |
|---|---|---|
| B0076 | `Rapport 716247-2025-10-18-161913.pdf` | Uppges vara rapportunderlag i det tidiga OCAB-/besiktningsspåret |
| B0079 | `Besiktningsprotokoll.pdf` | Kan visa vad som faktiskt besiktigades och noterades |
| B0079 | `Skärmklipp på beställning.png` | Kan visa beställningens omfattning |
| B0079 | `Svar från Gaby angående sovrum 1.png` | Kan innehålla separat skriftligt FB-besked |
| B0442 | `Mätning av ventilation av vår drifttekniker Caroline Blomberg.docx` | Primär kontrollkälla för vad driftteknikern mätte och antecknade |
| B0442 | `1_2022-11-08.pdf` | Åberopat OVK-underlag |
| B0442 | `Ärende 2025-23696 Klagomål.pdf` | Åberopad myndighetshandling |
| B0434 | `2017010144_Kilsgatan 3_2017-11-16.pdf` | Brandförsvarets händelserapport |

B0076, B0079, B0442 och B0434 visar att bilagorna skickades eller registrerades med mejlen. De visar inte bilagornas fullständiga innehåll förrän filerna själva har hämtats och kontrollerats.

## 9. Filer som faktiskt finns som separata mejlbilagor

| Koppling | Fil | Källkaraktär |
|---|---|---|
| B0003 | `HopaGetView4Object.pdf` | Ritning/objektsunderlag som bifogades av Familjebostäder |
| B0007 | `Anmälan om brister ...pdf` | Ericas egen anmälan till Jennifer |
| B0011 | `delar installerades eller byttes ut i lägenheten.pdf` | Ericas egen begäran/formulär om installationsår |

Endast B0003 är en separat bilaga som kom från Familjebostäder. B0007 och B0011 är bilagor som Erica skickade till Familjebostäder.

## 10. Särskild bedömning av Marko-spåret

Ingen originalinspelning, transkription eller direkt skriftlig uppgift från Marko har lokaliserats i repositoryt.

Uppgifter om vad Marko sade vid platsbesök kan finnas i:

- Ericas samtidiga eller senare mejl,
- andra närvarandes vittnesuppgifter,
- Familjebostäders eventuella interna anteckningar.

Sådana uppgifter ska i FAS 2 klassificeras som parts-, vittnes- eller minnesuppgifter. De får inte citeras som om de vore ett direkt verifierat Familjebostäder-dokument utan att en direkt källa tillkommer.

## 11. Brister i källbeståndet som påverkar FAS 3

Följande luckor måste hållas synliga:

1. OCAB-rapportens originalfil saknas trots att bilagan är identifierad.
2. Driftteknikerns anteckningar saknas som fil.
3. Det åberopade OVK-protokollet saknas som fil.
4. Miljöförvaltningens åberopade huvudhandling saknas som fil.
5. Brandförsvarets händelserapport saknas som fil; en skärmbild ersätter inte rapporten.
6. Familjebostäders interna felanmälanshistorik, fullständiga arbetsorder, beställningar och avslutsanteckningar saknas.
7. Saneringsrapport, saneringsbeställning, intyg eller verifierbar entreprenörshandling har inte lokaliserats.
8. Originalinspelningar och transkriptioner saknas.
9. Direkt dokumentation från Marko saknas.
10. Eventuella yttranden som Familjebostäder lämnat direkt till Miljöförvaltningen behöver lokaliseras som egna handlingar.

Avsaknad av handling ska i senare faser beskrivas som `UNDERLAG SAKNAS`. Den får inte omformuleras till att den bakomliggande händelsen aldrig inträffade.

## 12. Överlämning till FAS 2

FAS 2 ska utgå från de 88 kandidatmejlen från Familjebostäder och behandla varje faktiskt meddelande separat.

För varje meddelande ska FAS 2 först avgöra om det innehåller minst ett materiellt:

- faktapåstående,
- bedömning,
- tolkning av tredje parts handling,
- plan/löfte,
- eller minnes-/muntlig uppgift.

Rena autosvar, nyhetsbrev, mottagningsbekräftelser och bokningsnotiser ska inte skapa materiella påståendeposter, men kan användas i löftes-/åtgärdsloggen eller kunskapsloggen när de faktiskt styrker ett relevant mottagande, en bokning eller en kontakt.

Verifiering mot OCAB, OVK, driftanteckningar, myndighetshandlingar och brandrapport ska inte slutföras förrän de registrerade bilagorna har materialiserats och lästs som egna källor.

---

**FAS 1-resultat:** Källpopulationen är identifierad. Ingen motsägelse eller sanningsbedömning har gjorts i detta dokument.
