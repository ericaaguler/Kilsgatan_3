# ALLA SPÅR – AKTIVERING AV GEMENSAM BEVIS-, TIDSLINJE- OCH SOURCE-LOCK-STANDARD

Datum: 2026-08-30  
Status: **STYRANDE FÖR ALLA SPÅR**

## 1. ÖVERORDNAD REGEL

Filen

`STORA-AUDITEN/00-ALLA-SPAR-JURIDISK-BEVISTIDSLINJE-SOURCE-LOCK-MASTERPROMPT.md`

ska tillämpas på **alla juridiska spår och alla bevis-/tidslinjeposter i projektet**.

Den kompletterar:

1. `00-JURIDISK-AI-MASTERPROMPT-KALLKONTROLL.md`
2. `00-MOD-OVERKLAGANDE-MASTERPROMPT-PT-KALLKONTROLL.md`
3. `00-FORSVARBAR-JURIDIK-SPARBARHET-OVERPRÖVNING-MASTERPROMPT.md`
4. `00-HUVUDLAGER-STYRNING-OCH-BEVISSTANDARD.md`

Vid konflikt gäller den regel som ger striktast kontroll av **källa, datum, bevisstatus, rekvisit, spårbarhet, motargument och extern användbarhet**.

---

# 2. GEMENSAM MINIMISTANDARD FÖR ALLA SPÅR

Varje materiellt viktig bevispost ska kunna redovisas som:

**Bevis-ID → händelsedatum → datumprecision → källa → källtyp → primär/sekundär → faktisk uppgift → vad den kan bevisa → vad den inte bevisar → juridisk funktion → saknad komplettering → verifieringsstatus → GRÖN/GUL/RÖD → extern användbarhet → juridiskt spår.**

För varje dom/rättskälla ska motsvarande rättskällekedja finnas:

**domstol → målnummer → datum → rättsfråga → lagrum → avgörande fakta → domstolens faktiska bedömning → prejudikatstatus → juridisk funktion → begränsning → source-lock.**

---

# 3. SPÅR 1 – MILJÖBALK / INOMHUSMILJÖ

Bevisstandarden ska särskilt kontrollera:

- vilka symptom-/olägenhetsuppgifter som är förstahandsuppgifter,
- tekniska mätningars datum, metod, scope och förhållanden,
- vad en punktmätning faktiskt kan och inte kan visa,
- vilka uppgifter som fanns före myndighetsbeslutet,
- vilka uppgifter som tillkom efter beslutet,
- vem som bar utrednings-/bevisbörda enligt tillämplig materiell regel,
- om orsak, olägenhet, omfattning och åtgärdsbehov har hållits isär.

**Förbjudet inferenshopp:** symptom/observation → viss teknisk orsak utan separat stöd.

---

# 4. SPÅR 2 – PBL / BYGGNADSTILLSYN

Bevisstandarden ska särskilt kontrollera:

- vilken konkret PBL-fråga en uppgift stödjer,
- tröskeln `anledning att anta` kontra beviskravet för ingripande,
- OVK-handlingars exakta objekt/system/scope,
- skillnaden mellan byggnadsnivå och lägenhetsnivå,
- tekniska egenskapskrav kontra underhållskrav,
- vad nämnden faktiskt hade i akten när tillsynen avslutades,
- vilka uppgifter som bara finns i senare sammanställningar.

**Förbjudet inferenshopp:** godkänd OVK/byggnad → verifierat felfritt skick i varje enskild lägenhet.

---

# 5. SPÅR 3 – HYRESRÄTT

Bevisstandarden ska särskilt kontrollera:

- lägenhetens faktiska skick vid tillträde,
- när brister felanmäldes,
- hyresvärdens kunskap och åtgärder,
- hinder/men och brukbarhet som juridiska slutsatser – inte faktaetiketter,
- vilken period en viss brist faktiskt är belagd,
- vilka rättsföljder som kräver separat bevisning och beräkning,
- skillnaden mellan fel enligt 12 kap. JB och andra rättsområdens rekvisit.

**Förbjudet inferenshopp:** senare konstaterad brist → lägenheten var automatiskt juridiskt obrukbar från första dagen.

---

# 6. SPÅR 4 – MYNDIGHETSPROCESS / UTREDNINGSANSVAR

Bevisstandarden ska särskilt kontrollera:

- exakt beslutsunderlag vid beslutstidpunkten,
- vad myndigheten visste och när,
- 23 § FL: vilken fråga behövde faktiskt utredas,
- 25 § FL: vilket material av betydelse kommunicerades eller inte kommunicerades,
- 27 § FL: muntliga uppgifter/observationer och dokumentation,
- 32 § FL: vilka omständigheter och regler som faktiskt angavs som avgörande,
- nya uppgifter efter beslut kontra ursprungligt beslutsunderlag,
- myndighetens handlingsplikt, nollbeslut, passivitet och överklagbarhet,
- vad en teknisk rapport faktiskt besvarade och vilka kärnfrågor som återstod.

**Förbjudet inferenshopp:** en rapport finns → ärendet är tillräckligt utrett.

---

