# STORA AUDITEN – STYRANDE HUVUDKONTROLLPANEL FÖR HELA PROJEKTET

**Datum:** 2026-08-30  
**Status:** **STYRANDE HUVUDLAGER – SKA LÄSAS FÖRE TIDSLINJER, BEVISREGISTER OCH SPÅRANALYSER**  
**Funktion:** Detta är inte en sammanfattning. Detta är projektets kontrollpanel för vad som får betraktas som verifierat faktum, vad som endast är stödbevis, vad som fortfarande är sammanställning/transkription, vilken juridisk funktion varje post kan bära och vad som måste tillbaka till originalfil innan extern användning.

---

# 0. ABSOLUT HUVUDREGEL

Varje materiellt relevant bevispost ska kunna följas genom hela kedjan:

> **DATUM → KÄLLA/ORIGINAL → FAKTISK UPPGIFT → BEVISKLASS → JURIDISK FUNKTION → VAD DEN INTE BEVISAR → SAKNAD KOMPLETTERING → RELEVANT LAG/PRINCIP → STATUS I HUVUDTIDSLINJEN/SPÅREN**

Ingen uppgift får användas externt som verifierat faktum endast därför att den finns i en ChatGPT-sammanställning, tidigare tidslinje, transkription, anteckning, juridiskt analysdokument, sekundär artikel eller en parts senare återgivning av ett äldre förlopp. När original finns ska originalet styra.

**SOURCE-LOCK-GATE:** Om posten fortfarande bara finns som **SAMMANSTÄLLNING**, **TRANSKRIPTION**, **SEKUNDÄR ÅTERGIVNING** eller **ANALYS**, ska den tillbaka till originalfilen innan den citeras externt som faktisk uppgift.

---

# 1. BEVISKLASSER OCH EXTERN GATE

| Klass | Definition | Extern användning |
|---|---|---|
| **A1 – ORIGINAL PRIMÄRKÄLLA LÅST** | Originalmejl, originalbeslut, originalrapport, originalfoto/video/ljud eller myndighetshandling har kontrollerats. | **JA**, inom källans faktiska scope. |
| **A2 – ORIGINAL FINNS, DELVIS LÅST** | Original finns men aktuell formulering/sida/tidskod är inte slutkontrollerad. | **NEJ för ordagrant/faktaprecist påstående** tills kontroll. |
| **B – FÖRSTAHANDSUPPGIFT** | Identifierad person lämnar egen observation/uppgift. | **JA som vittnes-/partsuppgift**, inte automatiskt som tekniskt faktum. |
| **C – SAMTIDA PARTSUPPGIFT** | Erica/annan part dokumenterar nära händelsen vad som upplevts/sagts. | **JA för att uppgiften lämnades då**, inte för att sakförhållandet objektivt är bevisat. |
| **D – TRANSKRIPTION** | Text från ljud/video utan slutkontroll mot original och tidskod. | **NEJ** som exakt citat innan originalkontroll. |
| **E – SAMMANSTÄLLNING/SEKUNDÄRKÄLLA** | Tidslinje, AI-sammanställning, artikel, referat utan original. | **NEJ** som självständigt faktabevis. |
| **F – ANALYS/HYPOTES/INFERENS** | Juridisk/teknisk slutsats eller möjlig förklaring. | **ALDRIG** som verifierat faktum. |

Status: **GRÖN – ORIGINAL LÅST / EXTERN GO**, **GUL – ANVÄNDBAR MED RESERVATION**, **ORANGE – ORIGINAL/SCOPE/REKVISIT MÅSTE KOMPLETTERAS**, **RÖD – STOPP FÖR EXTERN FAKTAANVÄNDNING**.

---

# 2. STYRNING MOT ÖVRIGA PROJEKTLAGER

- `BEVISREGISTER.md` = inventering och länkning av originalposter.
- `BRAND-TIDSLINJE.md` = kronologi för brandspåret.
- `KANALRENSNING-TIDSLINJE.md` = kronologi för ventilations-/kanalspåret.
- `PRAXIS/00ZZ-MASTER-AUDIT-SPAR1-5-LASSTATUS-OCH-OVERKLAGANDE-2026-08-30.md` = juridisk låsstatus.
- `PRAXIS/01...05...` = detaljanalys per rättsspår.
- `STORA-AUDITEN.md` = äldre huvudlager och detaljkälla.

**Vid konflikt om bevisstatus ska denna fil vara styrande tills posten source-lockats på nytt.**

---

# 3. HUVUDKONTROLLPANEL – BEVISPOSTER

