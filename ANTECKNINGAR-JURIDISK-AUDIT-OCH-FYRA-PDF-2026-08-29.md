# Anteckningar – juridisk audit och fyr-PDF-metod

**Datum:** 29 augusti 2026  
**Status:** Styrande arbetsanteckning. Inte primärbevis och inte avsedd att citeras som faktisk tidslinje.

## 1. Syfte

När ny information tillkommer i Kilsgatan 3-ärendet ska den inte bara läggas till i befintlig berättelse. Den ska testas mot:

1. bevisvärde,
2. rättsfaktum,
3. aktuell process,
4. de fyra juridiska PDF-källorna,
5. aktuell lag/praxis,
6. motpartens bästa invändning.

Den uppdaterade standardprompten finns i:

`analyser/PROMPT-GRANSKA-NYTT-DOKUMENT-MOT-FYRA-JURIDISKA-PDFER-2026-08-26.md`

Den gäller nu både **nya dokument och enstaka nya uppgifter**.

## 2. Audit av tidigare fyr-PDF-prompt

Den äldre prompten var stark i fråga om:

- faktum/inferens/hypotes/bevislucka,
- separat relevansbedömning per bok,
- source-lock,
- adversarialt test,
- specialprocess framför FPL,
- försiktighet med äldre hyresrättsdoktrin.

Men den hade fyra luckor som nu är korrigerade:

### A. Den var dokumentcentrerad

Den utgick främst från att ett helt nytt dokument laddades upp. Projektet får ofta **enstaka nya sakuppgifter** från mejl, foton, ljud, arbetsorder eller svar. Ny standard börjar därför med:

`ny uppgift → vilken tidigare arbetsposition ändras? → korrigering/source-lock`

### B. Den skilde inte tillräckligt mellan bok och aktuell lag

En bok kan peka mot en juridisk princip utan att bokens beskrivning automatiskt motsvarar gällande rätt 2026. Ny standard kräver därför ett **lagkort**:

`bok → lagrum/princip → aktuell lydelse? → direkt tillämplig? → specialregel? → rättsfaktum → bevis → motargument → extern användbarhet`

### C. Den gav inte ett snabbt svar på "kan jag använda lagen?"

Ny standard ska alltid avsluta med:

- vad som faktiskt kan användas,
- i vilket forum,
- om det kan användas nu eller först efter source-lock/juridisk kontroll,
- vilket ytterligare bevis som behövs.

### D. Den saknade ett kortkommando

Nytt kortkommando:

> **Granska den här nya informationen enligt fyr-PDF- och lagutnyttjandeauditen. Visa om någon av böckerna ger ett juridiskt argument jag faktiskt kan använda, vilket lagrum/princip det gäller, om regeln är direkt tillämplig, vad som måste verifieras i aktuell rätt och vilket ytterligare bevis som behövs. Uppdatera GitHub om jag skriver @GitHub.**

## 3. De fyra böckernas fasta roller

### 1. Förvaltningsprocesslagen – en kommentar

**Roll:** processrättsligt metod-/doktrinstöd.  
**Styrka:** bevisning, processledning, PT, återförvisning, domstolsprocess.  
**Risk:** att FPL används som om den alltid vore direkt tillämplig i MÖD.  
**Regel:** specialprocess måste kontrolleras först.

### 2. Myndigheternas skrivregler

**Roll:** klarspråk, terminologi, disposition, begriplighet.  
**Styrka:** visa att en motivering är svår att följa eller oklart formulerad.  
**Risk:** att göra språkbrist till självständig ogiltighetsgrund.  
**Regel:** skilj alltid språk-/klarhetsproblem från materiellt rättsligt fel.

### 3. Den nya hyresrätten efter hyresregleringens avskaffande

**Roll:** äldre hyresrättsligt bakgrunds-/doktrinstöd.  
**Styrka:** brukbarhet, brist, hinder/men, påföljdslogik.  
**Risk:** äldre rättsläge.  
**Regel:** aktuell 12 kap. jordabalken och senare praxis måste verifieras.

### 4. Lägenhetsbyten och andrahandsuthyrning

**Roll:** specialiserad bok för byte/andrahandsuthyrning och begränsat metodstöd.  
**Styrka:** endast om sakfrågan faktiskt berör dessa områden eller ett tydligt överförbart Hyresnämnds-/bevisresonemang.  
**Risk:** artificiell användning i miljö-/MÖD-spår.  
**Regel:** parkera som EJ RELEVANT när konkret koppling saknas.

## 4. Styrande lagutnyttjanderegel

Ingen ny uppgift ska förvandlas direkt till ett lagpåstående.

Använd alltid:

`ny uppgift → bevistema → rättsfaktum → bevisfaktum → bokstöd → aktuellt lagrum → direkt tillämplighet → motargument → bevislucka → användbarhet`

Markera:

- `VERIFIERAT I PRIMÄRKÄLLA`
- `STARKT STÖD`
- `SOURCE-LOCK KRÄVS`
- `KAN INTE FASTSTÄLLAS`
- `JURIDISK KONTROLL KRÄVS`
- `TEKNISK SAKKUNNIG KRÄVS`

## 5. Viktig skillnad: bokstöd är inte rättskälla med samma tyngd som lag

Före extern användning ska materialet delas upp i:

**A. Boken säger** – doktrin/metod/kommentar.  
**B. Gällande lag säger** – aktuell officiell lagtext.  
**C. Praxis säger** – om vägledande avgörande finns.  
**D. Mitt bevis visar** – vad som faktiskt är source-lockat i Kilsgatan 3.

Argumentet får först behandlas som externt robust när dessa nivåer inte blandas ihop.

## 6. Processkontroll för Miljöförvaltningen

När ny information rör myndighetens handläggning ska följande alltid köras:

`fråga → begäran → svar → verifiering → kommunicering → bedömning → motivering`

Särskilt:

- fanns materialet före beslutet?
- går det att se hur det värderades?
- behövde myndigheten komplettera?
- om inte, framgår varför?

Frånvaro i beslutsmotiveringen betyder inte automatiskt att materialet ignorerades. Aktkedjan måste kontrolleras.

## 7. Auditregel för juridiska råd utifrån ofullständig bild

Ett allmänt juridiskt råd får inte behandlas som en fullständig bedömning av Kilsgatan 3 om rådgivaren uttryckligen saknat konkreta uppgifter eller själv beskrivit svaret som generellt.

Fråga alltid:

- vilken fråga fick rådgivaren faktiskt?
- vilka handlingar hade rådgivaren?
- analyserade rådgivaren den processuella frågan eller endast allmänna bostadsbrister?
- bedömde rådgivaren bevisningen eller gav hen bara en generell vägkarta?

Detta är en tolkningsregel, inte kritik av rådgivaren.

## 8. GitHub-regel

Ny information som ändrar projektets arbetsposition ska:

1. dokumenteras i relevant analys,
2. få statusdelta om ändringen är materiell,
3. länkas i central styrning när den påverkar metod eller huvudlinje,
4. inte läggas i faktatidslinjen utan primärkälla.

## 9. Kort arbetsinstruktion

När Erica skriver exempelvis:

> `@GitHub granska detta mot böckerna`

ska arbetet förstås som:

> läs nya materialet → jämför mot fyra PDF:er → hitta potentiellt användbar juridisk princip → kontrollera direkt tillämplighet → markera behov av aktuell rätt → stresstesta → uppdatera rätt GitHub-spår.