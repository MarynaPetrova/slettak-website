#!/usr/bin/env python3
"""Bygger seksjonen «Råd og tips» (/rad/): hub + artikler.

Kjør fra repo-roten:  python3 tools/build_rad.py
Header og footer hentes fra public/hva-er-strekktak/index.html, slik at
alle sider har samme meny og stil. Nye artikler legges til i ARTICLES
(innholdet ligger i tools/rad_articles.py).
"""
import html, json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rad_articles import ARTICLES, CATEGORIES, GUIDES

ROOT = os.path.join(os.path.dirname(__file__), '..', 'public')
SITE = 'https://taknova.com'
import datetime
TODAY = datetime.date.today().isoformat()

src = open(os.path.join(ROOT, 'hva-er-strekktak', 'index.html'), encoding='utf-8').read()
HEADER = src[src.index('<header class="top">'):src.index('</header>') + 9]
FOOTER = src[src.index('<footer class="site-footer">'):src.index('</footer>') + 9]
GC = '<script data-goatcounter="https://taknova.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'
SCRIPT = re.search(r'<script src="/script\.js[^"]*"></script>', src).group(0)
CSS = ('<link rel="stylesheet" href="/style.css?v=r3"><link rel="stylesheet" href="/footer-video.css?v=5">'
       '<link rel="stylesheet" href="/rad.css?v=1">')
ORG = {"@type": "Organization", "name": "TakNova", "url": SITE + "/",
       "logo": SITE + "/favicon-512.png"}
e = html.escape


def head(title, desc, url, image, ld, og_type='article'):
    ld_html = ''.join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in ld)
    return ('<!doctype html><html lang="nb"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><meta name="description" content="{e(desc)}">'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<link rel="canonical" href="{url}"><meta property="og:title" content="{e(title)}">'
            f'<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{SITE}{image}"><meta property="og:locale" content="nb_NO">'
            f'<meta property="og:type" content="{og_type}"><meta name="twitter:card" content="summary_large_image">'
            f'{CSS}{ld_html}{GC}</head><body>{HEADER}')


def crumbs(items):
    """items: [(navn, url|None)]"""
    parts = []
    for name, url in items:
        parts.append(f'<a href="{url}">{e(name)}</a>' if url else f'<span aria-current="page">{e(name)}</span>')
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + u} if u else {})}
        for i, (n, u) in enumerate(items)]}
    return '<nav class="crumbs" aria-label="Brødsmuler">' + ' <span aria-hidden="true">›</span> '.join(parts) + '</nav>', ld


def all_cards():
    """Artikler + eldre veiledninger som kort, i én liste."""
    out = []
    for a in ARTICLES:
        out.append(dict(url=f'/rad/{a["slug"]}/', title=a['card'], desc=a['teaser'], img=a['image'], cat=a['cat'], new=True))
    for g in GUIDES:
        out.append(dict(g, new=False))
    return out


def card(c):
    cat = CATEGORIES[c['cat']]
    return (f'<a class="rcard" href="{c["url"]}"><img src="{c["img"]}" alt="" loading="lazy" width="480" height="320">'
            f'<span class="rcat">{e(cat)}</span><strong>{e(c["title"])}</strong><span class="rdesc">{e(c["desc"])}</span></a>')


def cta_box(a):
    subj = f'Forespørsel fra artikkel: {a["card"]} | taknova'
    return f'''<aside class="rcta" id="befaring"><h2>Lurer du på hva som passer hos deg?</h2>
<p>Vi kommer på gratis befaring i Oslo og Akershus, ser på taket, måler opp og gir et fast pristilbud. Det er helt uforpliktende.</p>
<form class="rform" action="https://formsubmit.co/taknova.norge@gmail.com" method="POST">
<input type="hidden" name="_next" value="https://taknova.com/takk"><input type="hidden" name="_subject" value="{e(subj)}"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="kilde" value="{SITE}/rad/{a['slug']}/"><input type="text" name="_honey" value="" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
<label>Navn *<input name="name" required autocomplete="name"></label>
<label>Telefon *<input name="phone" type="tel" required autocomplete="tel" placeholder="+47 ..."></label>
<label>E-post<input name="email" type="email" autocomplete="email" inputmode="email"></label>
<label>Postnummer / sted<input name="location" placeholder="F.eks. Bærum"></label>
<label class="full">Hva gjelder det?<textarea name="message" rows="3" placeholder="{e(a['form_hint'])}"></textarea></label>
<button class="btn primary full" type="submit">Bestill gratis befaring</button>
<p class="full rsmall">Du kan også ringe <a href="tel:+4796805961">968 05 961</a> eller skrive til <a href="mailto:info@taknova.com">info@taknova.com</a>. Opplysningene brukes bare til å svare deg. <a href="/personvern">Personvern</a>.</p>
</form></aside>'''