## A. BRAND / HISTORIK / SANERING / DOKUMENTATION

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-001 / 2017-11-16** | Storstockholms brandförsvar, händelserapport | Brand i byggnad/lägenheten; brandstart i kök; lägenheten ventilerades; Familjebostäder kontaktades under insatsen. | A1 | Verifierar historisk brand och att fastighetsägaren blev kontaktad. Relevans för historik, kunskapskedja, återställnings-/dokumentationsspår. | Att branden orsakar dagens besvär; att sanering uteblev; hur stor brandpåverkan blev efter insatsen. | Full återställningskedja efter räddningstjänstens avslut: beställning, entreprenör, sanering, teknisk kontroll, slutkontroll. | Bevisvärdering; PBL 8:14 som möjlig senare funktionsram; MB/JB endast efter sakanknytning. | **GRÖN fakta. Spår 1/2/3/5. Huvudtidslinje: JA.** |
| **SA-002 / 2017-11-16 → efter insats** | SSBF:s senare besked 2026 | SSBF uppger att deras dokumentation inte visar hur fortsatt restvärdesarbete genomfördes och att ansvar för byggnaden efter avslutad räddningsinsats ligger på fastighetsägaren. | A1 | Avgränsar räddningstjänstens scope och visar att senare återställning måste verifieras i andra källor. | Att FB faktiskt brustit i återställning; att ingen sanering utfördes. | Fastighetsägarens skade-/underhålls-/entreprenörsakt. | Scope-princip; bevisvärdering. | **GRÖN för vad SSBF:s akt inte omfattar. Spår 2/5.** |
| **SA-003 / 2025-11-07** | Thomas Duvsjö / Thomas Bartsch, vittneskedja | Uppgift lämnas att det tidigare brunnit i lägenheten. | B/C | Tidig kunskapsmarkör för när branduppgiften kom in i huvudärendet. | Exakt branddatum, brandorsak, saneringsstatus eller dagens kausalitet. | Direkt vittnesintyg/ljud/samtida meddelande. | Fri bevisvärdering. | **GUL. Brandtidslinje. Spår 5 kunskap efter avtal.** |
| **SA-004 / 2025-11-10** | Äldre kvinnlig granne, enligt samtida uppgift | Ytterligare granne uppger att det tidigare brunnit i lägenheten. | B/C | Oberoende stöd för att brandhistoriken inte uppstod först långt senare. | Exakt brandomfattning/sanering/orsak till dagens problem. | Identifiering + förstahandsintyg om möjligt. | Fri bevisvärdering. | **GUL. Huvudtidslinje som vittnesuppgift.** |
| **SA-005 / 2025-11-11** | Möte med Familjebostäder + ljudspår | Branduppgiften tas upp vid mötet enligt projektets samtidiga kedja. Exakt dialog beror på ljudsource-lock. | A2/D | Kunskapsmarkör för när brandfrågan uttryckligen nådde FB i pågående ärende. | Exakta uttalanden, erkännanden eller besked om sanering. | Ljudfil → talare → tidskod → ordagrann kontroll. | Bevisvärdering; kunskapstidpunkt. | **ORANGE tills ljud låsts. Spår 5.** |
| **SA-006 / 2025-11-24** | Gaby Khalaf, originalmejl | Gaby anger att hon inte ser dokumenterad brand från FB:s sida och drar slutsatsen att sådan händelse inte inträffat där. | A1 | Visar FB-företrädares faktiska besked efter att frågan uppkommit. Central för senare motsägelse-/kunskapsaudit. | Vad FB faktiskt visste 2017 eller före avtalet 2025; att branden saknades i alla system. | Native mejl direktlänkas i Bevisregister. | Bevisvärdering; AvtL endast som senare kunskaps-/systembevis, inte föravtalsbevis. | **GRÖN när native mejl åberopas. Spår 5.** |
| **SA-007 / 2025-11-25** | Gaby Khalaf, originalmejl | Gaby upprepar att hon inte ser att det funnits någon brand i lägenheten. | A1 | Bekräftar samma skriftliga ståndpunkt vid två tillfällen. | Att FB som juridisk person saknade historisk kunskap; att branden inte registrerats i annat system. | System-/objektsakt och organisatorisk kunskapskedja. | AvtL 30/33 endast indirekt; bevisvärdering. | **GRÖN faktisk post / GUL avtalsfunktion.** |
| **SA-008 / 2025-11-28** | Erica → Gaby, cc Jennifer | Erica anger att tre grannar berättat om branden och frågar om lägenheten sanerats efter brandtillbudet. | A1/C | Visar exakt vilken kontrollfråga FB fick och när. | Att vittnenas uppgifter är tekniskt korrekta i alla detaljer; att sanering saknades. | Source-lock vittnen separat. | Kunskaps-/reklamationskedja. | **GRÖN för kommunicerad fråga. Spår 5.** |
| **SA-009 / 2025-11-28** | Jennifer Ehlin, originalmejl | Jennifer svarar i tråden men besvarar inte brand-/saneringsfrågan i sak och föreslår möte. | A1 | Process-/kommunikationsbevis: frågan var uttryckligen ställd men skriftligt sakbesked uteblev då. | Att Jennifer saknade kunskap eller medvetet undvek frågan. | Mötesljud + senare svar. | Bevisvärdering. | **GRÖN faktisk post. Spår 5.** |
| **SA-010 / 2025-12-02** | Jennifer Ehlin, native e-post | Jennifer skriver att lägenheten ”självklart” har sanerats efter en eventuell brand men att hon saknar dokumentation och att äldre uppgifter inte finns i fastighetssystemet. | A1 | Mycket viktig senare bolagsuppgift om historik och dokumentationsläge. Öppnar frågan vilken faktisk källa påståendet om sanering bygger på. | Att sanering faktiskt skett; att den var korrekt; att Jennifer/uthyrningen visste detta före 12 aug 2025; att dagens problem har brandorsak. | Underliggande källa för Jennifers slutsats; intern akt/systemhistorik. | AvtL 30/33 – endast som senare bevisled; bevisvärdering. | **GRÖN fakta / ORANGE för svekslutledning. Spår 5.** |
| **SA-011 / 2025-12-10** | Erica → Jennifer | Erica pekar uttryckligen ut motsättningen mellan Gabys besked och Jennifers uppgift och begär korrekt version skriftligen. | A1/C | Visar att motsägelsen identifierades och kommunicerades i realtid. | Vilken av versionerna som objektivt är sann. | FB:s underliggande dokument/systemkontroll. | Bevisvärdering. | **GRÖN för kommunicerad motsägelse. Spår 5.** |
| **SA-012 / 2025-12-12** | Jennifer Ehlin | Jennifer skriver att kvarvarande frågor ska gås igenom 17 december. | A1 | Visar uttryckligt åtagande att ta upp kvarstående frågor. | Att frågorna faktiskt togs upp eller besvarades. | 17 dec ljud/source-lock + efterföljande skrift. | Bevisvärdering/ansvar. | **GRÖN. Spår 5/huvudtidslinje.** |
| **SA-013 / 2025-12-17** | Möte + ljudinspelning | Projektets sammanställning anger att kvarstående brand-/sanerings-/dokumentationsfrågor inte tas upp/besvaras. | D | Kan bli viktigt process-/ansvarsbevis om originalet bekräftar detta. | Exakt vad som inte sades; medvetet undvikande. | Full ljudkontroll med tidskod och agenda/frågelista. | Bevisvärdering. | **RÖD för extern exakt formulering tills ljud låst.** |
| **SA-014 / 2026-08-11** | S:t Erik Försäkrings AB | Bolaget bekräftar att FB var försäkrat där 2017 men att inget skadeärende finns/har funnits registrerat för Kilsgatan 3 och att skadan inte anmälts dit. | A1 | Verifierar frånvaro av skadeärende hos just detta försäkringsbolag/system. | Att FB inte hanterade branden internt eller genom annan entreprenör/försäkringslösning; att ingen sanering skedde. | FB:s egen skade-/entreprenörsakt. | Negativ bevisning avgränsas till källans register/scope. | **GRÖN inom scope. Spår 5/brand.** |
| **SA-015 / 2026-08-17** | Brandskyddsföreningen Restvärderäddning | RVR uppger att det inte verkar finnas någon rapport hos dem för händelsen. | A1 | Verifierar frånvaro i RVR:s tillgängliga rapportspår. | Att inget restvärdesarbete eller sanering skett. | Eventuella kund-/försäkringsbolagsakter och FB-order. | Scope/negativ bevisning. | **GRÖN inom scope.** |

