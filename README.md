# Kilsgatan 3 – källbaserat bevis- och tidslinjearkiv

Detta repository ska fungera som **en sammanhängande källbank, huvudtidslinje, audit- och rättsfunktionsstruktur för hela ärendet**.

## Huvudprincip

Det finns **EN huvudtidslinje**:

- [`TIDSLINJE.md`](TIDSLINJE.md)

Alla separata tidslinjer och sakspår ska vara **filtrerade vyer av huvudmaterialet**. De får aldrig byggas fristående eller innehålla en egen konkurrerande kronologi.

Arbetsordningen är:

`originalkälla → bevisregister → STORA AUDITEN → huvudtidslinje → separat sakspår → extern argumentation`

Om en viktig uppgift upptäcks i ett separat spår men saknas i huvudtidslinjen ska den flaggas och föras tillbaka till huvudmaterialet.

---

# 1. KÄRNFILER OCH HUVUDLAGER

## STORA AUDITEN – projektets kontrollager

- [`STORA-AUDITEN/README.md`](STORA-AUDITEN/README.md) – styrregler och obligatoriska auditfält.
- [`STORA-AUDITEN/01-KONTROLLPANEL.md`](STORA-AUDITEN/01-KONTROLLPANEL.md) – hela projektets levande kontrollpanel.
- [`STORA-AUDITEN/02-BEVISPOSTER-MASTER.md`](STORA-AUDITEN/02-BEVISPOSTER-MASTER.md) – masteraudit per bevispost/beviskedja.
- [`STORA-AUDITEN/03-ORIGINALKONTROLL-OCH-KOMPLETTERINGSKO.md`](STORA-AUDITEN/03-ORIGINALKONTROLL-OCH-KOMPLETTERINGSKO.md) – kö för source-lock, originalkontroll och saknade kompletteringar.

**STORA AUDITEN är ett eget huvudlager, inte en sammanfattning och inte en alternativ tidslinje.** Där ska varje identifierad bevispost få:

`datum → källa → faktisk uppgift → bevisklass → juridisk funktion → vad den inte bevisar → saknad komplettering → relevant lag/princip → status i huvudtidslinje/spår → originalkontroll → extern användbarhet`

Material som bara finns som sammanställning eller ej originalkontrollerad transkription ska markeras och får inte användas externt som säker ordalydelse innan originalfilen har kontrollerats.

## Huvudtidslinje

- [`TIDSLINJE.md`](TIDSLINJE.md) – kanonisk kronologi för hela ärendet.

## Bevisregister

- [`BEVISREGISTER.md`](BEVISREGISTER.md) – register över bevis och källor. Registrerade bevis-ID B0001–B0464 ingår i STORA AUDITENS scope.

## Struktur

- [`STRUKTUR-HUVUDTIDSLINJE-OCH-SPAR.md`](STRUKTUR-HUVUDTIDSLINJE-OCH-SPAR.md) – styr hur originalkällor, anteckningar, audit, juridisk bevisfunktion, huvudtidslinje och separata spår hänger ihop.

## Tidigare audit-/analysfiler – underlag till huvudlagret

- [`analyser/STORA-AUDITEN-BEVIS-KRONOLOGI-RATTSFUNKTION-2026-08-29.md`](analyser/STORA-AUDITEN-BEVIS-KRONOLOGI-RATTSFUNKTION-2026-08-29.md)
- [`analyser/BEVIS-OCH-RATTSFUNKTION-HUVUDAUDIT-ALLT-MATERIAL-2026-08-29.md`](analyser/BEVIS-OCH-RATTSFUNKTION-HUVUDAUDIT-ALLT-MATERIAL-2026-08-29.md)
- [`analyser/PROJEKTAUDIT-KILSGATAN-3-2026-08-29.md`](analyser/PROJEKTAUDIT-KILSGATAN-3-2026-08-29.md)
- [`analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md`](analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md)
- [`analyser/AUDIT-FYND-OCH-OMISSION-REGISTER-2026-08-29.md`](analyser/AUDIT-FYND-OCH-OMISSION-REGISTER-2026-08-29.md)
- [`analyser/MF-AKT-01-107-BRAND-SANERING-AUDIT-2026-08-29.md`](analyser/MF-AKT-01-107-BRAND-SANERING-AUDIT-2026-08-29.md)
- [`analyser/MF-AKT-01-107-KONTROLLREGISTER-2026-08-29.md`](analyser/MF-AKT-01-107-KONTROLLREGISTER-2026-08-29.md)

