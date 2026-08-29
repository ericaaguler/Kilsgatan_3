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

### Brand / tillsyn 11 mars / frågelogg

- [`2026-08-29_BRAND-TILLSYN-FRAGELOGG-MALNING-OCH-DOKUMENTATIONSLUCKA.md`](2026-08-29_BRAND-TILLSYN-FRAGELOGG-MALNING-OCH-DOKUMENTATIONSLUCKA.md)

Denna fil är ett **obligatoriskt bevarandelager** för de nya fynden från ljudfil/transkribering, Outlook och brandspåret. Den innehåller bland annat:

- Hevals råd vid tillsynen 11 mars: **”Jag tycker att du ska tacka ja”** till målning/åtgärd,
- att toxiner, brandpartiklar/rökpartiklar diskuterades men inte provtogs/tekniskt utreddes vid tillsynen,
- muntlig observation om att det känns tungt i lägenheten,
- att målning diskuteras som möjlig praktisk åtgärd utan fastställd brandorsak,
- att MF på plats ännu inte hade tagit slutlig ställning till om lägenheten var beboelig,
- datumkorrigeringen att det omfattande MF-yttrandet är **7 januari 2026** enligt Outlook-tidsstämpeln,
- den viktiga posten **9 mars 2026**, då Erica uttryckligen ber MF kräva in uppgifter/dokumentation om eventuell sanering efter rök/brand,
- konservativ räknad frågelogg: minst **5** materiella brand-/saneringsfrågetillfällen till Familjebostäder och minst **7** till Miljöförvaltningen,
- dokumentationskedjan SSBF → FB → S:t Erik → Restvärderäddning → SBK,
- frågan vilken felsökning som faktiskt fullföljde Familjebostäders löfte den 6 november 2025.

**Denna fil får aldrig ersättas av en kortare sammanfattning.** Vid ny source-lockning ska status uppdateras eller kompletteras, inte raderas.

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

## Obligatoriska arbetslinjer som inte får försvinna

> **Orsaksfrågan är fortfarande obesvarad i det granskade underlaget.**

> **En rapport kan inte besvara en fråga den aldrig har undersökt.**

> **En rapport kan inte fylla en historisk dokumentationslucka när de handlingar som skulle verifiera åtgärden aldrig har redovisats.**

> **Frågan är inte om brand-/saneringsfrågan var känd. Frågan är vilket verifierbart underlag som faktiskt besvarade den.**

## Juridisk separationsregel

**Huvudtidslinjen ska innehålla vad som hände.**

**Audit-/rättsfunktionslagret ska innehålla vad händelsen juridiskt kan användas till.**

Detta förhindrar att analys, slutsats och faktum blandas ihop.

## Viktigt om `.gitignore`

Anteckningar ska vara versionshanterade och spårbara. De ska därför **inte ignoreras**. Repositoryts `.gitignore` innehåller uttryckliga skyddsregler (`!anteckningar/**`, `!analyser/**`, m.fl.) för att viktiga bevis-, audit- och tidslinjefiler inte oavsiktligt ska falla bort.

### Särskild bevaranderegel

Följande kategorier får inte senare läggas i `.gitignore` utan ett uttryckligt, dokumenterat beslut:

- användaranteckningar,
- auditfiler,
- tidslinjer och spårtidslinjer,
- source-lockade transkriptioner,
- ljud-/videoreferenser och källindex,
- myndighetsakter,
- mejl-/korrespondensfiler,
- bevisregister,
- rättsfunktions- och frågeloggar.