def build_article(a):
    url = f'{SITE}/rad/{a["slug"]}/'
    nav, bc_ld = crumbs([('Hjem', '/'), ('Råd og tips', '/rad/'), (CATEGORIES[a['cat']], f'/rad/#{a["cat"]}'), (a['card'], None)])
    words = len(re.sub('<[^>]+>', ' ', a['body'] + a['short']).split())
    mins = max(3, round(words / 200))
    faq_html = ''.join(f'<details class="rfaq"><summary>{e(q)}</summary><p>{ans}</p></details>' for q, ans in a['faq'])
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', ans)}}
        for q, ans in a['faq']]}
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": a['h1'], "description": a['desc'],
              "image": SITE + a['image'], "datePublished": a.get('date', '2026-11-22'), "dateModified": a.get('date', '2026-11-22'),
              "inLanguage": "nb-NO", "mainEntityOfPage": url, "author": ORG, "publisher": ORG}
    src_html = ''
    if a.get('sources'):
        src_html = '<p class="rsrc"><strong>Kilder:</strong> ' + ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in a['sources']) + '. Teksten er skrevet av TakNova.</p>'
    related = [c for c in all_cards() if c['url'] in a['related']]
    rel_html = ''.join(card(c) for c in related)
    page = head(a['title'], a['desc'], url, a['image'], [art_ld, bc_ld, faq_ld])
    page += f'''<main class="lp rart">{nav}<p class="rmeta"><a href="/rad/#{a['cat']}">{e(CATEGORIES[a['cat']])}</a> · {mins} min lesing · Oppdatert {a.get('date_text', '22. november 2026')}</p>
<h1>{e(a['h1'])}</h1><p class="lead">{a['lead']}</p>
<div class="rshort"><strong>Kort fortalt</strong>{a['short']}</div>
<img class="hero" src="{a['image']}" alt="{e(a['alt'])}" loading="eager"><p class="cap">Bildet viser et eksempel på en løsning.</p>
{a['body']}
<a class="rinline" href="#befaring">Vil du at vi ser på taket ditt? Bestill gratis befaring</a>
{src_html}<h2>Vanlige spørsmål</h2>{faq_html}
{cta_box(a)}
<section class="rrel"><h2>Les også</h2><div class="rgrid">{rel_html}</div><p><a href="/rad/">Alle råd og tips</a></p></section>
</main>{FOOTER}{SCRIPT}</body></html>'''
    d = os.path.join(ROOT, 'rad', a['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page)


def build_hub():
    url = SITE + '/rad/'
    title = 'Råd og tips om tak, lys og oppussing | TakNova'
    desc = ('Praktiske råd om tak, belysning, bad og oppussing: sprekker i taket, mugg på badet, lys i mørketiden, '
            'oppussing før salg og hva strekktak er. Skrevet av folk som monterer tak.')
    nav, bc_ld = crumbs([('Hjem', '/'), ('Råd og tips', None)])
    cards = all_cards()
    chips = ''.join(f'<a href="#{k}">{e(v)}</a>' for k, v in CATEGORIES.items() if any(c['cat'] == k for c in cards))
    sections = ''
    for k, v in CATEGORIES.items():
        cs = [c for c in cards if c['cat'] == k]
        if cs:
            sections += f'<section class="rsec" id="{k}"><h2>{e(v)}</h2><div class="rgrid">{"".join(card(c) for c in cs)}</div></section>'
    newest = ''.join(card(c) for c in cards if c['new'])
    list_ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Råd og tips om tak, lys og oppussing",
               "url": url, "inLanguage": "nb-NO", "publisher": ORG,
               "hasPart": [{"@type": "Article", "headline": c['title'], "url": SITE + c['url']} for c in cards if c['new']]}
    areas = ('<a href="/strekktak-oslo/">Oslo</a> · <a href="/strekktak-baerum/">Bærum</a> · <a href="/strekktak-asker/">Asker</a> · '
             '<a href="/strekktak-akershus/">Akershus</a> · <a href="/strekktak-pris/">Priser</a>')
    page = head(title, desc, url, '/eksempler/stue-lyslinjer.jpg', [list_ld, bc_ld], og_type='website')
    page += f'''<main class="lp rhub">{nav}<h1>Råd og tips om tak, lys og oppussing</h1>
<p class="lead">Her samler vi svar på det vi oftest får spørsmål om når vi er hjemme hos folk: sprekker og flekker i taket, fukt på badet, for lite lys i mørketiden og hva som lønner seg før man selger eller flytter inn. Noen råd kan du gjøre selv. Der strekktak er en god løsning, sier vi det, og der det ikke er det, sier vi det også.</p>
<nav class="rchips" aria-label="Kategorier">{chips}</nav>
<section class="rsec"><h2>Nye artikler</h2><div class="rgrid">{newest}</div></section>
{sections}
<aside class="rcta"><h2>Vil du heller at vi ser på det?</h2><p>Gratis og uforpliktende befaring i Oslo og Akershus. Du får et fast pristilbud etter oppmåling.</p><div class="cta"><a class="btn primary" href="/#kontakt">Bestill gratis befaring</a><a class="btn" href="tel:+4796805961">Ring 968 05 961</a></div></aside>
<p class="more">Vi monterer strekktak i {areas}.</p>
</main>{FOOTER}{SCRIPT}</body></html>'''
    os.makedirs(os.path.join(ROOT, 'rad'), exist_ok=True)
    open(os.path.join(ROOT, 'rad', 'index.html'), 'w', encoding='utf-8').write(page)


def update_sitemap():
    p = os.path.join(ROOT, 'sitemap.xml')
    s = open(p, encoding='utf-8').read()
    urls = [f'{SITE}/rad/'] + [f'{SITE}/rad/{a["slug"]}/' for a in ARTICLES]
    add = ''
    for u in urls:
        if f'<loc>{u}</loc>' not in s:
            add += f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n'
    if add:
        s = s.replace('</urlset>', add + '</urlset>')
        open(p, 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    for a in ARTICLES:
        build_article(a)
    build_hub()
    update_sitemap()
    print('ok:', 1 + len(ARTICLES), 'sider')
