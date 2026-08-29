# 34 – Besiktningsprotokoll 12 augusti vs 30 oktober – filjämförelse och korrigering

**Datum för audit:** 2026-08-30  
**Status:** SOURCE-LOCKAD FILJÄMFÖRELSE  
**Styrande funktion:** Korrigerar tidigare antagande att de två PDF-filerna i sig skulle visa två separata besiktningar eller att Gaby Khalafs namn/signatur finns i båda.

## 1. Granskade originalfiler

1. `60020562 Besiktningsprotokoll.pdf`
   - PDF-metadata: skapad 2025-08-12 10:06:09 UTC
   - Creator/Producer: PDFium
   - 3 sidor
   - SHA-256: `788582e5aa55973cddc0a4fe722c2a3f8f63578b038f0ee08941f67ac668cf37`

2. `Besiktningsprotokoll.pdf`
   - PDF-metadata: skapad 2025-10-30 11:07:55 UTC
   - Creator: JasperReports (`Besiktningsprotokoll_inflytt_FB`)
   - Producer: iText 2.1.7
   - 3 sidor
   - SHA-256: `84b3eac9c3e2999dda1726a819640571ba67b57a30c63fe10d120208277c88d6`

Filerna är alltså olika binära PDF-filer och skapades/genererades vid olika tidpunkter.

## 2. Vad båda protokollen faktiskt visar

Båda innehåller:

- objektsnummer `60020562`,
- Kilsgatan 3,
- **Besiktningsdag: 20250709 (9 juli 2025)**,
- avflyttningsdatum 20250930,
- samma huvudsakliga rumsposter,
- samma anmärkningar/status i sak,
- samma standardfält `Besiktningsvärd` på sista sidan.

Det centrala är därför:

> **De två PDF-filerna visar inte två olika besiktningsdagar. Båda hänför sig till samma angivna besiktningsdag: 9 juli 2025.**

Det går därför inte att använda dessa två PDF-filer som bevis för formuleringen att "två besiktningar" utfördes.

## 3. Faktiska visuella skillnader

Pixeljämförelse visar endast mycket små förändringar på sida 1 och 3; sida 2 är visuellt identisk.

### Version skapad 12 augusti 2025

- dokument-/genereringsdatum uppe till höger: `2025-08-12`,
- fältet för inflyttande hyresgäst på sida 1 är tomt,
- på sida 3 står `Inflyttande hyresgäst:` utan namn.

### Version skapad 30 oktober 2025

- dokument-/genereringsdatum uppe till höger: `2025-10-30`,
- `Erica Aylin Güler` har lagts in som inflyttande hyresgäst på sida 1,
- på sida 3 står `Inflyttande hyresgäst: Erica Aylin Güler`.

I övrigt är det granskade sakinnnehållet i rums-/anmärkningsdelen i praktiken samma, och sida 2 är pixelidentisk.

## 4. Besiktningsvärd / Gaby

På båda PDF-filerna finns på sida 3 en signaturrad med etiketten:

`Besiktningsvärd`

Men själva raden är **blank i båda**.

Ingen av de två granskade original-PDF:erna visar:

- namnet `Gaby`,
- namnet `Gaby Khalaf`,
- en läsbar signatur från Gaby,
- någon annan namngiven besiktningsvärd.

### Bevisstatus

**GRÖNT:** Besiktningsvärdsfältet är blankt i båda original-PDF:erna.  
**RÖTT:** Påstående att Gaby är signerad/namngiven som besiktningsvärd i någon av dessa två PDF-filer.

Detta utesluter inte att Gaby faktiskt utförde besiktningen. Den frågan måste styrkas genom annan primärkälla, t.ex. originalljud, intern FB-logg, systempost, arbetsorder eller annan handling där hans roll anges.

## 5. Vad de två PDF-filerna sannolikt representerar – juridiskt försiktig slutsats

Eftersom båda har samma besiktningsdag (9 juli), samma objekt och i huvudsak samma sakuppgifter, medan den senare PDF:n framför allt har fått den inflyttande hyresgästens namn ifyllt, är den säkra formuleringen:

> **Det finns två olika genererade PDF-versioner av ett besiktningsprotokoll som båda anger samma besiktningsdag den 9 juli 2025. Den senare versionen innehåller uppgift om Erica Aylin Güler som inflyttande hyresgäst.**

Vi ska inte utan ytterligare system-/versionsdata skriva att:

