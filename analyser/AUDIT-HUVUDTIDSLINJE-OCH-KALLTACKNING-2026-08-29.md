# AUDIT – HUVUDTIDSLINJE OCH KÄLLTÄCKNING

**Datum:** 29 augusti 2026  
**Repository:** `ericaaguler/Kilsgatan_3`  
**Status:** AKTIV AUDIT – BASLINJE UPPRÄTTAD  
**Syfte:** Säkerställa att `TIDSLINJE.md` är den kanoniska, fullständiga händelsekedjan och att separata tidslinjer/spår aldrig tappar bevis, mejl, skriftliga formuleringar, personer, handlingar, uttalanden, åtgärder eller anteckningar.

---

## 1. Grundregel

`TIDSLINJE.md` ska behandlas som huvudtidlinje. Separata filer, exempelvis brand-, kanalrensnings-, OVK-, Miljöförvaltnings- eller myndighetsspår, är **filtrerade vyer av huvudmaterialet** och får inte byggas fristående från detta.

Ingen uppgift får utelämnas enbart för att den:

- saknar fullständig dokumentation,
- ännu inte är verifierad,
- motsägs av annan uppgift,
- kommer från en anteckning,
- kommer från ett vittne,
- senare behöver rättas.

I stället ska uppgiften finnas med och få tydlig status.

---

## 2. Källhierarki

Vid konflikt gäller befintlig styrning:

1. originalbevis / primärhandling,
2. verifierad transkription eller dokumenterad förstahandsuppgift,
3. `TIDSLINJE.md` / `BEVISREGISTER.md` när posten är källåst,
4. aktuell korrigerad analys,
5. äldre analys / sammanställning.

Ingen separat tidslinje får ges högre bevisvärde än sin underliggande källa.

---

## 3. Minimikrav för varje händelsepost

Varje relevant händelse ska, när uppgifterna finns, kunna bära följande fält:

- **Event-ID**
- **Datum** och vid behov tid / datumintervall
- **Person / aktör / organisation**
- **Vad personen skrev, sade, gjorde, beslutade, observerade eller underlät att göra**
- **Exakt formulering/citat** när ordalydelsen har självständig betydelse
- **Primär källa**
- **Sekundär källa** om sådan finns
- **Källfil / sökväg / mejldatum / handling / bilaga**
- **Bevisstatus:** verifierad / förstahandsuppgift / vittnesuppgift / användaranteckning / inferens / obekräftad
- **Motsägelse eller osäkerhet**
- **Vilka sakspår posten hör till**
- **Om uppgiften finns i relevant separat tidslinje**

En person får inte försvinna ur tidslinjen därför att fokus för ett separat spår är tekniskt. Personens uppgift eller handling kan vara en del av dokumentations-, kännedom-, ansvar- eller beviskedjan.

---

## 4. Material som alltid ska omfattas av audit

Auditten ska söka efter och jämföra:

- mejl och mejltrådar,
- SMS/chattar,
- brev,
- myndighetshandlingar och beslut,
- Familjebostäders skriftliga uppgifter,
- arbetsordrar, protokoll, rapporter och felanmälningar,
- bilagor och metadata som påverkar datum/avsändare/innehåll,
- mötesanteckningar,
- användarens egna anteckningar,
- vittnesuppgifter,
- foton och videoanalyser,
- verifierade transkriptioner när sådana finns,
- tidigare korrigeringar,
- `BEVISREGISTER.md`,
- `TIDSLINJE.md`,
- tidslinjekompletteringar och tillägg,
- aktuella styr- och korrigeringsfiler,
- separata sakspår.

**Viktigt:** audit avser inte bara händelser. Den ska även hitta enskilda skriftliga meningar och formuleringar som får betydelse för kännedom, löfte, påstående, motsägelse, uteblivet svar, planerad åtgärd eller ansvarskedja.

---

## 5. `.gitignore` – kontroll 29 augusti 2026

Vid auditstart finns **ingen `.gitignore`-fil i repositoryts root**.

