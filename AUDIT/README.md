# AUDIT – projektets översta kontrollnivå

Detta lager ligger **över** huvudtidslinjen och mikrotidslinjerna.

## Hierarki

1. **`AUDIT/STORA-AUDITEN-KONTROLLPANEL.md`** – projektets huvudkontrollpanel. Varje bevispost ska ha datum, källa, faktisk uppgift, bevisklass, juridisk funktion, vad posten inte bevisar, saknad komplettering, relevant lag/princip, status i tidslinjer/spår och source-lock-status.
2. **`AUDIT/FYR-PDF-LAGUTNYTTJANDE-2026-08-29.md`** – juridiskt underlager. Prövar vilka argument de fyra juridiska PDF:erna faktiskt stödjer, om regeln är direkt tillämplig, vad som måste kontrolleras mot aktuell rätt och vilket ytterligare bevis som krävs. Detta lager får aldrig ersätta beviskontrollen i STORA AUDITEN.
3. **`TIDSLINJE.md`** – kronologin för hela ärendet.
4. **`analyser/MIKROTIDSLINJER-INDEX.md` + mikrotidslinjer** – isolerar motsägelser, dokumentationsluckor och kontrollfrågor.
5. **`bevis/`, `korrespondens/`, `transkriptioner/`, originalhandlingar** – källagret.

## Arbetsregel

Ingen uppgift ska behandlas som externt verifierad bara för att den finns i en tidslinje eller analys. **STORA AUDITEN är kontrollpunkten.** Om auditstatus säger att originalkontroll krävs ska originalfilen öppnas och source-lockas innan uppgiften används som faktapåstående eller ordagrant citat.

Juridisk användning följer därefter denna kedja:

**originalkälla → STORA AUDITEN → source-lock → bevisvärde/begränsning → juridisk funktion → fyr-PDF/lagutnyttjandekontroll → aktuell rätt → extern användning.**

En juridisk bok är aldrig primärrätt. Lagtext, aktuell praxis och specialregler ska kontrolleras innan ett bokargument används externt.

## Styrissue

GitHub issue **#14 – STORA AUDITEN – kontrollpanel för hela projektet** används för auditens öppna kontrollfrågor, source-lock-arbete och juridiska verifieringskö.
