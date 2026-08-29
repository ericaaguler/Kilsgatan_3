# AUDITFYND OCH OMISSION REGISTER – 29 AUGUSTI 2026

**Status:** AKTIVT REGISTER  
**Hör ihop med:** `analyser/AUDIT-HUVUDTIDSLINJE-OCH-KALLTACKNING-2026-08-29.md`

Detta register ska innehålla identifierade fall där `TIDSLINJE.md` saknar, förkortar, blandar ihop eller otillräckligt källhänvisar en relevant händelse eller uppgift.

---

## FYND 001 – Thomas saknas i huvudtidlinjen 7–11 november 2025

**Status:** `SAKNAS I HUVUDTIDSLINJE` / `PERSON SAKNAS`

**Källa:** `bevis/2025-11-07--2025-11-11-sms-thomas-infor-mote.md`

Källan visar bland annat:

- 7 november: Erica ber Thomas följa med som **”stöd, vittne”** inför Familjebostäders möte.
- Thomas accepterar.
- 8 november: Erica tackar Thomas efter en genomgång och skriver att han ”hittade fler brister”.
- 10 november: de planerar att ses före mötet den 11 november kl. 14.
- 11 november kl. 13: Erica skriver att de ses snart och tackar honom för att han kommer med; därefter skriver hon att hon väntar utanför hans port.

**Personkorrigering 29 augusti:** Thomas Bartsch ska registreras som **vän till Erica Güler** och ska hållas strikt åtskild från Thomas Duvsjö.

**Avgränsning:** SMS-kedjan stöder starkt planerat och omedelbart förestående deltagande men exakt fysisk närvaro under hela mötet ska vid behov source-lockas med ytterligare möteskälla.

**Auditåtgärd:** Händelserna ska bedömas för införande i `TIDSLINJE.md` med korrekt bevisstatus och utan att överdriva vad SMS-källan ensam visar.

---

## FYND 002 – Själva Familjebostäders möte 11 november 2025 saknas som händelse

**Status:** `SAKNAS I HUVUDTIDSLINJE`

`TIDSLINJE.md` innehåller bokningskedjan 7 november och ett mejl 11 november kl. 08:02, men därefter går tidslinjen vidare utan en särskild post för själva platsmötet den 11 november kl. 14.

**Ny source-lock 29 augusti:** B0100 och B0101 verifierar i efterhand att platsmötet faktiskt ägde rum. Den 14 november skriver Erica **”Tack för ett trevligt tisdagsmöte”** och Gaby svarar **”Tack själv för ett fint platsmöte.”**

**Rubrik som ska användas:** `11 november 2025 – 1:a mötet med FB (Familjebostäder) i lägenheten`.

**Auditåtgärd:** deltagare, uttalanden, förslag, observationer och åtgärdsbesked ska därefter registreras som separata eller tydligt strukturerade händelseuppgifter.

---

## FYND 003 – Jennifer Ehlins besked 12 december 2025 är materiellt underrepresenterat

**Status:** `FINNS MEN ÄR FÖR KORTFATTAD` / `ORDALYDELSE SAKNAS`

**Bevis-ID:** B0174  
**Källa:** `korrespondens/familjebostader/2025-12-12_1013_B0174_jennifer-ehlin_sv-kilsgatan-3-123-44-farsta-lgh-nr-1202.md`

`TIDSLINJE.md` beskriver i nuläget posten i huvudsak som att Jennifer skickade ett mejl med visst ämne.

Originalkällan innehåller däremot det materiellt viktiga beskedet:

> ”Vi ses den 17/12 kl 09:00. Jag tar med mig husvärd Peter.”
>
> ”Vi går igenom dina kvarvarande frågor då.”

Den citerade underliggande tråden visar dessutom att de kvarvarande frågorna omfattade brandhistorik, motstridiga uppgifter om brand, saneringsdokumentation och andra kvarstående brister.

**Auditåtgärd:** Huvudtidlinjen ska återge sakinnebörden och den centrala exakta formuleringen, inte bara mejlets existens/ämnesrad.

---

## FYND 004 – Mötet 17 december 2025 saknas som egen händelse i huvudtidlinjen

**Status:** `SAKNAS I HUVUDTIDSLINJE`

`TIDSLINJE.md` innehåller e-postposter 17 december men ingen tydlig egen post som registrerar Familjebostäders platsmöte i lägenheten som Jennifer bokade i B0174.

Detta är särskilt relevant eftersom Jennifer den 12 december uttryckligen skrev att de kvarvarande frågorna skulle gås igenom då. Om dessa frågor inte togs upp/besvarades under mötet är det en separat relevant händelse i dokumentations- och svarskedjan.

**Auditåtgärd:** Source-locka mötet 17 december och kontrollera exakt:

1. vilka som deltog,
2. vilka frågor som faktiskt behandlades,
3. vilka av de uttryckligen kvarvarande frågorna som inte behandlades,
4. vad som senare skrevs om det som inte hanns med,
5. vilka sakspår detta hör till, särskilt brand/sanering/dokumentation.