# 7. SPÅR 5 – AVTALSRÄTT / SVEK / INFORMATION FÖRE AVTAL

För avtalsrättsdelen ska bevisstandarden särskilt kontrollera:

- exakt prekontraktuell information,
- avtalets signeringstidpunkt,
- vad motparten faktiskt visste före signering,
- vilken konkret omständighet som påstås ha uppgivits felaktigt eller förtegits,
- skillnaden mellan okunskap, administrativ lucka, oaktsamhet och svikligt förfarande,
- väsentlighet/påverkan,
- rättsföljd separat från själva ogiltighetsgrunden.

**Förbjudet inferenshopp:** gammal skadehistorik + saknad handling → medvetet svek.

---

# 8. TVÄRGÅENDE BEVIS-/ORSAKSSPÅR

När materialet används tvärgående för orsak, indicier, vittnesuppgifter eller tekniska motsägelser ska posten fortfarande behålla sitt ursprungliga Bevis-ID och faktainnehåll.

Samma faktapost får kopplas till flera juridiska spår, men den får **inte ändra innehåll eller säkerhetsgrad för att passa ett visst argument**.

Exempel:

- ett vittnesbesök kan vara relevant för både Spår 1 och Spår 3,
- en ventilationsmätning kan vara relevant för Spår 1, 2 och 4,
- ett mejl före avtal kan vara relevant för Spår 3 och avtalsrättsdelen i Spår 5.

Det ska vara **samma bevispost, flera juridiska funktioner**, inte flera versioner av samma faktum.

---

# 9. OBLIGATORISK DUBBELRÄKNINGSKONTROLL

Innan en post skapas i något spår ska det kontrolleras om den redan finns i:

- huvudtidslinjen,
- STORA AUDITEN,
- annat sakspår,
- tidigare praxis-/bevismatris,
- vidarebefordrat mejl,
- senare återberättande.

Klassificera som:

- **NY HÄNDELSE**
- **NY KÄLLA TILL BEFINTLIG HÄNDELSE**
- **MÖJLIG DUBBLETT**
- **DUBBLETT – INTE NY BEVISPOST**

---

# 10. MOTSÄGELSER

Ingen konflikt ska lösas genom att välja den version som verkar mest sannolik.

Varje materiell konflikt ska få ett **MOTSÄGELSE-ID** med:

- Uppgift A / källa A
- Uppgift B / källa B
- bevisstyrka
- möjlig förklaring
- vad som krävs för att lösa konflikten
- vilka juridiska analyser som påverkas

Tills konflikten är löst får ingen version presenteras som säker.

---

# 11. PRAXISLAGRET

Praxisfiler ska inte bara registrera en doms slutsats. För varje dom ska det finnas:

- vad som faktiskt prövades,
- vilka fakta som bar utgången,
- vad domstolen krävde eller accepterade,
- direkt eller analog tillämplighet,
- positiv praxis / motpraxis / processdom,
- vad domen inte bevisar,
- originalstatus,
- eventuell koppling till bevisposter i huvudärendet först efter source-lock.

Praxis får aldrig retroaktivt uppgradera ett GULT/RÖTT faktapåstående till GRÖNT.

---

# 12. EXTERN ANVÄNDBARHET

En post får betecknas:

- **DOMSTOLSKLAR** först efter fullständigt försvarbarhetstest,
- **MYNDIGHETSKLAR** när erforderlig källa, datum och sakuppgift är source-lockade för den användningen,
- annars **KRÄVER KOMPLETTERING**, **INTERN ANALYS ENDAST** eller **FÅR INTE ANVÄNDAS ÄNNU**.

Ingen GUL/RÖD detalj får gömmas i en i övrigt GRÖN mening.

---

# 13. SLUTAUDIT EFTER VARJE STÖRRE UPPDATERING

För varje spår och för projektet som helhet ska redovisas:

1. **SOURCE-LOCKAT**
2. **KRÄVER ORIGINALKONTROLL**
3. **FÅR INTE ANVÄNDAS**
4. **DATUMKONFLIKTER**
5. **PERSON-/TALARKONFLIKTER**
6. **MÖJLIGA DUBBLETTER**
7. **BEVISLUCKOR**
8. **JURIDISKT BÄRANDE HÄNDELSER**
9. **NÄSTA 3–5 SOURCE-LOCK-KONTROLLER**

---

# 14. ÖVERORDNAD ARBETSKEDJA

För **fakta**:

**ORIGINALKÄLLA → DATUM → FAKTISK UPPGIFT → BEVISKLASS → SOURCE-LOCK → JURIDISK FUNKTION → BEGRÄNSNING → EXTERN ANVÄNDBARHET**

För **juridiska slutsatser**:

**FRÅGA → RÄTTSKÄLLA → REKVISIT → SOURCE-LOCKADE FAKTA → TILLÄMPNING → MOTARGUMENT → SLUTSATS → KONTROLL**

## Slutregel

**SAMMA BEVISDISCIPLIN GÄLLER I ALLA SPÅR. RÄTTSREGLERNA FÅR DÄREMOT ALDRIG BLANDAS IHOP MELLAN SPÅREN.**
