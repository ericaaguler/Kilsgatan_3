# Struktur – huvudtidslinje, bevisfunktion och separata sakspår

**Fastställd:** 29 augusti 2026

## 1. En huvudtidslinje

`TIDSLINJE.md` är den enda kanoniska huvudtidslinjen.

Alla daterbara relevanta uppgifter ska kunna landa där, oavsett om de senare används i ett särskilt sakspår.

Huvudtidslinjen ska innehålla hela händelsekedjan, inte bara slutresultatet:

- vad Erica skrev,
- vad andra skrev,
- vad som sades/gjordes vid möten,
- vad som beställdes eller utfördes,
- vad som inte blev gjort,
- frågor som ställdes,
- frågor som inte besvarades,
- löften om senare svar,
- motsägande besked,
- dokument som efterfrågades,
- dokument som återfanns eller saknades,
- relevanta vittnesuppgifter,
- Ericas förstahandsanteckningar med tydlig status.

**Huvudtidslinjen ska beskriva fakta/källstatus – inte blanda in juridiska slutsatser i själva kronologin.**

## 2. Originalkällor

Originalkällor ligger under exempelvis:

- `korrespondens/`
- `bevis/`
- `handlingar/`
- `inspelningar/`
- `transkriptioner/`

Originalkällan får aldrig ersättas av en sammanfattning.

## 3. Bevisregister

`BEVISREGISTER.md` är källindexet.

En post i bevisregistret ska kunna länkas till en eller flera händelser i huvudtidslinjen.

## 4. Anteckningar

`anteckningar/` används för Ericas egna anteckningar, korrigeringar och juridiska arbetsanteckningar.

De ska bevaras även när de ännu inte kunnat verifieras fullt ut. De får inte tyst tas bort när en senare källa hittas.

Aktiva huvudfiler:

- `anteckningar/2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md`
- `anteckningar/2026-08-29_HUVUDANTECKNING-JURIDISK-BEVISFUNKTION.md`
- `anteckningar/2026-08-29_BRAND-TILLSYN-FRAGELOGG-MALNING-OCH-DOKUMENTATIONSLUCKA.md`

Den sistnämnda filen är ett obligatoriskt bevarandelager för nya fynd från tillsynen 11 mars, Outlook-frågeloggen och dokumentationsspåret. Den får inte kortas bort när externa tidslinjer förenklas.

Tillåtna statusar:

- `SOURCE-LOCKAD`
- `STÖDS AV KÄLLA MEN EXAKT ORDALYDELSE EJ LÅST`
- `ANVÄNDARENS FÖRSTAHANDSUPPGIFT/ANTECKNING`
- `VITTNESUPPGIFT`
- `BEHÖVER VERIFIERAS`
- `MOTSÄGELSE`
- `DOKUMENTATIONSLUCKA`
- `OBESVARAD FRÅGA`

Anteckningar ska versionshanteras och får inte ignoreras av Git.

## 5. Bevis- och rättsfunktionslager

Huvudfil:

- `analyser/BEVIS-OCH-RATTSFUNKTION-HUVUDAUDIT-ALLT-MATERIAL-2026-08-29.md`

Varje relevant bevis/händelse ska här kunna få juridisk funktion, exempelvis:

- `J1 KÄNNEDOM`
- `J2 FAKTISKT SKICK/HINDER`
- `J3 SYMPTOM-/EXPONERINGSMÖNSTER`
- `J4 TEKNISKT SCOPE`
- `J5 MOTSÄGELSE/TILLFÖRLITLIGHET`
- `J6 DOKUMENTATIONSLUCKA`
- `J7 MYNDIGHETENS KÄNNEDOM`
- `J8 UTREDNINGSVAL/AVGRÄNSNING`
- `J9 BESLUTSMOTIVERING`
- `J10 DOMSTOLENS UTREDNING`

Detta lager svarar på **vad ett bevis faktiskt kan användas till juridiskt** och lika viktigt **vad det inte kan bevisa ensamt**.

## 6. Auditlager

Följande filer styr auditten:

- `analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md`
- `analyser/AUDIT-FYND-OCH-OMISSION-REGISTER-2026-08-29.md`
- `analyser/PROJEKTAUDIT-KILSGATAN-3-2026-08-29.md`
- `analyser/MF-AKT-01-107-BRAND-SANERING-AUDIT-2026-08-29.md`
- `analyser/MF-AKT-01-107-KONTROLLREGISTER-2026-08-29.md`
- `analyser/BEVIS-OCH-RATTSFUNKTION-HUVUDAUDIT-ALLT-MATERIAL-2026-08-29.md`
- `analyser/STORA-AUDITEN-BEVIS-KRONOLOGI-RATTSFUNKTION-2026-08-29.md`
- `analyser/BRAND-FRAGELOGG-OCH-MF-TILLSYN-11-MARS-2026.md`