---

## FYND 005 – Huvudtidlinjens nuvarande princip riskerar att tappa bevisad sakinnebörd

**Status:** `STRUKTURELL AUDITBRIST`

`TIDSLINJE.md` anger att endast källbelagda händelser ska läggas in. Det är korrekt som huvudprincip, men flera källbelagda mejlposter är i nuläget automatiskt formulerade som endast:

> ”[Person] skickade e-post ... med ämnet ...”

Detta gör att juridiskt/faktiskt betydelsefull saktext kan finnas i originalbeviset men inte vara synlig i huvudtidlinjen.

**Auditåtgärd:** Vid PASS B ska varje mejl som rör ett relevant bevistema granskas för sakinnebörd. Ämnesrad räcker inte när meddelandet innehåller löfte, besked, fråga, svar, uteblivet svar, motsägelse, kännedom, planerad åtgärd eller dokumentationsuppgift.

---

## FYND 006 – 10 november 2025 saknar Ericas förstahandsanteckningar om felsökning med Thomas Bartsch

**Status:** `NY ANTECKNING – BEHÖVER KOMPLETTERANDE SOURCE-LOCK`

Erica uppger 29 augusti 2026 att hon och vännen Thomas Bartsch den 10 november gick igenom/felsökte lägenheten, satte post-it-lappar vid brister inför mötet, att Thomas blev dålig och behövde sätta sig samt bad om öppen balkongdörr för frisk luft.

Erica uppger även att de träffade damen i lägenhet 1102 under hennes lägenhet, blev inbjudna och att damen bekräftade att det brunnit i 1202. Uppgiften om brand ska behandlas som **vittnesuppgift**. Erica observerade också att luften i 1102 inte upplevdes lika tung och att kökens el/utformning och metallgaller skiljde sig åt.

**Auditåtgärd:** anteckningen finns nu i `anteckningar/2026-08-29_AUDIT-ANTECKNINGAR-11-24-NOVEMBER-2025.md`. Source-locka mot SMS, foto/video eller annan samtidig dokumentation där sådan finns.

---

## FYND 007 – 11 november: branddialogen finns som förstahandsanteckning men inte som source-lockad tidslinjepost

**Status:** `ANVÄNDARENS FÖRSTAHANDSUPPGIFT – BEHÖVER SOURCE-LOCK`

Erica uppger att Thomas Bartsch inför samtliga närvarande tog upp att en oberoende granne uppgett att det brunnit i lägenheten; att Gaby svarade att uppgiften inte stämde; och att Thomas frågade varför en oberoende granne skulle säga detta om det inte stämde. Enligt Erica bemötte ingen annan uppgiften.

**Auditåtgärd:** source-locka mot möteskälla innan exakt ordalydelse används externt.

---

## FYND 008 – 11 november: ventilationsdon/lock i köket saknas i möteskedjan

**Status:** `ANVÄNDARENS OBSERVATION + SENARE SKRIFTLIGT SPÅR`

Erica uppger att donet/locket i köket inte var ditsatt under mötet. Senare skriftlig kommunikation från Gaby anger att locket till frånluften i köket ska vara monterat.

**Auditfråga:** vem ansvarade för monteringen, när beställdes den, och finns arbetsorder/utförandebekräftelse?

---

## FYND 009 – 14–18 november visar att ett åtgärdspaket sattes i rörelse efter första mötet

**Status:** `SOURCE-LOCKAD KEDJA`

- B0100/B0101 verifierar platsmötet.
- B0102 visar att städningen efter mötet hade **Familjebostäder som beställare**.
- B0106 visar att Peter och Micke skulle påbörja arbete samt att städning bokats till 20 november.
- B0107 sammanfattar planerade arbeten: köksgolv, målning/snickeri, el, arbetsbänk samt arbeten i hall, vardagsrum och sovrum 1.

**Auditfråga:** vilka av dessa punkter var uttryckligen överenskomna redan 11 november och vilka beslutades senare?

---

## FYND 010 – 20–25 november innehåller en tät mejlkedja vars saktext saknas i huvudtidlinjen

**Status:** `FINNS MEN ÄR UNDERREPRESENTERAD`

B0108–B0129 finns som datum/ämnesrader i `TIDSLINJE.md`, men sakinnebörden är till stor del inte synlig där. Detta block omfattar frågor/svar om brister, städning, felanmälningar, brand, ventilation och senare åtgärder.

**Auditåtgärd:** fulltextgranska varje post och lägg in de materiellt relevanta frågorna, svaren och uteblivna svaren.

---

## FYND 011 – brandformuleringen ska ligga den 24 november, inte den 25 november

**Status:** `DATUMKORRIGERING / SOURCE-LOCKAD`

B0120, 24 november 2025 kl. 09:51, innehåller Gabys formulering:

> ”det finns som sagt ingen brand situation i denna lägenhet, vi ser inget dokumenterad från vår sida det betyder att det är inget sådant som har inträffat här.”

