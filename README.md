# TakNova

Statisk nettsted med norsk, engelsk og ukrainsk innhold i HTML. Alle publiserte filer ligger i `public/`. README.md og SKILL.md skal ikke publiseres.

## GitHub Pages

Nåværende adresse: https://marynapetrova.github.io/slettak-website/

Velg Settings → Pages → Build and deployment → Source → GitHub Actions. Arbeidsflyten `.github/workflows/pages.yml` publiserer bare `public/` fra `main`.

Språksidene kan åpnes med `/en` og `/uk`. GitHub Pages legger til avsluttende skråstrek for mapper. De tidligere `.html`-adressene beholdes.

## Cloudflare Pages

- Production branch: `main`
- Framework preset: None
- Build command: la feltet stå tomt
- Build output directory: `public`

Før flytting: erstatt `https://marynapetrova.github.io/slettak-website` med den nye HTTPS-adressen i canonical, hreflang, Open Graph, JSON-LD, `_next`, robots.txt og sitemap.xml. Bytt også `/slettak-website/` i interne lenker til `/`. Gjør endringen i både `.html`-sidene og `index.html`-filene i rutemappene. Kjør språk-, lenke- og skjematestene på den nye adressen.

## Kontaktskjema og ressurser

Kontaktskjemaet bruker FormSubmit. Behold språkparameteren i bekreftelseslenken. Løsningsbildene er inspirasjonsbilder. DM Sans lagres lokalt med SIL Open Font License i `public/fonts/OFL.txt`. Bildet i «Om oss» lastes fortsatt fra Unsplash.