Den sista filen är ett särskilt kontrollager för:

- tillsynsljud/transkribering 11 mars,
- Hevals målningråd,
- toxiner/rökpartiklar som diskuteras men inte provtas,
- muntlig observation om tung luft,
- MF:s ännu inte färdiga beboelighetsbedömning på plats,
- räknad frågelogg till FB och MF,
- dokumentationsluckan efter branden.

Auditfilerna registrerar sådant som:

- saknas i huvudtidslinjen,
- finns men är för kortfattat,
- har fel datum,
- har fel person,
- saknar ordalydelse,
- saknar källa,
- är motsägelsefullt,
- är en dokumentationslucka,
- är en obesvarad fråga,
- bara finns i ett tidslinjetillägg,
- saknas i relevant separat spår,
- har fel juridisk funktion eller överdriven slutsats.

## 7. Nya obligatoriska auditfynd 29 augusti 2026

Följande får inte tappas bort i senare versioner:

1. **Heval / tillsyn 11 mars:** Erica rekommenderas i ljudet att tacka ja till målning/åtgärd: **”Jag tycker att du ska tacka ja.”** Talaridentitet ska slutlåses mot originalet vid extern direktcitering.
2. **Toxiner/rökpartiklar:** frågan diskuteras men provtas/tekniskt utreds inte under tillsynen.
3. **Tung luft:** en inspektör säger muntligt att det känns tungt; detta är observation, inte orsaksbevis.
4. **Beboelighet:** på plats sägs i sak att MF ännu inte tagit ställning; ventilationsresultat ska först bedömas.
5. **7 januari 2026:** Outlook-tidsstämpeln korrigerar tidigare 6 januari-datering för det omfattande MF-yttrandet.
6. **9 mars 2026:** Erica ber två dagar före tillsynen MF kräva in uppgifter/dokumentation om eventuell sanering efter rök/brand.
7. **Frågelogg:** konservativt minst **5** materiella frågetillfällen till Familjebostäder och minst **7** till Miljöförvaltningen, totalt minst **12**.
8. **6 november 2025:** FB:s löfte att `felsöka vad problemet är` ska alltid följas till frågan vilken utredning som faktiskt identifierade grundorsaken.
9. **Dokumentationskedjan:** SSBF verifierar händelsen och FB-kontakten; S:t Erik saknar skadeärende för Kilsgatan; RVR hittar ingen rapport; SBK redovisar inget efterbrandsspår; FB har fortfarande inte redovisat en sammanhängande primär akt för efterarbetet.
10. **Målning vs orsaksutredning:** Hevals praktiska råd ska hållas isär från Malin Larssons senare principiella besked att målning för att stänga in eventuella problem inte är lämplig metod och att orsaken ska utredas och åtgärdas.

## 8. Tidslinjetillägg

Daterade `TIDSLINJE-TILLAGG-*` och `TIDSLINJE-KOMPLETTERING-*` är tillfälliga arbetslager under audit.

De är inte konkurrerande huvudtidslinjer.

Varje källsäkrad händelse i ett tillägg ska därefter föras in i `TIDSLINJE.md`.

## 9. Separata spår

Separata spår skapas efter att huvudmaterialet är tillräckligt komplett. De ska vara filtrerade vyer av huvudtidslinjen och kunna länka tillbaka till samma källor.

### Brand / brandhistorik / dokumentation

- branden 2017,
- vem som senare informerar om branden,
- vittneskedjan,
- FB:s kännedom,
- FB:s nekanden/besked,
- frågor om sanering,
- varje dokumenterat tillfälle där brand-/saneringsfrågan ställs och om den faktiskt besvaras,
- frågor om dokumentation,
- försäkrings-/skadehantering,
- myndighetskontakter,
- MF:s avgränsning 9 januari och återöppning i mars,
- tillsynen 11 mars och exakt vad som inte undersöktes,
- målningråd kontra orsaksutredning,
- kvarstående dokumentationsluckor.

### Ventilation / kanalrensning

- ventilationsproblem,
- Caroline/Karolins besök,
- mätningar och justeringar,
- ventilationsdon/lock,
- rengöring inne i kanal/rör,
- när uttrycket `kanalrensning` först förekommer,
- vem som föreslår åtgärden,
- vad Micke/Jennifer/Gaby uppger,
- beställning,
- utförande,
- omfattning/längd,
- kontroll före/efter.

### Städning / sanering / ytskikt

- första, andra och tredje städningen,
- reklamationer,
- vad som inte gick bort,
- vad som därefter klassades som underhåll,
- målning,
- köksstomme,
- golv,
- eventuella saneringsfrågor.

### Hälsa / exponeringsmönster

- datum för vistelser,
- vem som varit i lägenheten,
- vilka symptom/reaktioner som uppges,
- om personen kände till problemet i förväg,
- vad som händer efter att personen lämnar/vädrar,
- tydlig markering att vittnesuppgifterna inte ensamma fastställer medicinsk kausalitet.