## B. TILLTRÄDE / SKICK / OCAB / STÄDNING

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-020 / 2025-08-12** | Hyresavtal + avtalsverifikat + besiktningsmaterial före signering | Avtalsbildningen sker; lägenhetsspecifikt besiktningsmaterial lämnas före BankID-signering enligt Spår 5-source-lock. | A1 | Fixerar den kritiska föravtalstidpunkten och vilken informationskanal som användes. | Att protokollet lovade fullständig skadehistorik; att FB kände till dold kvarvarande brist. | Full prekontraktuell kommunikationskedja i ett paket. | AvtL 30/33; 12:9 JB. | **GRÖN. Spår 5 kärna.** |
| **SA-021 / 2025-10-01** | Avtal/tillträdeshandling | Tillträde till lägenheten. | A1 | Startpunkt för 12:9 JB och faktisk nyttjandekedja. | Att lägenheten objektivt var bristfällig just då. | Tillträdesfoto/video + besiktningsprotokoll rad för rad. | 12 kap. 9 § JB. | **GRÖN. Spår 3.** |
| **SA-022 / tidigt okt 2025** | Foto/video vid tillträde | Bilder/video dokumenterar kök/badrum/skick. | A1/A2 | Kan objektivt jämföras mot besiktningsprotokollet och senare åtgärder. | Orsak, ålder eller teknisk betydelse utan sakkunnig bedömning. | Datum- och filmetadata + rad-för-rad-matris mot besiktningsprotokoll. | 12:9 JB; bevisvärdering. | **GUL tills full fil-till-protokollmatris. Spår 3/5.** |
| **SA-023 / okt 2025** | OCAB-rapport | OCAB tillkallas efter missfärgningar inför inflytt; fuktproblem/missfärgning hanteras inom ett begränsat uppdrag. | A1 | Objektiv teknisk post om att ett konkret skick-/fuktspår utreddes före/kring inflytt. Viktig för scope-analys. | Total inomhusmiljö, VOC, brandrester, mögeldiagnos eller full orsaksutredning om detta låg utanför uppdraget. | Uppdragsbeställning + hela rapporten + exakt scope. | 12:9/15/16 JB; MB-utredningens scope endast analogt. | **GRÖN/GUL beroende exakt proposition. Spår 1/3/5.** |
| **SA-024 / 2025-10-27** | Städorder + samtida mejl/uppgift | Första professionella städningen genomförs. | A1/C | Åtgärdskedja; kan användas för före/efter-jämförelse av rapporterade problem. | Att städningen eliminerade eller inte eliminerade en teknisk källa utan effektkontroll. | Arbetsrapport + före/efterobservationer. | 12:15/16 JB; bevisvärdering. | **GUL.** |
| **SA-025 / 2025-11-20** | Foto på TASKI Sani MouldOut | Rengöringsmedel avsett för mögelrelaterad rengöring finns på plats vid städning. | A1 | Visar produktval/åtgärdsmiljö. | Att mögel var konstaterat; att produkten användes på viss yta; att mikrobiell skada fanns. | Städarbetsrapport/beställning. | Bevisvärdering. | **GRÖN för produktens närvaro / RÖD för mögeldiagnos.** |
| **SA-026 / 2025-11-20 kväll** | Erica → Gaby | Erica rapporterar att städarna sagt att ingrodd smuts/”mögel” inte går bort och skiljer detta från vanlig städreklamation. | A1/C | Samtida kunskaps-/reklamationsbevis mot FB. | Att städarnas benämning var en fackmässig mögeldiagnos. | Direkt städfirmaoriginal/intyg. | 12:15/16 JB; kunskapskedja. | **GRÖN för att uppgiften rapporterades; GUL för underliggande sakförhållande.** |
| **SA-027 / 2025-11-27** | Tredje städning/foto | Ytterligare städ-/rengöringsåtgärd genomförs. | A1/A2 | Visar upprepade åtgärder före senare myndighetsinspektion och att okulärt tillstånd kan ha förändrats. | Orsak eller faktisk avhjälpning. | Arbetsorder/rapport + ytor. | Scope/tidsfaktor i bevisvärdering. | **GUL. Spår 1/3.** |