Det innebär att inga anteckningsfiler för närvarande exkluderas från Git-spårning genom repositoryts `.gitignore`.

### Regel framåt

Anteckningar, bevis, tidslinjer, källregister och auditmaterial får **inte** läggas till som ignore-mönster. Om `.gitignore` skapas senare ska den kontrolleras mot detta auditkrav.

Det användaren efterfrågar som "alla anteckningar med i gitignore" tolkas korrekt tekniskt som:

> **Alla relevanta anteckningar ska vara inkluderade och spårbara i GitHub/repositoryt – inte ignorerade av Git.**

---

## 6. Baslinje – centrala källor som måste korsgranskas

Följande centrala filer är identifierade vid auditstart och får inte granskas isolerat från varandra:

### Kanoniska register

- `TIDSLINJE.md`
- `BEVISREGISTER.md`

### Tidslinjekompletteringar / tillägg

- `TIDSLINJE-KOMPLETTERING-2025-11-20--2026-01-15.md`
- `TIDSLINJE-TILLAGG-2026-04-13--2026-08-25-MF-FB-SAMMA-SAKFRAGA.md`
- `TIDSLINJE-TILLAGG-2026-08-27-SBK-FB.md`

### Separata sakspår som måste verifieras mot huvudmaterialet

- `BRAND-TIDSLINJE.md`
- `TIDSLINJE-BRAND-2017-2026.md`
- `JAMFORELSE-ANDRA-BRANDER.md`
- `KANALRENSNING-TIDSLINJE.md`

### Identifierade separata bevisfiler i `bevis/`

- `bevis/2025-11-07--2025-11-11-sms-thomas-infor-mote.md`
- `bevis/2025-11-21--2026-07-10-sms-peter-husvard.md`
- `bevis/2025-11-27-koksbank-efter-stadning.md`
- `bevis/2026-04-04--2026-08-06-sms-thomas-duvsjo-granne-kilsgatan.md`

### Aktuella styrfiler

Auditten ska även följa `analyser/AKTUELL-STYRNING-OCH-KORRIGERINGSREGLER-2026-08-25.md` och de där utpekade aktuella arbetskartorna. Äldre analys får inte överstyra senare källåst korrigering.

---

## 7. Auditpass – ska göras systematiskt

### PASS A – Fil- och källinventering

Kontrollera att alla relevanta källor i repositoryt är identifierade och klassificerade.

### PASS B – Huvudtidlinje mot BEVISREGISTER

För varje daterbar eller på annat sätt tidsplacerbar bevispost:

- finns motsvarande händelse i `TIDSLINJE.md`?
- finns rätt person?
- finns rätt datum?
- finns den relevanta ordalydelsen?
- finns handlingen/underlåtenheten?
- finns källhänvisningen?

### PASS C – Tillägg mot huvudtidlinje

Alla tidslinjekompletteringar och senare tillägg ska kontrolleras rad för rad mot `TIDSLINJE.md`. Poster som endast finns i tillägg ska flaggas för införande eller uttrycklig markering.

### PASS D – Person- och aktörstäckning

Skapa kontroll per person/aktör:

`person → datum → sade/skrev/gjorde → källa → finns i huvudtidlinjen → finns i relevant separat spår`

Särskild kontroll krävs där personer med samma förnamn riskerar att blandas ihop.

### PASS E – Exakta formuleringar och uteblivna svar

Kontrollera särskilt:

- löften,
- besked,
- frågor som ställts,
- frågor som uttryckligen skulle tas upp senare,
- frågor som aldrig besvarades,
- formuleringar som senare ändrats,
- påståenden om vad som gjorts,
- uppgifter om att något inte finns dokumenterat.

### PASS F – Separata tidslinjer

Varje separat tidslinje ska diffas mot huvudtidlinjen och bevisregistret utifrån sitt sakspår.

För varje utelämnad post ska det finnas ett medvetet skäl. **Tyst utelämning är inte tillåten.**