### Myndighetsspår

- Miljöförvaltningen,
- Stadsbyggnadskontoret / PBL / OVK,
- Länsstyrelsen,
- Mark- och miljödomstolen.

### Dokumentationsspår

- besiktningsprotokoll,
- OVK,
- arbetsordrar,
- brandskade-/saneringshandlingar,
- försäkringshandlingar,
- dokument som efterfrågats men inte återfunnits,
- exakt vilken aktör som sökts och vilket svar aktören gav.

## 10. Personkontroll

Personer ska alltid identifieras med fullständigt namn/roll när det behövs för att undvika sammanblandning.

Särskilt:

- **Thomas Bartsch** – Ericas vän; stöd/vittne i november 2025.
- **Thomas Duvsjö** – separat person/granne/vittne.

## 11. Händelser får tillhöra flera spår

En händelse kan samtidigt vara relevant för exempelvis brand, ventilation, dokumentation, hälsa och myndighetskännedom.

Den ska då **inte dupliceras som olika fakta**. Samma huvudtidslinjepost ska kunna märkas/länkas mot flera spår och flera juridiska funktioner.

Exempel:

`11 november 2025 – 1:a mötet med FB` kan samtidigt innehålla:

- branduppgift,
- ventilation,
- kanalrensningsfråga,
- ventilationsdon,
- beslut/åtgärder,
- vem som var närvarande,
- juridisk funktion: kännedom/motsägelse/tekniskt scope.

## 12. Juridisk argumentregel

Varje argument ska testas i fyra steg:

1. **Vad säger källan faktiskt?**
2. **Vilken juridisk funktion kan den fylla?**
3. **Vilket lagrum/princip är relevant och är aktuell rätt verifierad?**
4. **Vilket ytterligare bevis behövs för den starkare slutsatsen?**

Exempel:

- `Saknat saneringsintyg` = dokumentations-/verifieringslucka, inte automatiskt bevis för utebliven sanering eller juridisk obeboelighet.
- `Flera personer får symptom` = stöd för ett återkommande fenomen/utredningsbehov, inte automatiskt medicinsk kausalitet.
- `Godkänd OVK` = bevis inom OVK:s/systemets faktiska scope, inte automatiskt bevis att en specifik lägenhet är fri från alla inomhusmiljöproblem.
- `OCAB-rapport` = slutsats inom uppdrag/metod, inte svar på frågor den inte undersökt.
- `Tillsyn 11 mars` = bevis för vad som observerades/mättes/diskuterades, inte automatisk teknisk uteslutning av toxiner, rökpartiklar eller historisk brandsanering som inte provtogs/verifierades.

## 13. Obligatoriska arbetslinjer

Följande ska finnas kvar i audit-/argumentlagret:

> **Orsaksfrågan är fortfarande obesvarad i det granskade underlaget.**

> **En rapport kan inte besvara en fråga den aldrig har undersökt.**

> **En rapport kan inte fylla en historisk dokumentationslucka när de handlingar som skulle verifiera åtgärden aldrig har redovisats.**

> **Frågan är inte om brand-/saneringsfrågan var känd. Frågan är vilket verifierbart underlag som faktiskt besvarade den.**

## 14. `.gitignore`-regel

`.gitignore` får bara användas för lokala, tillfälliga eller tekniska filer. Repositoryt innehåller uttryckliga negationsregler som skyddar `anteckningar/`, `analyser/`, `bevis/`, `handlingar/`, `korrespondens/`, `inspelningar/`, `transkriptioner/` och huvudtidslinjer från att oavsiktligt ignoreras.

PDF, ljud, bilder och video ignoreras inte generellt. Om en specifik fil inte ska versionshanteras av integritets-, storleks- eller säkerhetsskäl måste beslutet dokumenteras så att källan fortfarande finns i auditens källförteckning.

## 15. Bevaranderegel

Ingen source-lockad uppgift eller viktig användaranteckning får försvinna genom att en äldre audit ersätts med en kortare sammanfattning.

När ett fynd korrigeras gäller:

`gammal uppgift → markera fel/osäker → bevara spårbarhet → lägg in korrigerad uppgift → länka till originalkälla`

Inte:

`gammal uppgift → radera utan spår`.

Särskilt gäller detta datumkorrigeringar, talaridentitet i ljud, personförväxlingar, obesvarade frågor och dokumentationsluckor.

## 16. Slutregel

**Originalkälla → bevisregister → anteckning/audit → juridisk bevisfunktion → huvudtidslinje → separat spår → extern juridisk argumentation.**

Först komplett huvudtidslinje. Därefter enskilda spår. Ingen separat tidslinje får ersätta huvudtidslinjen och inget viktigt material får falla bort när ett sakspår filtreras fram.