## C. VENTILATION / KANALRENSNING / OVK / TEKNISKA KONTROLLER

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-030 / 2025-11-04** | Drift-/serviceanteckning | Luftflöde justeras från ca 7,4 till 10,2 l/s i grundläge och 35 l/s forcerat; uppgift finns om kanalrensning/rensning. | A1/A2 | Objektiv teknisk åtgärds-/mätpunkt. Visar att ventilationen faktiskt var föremål för åtgärd. | Full systemfunktion, exakt kanalsträcka, långtidseffekt eller orsak till alla symptom. | Arbetsorder + utföranderapport + systemritning + före/eftermätning. | PBL 8:14; 11:5; MB 26:22 analogt för scope; 12:15/16 JB. | **GUL p.g.a. scope. Spår 1/2/3.** |
| **SA-031 / 2025-11-10** | Gaby Khalaf originalmejl | Gaby skriver att ventilation som inte fungerar är ny information för henne och att problemet ska felsökas; hon beskriver svårigheten att förstå varför problemet upplevs just i denna lägenhet. | A1 | Stark kunskapsmarkör för att orsaks-/felsökningsfrågan fortfarande var öppen efter åtgärden 4 nov. | Att objektiv ventilationsbrist redan var slutligt konstaterad. | Vad felsökningen faktiskt bestod av efter 10 nov. | 12:15/16 JB; senare MB/PBL tillsyn; bevisvärdering. | **GRÖN. Spår 1/2/3.** |
| **SA-032 / 2025-11-12** | Erica → Jennifer | Erica skriver efter mötet att huvudvärk/luft inte hann behandlas och föreslår rengöring i kanal. | A1/C | Samtida bevis för att luft-/symptomfrågan enligt henne stod kvar efter mötet. | Teknisk riktighet eller att kanalrensning var rätt åtgärd. | Koppla till vad mötet faktiskt behandlade via ljud. | Kunskaps-/reklamationskedja. | **GRÖN som partsuppgift.** |
| **SA-033 / 2025-12-17** | Ljud från möte | Projektets transkription innehåller uppgifter om kanalrensning/fem meter och andra ventilationsuttalanden. | D | Kan bli central för vad FB faktiskt sade om utförd åtgärd och dess begränsning. | Exakt citat eller teknisk omfattning innan originalkontroll. | Original ljud + talare + tidskod. | Bevisvärdering; PBL/MB/JB scope. | **RÖD tills ljudsource-lock.** |
| **SA-034 / 2026-03-11** | MF-inspektion / ventilationsmätning | Mätningar redovisar ca 43 l/s med stängt fönster, ca 73 l/s med öppet fönster och ca 8 Pa undertryck; inspektionen innehåller okulär bedömning och ventilationskontroller. | A1 | Direkt tekniskt/myndighetsbevis för förhållandena vid just inspektionstillfället och det som faktiskt mättes. | VOC, brandrestprodukter, dold kontaminering, generell luftkvalitet, långtidsfunktion eller orsaken till återkommande symptom om dessa inte undersöktes. | Full metod, instrument, kalibrering, rådata, mätpunkter, uppdrag/scope. | MB 9:3; 26:21–22; FL 23; scope-princip. | **GRÖN för mätvärden inom scope / GUL för bredare slutsatser. Spår 1/4.** |
| **SA-035 / 2026-03-11** | MF/FB åtgärd i lägenheter över/under | Blockeringar/ventilationsförhållanden i angränsande lägenheter åtgärdas enligt tillsynsmaterialet. | A1/A2 | Systemrelevant omständighet; visar att ventilationsförhållanden inte endast bedömdes isolerat i 1202. | Att alla senare problem i 1202 avhjälptes. | Exakt åtgärd, systemkoppling, före/efter. | PBL/MB teknisk bevisning. | **GUL.** |
| **SA-036 / OVK 2018/2022** | OVK-protokoll | 2018 godkänt; 2022 först ej godkänt och senare godkänt efter ombesiktning enligt projektets original-/myndighetsmaterial. | A1/A2 | Relevant historisk kontroll av ventilationssystemet. | Att varje lägenhet eller varje senare specifik funktionsfråga kontrollerades; att dagens funktion är bevisad. | Objekt 0562/system 01, bilagor, mätblad, vilka lägenheter/mätpunkter som faktiskt ingick. | PBL 8:25/PBF 5 kap.; scope-princip. | **GUL. Spår 2.** |
| **SA-037 / 2026-08-20** | SBK/OVK-besked | SBK uppger att det inte finns lagkrav att varje lägenhet redovisas separat i OVK-protokollet och att vissa äldre handlingar inte finns registrerade hos kontoret. | A1 | Avgränsar vad frånvaro ur protokollet kan respektive inte kan användas till. | Att lägenheten faktiskt kontrollerades eller inte kontrollerades; att ventilationen fungerar idag. | Original OVK-bilagor/mätblad och systemspecifik spårning. | PBL/OVK. | **GRÖN för administrativt besked; konkret scope fortfarande GUL.** |
| **SA-038 / 2026-08-25** | Erica → SBK/Sheida/Jenny | Erica ställer fem konkreta frågor om vilka tekniska undersökningar som utförts efter branden, vilka handlingar som styrker dem och på vilket underlag SBK kan bedöma PBL-relevanta krav i objektet. | A1/C | Fixerar det konkreta PBL-bevistema och kräver frågespecificerat underlag. | Att PBL-överträdelse redan är bevisad eller att SBK måste utföra just vissa specificerade tester. | SBK:s punktvisa svar + underlag. | 11 kap. 5 § PBL; 8:14; 8:4; scope/utredning. | **GRÖN för kommunicerad fråga. Spår 2.** |

