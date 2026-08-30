# AUDIT 35 – BESIKTNINGSPROTOKOLL, MF 80–87 OCH TIDSLINJE-CATCHUP

**Datum:** 2026-08-30  
**Objekt:** 60020562, Kilsgatan 3, Farsta  
**Status:** STYRANDE KORRIGERINGS- OCH CATCH-UP-AUDIT  
**Syfte:** jämföra de två nu uppladdade besiktningsprotokollen mot originalfilerna, korrigera tidigare slutsatser, integrera handling 80–87 från Miljöförvaltningen och föra in de nya verifierade händelserna i tidslinjestrukturen.

---

## 1. HUVUDSLUTSATS

De två PDF-filerna är **inte bevis för två olika fysiska besiktningar**.

Båda anger samma registrerade:

- objekt: **60020562**,
- adress: **Kilsgatan 3**,
- besiktningsdag: **2025-07-09**,
- tidigare/registrerat inflyttningsdatum: **2022-07-16**,
- avflyttningsdatum: **2025-09-30**,
- lägenheten: **tom**,
- inflyttande hyresgäst: **inte närvarande vid besiktningen**.

Det sakliga rums-/anmärkningsinnehållet är, efter textdiff, identiskt. Skillnaderna är:

1. synligt genererings-/dokumentdatum högst upp: **2025-08-12** respektive **2025-10-30**,
2. augustifilen saknar namn i fältet för inflyttande hyresgäst,
3. oktoberfilen har **Erica Aylin Güler** införd i detta fält och i nederdelen vid texten ”Inflyttande hyresgäst”.

Det finns därför **inte stöd för att kalla 12 augusti- och 30 oktober-PDF:erna två besiktningar**. Den säkra formuleringen är:

> **Två systemgenererade PDF-versioner av ett besiktningsprotokoll med samma registrerade besiktningsdag 9 juli 2025.**

---

# 2. ORIGINALKONTROLL AV PDF-FILERNA

## 2.1 Fil A – 12 augusti 2025

**Fil:** `60020562 Besiktningsprotokoll.pdf`  
**Synligt dokumentdatum:** 2025-08-12  
**Besiktningsdag i dokumentet:** 2025-07-09  
**SHA-256:** `788582e5aa55973cddc0a4fe722c2a3f8f63578b038f0ee08941f67ac668cf37`  
**PDF-metadata:** Creator PDFium / Producer PDFium  
**Filstorlek i originalkontrollen:** 55 304 byte  
**Bevisstatus:** GRÖN – original-PDF kontrollerad

PDF-filen anger inte Ericas namn i fältet ”Inflyttande hyresgäst”.

## 2.2 Fil B – 30 oktober 2025

**Fil:** `Besiktningsprotokoll.pdf`  
**Synligt dokumentdatum:** 2025-10-30  
**Besiktningsdag i dokumentet:** 2025-07-09  
**SHA-256:** `84b3eac9c3e2999dda1726a819640571ba67b57a30c63fe10d120208277c88d6`  
**PDF-metadata:** Creator JasperReports (`Besiktningsprotokoll_inflytt_FB`) / Producer iText 2.1.7  
**Filstorlek i originalkontrollen:** 55 765 byte  
**Bevisstatus:** GRÖN – original-PDF kontrollerad

Den senare PDF-filen anger Erica Aylin Güler som inflyttande hyresgäst.

## 2.3 Textdiff

Maskinell textdiff mellan PDF-filerna ger endast följande sakskillnader:

- `2025-08-12` → `2025-10-30`,
- blankt namn → `Erica Aylin Güler` i toppfältet,
- `Inflyttande hyresgäst:` → `Inflyttande hyresgäst: Erica Aylin Güler` på sida 3.

**Ingen annan textuell skillnad har identifierats i de dokumenterade rumsanmärkningarna eller statusbedömningarna.**

### Vad detta kan visa

- samma registrerade besiktningsunderlag har genererats vid minst två tillfällen,
- information om den inflyttande hyresgästen har tillkommit i systemuttaget senast 30 oktober,
- det finns ingen textdiff som stödjer att själva lägenhetsbedömningen ändrats mellan dessa två PDF-uttag.

### Vad detta INTE visar

- vem som faktiskt utförde besiktningen 9 juli,
- att Gaby Khalaf var formell besiktningsvärd,
- att en fysisk återbesiktning ägde rum 30 oktober,
- att protokollet manipulerats,
- att någon sakuppgift om lägenhetens skick ändrades 30 oktober.

---

# 3. BESIKTNINGSVÄRD – BLANKT I BÅDA PDF-FILERNA

Båda PDF-versionerna har en signatur-/namnrad med etiketten:

> **Besiktningsvärd**

