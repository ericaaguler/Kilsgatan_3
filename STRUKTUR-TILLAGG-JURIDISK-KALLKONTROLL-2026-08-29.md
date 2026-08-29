# STRUKTURTILLÄGG – JURIDISK KÄLLKONTROLL

**Datum:** 29 augusti 2026  
**Status:** AKTIVT STRUKTURTILLÄGG TILL `STRUKTUR-HUVUDTIDSLINJE-OCH-SPAR.md`

Detta tillägg inför ett nytt permanent styrningslager utan att skapa en konkurrerande tidslinje.

## Ny struktur

`originalkälla`
→ `BEVISREGISTER.md`
→ `STORA-AUDITEN/`
→ `styrning/MASTERPROMPT-JURIDISK-AI-ANALYS-MED-KALLKONTROLL.md`
→ `rättskällekontroll och aktualitetskontroll`
→ `juridisk styrkegrad + motargument`
→ `TIDSLINJE.md / sakspår`
→ `juridik/ arbetsutkast`
→ `extern text`

## Lager

### `styrning/`

Obligatoriska metod- och källkontrollregler. Ingen faktisk uppgift blir bevisad genom att finnas här.

### `STORA-AUDITEN/`

Kontrollerar bevispost, räckvidd, source-lock, juridisk funktion, förbjuden inferens, kompletteringsbehov och rättslig användning.

### `juridik/`

Arbetsutkast, möjliga överklaganden, källregister och juridiska processprodukter. En fil i denna mapp är inte automatiskt klar för inlämning.

### `audit/`

Underordnade register-/basmatriser som hör till STORA AUDITEN.

## Nya obligatoriska auditdimensioner

Varje större juridisk audit ska, utöver projektets tidigare fält, kunna redovisa:

- rättskälletyp,
- aktualitetsstatus,
- source-lock: GRÖN/GUL/RÖD,
- juridisk styrkegrad,
- motargument,
- alternativ rättslig tolkning,
- extern användbarhet.

## Hård separation

`FAKTISK UPPGIFT` ≠ `RÄTTSKÄLLA` ≠ `JURIDISK BEDÖMNING`.

Följande markeringar är obligatoriska när de behövs:

- **INTE VERIFIERAT**
- **JURIDISK BEDÖMNING – INTE FASTSLAGET FAKTUM**

## Source-lock

Direktcitat, datum, talare, tekniska värden, målnummer, lagrum och påståenden om vad en aktör visste får inte användas externt i högre säkerhetsgrad än källan medger.

## Bevaranderegel

Detta strukturtillägg, `styrning/`, `STORA-AUDITEN/`, `juridik/` och `audit/` skyddas uttryckligen i `.gitignore` genom negationsregler och ska versionshanteras.

## Relation till befintlig struktur

`TIDSLINJE.md` förblir enda kanoniska huvudtidslinje. Detta tillägg förändrar endast kvalitetssäkringen mellan bevis och extern juridisk användning.
