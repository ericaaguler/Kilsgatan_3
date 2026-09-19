# Akt 1–107 – uttryckliga hänvisningar till handlingar och saknade original

**Datum för audit:** 19 september 2026  
**Ärende:** Miljöförvaltningen 2025-23696  
**Objekt:** Kilsgatan 3, lägenhet 1202 / objekt 0562  
**Omfattning:** Akt 1–107, jämförda mot kontrollregistret i `analyser/MF-AKT-01-107-KONTROLLREGISTER-2026-08-29.md`, den nya ärenderapporten från 16 september 2026 och repots faktiska trädlager.

## 1. Källregel

Den här kontrollen skiljer mellan:

- **A – uttryckligen angiven men inte återfunnen:** handlingen/bilagan nämns konkret i aktmaterialet, men den har inte återfunnits i det tillgängliga utlämnade materialet.
- **B – aktposten finns, men originalet är inte separat säkrat i GitHub:** detta är en repo-/originalfilslucka. Det bevisar inte att handlingen saknades hos Miljöförvaltningen.
- **C – uttryckligen efterfrågat underlag/svar saknas i den identifierade kedjan:** detta är en dokumentations- eller svarslucka, inte nödvändigtvis en saknad bilaga.
- **D – inte räknat som akt 1–107-fynd:** senare material, externa spår eller rena kontrollhypoteser.

Frånvaro i repot eller i den utlämnade kopian bevisar inte att en handling aldrig har funnits. Extern formulering ska därför vara: **”inte återfunnen/inte identifierad i det granskade materialet”**.

## 2. Fynd i själva aktkedjan 1–107

| Akt | Uttrycklig hänvisning | Kontrollresultat | Status |
|---:|---|---|---|
| **81** | En konkret bifogad `.msg`-fil med angiven ämnesrad. | Den specifika MSG-filen har inte återfunnits. Akt 82 återger en tråd med samma centrala ämne, men ersätter inte säkert originalfilen eller dess metadata/bilagor. | **A – verifierad spårbarhetslucka** |
| **58** | Miljöförvaltningen hänvisar till en OVK utförd 2018. | Akt 58:s bilageförteckning innehåller tre 2022-filer. Ingen 2018-fil anges där. Akt 62 kommunicerar åter endast 2022-handlingarna och någon 2018-OVK har inte identifierats i akt 58–68. | **A – uttryckligen hänvisad men inte återfunnen** |
| **89–90** | MF anger att Familjebostäder ska svara om sanering efter brand, om/när kanalrensning utförts, tidigare kanalrensning och VOC-test. | Något konkret primärunderlag eller ett substantiellt svar på dessa fyra frågor har inte identifierats före beslutet. Akt 95 innehåller ”Vi har inget mer att tillägga”, men redovisar inte saneringsintyg, arbetsrapport, kanalrensningsrapport eller VOC-resultat. | **C – uttryckligen efterfrågat underlag/svar inte identifierat** |
| **58** | Familjebostäder uppger att kanalrensning utfördes 2021-03-22–30 och att lägenhet 562 inte lämnade tillträde. | Ingen separat HA Ventilation-rapport, kanalrensningsrapport, tillträdeslista, arbetsorder eller annan samtidig primär teknisk handling har identifierats som självständigt verifierar uppgiften. | **C – teknisk verifieringslucka; inte bevis för att åtgärden aldrig skedde** |
| **107** | Erica begär bl.a. tjänste-/besöksanteckningar, Stina Jurells iakttagelser och korrespondens. | Ingen separat Stina-anteckning har identifierats i den återhämtade aktkedjan. Akt 107 är dock en begäran efter beslutet och bevisar inte att en separat anteckning måste ha funnits. | **C/D – kontrollpunkt, inte fastslaget saknat dokument** |

## 3. Ytterligare original som saknas i GitHub-lagret

Följande handlingar är registrerade eller uttryckligen åberopade i akt-/projektmaterialet, men deras separata original har inte identifierats i repots trädlager:

| Akt/post | Handling | Vad som finns i stället | Status |
|---:|---|---|---|
| **31** | OCAB-rapport, registrerad 22 december 2025 | B0449, som bemöter OCAB-rapporten, samt analyser. Själva OCAB-originalet finns inte som identifierad original-PDF i repot. | **B – repo-original saknas; inte bevis för att akt 31 saknas** |
| **33** | Flödesmätning/Caroline Blombergs ventilationsanteckning | Hänvisningar och återgivningar finns; den separat angivna `.docx`-originalfilen har inte identifierats. | **B – originalfil inte säkrad** |
| **59–61** | Tre OVK-protokoll från 2022 | Metadata/analyser finns. De underliggande OVK-originalen är inte identifierade som egna PDF-filer i repot. Akt 60 är den objektsrelevanta 2022-handlingen för 0562. | **B – originalfiler inte säkrade** |
| **87, 88, 98, 101, 104** | Fotodokumentation/foton registrerade i aktlistan | Vissa bilder och parts-PDF:er finns, men ingen säker separat originalkedja är kopplad till vart och ett av dessa aktnummer. | **B – aktbilagekoppling inte säkrad** |
| **100, 102, 103** | Skriftliga förstahands-/vittnesuppgifter | Korrespondensåtergivningar finns, men de exakta aktoriginalen är inte identifierade som separata originalfiler. | **B – aktoriginal inte säkrade** |
| **84, 85, 89, 92–96** | Centrala MF-/partsakter i den senare beslutsfasen | Källåtergivningar, registeruppgifter och analyser finns; separata aktoriginal är inte konsekvent source-lockade i GitHub. Akt 90:s kontrollrapport finns som PDF i `handlingar/miljoforvaltningen/`. | **B – delvis täckt, originalnivån behöver kompletteras** |
| **105–106** | Beslutet 13 april 2026 och expedieringsmejlet | Beslutet och utskicket är återgivna/analyserade, men original-PDF/aktfil för själva beslutet är inte identifierad i repot. | **B – repo-original saknas** |

## 4. Fynd som inte ska blandas ihop med akt 1–107

- Det senare utlämnade 2018-materialet från Stadsbyggnadskontoret är inte därmed bevisat vara en del av Miljöförvaltningens beslutsunderlag före 13 april 2026.
- RVR:s uppgift att ingen rapport verkar finnas hos dem är ett senare externt spår, inte en saknad MF-aktbilaga.
- Jennifers senare mejl och dess bilagor från augusti 2026 är inte akt 1–107.
- En aktpost som finns i Miljöförvaltningens ärenderapport men vars original inte finns i GitHub ska beskrivas som **”original inte säkrat i repot”**, inte som **”akten saknar handlingen”**.

## 5. Samlad slutsats

Utöver de två redan identifierade huvudfynden finns följande ytterligare dokumentationsluckor:

1. **Akt 89–90:** fyra uttryckligt efterfrågade tekniska/administrativa svar eller underlag (sanering, kanalrensning, tidigare kanalrensning och VOC-test) har inte identifierats som konkreta primärhandlingar före beslutet.
2. **Akt 58:** den uppgivna kanalrensningen 2021 saknar identifierad separat arbets-/utförandedokumentation.
3. **Akt 31:** OCAB-rapporten är registrerad i aktförteckningen men originalet är inte säkrat i GitHub.
4. **Akt 33:** Caroline Blombergs ventilationsunderlag/`.docx`-originalet är inte säkrat.
5. **Akt 59–61, 87, 88, 98, 101, 104, 100, 102 och 103:** de registrerade originalbilagorna är inte separat säkrade i repot.
6. **Akt 105–106:** beslutet och expedieringsoriginalet är återgivna men originalfilerna är inte identifierade i repot.

De två starkaste fynden som kan formuleras som uttryckligen hänvisade men inte återfunna handlingar är fortfarande:

- **Akt 81 – den specifika MSG-bilagan.**
- **Akt 58–62 – 2018 års OVK-protokoll.**

Alla övriga fynd ska hållas i kategorin **original-/spårbarhetslucka eller uteblivet identifierat underlag**, inte automatiskt beskrivas som att handlingen har förstörts, undanhållits eller aldrig funnits.