Raden är visuellt blank i båda dokumenten.

**Status:** GRÖN.

Det innebär att PDF-filerna ensamma inte identifierar personen som gjorde besiktningen.

### Stoppregel

Frågan om Gaby som formell besiktningsman är **deprioriterad**. Den ska inte längre driva ett eget omfattande ljudsökspår.

Om ett redan relevant originalljud innehåller att Gaby själv instruerade tidigare hyresgäst om köksbänkens folie, används det endast för:

- J1 KÄNNEDOM,
- dokumenterad åtgärdsinstruktion före tillträdet,
- möjlig koppling mellan protokollets rad om folien och FB:s faktiska handläggning.

---

# 4. VAD PROTOKOLLET FAKTISKT SÄGER OM KÖKET

Båda versionerna innehåller samma uppgifter.

## Kök – linoleumgolv

> **”Inga synliga skador”**  
> **”Ej åtgärd”**  
> Status: **Ej Åtg**

Detta gäller **köksgolvet**.

## Kök – arbetsbänk

> **”Arbetar bänk har folie över”**

Anmärkningen anger att hyresgästen ska:

> **avlägsna folien fackmannamässigt samt ta bort limrester i samband med flyttstädning**

och att underlåtenhet kan leda till debitering.

Status: **Åtg HG**.

### Viktig tolkning

Detta är två olika poster:

- köksgolvet bedömdes okulärt som utan synliga skador och skulle inte åtgärdas,
- folien på arbetsbänken var en konkret känd avvikelse som skulle tas bort av den avflyttande hyresgästen.

De är inte motsägande eftersom de avser olika byggnadsdelar.

### Juridisk/bevismässig funktion

**J1 KÄNNEDOM / J6 DOKUMENTATION / J5 TILLFÖRLITLIGHET**

Protokollet visar att FB före Ericas tillträde hade ett registrerat objektspår om folien på arbetsbänken och att borttagning skulle ske fackmannamässigt.

Den naturliga kontrollfrågan är därför:

> **Hur verifierades före överlämnandet att folien och limresterna faktiskt hade avlägsnats fackmannamässigt, och dokumenterades arbetsbänkens skick efter att den täckande folien avlägsnats?**

Detta bevisar inte att folien dolde brand-, fukt- eller annan skada.

---

# 5. ”LINOLEUM HLU – EJ ÅTG” – KORREKT AVGRÄNSNING

”Linoleum HLU” är en separat HLU-post i andra utrymmen, bland annat sovrum och hall.

Exempel:

- Sovrum 2: `Linoleum HLU – Ny golv sen tidigare – Ej åtgärd`,
- Sovrum 1: `Linoleum HLU – Nytt golv, påträffas inga synliga skador – Ej åtgärd`,
- Hall: `Linoleum HLU – Ny golv – Ej åtgärd`.

Köksraden är däremot **”Linoleumgolv – Inga synliga skador – Ej åtgärd”** och är inte markerad `HLU` i protokollet.

Detta ska hållas isär i extern argumentation.

---

# 6. PROTOKOLLETS EGEN SCOPE-BEGRÄNSNING

Båda protokollen säger uttryckligen:

> **”Mindre fel som inte är av akut karaktär har inte noterats i protokollet.”**

Det är viktigt för bevisvärderingen.

### Vad protokollet kan visa

- vad FB faktiskt noterade inom protokollets registrerade poster,
- vilka synliga avvikelser som gav status Åtg HG / Bet HG / Åtg HV / Ej Åtg,
- vilka åtgärder som enligt protokollet skulle ske inför avflyttning/inflyttning.

### Vad protokollet inte kan användas för att bevisa

- att alla fel i lägenheten var identifierade,
- att det inte fanns dolda brister,
- att alla mindre brister noterades,
- att lägenhetens totala inomhusmiljö var tekniskt utredd,
- att brand-/saneringshistorik, ventilation, VOC, fukt eller materialemissioner hade kontrollerats.

Detta är ett viktigt scope-lås.

---

# 7. TIDSLINJEFUNKTION – JULI → AUGUSTI → OKTOBER

## 9 juli 2025 – registrerad besiktning

Båda original-PDF:erna anger besiktningsdag **2025-07-09**.

Lägenheten är markerad som tom och inflyttande hyresgäst inte närvarande.

Bland de registrerade posterna finns:

- köksgolv: inga synliga skador / ej åtgärd,
- arbetsbänk: folie över / avflyttande hyresgäst ska avlägsna fackmannamässigt och ta bort limrester,
- kyl/frys: inga synliga skador,
- spricka i tvättställ: HV åtgärdar,
- badrumsskåp: lite rost / HV kontrollerar för byte,
- HLU-/ytskikts- och golvposter i sovrum/hall.