Dessa filer är nu **underlag** till `STORA-AUDITEN/`; de är inte konkurrerande kontrollpaneler.

---

# 2. ANTECKNINGAR

Användarens egna förstahandsanteckningar ska ligga i `anteckningar/` och **ska alltid bevaras även innan de är source-lockade**.

Aktiva filer:

- [`anteckningar/2026-08-29_HUVUDANTECKNING-JURIDISK-BEVISFUNKTION.md`](anteckningar/2026-08-29_HUVUDANTECKNING-JURIDISK-BEVISFUNKTION.md)
- [`anteckningar/2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md`](anteckningar/2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md)
- [`anteckningar/README.md`](anteckningar/README.md)

Anteckningar märks med status, exempelvis:

- `SOURCE-LOCKAD`
- `STÖDS AV KÄLLA MEN EXAKT ORDALYDELSE EJ LÅST`
- `ANVÄNDARENS FÖRSTAHANDSUPPGIFT/ANTECKNING`
- `VITTNESUPPGIFT`
- `BEHÖVER VERIFIERAS`
- `MOTSÄGELSE`
- `DOKUMENTATIONSLUCKA`
- `OBESVARAD FRÅGA`

---

# 3. JURIDISK BEVISFUNKTION

Varje viktig uppgift ska kunna klassificeras efter vad den faktiskt kan bevisa:

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

**Huvudtidslinjen ska säga vad som hände. STORA AUDITEN ska säga vad källan faktiskt kan användas till, vad den inte bevisar och vad som fortfarande saknas.**

---

# 4. TIDSLINJETILLÄGG UNDER AUDIT

När huvudtidslinjen ännu inte hunnit få en fullständig källsäkrad omskrivning används daterade tidslinjetillägg som arbetslager.

Exempel:

- [`TIDSLINJE-TILLAGG-2025-11-10--2025-11-26-AUDIT-2026-08-29.md`](TIDSLINJE-TILLAGG-2025-11-10--2025-11-26-AUDIT-2026-08-29.md)

**Viktigt:** ett tillägg är inte en andra huvudtidslinje. Varje källsäkrad post i ett tillägg ska senare införas i `TIDSLINJE.md`.

---

# 5. SEPARATA SAKSPÅR

Separata spår används när huvudmaterialet är tillräckligt komplett. De ska kunna härledas tillbaka till huvudtidslinjen och originalkällorna.

## Brand / brandhistorik / dokumentationskedja

- [`BRAND-TIDSLINJE.md`](BRAND-TIDSLINJE.md)
- [`TIDSLINJE-BRAND-2017-2026.md`](TIDSLINJE-BRAND-2017-2026.md)

Brandspåret ska omfatta:

`brand → kännedom → vittnesuppgifter → frågor → FB:s svar/nekanden → sanering/återställning → dokumentation → myndighets-/försäkringsspår → kvarstående verifieringsluckor`

## Kanalrensning / ventilation

- [`KANALRENSNING-TIDSLINJE.md`](KANALRENSNING-TIDSLINJE.md)

Spåret ska skilja mellan ventilationskontroll, mätning, justering, ventilationsdon/lock, rengöring i kanal/rör, termen `kanalrensning`, faktisk utförd rensning och vem som föreslog/beställde/utförde åtgärden.

## Hälsa / exponeringsmönster