Direkt därefter skriver Gaby att Caroline bokats in igen beträffande ventilationen.

Den 25 november finns en **separat** formulering i B0124:

> ”Jag ser inte heller att det har funnits någon brand i denna lägenhet, så vet inte vart du har fått detta ifrån...”

Dessa ska inte slås ihop.

---

## FYND 012 – 26 november dokumenterar ett konkret godkänt arbetsupplägg

**Status:** `SOURCE-LOCKAD`

Gaby sammanfattar senare skriftligen att husvärden utför beställningarna, att städning sker först, därefter målning inklusive invändigt köksstomme enligt överenskommelse, sovrum 1, hall, kök och golvsocklar, samt därefter golvbyte.

**Auditfråga:** jämför detta med tidigare besked där Erica uppfattat att hon själv skulle betala för vissa arbeten. Kartlägg när och varför ansvar/kostnad ändrades.

---

## FYND 013 – Miljöförvaltningen hade brand-/saneringsluckan uttryckligen i anmälan men dess bedömning är inte redovisad

**Status:** `DOKUMENTATIONSLUCKA / EJ REDOVISAD BEDÖMNING`

**Bevis-ID:** B0143  
**Källa:** `korrespondens/miljoforvaltningen/2025-11-30_1805_B0143_erica-a-guler_begaran-om-myndighetsinspektion-misstankt-halsorisk-ventilation-och-moge.md`

Den 30 november 2025 skickar Erica en begäran om myndighetsinspektion till Miljöförvaltningen med ämnet:

> `Begäran om myndighetsinspektion – misstänkt hälsorisk, ventilation och mögel-/brandpåverkan`

Mejlet innehåller en särskild rubrik **”Uppgifter om tidigare brand”**, länk till Brottsplatskartan, uppgiften att Familjebostäder inte besvarat frågan om sanering och en uttrycklig begäran om inspektion med hänvisning till bland annat **”misstanke om osanerade brandrester”**.

Det är därför verifierat att Miljöförvaltningen hade brand-/saneringsfrågan framför sig redan vid anmälan.

**Det som ännu måste source-lockas ur dokument 1–107 och övrig akt är:**

1. hur brandhistoriken värderades,
2. hur Gabys förnekande av brand vägdes mot andra uppgifter,
3. hur Jennifers senare påstående om genomförd sanering utan dokumentation värderades,
4. om Miljöförvaltningen begärde saneringsintyg, arbetsrapport eller annat primärt underlag från Familjebostäder,
5. om sådant underlag bedömdes onödigt och i så fall på vilken grund,
6. om brand-/saneringsspåret tekniskt utreddes eller avgränsades bort,
7. var denna bedömning finns dokumenterad inför beslutet 13 april 2026.

**Auditregel:** skriv inte att Miljöförvaltningen ”inte kände till” brandfrågan. Den korrekta öppna frågan är **varför och hur den kända brand-/saneringsluckan hanterades i tillsynen**.

---

## FYND 014 – SSBF:s senare besked flyttar efterarbetsfrågan tillbaka till fastighetsägaren och inomhusmiljöfrågan mot Miljöförvaltningen

**Status:** `NY SOURCE-LOCK / SKA KOPPLAS TILL HUVUDTIDSLINJEN`

I korrespondens med Storstockholms brandförsvar, dnr **3934/2026**, uppger Max Ekberg bland annat att:

- SSBF ventilerade lägenheten för att minimera fortsatta rök- och sotskador,
- deras dokumentation inte visar hur det fortsatta restvärdesarbetet genomfördes,
- kontakt etablerades med Familjebostäder,
- SSBF inte har formellt ansvar för den fortsatta hanteringen efter avslutad insats utan att ansvaret för byggnaden vilar på fastighetsägaren,
- SSBF normalt informerar fastighetsägaren om vidtagna åtgärder och ger råd om vad som återstår,
- Erica hänvisas till fastighetsägaren, berört försäkringsbolag och Brandskyddsföreningen Restvärderäddning för efterarbets-/dokumentationsspåret,
- frågor om inomhusmiljö och kontroll av saneringsarbete hänvisas till Miljöförvaltningen i Stockholms stad.

**Auditbetydelse:** denna ansvarskedja ska ligga i både huvudtidlinjen och brandspåret. Den gör frågan om Miljöförvaltningens hantering av den redan kända sanerings-/inomhusmiljöluckan särskilt relevant, utan att i sig bevisa att MF handlagt fel.

---

## Nästa kontrollblock

- fulltext B0108–B0129,
- exakt mötesinnehåll 11 november,
- kanalrensningens första uppkomst och ordalydelse,
- ventilationsdon/arbetsorder,
- städningens beställningsorsak,
- tidigare mejl/bilder om köksstomme och material nära golvet,
- kostnadsspåret: köksbänk, golv och målning,
- **Miljöförvaltningens dokument 1–107 rad för rad mot brand/sanering/beboelighetsunderlag**,
- därefter fortsatt BEVISREGISTER ↔ TIDSLINJE-audit.