## 12 augusti 2025 – första verifierade PDF-uttaget och utskick

PDF-filens synliga datum är **2025-08-12**.

Patrick Segersten skickade samma datum ett mejl till Erica med bilagan `60020562 Besiktningsprotokoll.pdf` och skrev att besiktningsprotokollet bifogades för att hon skulle kunna ta del av anmärkningarna.

Detta är en separat tidslinjehändelse från själva besiktningen 9 juli.

## 30 oktober 2025 – nytt systemgenererat PDF-uttag

Den andra PDF-filen har synligt datum **2025-10-30** och Ericas namn infört som inflyttande hyresgäst.

Saktexten om lägenheten är enligt diff oförändrad jämfört med 12-augusti-filen.

Detta ska registreras som **nytt dokumentuttag/version**, inte som en ny fysisk besiktning.

---

# 8. MF HANDLING 80–87 – NY CATCH-UP OCH KORRIGERING

## Handling 80 – Heval till Erica 11 mars 08:26

Heval meddelar att det planerade besöket behöver ställas in p.g.a. sjukdom och ber om nya tider. I mejlkedjan finns Ericas tidigare begäran att MF ska fråga FB om:

- sanering efter brand/rök,
- om och när kanalrensning genomförts,
- tidigare kanalrensning omkring 2014–2015 / uteblivet tillträde.

**Status:** GRÖN.

## Handling 81 – Heval till Jennifer 11 mars 08:31 – MYCKET VIKTIG KORRIGERING

Heval skriver till Jennifer Ehlin:

> **”Klagande har inkommit med ett yttrande i ditt ärende, se bifogade e-post.”**

FB ges möjlighet att bemöta uppgifterna senast **18 mars 2026**.

Den bifogade mejlkedjan innehåller Ericas konkreta frågor om sanering och kanalrensning.

### Korrigering av Audit 31

Tidigare formulering att själva MF→FB-frågeöverföringen inte hade identifierats alls är nu **för bred**.

**Ny styrande bedömning:**

> **Handling 81 visar en konkret MF→FB-kommunicering där Ericas yttrande med de tre kärnfrågorna skickades till Jennifer för bemötande.**

Detta visar att frågor om:

1. sanering efter brand/rök,
2. om/när kanalrensning genomförts,
3. tidigare kanalrensning / tillträde,

faktiskt nådde FB via denna kommunicering.

### Kvarstående lucka

Handling 81 visar inte i den synliga huvudtexten den senare fjärde frågan om **VOC-test** som Miriam preciserade 12 mars.

Det återstår därför att följa:

- vad FB svarade på handling 81,
- om VOC-frågan skickades i en senare kommunicering,
- hur MF bedömde eventuella svar före beslutet.

## Handling 83 – Erica till Miriam 11 mars 09:31

Erica eskalerar handläggningen och begär uttryckligen att sanerings- och kanalrensningsfrågorna inhämtas från fastighetsägaren.

**Juridisk funktion:** J7 myndighetens kännedom / J8 utredningsbehov.

## Handling 84 – Miriam 11 mars 11:00

Miriam skriver att Heval har skickat frågorna om sanering, kanalrensning och när detta skett till fastighetsägaren ”igår eller idag” och att hon ska följa upp:

> att frågorna verkligen kommer till fastighetsägaren **och att Erica får svar**.

Detta är nu förenligt med handling 81 kl. 08:31.

## Handling 85 – Erica 11 mars 16:27

Erica skriver att hon inte har sett de frågor som skickats och ber att få del av korrespondensen. Hon påtalar också att ventilation mättes men att inga analyser av luftens innehåll eller laboratorieprov av material genomfördes enligt hennes iakttagelse.

**Juridisk funktion:** J7 / J8 / senare partsinsyns- och kommuniceringsspår.

## Handling 86 – Erica 11 mars 16:33

Erica skickar foto-/materialkomplettering av brun förekomst i konstruktionen och dokumenterar att inget prov, såvitt hon kunde se, togs av materialet.

**Vad detta visar:** samtida partsuppgift och bilddokumentation.

**Vad detta inte visar:** teknisk identifiering av materialet eller mikrobiell/kemisk orsak.

## Handling 87 – Foto

Fotot dokumenterar visuellt en brun förekomst/materialdel i konstruktionen.

**Bevisklass:** A för att fotografiet existerar och visar det synliga utseendet.  
**Inte expertbevis:** det identifierar inte ämne, orsak eller hälsorisk.

---

# 9. 18 MARS OCH SENARE – KEDJAN SKA BYGGAS VIDARE

Den 18 mars skickade Heval tillsynsrapporten till Erica och Jennifer och gav båda möjlighet att yttra sig senast 1 april.

