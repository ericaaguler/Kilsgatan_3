# STORA AUDITEN – projektets kontrollager

**Fastställd:** 29 augusti 2026  
**Status:** AKTIVT HUVUDLAGER  
**Funktion:** kontrollpanel och fullständig bevis-/rättsfunktionsaudit för hela Kilsgatan 3-projektet.

## 1. Detta är inte en sammanfattning

`STORA-AUDITEN/` ligger som ett eget huvudlager ovanpå projektets befintliga tidslinjer, sakspår och analyser.

Lagret ska inte återberätta ärendet. Det ska kontrollera om varje påstående faktiskt kan följas tillbaka till rätt källa och om beviset används för rätt juridisk funktion.

**Styrande kedja:**

`originalkälla → BEVISREGISTER → STORA AUDITEN → TIDSLINJE.md → sakspår → extern juridisk användning`

- `BEVISREGISTER.md` = källindex.
- `TIDSLINJE.md` = enda kanoniska kronologiska huvudtidslinjen.
- `STORA-AUDITEN/` = kontrollagret som avgör vad som är källsäkert, vad ett bevis faktiskt visar, vad det inte visar och vad som saknas.
- Separata brand-, ventilation-, myndighets- och övriga spår är filtrerade arbetsvyer och får inte ersätta original eller huvudtidslinje.

## 2. Obligatoriska fält för varje identifierad bevispost

Varje bevispost ska auditeras enligt exakt denna kedja:

1. **Datum/tid**
2. **Källa/originalfil/bevis-ID**
3. **Faktisk uppgift** – vad källan direkt visar, utan slutsatsinflation
4. **Bevisklass**
5. **Juridisk funktion**
6. **Vad beviset INTE bevisar**
7. **Saknad komplettering**
8. **Relevant lag/princip**
9. **Status i huvudtidslinjen**
10. **Status i relevanta sakspår**
11. **Originalkontroll** – om uppgiften är låst mot originalfil eller bara finns i sammanställning/transkription
12. **Extern användbarhet** – JA / JA MED RESERVATION / NEJ ÄNNU

En post är inte fullauditerad bara för att den finns i `BEVISREGISTER.md` eller är markerad `Kontrollerat: Ja` där. STORA AUDITEN gör en separat kontroll av bevisfunktion, avgränsning och extern användbarhet.

## 3. Bevisklasser

- `A – PRIMÄRHANDLING`: originalmejl, myndighetsbeslut, rapport, arbetsorder, mätanteckning eller annan registrerad handling.
- `B – DIREKT DOKUMENTERAD HÄNDELSE`: foto/video eller source-lockad ljud-/mötesåtergivning.
- `C – SAMTIDA FÖRSTAHANDSUPPGIFT`: Ericas samtida uppgift om vad hon själv sett, hört eller upplevt.
- `D – VITTNESUPPGIFT`: annan persons förstahandsuppgift.
- `E – SENARE SAMMANSTÄLLNING/ANALYS`: tidslinje, partsinlaga, transkriptionssammanställning, handover eller analys. Får inte ersätta primärkällan.
- `F – HYPOTES/INFERENS`: möjlig förklaring eller slutsats som ännu inte är fastställd.

## 4. Juridiska funktionskoder

- `J1 KÄNNEDOM` – när Familjebostäder fick information.
- `J2 FAKTISKT SKICK/HINDER` – bostadens faktiska skick eller begränsat nyttjande.
- `J3 SYMPTOM-/EXPONERINGSMÖNSTER` – återkommande reaktioner; inte medicinsk kausalitet.
- `J4 TEKNISKT SCOPE` – exakt vad en undersökning mätte/undersökte och vad den inte täckte.
- `J5 MOTSÄGELSE/TILLFÖRLITLIGHET` – motstridiga besked eller instabil faktabas.
- `J6 DOKUMENTATIONSLUCKA` – efterfrågad primär dokumentation har inte redovisats.
- `J7 MYNDIGHETENS KÄNNEDOM` – vad myndigheten faktiskt hade före beslut.
- `J8 UTREDNINGSVAL/AVGRÄNSNING` – vad myndigheten valde att utreda, avgränsa eller lämna obesvarat.
- `J9 BESLUTSMOTIVERING` – kopplingen mellan akten och de avgörande skälen.
- `J10 DOMSTOLENS UTREDNING` – domstolens hantering av utredning/oklarheter.

## 5. Originalkontroll – hård regel

Följande får **inte** användas externt som säker ordalydelse eller säker faktisk händelse endast därför att uppgiften finns i en sammanställning:

- AI-/manuell sammanfattning,
- tidslinjetillägg,
- handover,
- juristunderlag,
- partsinlaga som återger ett tidigare bevis,
- transkription som inte är kontrollerad mot originalinspelningen,
- filnamn som påstår vilket möte en ljudfil avser,
- inklistrat mejl eller markdown-export som inte kan knytas till native original/official aktkopia.

De ska markeras:

- `ORIGINAL-LOCKAD`
- `SOURCE-LOCK KRÄVS`
- `TRANSKRIPTION – ORIGINALKONTROLL KRÄVS`
- `SAMMANSTÄLLNING – PRIMÄRKÄLLA KRÄVS`
- `JURIDISK KONTROLL KRÄVS`
- `TEKNISK SAKKUNNIG KRÄVS`

**Exakta citat ur ljud får inte användas externt förrän ordalydelse, talare och tidskod är verifierade mot originalfilen.**

## 6. Kontroll mot överdrivna slutsatser

STORA AUDITEN ska aktivt stoppa följande felslut:

- saknat saneringsintyg = inte automatiskt bevis för att sanering aldrig skedde,
- flera symptomvittnen = inte automatiskt medicinsk kausalitet,
- godkänd OVK = inte automatiskt bevis att objekt 60020562 kontrollerats eller att alla inomhusmiljöproblem är uteslutna,
- OCAB-resultat = gäller endast rapportens faktiska uppdrag/metod,
- motsägelse inom Familjebostäder = visar motstridiga uppgifter, inte automatiskt vilken version som är sann,
- brand 2017 + symptom 2025/2026 = visar inte i sig kausalitet mellan branden och dagens problem,
- `samma sakfråga` = inte automatiskt bevis för hur alla senare faktiska omständigheter ska behandlas processuellt,
- `gallras` i ett kundservicesvar = inte automatiskt bevis för faktisk gallring/radering,
- korrigerat ordval om `gallring` = inte automatiskt svar på en bredare GDPR-/allmän-handlingsbegäran.

## 7. Aktuell omfattning

`BEVISREGISTER.md` innehåller för närvarande bevis-ID **B0001–B0464**. Alla dessa poster ingår i STORA AUDITENS scope.

**B0001–B0464 har nu fått 464/464 separata bas-auditrader i registermatrisen.** Bas-audit innebär att varje registrerad post har kvalitetsstatus/originalspärr; det betyder inte att varje post redan är postspecifikt fullauditerad eller EXTERN-READY.

Nya identifierade bilder, video, ljud och processuppgifter som ännu saknar B-ID ska läggas i originalkarantänen tills original/source-lock är säkrat och posten har registrerats. Materiellt viktiga sådana poster får samtidigt ett tillfälligt `AUD-...`-ID och fullauditeras i `07-NYA-BEVISPOSTER-FULLAUDIT-CHAT-2026-08-29.md`, utan att `AUD-...` ersätter ett permanent B-ID.

Nya bevis-ID ska automatiskt läggas till auditens scope.

## 8. Filer i huvudlagret

- `01-KONTROLLPANEL.md` – hela projektets aktuella kontrollpanel.
- `02-BEVISPOSTER-MASTER.md` – detaljaudit av bevisposter och kritiska beviskedjor.
- `03-ORIGINALKONTROLL-OCH-KOMPLETTERINGSKO.md` – sådant som måste tillbaka till originalfil eller kompletteras innan extern användning.
- `04-MF-MMD-PROCESSAUDIT.md` – fördjupad processaudit av Miljöförvaltningen och Mark- och miljödomstolen.
- `05-REGISTERMATRIS-B0001-B0464.md` – index till 464/464 separata bas-auditrader för samtliga registrerade Bevis-ID.
- `06-CHAT-BEVIS-ORIGINALKARANTAN.md` – nya visuella/ljud-/SMS-/processbevis från arbetschatten som ännu saknar B-ID eller source-lock.
- `07-NYA-BEVISPOSTER-FULLAUDIT-CHAT-2026-08-29.md` – full audit enligt samtliga obligatoriska fält för materiellt viktiga nya bevis från chatten, med `AUD-...`-ID tills permanent B-ID/source-lock finns.
- `08-MIRIAM-SAMMA-SAKFRAGA-JENNIFER-MMD-AUDIT.md` – full processaudit av Miriams `samma sakfråga`, senare omständigheter efter 13 april och Jennifer/MF-spåret.
- `09-PROCESS-DOKUMENTHANTERING-HGF-GALLRING-SAMMA-SAKFRAGA-AUDIT.md` – samlad process-/dokumenthanteringsaudit som låser gallringskedjan, HGF-originalkarantänen och de nya processreglerna.
- `08-FYR-PDF-OCH-LAGUTNYTTJANDEAUDIT-NYA-BEVISPOSTER-2026-08-29.md` – fyr-PDF-audit av de nya bevisposterna med kontroll mot aktuell 2026-rätt; särskilt LOMD/ärendelagen, miljöbalken 26 kap., förvaltningslagen och 12 kap. JB.

Registermatrisens fem segment ligger i `audit/` men är **underordnade STORA-AUDITEN** och nås via `05-REGISTERMATRIS-B0001-B0464.md`. De är inte ett konkurrerande huvudlager.

## 9. Rättsliga kontrolltaggar i den nya registerauditen

Vid postspecifik fördjupning används bland annat:

- `JB12:9` – 12 kap. 9 § jordabalken, brukbart skick på tillträdesdagen.
- `JB12:15` – 12 kap. 15 § jordabalken, skick/underhåll under hyrestiden.
- `JB12:16` – 12 kap. 16 § jordabalken, skada/hinder/men och åtgärdsfunktion.
- `MB9:3` – 9 kap. 3 § miljöbalken, olägenhet för människors hälsa.
- `MB26:19` – 26 kap. 19 § miljöbalken, kontroll/egenkontroll.
- `FL23` – 23 § förvaltningslagen, myndighetens utredningsansvar.
- `PBL-OVK` – PBL/PBF:s bestämmelser om obligatorisk ventilationskontroll inom deras faktiska scope.
- `KÄLLA`, `UNDERRÄTTELSE`, `SPÅRBARHET`, `DUBBELRÄKNING`, `DOKUMENTHANTERING`, `GDPR/TF` – kontrolltaggar som hindrar att derivat, partsuppgifter och dubbletter ges större räckvidd än källan.

## 10. Slutregel

**Ingen berättelse får vinna över källan. Ingen juridisk slutsats får bli starkare än beviset. Ingen sammanställning får ersätta originalet.**