- två fysiska besiktningar genomfördes,
- den 12 augusti respektive 30 oktober var besiktningsdagar,
- protokollet manipulerades,
- Gaby skapade eller ändrade någon av versionerna.

## 6. Korrigering av tidigare formulering – "två besiktningar utförda av samma person"

En tidigare process-/sammanställningstext innehåller formuleringen:

> `Två besiktningar utförda av samma person visar motstridiga bedömningar.`

Efter kontroll av de två nu tillgängliga original-PDF:erna kan **just dessa två dokument inte användas som primärstöd för den formuleringen**, eftersom båda anger samma besiktningsdag 2025-07-09 och samma huvudsakliga besiktningsinnehåll.

Formuleringen måste därför behandlas som **GUL/E-uppgift** tills vi identifierar vilka två separata besiktningstillfällen som avsågs och källan för att samma person utförde båda.

Om den "andra besiktningen" i stället avser ett senare faktiskt platsbesök med Gaby måste detta styrkas separat genom datum, ljud, mejl eller annan originalhandling.

## 7. Koppling till Patrick Segerstens mejl 12 augusti

Patrick Segersten skickade den 12 augusti 2025 bilagan `60020562 Besiktningsprotokoll.pdf` till Erica. Metadata på den nu uppladdade filen visar skapandetid samma dag kl. 10:06 UTC och Patricks mejl är daterat 10:09.

Det är ett starkt sammanhängande källspår för att den uppladdade augusti-PDF:n är den version som skickades i samband med godkännandet som hyresgäst.

Det bevisar inte vem som utförde den fysiska besiktningen den 9 juli.

## 8. Juridisk/bevismässig funktion

### J5 – Motsägelse/tillförlitlighet

Inte ännu på grund av "två protokoll" i sig. Först när en senare separat besiktning/platskontroll med annan bedömning source-lockas kan jämförelsen göras.

### J6 – Dokumentation/spårbarhet

Relevant: båda PDF-versionerna saknar namngiven besiktningsvärd trots att systemet har ett särskilt fält för detta.

### J1 – Kännedom

Om Gaby senare kan knytas till 9-juli-besiktningen genom originalljud eller intern handling kan protokollet få stark betydelse för vad han personligen såg/noterade före upplåtelsen.

## 9. GRÖN / GUL / RÖD

### GRÖN

- Två separata PDF-filer finns.
- De skapades/genererades 12 augusti respektive 30 oktober 2025 enligt PDF-metadata.
- Båda anger **Besiktningsdag 2025-07-09**.
- Objekt och sakuppgifter är i huvudsak desamma.
- Sida 2 är visuellt identisk.
- Senare versionen har Erica Aylin Güler som inflyttande hyresgäst; augustiversionen saknar namnet i motsvarande fält.
- `Besiktningsvärd` är blankt i båda.

### GUL

- Att det är exakt samma databaspåstående återgenererat vid två tillfällen. Det är starkt förenligt med filerna men bör verifieras genom FB:s system-/versionshistorik.
- Att Gaby utförde besiktningen den 9 juli.
- Att en senare separat besiktning utfördes av Gaby och gav motstridig bedömning.

### RÖD

- Att Gaby är signerad i någon av de två PDF-filerna.
- Att 12 augusti och 30 oktober är två besiktningsdagar.
- Att de två PDF-filerna i sig bevisar två fysiska besiktningar.
- Att någon har manipulerat protokollet.

## 10. Nästa kontroll

1. Source-locka Gabys uttalande i originalljud om att han utförde besiktningen.
2. Identifiera exakt vilket datum och vilket fysiskt tillfälle han avser.
3. Identifiera eventuell senare separat besiktning/återbesök som den tidigare formuleringen "två besiktningar" syftar på.
4. Begär/identifiera FB:s systemhistorik för objekt 60020562: skapad av, ändrad av, utskrifts-/genereringsdatum, revisionshistorik och vem som står som besiktningsvärd internt.
5. Jämför sedan första fysiska besiktningen med den senare kontrollen – inte bara PDF-genereringarna.

## 11. Styrande slutsats

> **De två nu source-lockade PDF-filerna visar två genererade versioner av ett protokoll med samma besiktningsdag 9 juli 2025. De visar inte två separata besiktningar, och Gaby Khalafs namn/signatur finns inte synligt i någon av dem. Frågan om Gaby var besiktningsmannen måste därför source-lockas genom annan primärkälla.**