## D. SYMPTOM / FLERA PERSONER / VITTNESKEDJA

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-040 / okt 2025 → 2026** | Ericas samtidiga mejl/anteckningar | Återkommande rapporter om symptom vid vistelse. | C/A1 när originalmejl | Visar konsekvent partsuppgift och tidsmönster; relevant indikator för tillsyn och nyttjandepåverkan. | Medicinsk diagnos, teknisk orsak eller specifik emission. | Symtomlogg kopplad till originalmejl. | 9:3 MB; 12:9/16 JB; bevisvärdering. | **GUL som indikator, inte orsaksbevis. Spår 1/3.** |
| **SA-041 / nov 2025 → 2026** | Namngivna personer/vittnen | Flera personer uppges ha reagerat vid vistelse i lägenheten. | B/C tills individuellt source-lock | Kan motverka teorin att problemet endast är en ensam subjektiv upplevelse och stärka behovet av fortsatt utredning. | Att en viss miljöfaktor finns; att alla reaktioner har samma orsak; medicinsk kausalitet. | Ett förstahandsintyg per person: datum, vistelsetid, observation, symtom, förhandsinformation. | MB risk-/utredningsspår; JB nyttjandepåverkan; fri bevisvärdering. | **ORANGE tills individuellt source-lock.** |
| **SA-042 / särskild astmareaktion** | Vittnes-/partsuppgift | En person med astma uppges reagera mycket snabbt och lämna bostaden. | B/C | Kan stärka återkommande reaktionsmönster och särskilt känslig grupp som faktisk observation. | Att lägenheten objektivt är astmaframkallande eller att orsaken är viss luftförorening. | Direkt förstahandsintyg + exakt datum/tid. | 9:3 MB; MÖD 2017:51 juridiskt riskstöd, inte kausalitetsbevis. | **GUL/ORANGE.** |
| **SA-043 / 2026-07-10** | Marko/husvärd, ljud | Uppgift finns att han känt ”någon form av doft”/att ”det är någonting”. | D/A2 | Potentiellt viktigt oberoende motpartsbevis för att någon FB-företrädare också noterade något. | Vad lukten var, om den var skadlig, orsaken eller kontinuitet. | Original ljud med tidskod och talare. | Bevisvärdering; 9:3 MB; 12:16 JB. | **RÖD för exakt citat tills originalkontroll.** |

## E. FAMILJEBOSTÄDERS KUNSKAP / ÅTGÄRDER / AVHJÄLPANDE

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-050 / 2025-11-06–10** | Gaby/Jennifer originalmejl | FB får skriftligt tydlig information om att frågan gäller inomhusmiljö/hälsobesvär och Gaby anger att problemet ska felsökas. | A1 | Kunskaps-/reklamationspunkt och start för att kontrollera vad FB faktiskt gjorde efteråt. | Att FB accepterade en viss teknisk orsak. | Arbetsorder/felsökningsplan/resultat. | 12:15/16 JB; MB fastighetsägarspår. | **GRÖN. Spår 1/3.** |
| **SA-051 / nov–dec 2025** | Städningar, målning, golvbyte, elåtgärd | Flera faktiska åtgärder görs/erbjuds. | A1/A2 | Visar att FB agerat och är centralt för frågan om påstått avhjälpande. | Att orsaken identifierades eller att problemet var slutligt avhjälpt. | Varje åtgärd: beställning, syfte, omfattning, resultat, efterkontroll. | RH 2016:17 analog bevisdynamik; 12:15/16 JB. | **GUL tills åtgärd→effekt-matris. Spår 3.** |
| **SA-052 / 2026-06-23** | Peter, ljudspår | Projektmaterialet innehåller uttalanden i stil med ”vi har gjort det vi kan” och att ingen tagit reda på orsaken. | D/A2 | Kan vara starkt stöd för att orsaksfrågan då fortfarande var öppen, om originalet bekräftar exakt innebörd. | Teknisk orsak; rättsligt ansvar; att ingen undersökning alls gjorts. | Original ljud + tidskod + hela kontexten. | Bevisvärdering. | **RÖD tills ljud source-lock.** |
| **SA-053 / 2026-08-17** | Jennifer Ehlin native mejl | Jennifer skriver att inomhusmiljön är konstaterad fullgod och nämner eventuell allergi-/astmaanpassad bostad. | A1 | Visar FB:s senare position och alternativ förklaringsram. Relevant för att kontrollera vilket underlag som bär slutsatsen ”fullgod”. | Att känslighet är orsaken; att lägenheten är objektivt olämplig för astmatiker; föravtalskunskap. | Underlaget bakom slutsatsen ”fullgod”. | Bevisvärdering; 12:16 JB; Spår 1/4 via underlaget. | **GRÖN faktisk post / GUL juridisk funktion.** |

## F. MILJÖFÖRVALTNINGEN – TILLSYN / BESLUT / PROCESS

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-060 / 2026-03-11** | MF inspektionsrapport | Okulär bedömning och ventilationskontroller utförs; inga konstaterade relevanta brister/lukt vid tillfället enligt rapportens scope. | A1 | Centralt myndighetsunderlag. Måste användas både positivt och negativt. | Att alla möjliga inomhusmiljöorsaker utretts eller uteslutits; att rapporten besvarar frågor utanför sitt uppdrag. | Full akt: uppdrag, metod, rådata, anteckningar, kommunikation med FB före beslut. | 9:3 MB; 26 kap.; FL 23/27/32. | **GRÖN inom scope / GUL för bred slutsats. Spår 1/4.** |
| **SA-061 / 2026-04-13** | MF beslut | MF avslutar tillsynsärendet. | A1 | Processuell slutpunkt i första instans; avgörande för vad som måste ha varit tillräckligt utrett och motiverat då. | Att alla senare uppgifter var kända; att civilrättslig brukbarhet avgjordes; att alla möjliga orsaker uteslöts. | Full akt per 13 april och exakt motivering/bevisvärdering. | FL 23/25/27/32; MB. | **GRÖN för beslutets existens/utgång. Spår 1/4.** |
| **SA-062 / efter 13 apr 2026** | Nya vittnes-/FB-/tekniska uppgifter | Ytterligare material tillkommer efter MF:s beslut, bl.a. senare förstahandsuppgifter och brandunderlag. | A1/B beroende post | Måste hållas tidsmässigt isär från frågan om MF:s ursprungliga beslut var korrekt på dåvarande akt; samtidigt relevant i överklagande/ny tillsyn beroende processram. | Att MF kände till materialet den 13 april. | Varje ny post: datum, när mottagen av MF/Lst/MMD, om kommunicerad. | FL/överprövning; instansordning; MMD-process. | **GUL – kräver processkarta per post. Spår 4.** |
| **SA-063 / 2026-08-10** | Tora Joby/MF | MF använder formuleringen ”samma sakfråga” i samband med pågående domstolsprocess. | A1 | Viktig för att precisera hur MF avgränsar sin fortsatta handläggning och om frågor om beslutsunderlag/nya omständigheter faktiskt besvaras. | Att MF rättsligt är förhindrad att redovisa hur tidigare beslut togs fram eller registrera nytt material. | Exakt full mejltråd + senare svar från enhetschef. | FL 23/27/32; processuell avgränsning. | **GRÖN faktisk post / juridisk innebörd GUL.** |
| **SA-064 / 2026-08-17–18** | Erica → MF/enhetschef Miriam | Fyra konkreta frågor ställs om beslutsunderlaget före 13 april, värderingen av uppgifter, nya omständigheter och tillgänglighet för MMD. | A1/C | Fixerar process-/utredningsbevistema och vad myndigheten ombetts redovisa. | Att handläggningsfel redan är bevisat. | Myndighetens svar + aktjämförelse. | FL 23/25/27/32. | **GRÖN för kommunicerade frågor. Spår 4.** |