Ska hållas som eget spår: vem som vistas i lägenheten, datum, exakt reaktion, kännedom i förväg, återhämtning efter vädring/lämnande. Vittnesuppgifter kan stödja ett återkommande fenomen men ska inte användas som medicinskt bevis för en specifik orsak.

## Myndighetsspår

- Miljöförvaltningen
- Stadsbyggnadskontoret / PBL / OVK
- Länsstyrelsen
- Mark- och miljödomstolen

## Dokumentationsspår

- OVK
- arbetsordrar
- sanerings-/brandskadehandlingar
- försäkring/RVR
- tekniska rapporter
- efterfrågade men ej återfunna handlingar

## Separat jämförelseunderlag

- [`JAMFORELSE-ANDRA-BRANDER.md`](JAMFORELSE-ANDRA-BRANDER.md)

Jämförelsefilen är ett analys-/referensunderlag och ska inte blandas ihop med huvudtidslinjen.

---

# 6. ORIGINALKÄLLOR

- `korrespondens/`
- `bevis/`
- `handlingar/`
- `inspelningar/`
- `transkriptioner/`

Originalkällan har alltid högre bevisvärde än en senare sammanfattning.

---

# 7. STYRREGLER FÖR HUVUDTIDSLINJEN

Varje materiellt relevant händelse ska, när uppgifterna finns, innehålla:

1. datum/tid,
2. person/aktör,
3. vad som skrevs/sades/gjordes/beslutades/observerades,
4. exakt formulering när ordalydelsen är viktig,
5. källa/bevis-ID,
6. bevisstatus,
7. eventuell motsägelse/osäkerhet/dokumentationslucka,
8. vilka separata sakspår händelsen hör till,
9. länk/klassning till juridisk bevisfunktion när relevant.

Även följande är tidslinjehändelser:

- en fråga ställs,
- ett svar uteblir,
- någon lovar att återkomma,
- ett möte bokas,
- en utlovad fråga inte behandlas,
- en uppgift motsägs senare,
- ett dokument efterfrågas men inte återfinns.

---

# 8. ARGUMENTREGEL

Varje juridiskt argument ska testas mot fyra frågor:

1. Vad säger källan faktiskt?
2. Vilken juridisk funktion kan den fylla?
3. Vilket lagrum/princip är relevant och är aktuell rätt verifierad?
4. Vilket ytterligare bevis behövs för en starkare slutsats?

Exempel:

- `Saknat saneringsintyg` är en verifieringslucka – inte automatiskt bevis för utebliven sanering.
- `Flera personer reagerar` kan stärka utredningsbehov – inte automatiskt bevisa medicinsk kausalitet.
- `OCAB` kan bära slutsatser inom sitt faktiska uppdrag/metod – inte besvara frågor som inte undersökts.
- `Godkänd OVK` måste knytas till rätt system/objekt och kan inte ensam bevisa att bostaden är fri från alla andra inomhusmiljöproblem.

---

# 9. PERSONKONTROLL

Personer med samma förnamn får aldrig blandas ihop.

- **Thomas Bartsch** – Ericas vän; stöd/vittne i november 2025.
- **Thomas Duvsjö** – separat granne/vittne.

---

# 10. `.gitignore`

`.gitignore` används endast för lokala/tempfiler. Viktiga projektmappar och kärnfiler har uttryckliga negationsregler så att `anteckningar/`, `analyser/`, `bevis/`, `handlingar/`, `korrespondens/`, `inspelningar/`, `transkriptioner/` och tidslinjer **inte oavsiktligt ignoreras**.

---

# Slutprincip

**Först källsäker kontroll i STORA AUDITEN. Därefter korrekt huvudtidslinje. Därefter enskilda spår och extern argumentation.**

Varje bevis ska användas för den juridiska funktion det faktiskt kan bära. Ett separat spår får aldrig bli en plats där uppgifter försvinner ur huvudhistoriken.