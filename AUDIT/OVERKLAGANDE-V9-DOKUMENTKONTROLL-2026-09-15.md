# Dokumentkontroll mot överklagande V9 – 2026-09-15

## Syfte

Denna kontroll jämför överklagandeversionen V9 med repots faktiska trädlager. Målet är att skilja mellan:

- ett identifierat originaldokument,
- en källåtergivning eller korrespondenspost,
- en analys/metadatafil,
- och ett dokument som ännu inte har kunnat återfinnas.

Ett dokument markeras inte som ett säkrat original enbart för att det nämns i en tidslinje, analys eller korrespondensåtergivning.

## Kontrollunderlag

- Uppladdad handling: `M-5167-26_Overklagande_Erica_Guler_V9_REVIEW_2026-09-07.pdf`
- Omfattning: 14 sidor
- SHA-256: `dd48db9e78ecd703ce48a1335e442a04c0bdc9f46c7f073f728e7c4c84c66d9c`
- GitHub-repository: `ericaaguler/Kilsgatan_3`
- Kontrollerad branch/commit: `main` / `6c81603e479a59179b568a1435757cf3a43230b2`
- Bilageförteckningen i V9 finns på sida 14.

## Resultat per åberopad handling

| Nr | Åberopad handling i V9 | Status i repot | Identifierad täckning eller brist |
|---:|---|---|---|
| 1 | Miljö- och hälsoskyddsnämndens beslut 13 april 2026, akt 105 | **ORIGINAL EJ IDENTIFIERAT** | Det finns analyser, tidslinjer och korrespondens om beslutet, men ingen identifierad original-PDF eller aktfil med beslutet i repots trädlager. |
| 2 | Länsstyrelsens beslut 3 juni 2026, dnr 21412-2026 | **ORIGINAL EJ IDENTIFIERAT** | Beslutet nämns i process- och tidslinjematerial, men ingen identifierad originalhandling med dnr 21412-2026 finns som egen fil i trädlagerkontrollen. |
| 3 | Nacka tingsrätts mark- och miljödomstols dom 19 augusti 2026, M 5167-26 | **ORIGINAL EJ IDENTIFIERAT** | Det finns domstolskorrespondens och analyser av domen, men ingen identifierad originaldom som egen PDF/aktfil i repot. |
| 4 | Relevanta e-post- och handläggningsakter, särskilt akt 84, 85, 89, 90 och 92–96 | **DELVIS TÄCKT – AKTORIGINAL EJ LÅSTA** | Det finns flera korrespondensåtergivningar, bland annat `B0254`, `B0255`, `B0297` och `handlingar/outlook-utskrifter/`. De kan inte automatiskt likställas med de angivna MF-akterna. Akt 84, 85, 89, 90, 92, 93, 94, 95 och 96 behöver identifieras mot originalakten. |
| 5 | Skriftliga förstahandsuppgifter i akt 100, 102 och 103 | **DELVIS TÄCKT – AKTORIGINAL EJ IDENTIFIERADE** | Vittnesrelaterade Outlook-återgivningar finns i `korrespondens/vittnen/`, bland annat för Karolin Bast, Jimmy Bast och Thomas Duvsjö. De exakta aktoriginalen 100, 102 och 103 finns inte identifierade som separata originalfiler. |
| 6 | Fotodokumentation i akt 87, 88, 98, 101 och 104 | **ORIGINAL EJ IDENTIFIERADE** | Repot innehåller parts-PDF:er och vissa bilder, men ingen säker separat originalfilskedja för just akt 87, 88, 98, 101 och 104. Fotona måste kopplas till rätt akt/datum innan de räknas som säkrade aktbilagor. |
| 7 | OVK-protokoll 4 april 2022 | **ORIGINAL EJ IDENTIFIERAT** | Det finns OVK-analyser och hänvisningar till system 01/objekt 0562, men ingen identifierad original-PDF för protokollet från 4 april 2022 i trädlagerkontrollen. |
| 8 | OVK-protokoll 8 november 2022 | **METADATA/ANALYS FINNS – ORIGINALFIL SAKNAS I TRÄDLAGRET** | `bevis/ovk/2022-11-08-system02-kilsgatan-7-11-dokumentidentitet-och-dubblettsparr.md` och `bevis/ovk/2022-11-08-ombesiktning-byggnad-2-kilsgatan-13-21.md` låser dokumentidentitet, scope och dubblettinformation. De underliggande PDF-filerna finns inte som egna binärer i det kontrollerade repot. |
| 9 | Caroline Blombergs ventilationsanteckning 4 november 2025 | **DELVIS TÄCKT – ORIGINAL .DOCX SAKNAS** | Jennifers källåtergivning från 17 augusti 2026, `B0442`, listar Outlook-bilagan `Mätning av ventilation av vår drifttekniker Caroline Blomberg.docx`. Själva DOCX-originalet finns inte identifierat i trädlagerkontrollen. |
| 10 | Jennifer Ehlins e-post 17 augusti 2026 med bifogat OVK-protokoll | **KORRESPONDENS FINNS – BILAGOR DELVIS SAKNADE** | `korrespondens/familjebostader/2026-08-17_1030_B0442_...` finns som Outlook-återgivning och innehåller bilageuppgifter. Bilagorna ska inte räknas som säkrade original förrän de faktiska filerna finns eller hämtas från källan. `B0447` finns också som separat senare meddelande. |
| 11 | Jenny Hamrins e-post 3 september 2026 och äldre OVK-protokoll för Kilsgatan 1–11 och 13–23 | **MEJL FINNS – ÄLDRE OVK-ORIGINAL EJ FULLT IDENTIFIERADE** | `korrespondens/stadsbyggnadskontoret/2026-09-03_1523_jenny-hamrin_ovk-2018.md` finns och är källklassad som originalmejl återgivet från Outlook. Den hänvisade 2018-handlingen och äldre OVK-protokoll behöver finnas som egna originalfiler eller uttryckligen märkas som ej återfunna. |
| 12 | Jennifer Ehlins e-post 7 september 2026 | **KORRESPONDENS FINNS** | `korrespondens/familjebostader/2026-09-07_0934_jennifer-ehlin_sv-ny-felanmalan-klagomal-kanalrensning-ao774725.md` finns. Den är en källåtergivning av meddelandet; eventuell original Outlook-export eller bilaga måste hållas separat om den finns. |
| 13 | Gaby Khalafs e-post 6 november 2025 om fortsatt felsökning | **KORRESPONDENS FINNS – EXAKT CITATKONTROLL KRÄVS** | `korrespondens/familjebostader/2025-11-06_1049_B0092_...` finns. Den angivna bevisfunktionen i V9 ska kontrolleras mot exakt meddelande och ordalydelse, inte enbart mot senare sammanställning. |