Ericas senare yttrande gör uttryckligen scope-invändningen:

- okulär kontroll + ventilation är inte material-/luftanalys,
- saneringsdokumentation hade inte redovisats,
- hon frågar på vilket underlag brandrelaterad kvarstående påverkan ansågs kunna lämnas utan fördjupad utredning.

Detta ska kopplas till den redan identifierade 9-april-kedjan och beslutet 13 april.

---

# 10. GRÖN / GUL / RÖD

## GRÖN

- båda original-PDF:erna har samma besiktningsdag 9 juli 2025,
- saktexten i rums-/anmärkningsdelen är identisk i textdiff,
- 12-augusti-PDF saknar Ericas namn i inflyttandefältet,
- 30-oktober-PDF har Ericas namn,
- båda har blank rad för Besiktningsvärd,
- arbetsbänkens folie och borttagningsinstruktion finns i båda,
- köksgolvet anges ha inga synliga skador och Ej Åtg,
- ”Linoleum HLU” gäller andra rum/hall, inte köksraden,
- protokollet säger att mindre icke-akuta fel inte noterats,
- handling 81 visar att Heval skickade Ericas yttrande till Jennifer 11 mars 08:31 för bemötande,
- handling 84 bekräftar att sanerings-/kanalrensningsfrågorna skickats och skulle följas upp.

## GUL

- vem som gjorde besiktningen 9 juli,
- vem som skrev in varje anmärkning,
- om och hur FB verifierade att arbetsbänkens folie/lim faktiskt avlägsnades fackmannamässigt,
- exakt systembetydelse av toppdatumet 30 oktober utöver att PDF:n genererades då,
- om VOC-frågan skickades separat efter 11 mars,
- vilket substantiellt FB-svar som lämnades på de tre frågorna i handling 81.

## RÖD / FÅR INTE PÅSTÅS

- att 12 augusti och 30 oktober är två fysiska besiktningar,
- att Gaby är identifierad av protokollen som besiktningsvärd,
- att folien dolde en brand-/fukt-/mögelskada,
- att protokollet bevisar att lägenheten saknade andra fel,
- att frånvaro av expertprov bevisar en viss orsak,
- att MF aldrig skickade sanerings-/kanalrensningsfrågorna till FB.

---

# 11. JURIDISK FUNKTION

### Besiktningsprotokollen

Primär funktion är **kännedom, dokumenterad lägenhetsstatus och scope**, inte teknisk friskförklaring.

Relevanta funktioner:

- **J1 KÄNNEDOM** – FB hade före tillträdet dokumenterade konkreta poster om kök, badrum och övriga rum.
- **J5 MOTSÄGELSE/TILLFÖRLITLIGHET** – senare dokumenterade brister kan jämföras med vad protokollet faktiskt omfattade, men bara inom korrekt scope.
- **J6 DOKUMENTATIONSLUCKA** – kontroll av om föreskrivna åtgärder verifierades före överlämnande.
- **J8 UTREDNINGSVAL** – protokollet är en okulär/administrativ besiktningshandling och kan inte ersätta orsaksutredning av inomhusmiljön.

### Handling 80–87

- **J7 MYNDIGHETENS KÄNNEDOM** – MF hade de konkreta frågorna.
- **J8 UTREDNINGSVAL** – frågorna sändes till FB och skulle följas upp.
- **J5/J6** – senare avgörande fråga är vilka konkreta svar som inkom och hur de värderades.

---

# 12. NÄSTA KONTROLL – PRIORITERING

1. **Identifiera FB:s faktiska svar på handling 81 / frågorna som skickades 11 mars.**
2. **Identifiera eventuell separat kommunicering av VOC-frågan efter Miriams besked 12 mars.**
3. **Följ kedjan fråga → svar → MF:s värdering → beslut 13 april.**
4. **För köksbänken:** sök bara efter dokumentation av utförd borttagning/efterkontroll om sådan handling redan finns i arbetsorder-/mailspåret. Ingen ny huvudjakt på Gabys formella besiktningsroll.
5. **Protokollversionerna:** betraktas framåt som samma registrerade besiktning med två systemuttag, om inte en ny primärkälla visar annat.

---

# 13. STATUS I HUVUDTIDSLINJEN

De verifierade händelserna har lagts i separat tidslinjetillägg:

`TIDSLINJE-TILLAGG-2026-08-30-BESIKTNING-MF80-87.md`

Tillägget är en del av tidslinjestrukturen och ska användas som styrande catch-up-lager tills posterna säkert kan slås ihop med den stora legacyfilen `TIDSLINJE.md` utan risk för truncation/full-replacement-fel.

**Viktigt:** audit 35 korrigerar äldre formuleringar i audit 31 och audit 32 där de strider mot originalfynden ovan.