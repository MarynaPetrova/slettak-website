# TakNova

Statisk nettsted med norsk, engelsk og ukrainsk innhold i HTML. Alle publiserte filer ligger i `public/`. README.md og SKILL.md skal ikke publiseres.

## Publisering

Adresse: https://taknova.com. En server henter `main` hvert 5. minutt og publiserer `public/`, så en endring i `main` er ute på nettstedet etter noen minutter. Interne lenker begynner med `/` (for eksempel `/en`, `/personvern?lang=en`), og fullstendige adresser med `https://taknova.com`.

Språksidene kan åpnes med `/en` og `/uk`. De tidligere `.html`-adressene beholdes.

GitHub Pages (https://marynapetrova.github.io/slettak-website/) sender nå bare besøkende videre til samme side på taknova.com (`.github/workflows/pages.yml`).

## Kontaktskjema og ressurser

Kontaktskjemaet bruker FormSubmit. Behold språkparameteren i bekreftelseslenken. Løsningsbildene er inspirasjonsbilder. DM Sans lagres lokalt med SIL Open Font License i `public/fonts/OFL.txt`. Bildet i «Om oss» (`about.jpg`) er fra Unsplash og lagres lokalt.
