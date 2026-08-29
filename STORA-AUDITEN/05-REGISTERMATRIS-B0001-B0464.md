# STORA AUDITEN – REGISTERMATRIS B0001–B0464

**Status:** FULL BASAUDIT – 464/464 registrerade Bevis-ID har egen kvalitetsrad.

Detta lager kompletterar `02-BEVISPOSTER-MASTER.md`. Masterfilen innehåller postspecifika fullauditeringar av kritiska beviskedjor. Registermatrisen säkerställer att **ingen av B0001–B0464 saknar grundklassning/originalspärr** medan fördjupningen pågår.

## Segment

- [`../audit/AUDIT-MATRIS-B0001-B0100.md`](../audit/AUDIT-MATRIS-B0001-B0100.md)
- [`../audit/AUDIT-MATRIS-B0101-B0200.md`](../audit/AUDIT-MATRIS-B0101-B0200.md)
- [`../audit/AUDIT-MATRIS-B0201-B0300.md`](../audit/AUDIT-MATRIS-B0201-B0300.md)
- [`../audit/AUDIT-MATRIS-B0301-B0400.md`](../audit/AUDIT-MATRIS-B0301-B0400.md)
- [`../audit/AUDIT-MATRIS-B0401-B0464.md`](../audit/AUDIT-MATRIS-B0401-B0464.md)

## Join-regel

Varje post ska läsas som:

`Bevis-ID → BEVISREGISTER (datum/källa/faktisk uppgift) → auditmatris (klass/originalspärr/begränsning/komplettering) → 02-BEVISPOSTER-MASTER (postspecifik juridisk fördjupning när materiellt relevant) → TIDSLINJE/spår`

Detta är avsiktligt en relationsmodell. Datum, avsändare och direkt uppgift ska ha **en** kanonisk version i `BEVISREGISTER.md`. Auditlagret ska inte skapa konkurrerande kopior av samma källmetadata.

## Extern-regel

En grundklassad registerrad är **inte automatiskt EXTERN-READY**. För kritiska citat, tekniska slutsatser och kausalitet krävs postspecifik kontroll enligt `README.md` och `03-ORIGINALKONTROLL-OCH-KOMPLETTERINGSKO.md`.
