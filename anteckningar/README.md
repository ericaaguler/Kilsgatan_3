# Anteckningar – arbetslager före huvudtidslinjen

Denna katalog innehåller Ericas egna anteckningar, korrigeringar och minnesuppgifter samt den juridiska arbetsanteckning som anger **vilken bevisfunktion en uppgift faktiskt kan bära**.

## Grundregel

Anteckningar ska **inte raderas** bara för att primärkälla ännu saknas. De ska i stället märkas med status och därefter kontrolleras mot originalkällor.

Tillåtna statusar:

- `SOURCE-LOCKAD`
- `STÖDS AV KÄLLA MEN EXAKT ORDALYDELSE EJ LÅST`
- `ANVÄNDARENS FÖRSTAHANDSUPPGIFT/ANTECKNING`
- `VITTNESUPPGIFT`
- `BEHÖVER VERIFIERAS`
- `MOTSÄGELSE`
- `DOKUMENTATIONSLUCKA`
- `OBESVARAD FRÅGA`

## Arbetsflöde

`anteckning → kontroll mot originalkälla → bevisstatus → juridisk funktion → huvudtidslinje → separat sakspår`

En uppgift som är relevant för flera sakspår ska först säkras i huvudtidslinjen. Därefter får den återanvändas i exempelvis brand-, ventilation-, kanalrensnings-, dokumentations- eller myndighetsspår.

## Aktiva anteckningsfiler

### Juridisk huvudanteckning

- [`2026-08-29_HUVUDANTECKNING-JURIDISK-BEVISFUNKTION.md`](2026-08-29_HUVUDANTECKNING-JURIDISK-BEVISFUNKTION.md)

Den styr hur varje uppgift ska klassificeras juridiskt: kännedom, skick/hinder, symptomfenomen, tekniskt scope, motsägelse, dokumentationslucka, myndighetens kännedom, utredningsval eller beslutsmotivering.

### Novemberaudit

- [`2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md`](2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md)

Den innehåller bland annat:

- Thomas Bartsch som Ericas vän,
- Caroline/Karolin och source-lockat besök 4 november,
- checklistan till Jennifer 7 november,
- ordkontroll att `kanalrensning` inte finns i checklistan,
- 10 november med Thomas och grannen i 1102,
- 11 november – första mötet med Familjebostäder,
- branduppgiften,
- kanalrensnings-/kanalrengöringsfrågan,
- ventilationsdonet,
- åtgärdskedjan efter mötet,
- 24–25 november Gabys brandsvar,
- 26 november skriftligt stöd om rengöring inne i kanalen och konsekvensen för andra lägenheter,
- 28 november hänvisning till Brottsplatskartan/Polisens händelserapport.

## Juridisk separationsregel

**Huvudtidslinjen ska innehålla vad som hände.**

**Audit-/rättsfunktionslagret ska innehålla vad händelsen juridiskt kan användas till.**

Detta förhindrar att analys, slutsats och faktum blandas ihop.

## Viktigt om `.gitignore`

Anteckningar ska vara versionshanterade och spårbara. De ska därför **inte ignoreras**. Repositoryts `.gitignore` innehåller uttryckliga skyddsregler (`!anteckningar/**`, `!analyser/**`, m.fl.) för att viktiga bevis-, audit- och tidslinjefiler inte oavsiktligt ska falla bort.