## G. STADSBYGGNADSKONTORET – PBL / OVK / BYGGNADSTILLSYN

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-070 / aug 2026** | SBK ärende 2026-06369 | SBK uppger att handläggning påbörjats, att stor mängd information lämnats och att endast vissa delar omfattas av PBL-tillsyn. | A1 | Visar att PBL-spåret är aktivt och avgränsat. | Att SBK accepterat någon konkret överträdelse. | Slutlig sakavgränsning och utredningsåtgärder. | 11 kap. 5 § PBL. | **GRÖN. Spår 2.** |
| **SA-071 / aug 2026** | SBK/Sheida | SBK anger att det inte finns lagkrav att varje lägenhet redovisas i OVK-protokoll. | A1 | Viktig motspärr mot felaktigt argument ”saknas i protokoll = inte kontrollerad”. | Att 1202 faktiskt mättes eller att all relevant funktion kontrollerats. | Mätblad/bilagor/systemkoppling. | PBL/PBF OVK. | **GRÖN uppgift; konkret scope GUL.** |
| **SA-072 / 2026-08-25** | Erica → Sheida/Jenny | Frågan flyttas uttryckligen från ”är OVK godkänd?” till ”vad har faktiskt kontrollerats i denna lägenhet och vilket underlag visar teknisk funktion?”. | A1/C | Preciserar NIVÅ A-bevistema under 11:5 och scope-frågan. | Att 11:5-tröskeln definitivt är passerad i sak eller att ett visst föreläggande ska meddelas. | SBK:s sakliga svar och handlingar. | 11:5 PBL; 8:14; 8:4; tidigare godkännandens scope. | **GRÖN som kommunicerad tillsynsfråga. Spår 2.** |

## H. HYRESRÄTT / BRUKBARHET / PÅSTÅTT AVHJÄLPANDE

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-080 / från 2025-10-01** | Hyresavtal + faktisk nyttjandekedja | Bostaden upplåts för boende och tillträde sker. | A1 | Grund för fullt brukbar enligt 12:9 JB vid tillträdet och 12:15 under hyrestiden. | Att brist fanns. | Konkret bristbevis. | 12:9 och 12:15 JB. | **GRÖN rättslig startpunkt.** |
| **SA-081 / 2025-10 → 2026** | Bilder, mejl, vittnen, tekniska kontroller | Ett antal konkreta skick-/inomhusmiljö-/ventilationsfrågor dokumenteras över tid. | Blandad | Bygger tesen om faktisk brist/nyttjandepåverkan, men varje del måste bevisas för sig. | Att alla observationer har gemensam orsak eller når juridisk tröskel. | Bristmatris per fenomen. | 12:9/15/16 JB; RH 2022:26; ÖH 11917-18. | **GUL. Spår 3.** |
| **SA-082 / åtgärder 2025–26** | FB arbetsorder/kommunikation | Städning, målning, golvbyte, ventilationsåtgärder m.m. utförs eller erbjuds. | A1/A2 | Relevant för värdens invändning att brister avhjälpts. | Att varje relevant problem faktiskt upphört. | Före/efter-resultat och objektiv effektkontroll. | RH 2016:17; 12:15/16 JB. | **GUL – avhjälpandematriser krävs.** |
| **SA-083 / MF avslut** | MF beslut | Miljötillsyn avslutas. | A1 | Relevant bevisning men civilrättslig verkan måste avgränsas. | Att lägenheten automatiskt är fullt brukbar enligt 12 kap. JB. | Jämför konkret brist mot vad MF faktiskt prövade. | NJA 2016 s.303; ÖH 11917-18; scope-princip. | **GRÖN som myndighetsfaktum / GUL civilrättslig effekt.** |

## I. SPÅR 5 – FÖRAVTALSINFORMATION / FÖRTIGANDE / AVTALSBETYDELSE

