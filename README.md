# Kilsgatan 3 – källbaserat bevis- och tidslinjearkiv

Detta repository ska fungera som **en sammanhängande källbank för hela ärendet**.

## Huvudprincip

Det finns **EN huvudtidslinje**:

- [`TIDSLINJE.md`](TIDSLINJE.md)

Alla separata tidslinjer och sakspår ska vara **filtrerade vyer av huvudmaterialet**. De får aldrig byggas fristående eller innehålla en egen konkurrerande kronologi.

Arbetsordningen är därför alltid:

`originalkälla → bevisregister → anteckning/audit → huvudtidslinje → separat sakspår`

Om en viktig uppgift upptäcks i ett separat spår men saknas i huvudtidslinjen ska den först flaggas och föras tillbaka till huvudmaterialet.

---

# 1. KÄRNFILER

## Huvudtidslinje

- [`TIDSLINJE.md`](TIDSLINJE.md) – kanonisk kronologi för hela ärendet.

## Bevisregister

- [`BEVISREGISTER.md`](BEVISREGISTER.md) – register över bevis och källor.

## Audit / kontroll

- [`analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md`](analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md)
- [`analyser/AUDIT-FYND-OCH-OMISSION-REGISTER-2026-08-29.md`](analyser/AUDIT-FYND-OCH-OMISSION-REGISTER-2026-08-29.md)

Auditfilerna används för att hitta sådant som saknas, är för kortfattat, har fel person, fel datum, saknar ordalydelse eller endast finns i ett tillägg.

---

# 2. ANTECKNINGAR

Användarens egna förstahandsanteckningar ska ligga i `anteckningar/` och **ska alltid bevaras även innan de är source-lockade**.

Aktuell arbetsfil:

- [`anteckningar/2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md`](anteckningar/2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md)

Anteckningar märks med status, exempelvis:

- `SOURCE-LOCKAD`
- `STÖDS AV KÄLLA MEN EXAKT ORDALYDELSE EJ LÅST`
- `ANVÄNDARENS FÖRSTAHANDSUPPGIFT/ANTECKNING`
- `BEHÖVER VERIFIERAS`
- `MOTSÄGELSE – ORIGINALKÄLLOR SKA KONTROLLERAS`

Anteckningar får **inte** läggas i `.gitignore`. De ska vara versionshanterade och spårbara i repositoryt.

---

# 3. TIDSLINJETILLÄGG UNDER AUDIT

När huvudtidslinjen ännu inte hunnit få en fullständig källsäkrad omskrivning används daterade tidslinjetillägg som arbetslager.

Aktuellt tillägg:

- [`TIDSLINJE-TILLAGG-2025-11-10--2025-11-26-AUDIT-2026-08-29.md`](TIDSLINJE-TILLAGG-2025-11-10--2025-11-26-AUDIT-2026-08-29.md)

**Viktigt:** ett tillägg är inte en andra huvudtidslinje. Varje källsäkrad post i ett tillägg ska senare införas i `TIDSLINJE.md`.

---

# 4. SEPARATA SAKSPÅR

Separata spår används först när huvudmaterialet är tillräckligt komplett. De ska kunna härledas tillbaka till huvudtidslinjen och originalkällorna.

## Brand / brandhistorik / dokumentationskedja

- [`BRAND-TIDSLINJE.md`](BRAND-TIDSLINJE.md)
- [`TIDSLINJE-BRAND-2017-2026.md`](TIDSLINJE-BRAND-2017-2026.md)

Brandspåret ska omfatta mer än själva branddatumet:

`brand → kännedom → vittnesuppgifter → frågor → FB:s svar → sanering/återställning → dokumentation → myndighets- och försäkringsspår → kvarstående dokumentationsluckor`

## Kanalrensning / ventilation

- [`KANALRENSNING-TIDSLINJE.md`](KANALRENSNING-TIDSLINJE.md)

Spåret ska skilja mellan:

- ventilationskontroll,
- mätning,
- justering,
- ventilationsdon/lock,
- rengöring i kanal/rör,
- uttrycket **kanalrensning**,
- faktisk utförd kanalrensning,
- vem som föreslog/beställde/utförde åtgärden.

