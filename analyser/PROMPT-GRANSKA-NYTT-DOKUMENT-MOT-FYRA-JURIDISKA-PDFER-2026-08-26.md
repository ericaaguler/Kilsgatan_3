# Standardprompt – granska nytt dokument mot fyra juridiska PDF-källor

**Syfte:** Denna prompt ska användas varje gång Erica laddar upp ett nytt dokument som ska analyseras inom Kilsgatan 3-projektet. Dokumentet ska inte bara sammanfattas. Det ska läsas mot projektets fyra juridiska PDF-källor och mot GitHub-strukturen.

## PROMPT

Jag laddar nu upp ett nytt dokument i Kilsgatan 3-ärendet.

Din uppgift är att göra en **fullständig dokumentgranskning** och därefter **matcha innehållet mot de fyra juridiska PDF-källor som finns i projektet**:

1. **Förvaltningsprocesslagen – en kommentar**
2. **Myndigheternas skrivregler**
3. **Den nya hyresrätten efter hyresregleringens avskaffande**
4. **Lägenhetsbyten och andrahandsuthyrning**

Du ska INTE utgå från att alla fyra är relevanta. Du ska för varje bok uttryckligen bedöma:

- HÖG RELEVANS,
- MEDEL RELEVANS,
- LÅG RELEVANS,
- eller EJ RELEVANT FÖR DETTA DOKUMENT.

Om en bok inte är relevant ska du säga det och **inte pressa in den artificiellt**.

## STEG 1 – VAD ÄR DET FÖR DOKUMENT?

Börja med att identifiera:

- dokumenttyp,
- avsändare/författare,
- datum,
- mottagare,
- processuell eller materiell funktion,
- vilket ärende/mål/spår det tillhör,
- om dokumentet är primärhandling, sekundär sammanställning, partsinlaga, myndighetsbeslut, tekniskt underlag eller analys.

Förklara därefter med vanlig svenska:

> Vad gör detta dokument faktiskt?

Inte bara vad det handlar om, utan vilken funktion det har i ärendet.

## STEG 2 – GÅ IGENOM HELA DOKUMENTET

Gå igenom dokumentet avsnitt för avsnitt och identifiera:

- centrala sakpåståenden,
- rättsliga påståenden,
- tekniska påståenden,
- processuella påståenden,
- bevispåståenden,
- slutsatser,
- antaganden,
- motsägelser,
- oklarheter,
- sådant som uttryckligen inte behandlas.

För varje viktig punkt ska du skilja:

**FAKTUM** – vad dokumentet faktiskt säger eller visar.

**INFERENS** – vad som kräver ett slutsatssteg.

**HYPOTES** – möjlig förklaring som inte är fastställd.

**BEVISLUCKA** – vad som behöver styrkas med annan handling.

## STEG 3 – VAD VISAR DOKUMENTET OCH VAD VISAR DET INTE?

För varje central uppgift ska du använda modellen:

`påstående → källa i dokumentet → vad det direkt visar → vad det inte visar → möjlig alternativ förklaring → vilket ytterligare bevis behövs`

Överdriv aldrig dokumentets bevisvärde.

Frånvaro av en handling får inte automatiskt likställas med att händelsen aldrig inträffat.

En personlig observation får inte behandlas som teknisk undersökning.

En teknisk mätning får inte ges större räckvidd än metod, tidpunkt och objekt stödjer.

Vittnesuppgifter kan styrka rapporterade observationer och tidsmönster men inte automatiskt teknisk eller medicinsk kausalitet.

## STEG 4 – MATCHA MOT FÖRVALTNINGSPROCESSLAGEN – EN KOMMENTAR

Kontrollera om dokumentet aktualiserar frågor om exempelvis:

- domstolens utredningsansvar/processledning,
- partsställning,
- kommunicering,
- bevisning,
- återförvisning,
- överklagande,
- prövningstillstånd,
- ändringsdispens,
- granskningsdispens,
- hur domskäl och processmaterial ska bedömas.

Ange:

**Vad i boken stärker dokumentets linje?**

**Vad i boken försvagar eller begränsar dokumentets linje?**

**Vilken regel är metodiskt relevant men inte direkt tillämplig på just denna måltyp?**

Kontrollera alltid om specialprocess gäller före FPL. För MÖD-spåret ska lagen om mark- och miljödomstolar och lagen om domstolsärenden kontrolleras separat mot aktuell lagtext.

## STEG 5 – MATCHA MOT MYNDIGHETERNAS SKRIVREGLER

Kontrollera om dokumentet aktualiserar:

- otydligt myndighetsspråk,
- vaga uttryck,
- svårbegripliga motiveringar,
- terminologisk inkonsekvens,
- problem med mottagaranpassning,
- disposition och begriplighet.

Skilj alltid mellan:

**språklig/klarhetsmässig brist**

och

**materiellt rättsligt fel**.

Skrivreglerna får inte användas som om de i sig bevisar att ett beslut ska ändras.

## STEG 6 – MATCHA MOT DEN NYA HYRESRÄTTEN

Kontrollera om dokumentet berör:

- lägenhetens skick,
- fullt brukbar för avsett ändamål,
- brist,
- hinder eller men i nyttjanderätten,
- underhållsansvar,
- avhjälpande,
- hyresnedsättning,
- skadestånd,
- andra hyresrättsliga påföljder.

Eftersom boken är äldre ska du uttryckligen markera:

> ÄLDRE DOKTRIN – AKTUELL LAG OCH PRAXIS MÅSTE KONTROLLERAS.

Använd inte boken som ensam grund för dagens rättsläge.

## STEG 7 – MATCHA MOT LÄGENHETSBYTEN OCH ANDRAHANDSUTHYRNING

Kontrollera om dokumentet faktiskt rör:

- byte,
- andrahandsuthyrning,
- Hyresnämndens praxis inom dessa områden,
- bevisbördefrågor som boken behandlar och som verkligen kan överföras till den aktuella frågan.

Om inte:

> EJ RELEVANT FÖR DETTA DOKUMENT – PARKERAS.

Pressa aldrig in denna bok i ett miljöbalks-, tillsyns- eller MÖD-spår om den inte har en konkret funktion.

## STEG 8 – MATCHA MOT GITHUB-STRUKTUREN

Efter bokanalysen ska dokumentet placeras i rätt befintliga spår, exempelvis:

- MÖD/process,
- Miljöförvaltningens handläggning,
- offentlighet/akt,
- ventilation/OVK,
- kanalrensning,
- brand/sanering,
- vittnen/förstahandsuppgifter,
- hyresrätt/remedy,
- ansvarskarta,
- påståendekatalog,
- juridisk huvudtidslinje,
- process- och bevisanalys,
- juristbrief.

Säg vilka befintliga GitHub-filer dokumentet ska uppdatera eller länkas från.

Skapa inte en ny teori bara för att dokumentet innehåller något nytt.

## STEG 9 – SOURCE-LOCK

Skapa en särskild lista:

### Source-lock krävs före extern användning

För varje materiellt viktigt påstående ange:

- vilken originalhandling som behövs,
- om original redan finns,
- om uppgiften endast finns i sekundär sammanställning,
- om ordalydelsen måste verifieras,
- om datum/avsändare/system/lägenhet/räckvidd måste kontrolleras.

Använd markörerna:

- `VERIFIERAT I PRIMÄRKÄLLA`
- `STARKT STÖD`
- `SOURCE-LOCK KRÄVS`
- `KAN INTE FASTSTÄLLAS`
- `JURIDISK KONTROLL KRÄVS`
- `TEKNISK SAKKUNNIG KRÄVS`

## STEG 10 – ADVERSARIALT TEST

Bygg först den starkaste rimliga motargumentationen mot vår tolkning.

Fråga:

- Hur skulle Miljöförvaltningen svara?
- Hur skulle Familjebostäder svara?
- Hur skulle domstolen kunna förklara dokumentet på ett annat sätt?
- Finns en oskyldig eller tekniskt rimlig alternativ förklaring?
- Överdriver vi bevisvärdet?

Därefter identifiera den **starkaste linje som fortfarande står kvar efter stresstestet**.

## STEG 11 – VAD BÖR STÄRKAS?

Avsluta med tre rubriker:

### Behåll
Vad i dokumentet är redan starkt och korrekt avgränsat?

### Stärk
Vad behöver bättre lagstöd, bättre bevis, tydligare formulering eller exaktare struktur?

### Ta bort eller tona ned
Vad är för kategoriskt, dåligt styrkt, irrelevant eller riskerar att försvaga huvudlinjen?

## STEG 12 – GITHUB

När analysen är klar och användaren har skrivit `@GitHub` ska du:

1. uppdatera GitHub med analysen,
2. länka dokumentet till rätt spår,
3. uppdatera centralt status-/styrindex om dokumentet ändrar projektets läge,
4. inte lägga obestyrkta sakpåståenden i faktatidslinjen,
5. tydligt skilja primärbevis från analys,
6. registrera vilka av de fyra PDF-böckerna som faktiskt användes och vilken relevans de hade.

## STANDARDOUTPUT

Svaret till användaren ska minst innehålla:

1. **Vad dokumentet är och vad det gör**
2. **Noggrann genomgång av innehållet**
3. **Vad som är starkt**
4. **Vad som är svagt/oklart**
5. **Vad dokumentet visar / inte visar**
6. **Matchning mot PDF 1 – Förvaltningsprocesslagen**
7. **Matchning mot PDF 2 – Myndigheternas skrivregler**
8. **Matchning mot PDF 3 – Den nya hyresrätten**
9. **Matchning mot PDF 4 – Lägenhetsbyten och andrahandsuthyrning**
10. **Vilka lag-/processfrågor som bör stärkas**
11. **Source-lock-lista**
12. **Motpartens starkaste motargument**
13. **Starkaste kvarstående linje efter stresstest**
14. **Vilka GitHub-spår/filer som ska uppdateras**

## ÖVERORDNAD PRINCIP

Målet är inte att hitta så många argument som möjligt.

Målet är att hitta:

> **de argument som kan styrkas, har rätt juridisk räckvidd och fortfarande håller när de utsätts för motargument.**

De fyra PDF-källorna ska användas som juridiska analysverktyg, inte som dekoration.