| ID / datum | Källa | Faktisk uppgift | Bevisklass | Juridisk funktion | Vad den INTE bevisar | Saknad komplettering | Relevant lag/princip | Status / spår |
|---|---|---|---|---|---|---|---|---|
| **SA-090 / före 2025-08-12** | Erbjudande, besiktningsprotokoll, avtalsbilagor | Den information som faktiskt lämnades före signering kan source-lockas i avtalsmaterialet. | A1 | Definierar representations-/informationssidan i 30/33 §-analysen. | Vad FB internt visste men inte kommunicerade. | Samlad prekontraktuell akt. | 30 och 33 §§ AvtL. | **GRÖN/GUL beroende full kedja. Spår 5.** |
| **SA-091 / före 2025-08-12** | FB:s interna historik | Relevant organisatorisk kunskap om brand/återställning före signering är ännu inte source-lockad. | F/E tills original | Avgörande rekvisitbevis för möjlig 30/33 §-tillämpning. | Får inte fyllas med senare uttalanden. | Intern objektsakt, skadeakt, arbetsorder, historiskt system, ansvarig uthyrnings-/förvaltningsfunktion. | AvtL 30/33; juridisk persons kunskap. | **RÖD/ORANGE – HUVUDLUCKA SPÅR 5.** |
| **SA-092 / 2026-03-26** | Erica → Hyresgästföreningen | Erica skriver att hon aldrig hade tackat ja om hon vetat det hon vet senare. | A1/C | Samtida, återkommande partsuppgift om informationens betydelse för avtalsbeslutet. | Sviklighet, FB:s kunskap eller objektiv väsentlighet ensam. | Samma linje i ytterligare native mejl; eventuell samtida föravtalskommunikation. | 30 § 2 st AvtL – betydelse/inverkan. | **GRÖN som partsuppgift / GUL juridiskt rekvisit.** |
| **SA-093 / 2026-05-11** | Erica → HGF | Samma kärnposition upprepas: hon hade inte accepterat lägenheten med den senare kända informationen. | A1/A2 | Stärker konsistensen i partsuppgiften om avtalsbetydelse. | Svek/kunskap. | Top-body-source-lock om ej redan gjort. | AvtL 30. | **GUL/GRÖN beroende top-body.** |
| **SA-094 / 2026-05-26** | Erica → HGF juridiska enhet | Samma kärnposition upprepas igen. | A1/A2 | Ytterligare stöd för konsekvent kausalitets-/betydelseuppgift. | FB:s sviklighet. | Native topptext. | AvtL 30. | **GUL/GRÖN.** |
| **SA-095 / senare 2025–26** | Jennifer/Gaby/brandakt | Senare FB-uttalanden visar motstridigt/oklart dokumentations- och kunskapsläge om brandhistoriken. | A1 | Kan användas för att rikta bevisinhämtning bakåt mot prekontraktuell kunskap. | Får INTE automatiskt backdatera kunskap till 12 aug 2025. | Prekontraktuell intern akt. | AvtL 30/33; bevisvärdering. | **GUL stödbevis / RÖD för slutsatsen ”svek visat”.** |

---

# 4. TRANSKRIPTION/SAMMANSTÄLLNING – OBLIGATORISK RETUR TILL ORIGINAL

| Post | Nuvarande form | Original som krävs | Prioritet |
|---|---|---|---|
| 11 nov 2025 – exakt mötesdialog om kanalrensning/brand/luft | transkription/sammanställning | original m4a + tidskoder | **HÖG** |
| 17 dec 2025 – frågor som inte togs upp | sammanställning + ljud | original m4a + frågelistan från 12 dec | **MYCKET HÖG** |
| 17 dec 2025 – ”fem meter” kanalrensning | transkription | original ljud + talare + teknisk kontext | **MYCKET HÖG** |
| 23 juni 2026 – Peter ”vi har gjort det vi kan / ingen har tagit reda på” | transkription/sammanställning | original ljud + tidskod | **HÖG** |
| 10 juli 2026 – Marko ”någon form av doft...” | transkription/sammanställning | original ljud + tidskod | **HÖG** |
| Individuella vittnesreaktioner | sammanställning | ett förstahandsintyg/ljud/mejl per person | **MYCKET HÖG** |
| Exakt kanalrensningsomfattning 4 nov | driftanteckning + senare uppgifter | arbetsorder/utföranderapport | **MYCKET HÖG** |
| Full prekontraktuell FB-kunskap före 12 aug 2025 | arbetsmodell | intern objekts-/skade-/systemakt | **KRITISK SPÅR 5** |

---

# 5. JURIDISK KORSKOPPLING

| Bevistema | Spår 1 MB | Spår 2 PBL | Spår 3 JB | Spår 4 FL/process | Spår 5 AvtL |
|---|---|---|---|---|---|
| Återkommande symptom/flera personer | indikator/risk/utredningsbehov | endast om kopplat till PBL-relevant teknisk egenskap | nyttjandepåverkan, men konkret brist måste visas | relevant om uppgifterna låg i akten | inte för föravtalskunskap |
| Ventilationsmätningar | direkt tekniskt stöd inom scope | direkt om rätt regel/systemkoppling | relevant bevisning om faktisk brist | scope/utredningsunderlag | normalt sekundärt |
| Godkänd OVK | relevant men ej dispositiv | central PBL-bevisning | relevant men ej automatiskt avgörande | underlagets scope | normalt ej kärna |
| Brand 2017 | historisk möjlig riskfaktor, ej kausalitet | relevant endast vid konkret teknisk anknytning | historik endast om kopplad till skick/brist | relevant om myndigheten hade uppgiften | central möjlig föravtalsomständighet men kunskap/sviklighet måste visas |
| Saknad saneringsdokumentation | öppnar utredningsfråga | endast om dokumentations-/funktionsanknytning | säger inte i sig att brist finns | relevant för vilken slutsats myndigheten kan dra | säger inte i sig svek; kan rikta kunskapsutredning |
| MF:s 11 mars-rapport | direkt | endast analogt/indirekt | relevant bevisning | central aktpost | inte för föravtalskunskap |
| FB:s senare uttalanden | verksamhets-/adressatbevis | eventuell teknisk kunskap | avhjälpande/kunskap | partsuppgift i myndighetsakt | kan vara lead bakåt, får inte backdateras automatiskt |

---

# 6. STOPP-REGLER