## V9-handlingen

Själva överklagandet V9 är nu inlagt som ett kanoniskt original i:

`handlingar/domstol/M-5167-26_Overklagande_Erica_Guler_V9_REVIEW_2026-09-07.pdf`

Detta är en separat handling från följeposten:

`korrespondens/domstol/2026-09-08_erica-overklagande-m5167-26-till-mod.md`

Följeposten har SHA-256 `92c55abb83df3c08d1239aac46afad130b7eb29f4fa1f1a29777d5178178275` och ska inte förväxlas med själva V9-PDF:en.

## Kritisk registeravvikelse

`BEVISREGISTER.md` slutar för närvarande vid B0464, medan trädlagerkontrollen visar senare filer med B0465–B0469 samt nyare icke-numrerade korrespondensposter från 28 augusti–15 september 2026.

Därför tilldelas V9 inte något gissat bevisnummer i denna kontroll. Nästa steg ska vara att:

1. stämma av B0465–B0469 mot bevisregistret,
2. fastställa vilka senare korrespondensposter som ska få bevis-ID,
3. därefter tilldela V9 nästa korrekta kanoniska bevisnummer,
4. och först då uppdatera `BEVISREGISTER.md`.

## Samlad slutsats

Överklagandet V9 kan nu spåras som handling, men V9:s bilageförteckning är ännu inte helt reproducerbar från repots egna originalfiler.

Repot har god täckning i form av korrespondensåtergivningar, analyser, tidslinjer och dokumentidentiteter. Den viktigaste kvarstående bristen är däremot att flera centrala myndighets- och domstolshandlingar samt underliggande OVK-, foto- och ventilationsoriginal inte finns som identifierade primärfiler.

**En sammanställning kan visa att ett dokument har åberopats. Den ersätter inte själva originalhandlingen.**
