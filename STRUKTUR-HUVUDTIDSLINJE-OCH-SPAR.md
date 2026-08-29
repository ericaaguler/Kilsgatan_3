# Struktur – huvudtidslinje och separata sakspår

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

`anteckningar/` används för Ericas egna anteckningar och korrigeringar.

De ska bevaras även när de ännu inte kunnat verifieras fullt ut. De får inte tyst tas bort när en senare källa hittas.

Tillåtna statusar:

- `SOURCE-LOCKAD`
- `STÖDS AV KÄLLA MEN EXAKT ORDALYDELSE EJ LÅST`
- `ANVÄNDARENS FÖRSTAHANDSUPPGIFT/ANTECKNING`
- `VITTNESUPPGIFT`
- `BEHÖVER VERIFIERAS`
- `MOTSÄGELSE`
- `DOKUMENTATIONSLUCKA`

Anteckningar ska versionshanteras och får inte läggas i `.gitignore`.

## 5. Auditlager

`analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md` styr auditten.

`analyser/AUDIT-FYND-OCH-OMISSION-REGISTER-2026-08-29.md` registrerar allt som:

- saknas i huvudtidslinjen,
- finns men är för kortfattat,
- har fel datum,
- har fel person,
- saknar ordalydelse,
- saknar källa,
- bara finns i ett tidslinjetillägg,
- saknas i relevant separat spår.

## 6. Tidslinjetillägg

Daterade `TIDSLINJE-TILLAGG-*` och `TIDSLINJE-KOMPLETTERING-*` är tillfälliga arbetslager under audit.

De är inte konkurrerande huvudtidslinjer.

Varje källsäkrad händelse i ett tillägg ska därefter föras in i `TIDSLINJE.md`.

## 7. Separata spår

Separata spår skapas först efter att huvudmaterialet är tillräckligt komplett.

De ska vara filtrerade vyer av huvudtidslinjen och kunna länka tillbaka till samma källor.

Planerade/aktuella spår:

### Brand / brandhistorik / dokumentation

- branden 2017,
- vem som senare informerar om branden,
- vittneskedjan,
- FB:s kännedom,
- FB:s nekanden/besked,
- frågor om sanering,
- frågor om dokumentation,
- försäkrings-/skadehantering,
- myndighetskontakter,
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

### Myndighetsspår

Exempel:

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
- dokument som efterfrågats men inte återfunnits.

## 8. Personkontroll

Personer ska alltid identifieras med fullständigt namn/roll när det behövs för att undvika sammanblandning.

Särskilt:

- **Thomas Bartsch** – Ericas vän; stöd/vittne i november 2025.
- **Thomas Duvsjö** – separat person/granne/vittne.

## 9. Händelser får tillhöra flera spår

En händelse kan samtidigt vara relevant för exempelvis brand, ventilation och dokumentation.

Den ska då **inte dupliceras som olika fakta**. Samma huvudtidslinjepost ska kunna märkas/länkas mot flera spår.

Exempel:

`11 november 2025 – 1:a mötet med FB` kan samtidigt innehålla:

- branduppgift,
- ventilation,
- kanalrensningsfråga,
- ventilationsdon,
- beslut/åtgärder,
- vem som var närvarande.

## 10. Slutregel

**Först komplett huvudtidslinje. Därefter enskilda spår.**

Ingen separat tidslinje får användas som ersättning för huvudtidslinjen och inget viktigt material får falla bort när ett sakspår filtreras fram.