1. **”Branden 2017 orsakar dagens hälsobesvär.”** – STOPP.
2. **”Ingen saneringsrapport betyder att sanering aldrig skedde.”** – STOPP.
3. **”Åtta personer bevisar att lägenheten innehåller en viss förorening.”** – STOPP.
4. **”Godkänd OVK bevisar att lägenheten fungerar idag.”** – STOPP som generell slutsats.
5. **”Godkänd OVK betyder ingenting.”** – STOPP.
6. **”MF:s inspektion uteslöt alla möjliga orsaker.”** – STOPP om scopet inte omfattade dem.
7. **”Familjebostäder visste före avtalet om en kvarvarande farlig brandskada.”** – STOPP tills prekontraktuell kunskap source-lockats.
8. **”Familjebostäder begick svek/bedrägeri.”** – STOPP.
9. **”Hyresavtalet är ogiltigt.”** – STOPP.
10. **”Lägenheten är juridiskt obeboelig bara eftersom personer fått symptom.”** – STOPP; konkret brist måste analyseras.

---

# 7. GRÖNA TESER SOM KAN BYGGAS

1. Branden den 16 november 2017 är en verifierad historisk omständighet.
2. SSBF:s material visar inte hur den efterföljande återställnings-/saneringskedjan genomfördes.
3. Avsaknad av handling hos en viss aktör bevisar endast avsaknad i den aktörens system/scope.
4. Familjebostäder fick senast i november 2025 tydlig information om återkommande inomhusmiljö-/ventilationsproblem och beskrev själva fortsatt felsökning som nödvändig.
5. MF:s kontroll den 11 mars 2026 måste läsas enligt det den faktiskt undersökte; dess bevisvärde kan inte utan stöd utsträckas till helt andra tekniska frågor.
6. En tidigare kontroll kan vara korrekt för sin fråga och tidpunkt utan att automatiskt besvara en annan senare fråga.
7. I hyresrätten måste den konkreta bristen visas; exakt teknisk orsak är inte i varje fall samma bevistema som bristens existens.
8. I Spår 5 är föravtalskunskap och sviklighet fortfarande öppna bevisfrågor; senare uttalanden får inte backdateras.

---

# 8. KRITISKA KOMPLETTERINGAR

**Prioritet 1 – original som redan finns:** ljud 11 nov, ljud 17 dec, ljud 23 juni, ljud 10 juli, kanalrensning 4 nov arbetsorder/rapport, individuella vittnesposter.

**Prioritet 2 – myndighetsakten:** MF:s kompletta akt före 13 april 2026; vad MF frågade FB efter 11 mars; vad FB svarade; vilka bilagor/tekniska dokument som fanns före beslutet; metod/scope/rådata; nytt material efter beslutet med exakt mottagningsdatum.

**Prioritet 3 – Spår 5:** full prekontraktuell akt före 12 augusti 2025; FB:s interna objekts-/skade-/underhållssystem; vilken funktion som hade kunskap om brand/återställning; vad den funktionen visste; besiktningsprotokoll kontra verifierat skick vid tillträde.

---

# 9. SPÅRSTATUS

| Spår | Rättsligt lager | Bevisläge | Största kvarvarande bevisfråga | Status |
|---|---|---|---|---|
| **Spår 1 – MB/inomhusmiljö** | juridiskt starkt/source-lockat | flera centrala fakta finns, men MF-akt/scope måste fullbindas | exakt beslutsunderlag och scope före 13 april | **GUL – LÅST MED RESERVATION** |
| **Spår 2 – PBL** | huvudmodell färdigbyggd | systemspecifik teknisk koppling/OVK-scope delvis öppen | objekt 0562/system 01 + konkret teknisk PBL-fråga | **GUL – LÅST MED RESERVATION** |
| **Spår 3 – hyresrätt** | rättsregel/praxis GO | konkret brist måste byggas fenomen för fenomen | faktisk civilrättsligt relevant brist + effekt efter åtgärder | **GUL – LÅST MED RESERVATION** |
| **Spår 4 – myndighetsprocess** | starkt GO | akten måste jämföras mot vad myndigheten faktiskt utredde/motiverade | full akt före beslut + nytt material kronologiskt | **GUL – LÅST MED RESERVATION** |
| **Spår 5 – AvtL/förtigande** | 30/33 §§ + kärnpraxis låsta | föravtalskunskap/sviklighet inte visade | FB:s kunskap före 12 aug 2025 | **ORANGE – EJ LÅST** |

---

# 10. ARBETSREGEL FÖR VARJE NY POST

Varje ny bevispost ska få: unikt SA-ID; datum/tid; originalkälla/filnamn; exakt faktisk uppgift utan tolkning; bevisklass A1–F; rekvisit/bevistema; vad posten inte bevisar; saknad komplettering; relevant lag/princip/praxis; spår/tidslinje; extern gate GO/RESERVATION/STOPP.

Ingen ny uppgift ska längre läggas direkt i en berättande tidslinje utan att först passera denna kontroll.

---

# 11. KONTROLLFRÅGAN ÖVER HELA PROJEKTET

> **KAN JAG VISA KÄLLAN?**  
> **KAN JAG VISA RÄTTSREGELN?**  
> **KAN JAG VISA REKVISITET OCH BEVISTEMAT?**  
> **KAN JAG FÖRKLARA TILLÄMPNINGEN?**  
> **KAN JAG BEMÖTA DEN STARKASTE INVÄNDNINGEN?**  
> **KAN JAG FÖRSVARA SLUTSATSEN NÄR DEN IFRÅGASÄTTS?**

För tekniska rapporter:

> **EN RAPPORT KAN INTE BESVARA EN FRÅGA DEN ALDRIG HAR UNDERSÖKT.**

Detta är en bevis-/scope-princip, inte en självständig lagregel. Den ska juridiskt uttryckas som en fråga om **vilken konkret sakfråga rapporten skulle besvara, vilket uppdrag/metod/scope den hade och vad resultatet därför faktiskt kan bära**.

---

# 12. SLUTSTATUS

**STORA AUDITEN ÄR ETT EGET STYRANDE HUVUDLAGER.**

Nästa arbete är inte bred research. Nästa arbete är source-lock och rad-för-rad-koppling mellan originalbevis och denna kontrollpanel.