## Separat jämförelseunderlag

- [`JAMFORELSE-ANDRA-BRANDER.md`](JAMFORELSE-ANDRA-BRANDER.md)

Jämförelsefilen är ett analys-/referensunderlag och ska inte blandas ihop med huvudtidslinjen eller kanalrensningstidslinjen.

---

# 5. ORIGINALKÄLLOR

## Korrespondens

- [`korrespondens/TRADINDEX.md`](korrespondens/TRADINDEX.md)
- [`korrespondens/GRANSKNINGSLOGG.md`](korrespondens/GRANSKNINGSLOGG.md)
- [`korrespondens/familjebostader/`](korrespondens/familjebostader/)
- [`korrespondens/miljoforvaltningen/`](korrespondens/miljoforvaltningen/)
- övriga aktörer under `korrespondens/`

## Bevisfiler

- `bevis/`

## Handlingar

- `handlingar/`

## Inspelningar och transkriptioner

- `inspelningar/`
- `transkriptioner/`

Originalkällan har alltid högre bevisvärde än en senare sammanfattning.

---

# 6. STYRREGLER FÖR HUVUDTIDSLINJEN

Varje materiellt relevant händelse ska, när uppgifterna finns, innehålla:

1. datum/tid,
2. person/aktör,
3. vad som skrevs/sades/gjordes/beslutades/observerades,
4. exakt formulering när ordalydelsen är viktig,
5. källa/bevis-ID,
6. bevisstatus,
7. eventuell motsägelse/osäkerhet/dokumentationslucka,
8. vilka separata sakspår händelsen hör till.

Enbart formuleringen **”mejl skickades med ämnet…”** är inte tillräcklig när mejlet innehåller materiellt viktig information.

Även följande är tidslinjehändelser:

- en fråga ställs,
- ett svar uteblir,
- en person lovar att återkomma,
- ett möte bokas,
- en fråga som skulle behandlas vid ett möte inte behandlas,
- en uppgift motsägs senare,
- ett dokument efterfrågas men inte återfinns.

---

# 7. SÄRSKILDA PERSONREGLER

Personer med samma förnamn får aldrig blandas ihop.

Exempel:

- **Thomas Bartsch** – Ericas vän; stöd/vittne i november 2025.
- **Thomas Duvsjö** – separat granne/vittne i Kilsgatan-spåret.

---

# 8. AKTUELL AUDIT – NOVEMBER 2025

Följande punkter är särskilt aktiva i auditten:

- 4 november: Caroline/Karolin – source-lockat ventilationsbesök.
- 7 november: Erica skickar Jennifer omfattande checklista inför första mötet.
- checklistan innehåller ventilation/ventilationskanal/OVK men inte termen **kanalrensning**.
- 10 november: Erica och Thomas Bartsch går igenom lägenheten inför mötet; förstahandsanteckningar bevaras.
- 11 november: **1:a mötet med FB (Familjebostäder) i lägenheten**.
- branduppgift, ventilationsdon och kanalrengöring/kanalrensning under mötet ska source-lockas.
- 14 november: skriftligt stöd för att platsmötet faktiskt ägt rum.
- 17–26 november: åtgärdskedja, städning, målning, golv, ventilation och frågor/svar granskas i fulltext.
- 24–25 november: Gabys två separata skriftliga uttalanden om att Familjebostäder inte ser någon dokumenterad brand.
- 26 november: Ericas mejl ger senare skriftligt stöd för att rengöring inne i kanalen diskuterats och att frågan kopplats till att det då skulle behöva göras i fler/alla lägenheter.
- 28 november: Erica hänvisar skriftligen till Brottsplatskartan/Polisens händelserapport i mejl till Gaby med Jennifer i kopia; exakt första överföring av själva skärmdumpen/länken är fortfarande en separat kontrollpunkt.

---

# Slutprincip

**Huvudtidslinjen ska vara komplett först. Därefter bygger vi enskilda spår.**

Ett separat spår får aldrig bli en plats där uppgifter försvinner ur huvudhistoriken. Om en post är relevant för flera spår ska den finnas i huvudtidslinjen och länkas/klassificeras mot samtliga relevanta spår.
