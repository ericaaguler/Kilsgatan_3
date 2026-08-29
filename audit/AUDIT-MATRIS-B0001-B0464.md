# AUDIT-MATRIS B0001–B0464 – INDEX

Detta är indexet som `../STORA_AUDITEN.md` pekar på. **Samtliga 464 registrerade Bevis-ID har en egen auditrad** i följande fem segment:

- [B0001–B0100](AUDIT-MATRIS-B0001-B0100.md)
- [B0101–B0200](AUDIT-MATRIS-B0101-B0200.md)
- [B0201–B0300](AUDIT-MATRIS-B0201-B0300.md)
- [B0301–B0400](AUDIT-MATRIS-B0301-B0400.md)
- [B0401–B0464](AUDIT-MATRIS-B0401-B0464.md)

## Datamodell

Varje rad ska läsas som en join mellan:

1. **`BEVISREGISTER.md`** – kanoniskt datum, källa och vad posten direkt visar.
2. **Auditmatrisen** – bevisklass, originalstatus, juridisk funktion, begränsning, saknad komplettering, rättsprincip och status i tidslinje/spår.
3. **`STORA_AUDITEN.md`** – postspecifik fördjupning för de bevis som bär materiell tyngd i ärendet.
4. **`OREGISTRERADE-BEVIS-OCH-ORIGINALKARANTAN.md`** – viktiga bilder/video/ljud/sökspår som ännu inte har fått B-ID eller inte är originalkontrollerade.

Det är avsiktligt att datum/källa/faktisk uppgift inte kopieras ordagrant till varje auditfil: de har en enda auktoritativ version i bevisregistret. Bevis-ID är relationsnyckeln. På så sätt kan en korrigerad källuppgift inte lämna en gammal, motsägande kopia kvar i auditlagret.
