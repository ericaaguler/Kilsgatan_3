# Styrning – juridisk analys och källkontroll

Detta lager innehåller bindande arbetsregler för hur juridisk analys, audit, source-lock och externa texter ska göras i Kilsgatan 3-projektet.

## Huvudregel

- `MASTERPROMPT-JURIDISK-AI-ANALYS-MED-KALLKONTROLL.md` är projektets obligatoriska juridiska analysstandard.
- Den kompletterar `STORA-AUDITEN/README.md`.
- Vid konflikt gäller den strängare käll-/verifieringsregeln.
- Den ändrar inte bevisvärdet hos en källa och får aldrig ersätta originalkälla eller gällande rätt.

## Arbetskedja

`originalkälla → source-lock → BEVISREGISTER → STORA AUDITEN → rättskällekontroll → juridisk styrkegrad → huvudtidslinje/sakspår → extern text`

## Obligatoriska extra fält från och med 29 augusti 2026

Utöver befintliga auditfält ska större juridiska analyser innehålla:

- rättskälletyp,
- aktualitetsstatus,
- source-lock-färg GRÖN/GUL/RÖD,
- juridisk styrkegrad,
- motargument,
- extern användbarhet,
- tydlig märkning `INTE VERIFIERAT` respektive `JURIDISK BEDÖMNING – INTE FASTSLAGET FAKTUM` när tillämpligt.

## Bevaranderegel

Styrfiler, auditfiler, juridiska arbetsutkast, anteckningar och källregister ska versionshanteras. De får inte ignoreras generellt av `.gitignore`.