### PASS G – Motsägelser, osäkerheter och luckor

Upprätta tre separata kategorier:

1. **MOTSÄGELSE** – två källor säger materiellt olika saker efter kontroll av originaluppgifterna.
2. **OSÄKERHET** – uppgift finns men kan ännu inte verifieras tillräckligt.
3. **DOKUMENTATIONSLUCKA** – relevant underlag har efterfrågats eller borde kunna identifieras men har inte återfunnits.

Frånvaro av handling får aldrig automatiskt skrivas som att händelsen inte inträffat.

---

## 8. Brandspåret – särskild auditregel

Brandspåret ska inte reduceras till själva branddatumet eller frågan om nuvarande orsak.

Det ska kunna följa hela kedjan:

`brand → kännedom → utredning → skadehantering → sanering/återställning → dokumentation → kontroll → senare uppgifter/vittnen → frågor till Familjebostäder → svar/uteblivna svar → myndighetskontakt → kvarstående dokumentationsluckor`

Följande typer av poster kan därför vara relevanta även om de ligger flera år efter branden:

- någon informerar om brandhistoriken,
- någon bekräftar eller ifrågasätter branden,
- någon lovar att kontrollera historiken,
- frågor ställs om sanering eller dokumentation,
- möte bokas för att gå igenom sådana frågor,
- frågorna tas inte upp eller besvaras inte,
- skade-/försäkrings-/saneringshandlingar efterfrågas,
- myndighet eller bolag uppger att handling saknas eller finns någon annanstans.

Detta ska hållas isär från påståendet att branden är dagens tekniska orsak.

---

## 9. Nya användaranteckningar från 29 augusti 2026 och framåt

När nya anteckningar tillförs i chatten ska de inte direkt behandlas som verifierade fakta.

De ska först registreras som:

**`USER_NOTE – 2026-08-29`**

med:

- uppgiften så exakt som möjligt,
- datum/händelse som anteckningen avser,
- person/aktör,
- vilket sakspår den berör,
- möjlig underliggande källa,
- kontrollstatus.

Därefter ska uppgiften kontrolleras mot repositoryts bevis innan huvudtidlinjen eller separat tidslinje ändras.

Om anteckningen korrigerar ett tidigare fel ska både felet och korrigeringen vara spårbara; felaktig äldre formulering får inte fortsätta användas som aktiv sanning.

---

## 10. Omission register – obligatoriskt

Under auditten ska varje identifierad potentiellt saknad post få en av följande statusar:

- `SAKNAS I HUVUDTIDSLINJE`
- `FINNS MEN ÄR FÖR KORTFATTAD`
- `PERSON SAKNAS`
- `ORDALYDELSE SAKNAS`
- `KÄLLA SAKNAS`
- `DATUM BEHÖVER KONTROLLERAS`
- `FEL PERSON / SAMMANBLANDNING`
- `FINNS I TILLÄGG MEN INTE HUVUDFIL`
- `SAKNAS I SEPARAT SPÅR`
- `KORREKT OCH KÄLLTÄCKT`

Inget auditfynd får lösas genom att det bara faller bort ur nästa sammanställning.

---

## 11. Definition av "audit klar"

Auditten är inte klar förrän:

1. relevanta repositorykällor är inventerade,
2. `BEVISREGISTER.md` är korsgranskat mot `TIDSLINJE.md`,
3. tidslinjetillägg är korsgranskade mot huvudtidlinjen,
4. personer/aktörer är kontrollerade,
5. relevanta exakta formuleringar och uteblivna svar är kontrollerade,
6. motsägelser/osäkerheter/dokumentationsluckor är separerade,
7. varje separat tidslinje är kontrollerad mot huvudmaterialet,
8. nya användaranteckningar är registrerade och källkontrollerade,
9. alla identifierade utelämnanden är korrigerade eller uttryckligen motiverade.

**Först därefter ska en separat tidslinje betraktas som audit-säkrad.**
