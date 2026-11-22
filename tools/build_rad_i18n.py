#!/usr/bin/env python3
"""Oversatte artikler (EN/UK/PL) + små hub-sider. Kjør: python3 tools/build_rad_i18n.py"""
import html, json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rad_i18n import UI, T
ROOT = os.path.join(os.path.dirname(__file__), '..', 'public'); SITE = 'https://taknova.com'; e = html.escape
SRC = {'en': 'en.html', 'uk': 'natyazhni-steli-oslo/index.html', 'pl': 'sufity-napinane-oslo/index.html'}
ORG = {"@type": "Organization", "name": "TakNova", "url": SITE + "/"}
GC = '<script data-goatcounter="https://taknova.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'

def parts(lang):
    s = open(os.path.join(ROOT, SRC[lang]), encoding='utf-8').read()
    h = s[s.index('<header class="top">'):s.index('</header>') + 9]
    f = s[s.index('<footer class="site-footer">'):s.index('</footer>') + 9]
    m = re.search(r'<script[^>]*src="/script\.js[^"]*"[^>]*></script>', s); sc = m.group(0) if m else '<script src="/script.js?v=static-2"></script>'
    if lang == 'en':
        h = h.replace('href="#', 'href="/en#'); f = f.replace('href="#', 'href="/en#')
    else:
        h = h.replace('href="#', 'href="/' + SRC[lang].split('/')[0] + '/#'); f = f.replace('href="#', 'href="/' + SRC[lang].split('/')[0] + '/#')
    return h, f, sc

def head(lang, title, desc, url, img, ld, alts):
    u = UI[lang]
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{h}">' for l, h in alts)
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<link rel="canonical" href="{url}">{alt}<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}{img}"><meta property="og:locale" content="{u["locale"]}"><meta property="og:type" content="article">'
            '<link rel="stylesheet" href="/style.css?v=r3"><link rel="stylesheet" href="/footer-video.css?v=5"><link rel="stylesheet" href="/rad.css?v=1">'
            + ''.join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in ld) + GC + '</head><body>')

def crumbs(lang, items):
    p = [f'<a href="{l}">{e(n)}</a>' if l else f'<span aria-current="page">{e(n)}</span>' for n, l in items]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + l} if l else {})} for i, (n, l) in enumerate(items)]}
    return '<nav class="crumbs">' + ' <span aria-hidden="true">›</span> '.join(p) + '</nav>', ld

def card(lang, key):
    d = T[key][lang]; return f'<a class="rcard" href="{UI[lang]["base"]}{d["slug"]}/"><img src="{T[key]["image"]}" alt="" loading="lazy"><strong>{e(d["card"])}</strong><span class="rdesc">{e(d["desc"][:120].rsplit(" ",1)[0])}…</span></a>'

def build(key, lang):
    u = UI[lang]; d = T[key][lang]; H, F, SC = parts(lang)
    url = f'{SITE}{u["base"]}{d["slug"]}/'
    alts = [('nb', f'{SITE}/rad/{key}/')] + [(l, f'{SITE}{UI[l]["base"]}{T[key][l]["slug"]}/') for l in UI] + [('x-default', f'{SITE}/rad/{key}/')]
    nav, bc = crumbs(lang, [(u['home'], u['landing']), (u['hub'], u['base']), (d['card'], None)])
    words = len(re.sub('<[^>]+>', ' ', d['body']).split()); mins = max(3, round(words / 200))
    faq = ''.join(f'<details class="rfaq"><summary>{e(q)}</summary><p>{a}</p></details>' for q, a in d['faq'])
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": d['h1'], "description": d['desc'], "image": SITE + T[key]['image'], "datePublished": "2026-11-22", "dateModified": "2026-11-22", "inLanguage": lang, "mainEntityOfPage": url, "author": ORG, "publisher": ORG}, bc,
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in d['faq']]}]
    others = ''.join(card(lang, k) for k in T if k != key)
    form = f'''<aside class="rcta" id="befaring"><h2>{e(u['cta_h'])}</h2><p>{e(u['cta_p'])}</p><form class="rform" action="https://formsubmit.co/taknova.norge@gmail.com" method="POST">
<input type="hidden" name="_next" value="https://taknova.com/takk"><input type="hidden" name="_subject" value="{e('['+lang.upper()+'] '+d['card'])} | taknova"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="kilde" value="{url}"><input type="hidden" name="sprak" value="{lang}"><input type="text" name="_honey" value="" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
<label>{u['name']}<input name="name" required autocomplete="name"></label><label>{u['phone']}<input name="phone" type="tel" required autocomplete="tel" placeholder="+47 ..."></label>
<label>{u['email']}<input name="email" type="email" autocomplete="email"></label><label>{u['place']}<input name="location"></label>
<label class="full">{u['msg']}<textarea name="message" rows="3" placeholder="{e(d['hint'])}"></textarea></label><button class="btn primary full" type="submit">{u['btn']}</button><p class="full rsmall">{u['small']}</p></form></aside>'''
    page = head(lang, d['title'], d['desc'], url, T[key]['image'], ld, alts) + H + f'''<main class="lp rart">{nav}<p class="rmeta"><a href="{u['base']}">{e(u['hub'])}</a> · {mins} {u['read']} · {u['updated']} · <a href="/rad/{key}/" lang="nb">{u['no']}</a></p>
<h1>{e(d['h1'])}</h1><p class="lead">{d['lead']}</p><div class="rshort"><strong>{u['short']}</strong>{d['short']}</div>
<img class="hero" src="{T[key]['image']}" alt="" loading="eager"><p class="cap">{u['cap']}</p>{d['body']}
<a class="rinline" href="#befaring">{u['inline']}</a><h2>{u['faq']}</h2>{faq}{form}
<section class="rrel"><h2>{u['also']}</h2><div class="rgrid">{others}</div><p><a href="{u['landing']}">{e(u['landing_name'])}</a></p></section></main>{F}{SC}</body></html>'''
    p = os.path.join(ROOT, u['base'].strip('/'), d['slug']); os.makedirs(p, exist_ok=True)
    open(os.path.join(p, 'index.html'), 'w', encoding='utf-8').write(page)
    return url

def hub(lang):
    u = UI[lang]; H, F, SC = parts(lang); url = SITE + u['base']
    nav, bc = crumbs(lang, [(u['home'], u['landing']), (u['hub'], None)])
    cards = ''.join(card(lang, k) for k in T)
    page = head(lang, u['hub_title'], u['hub_lead'], url, '/eksempler/stue-lyslinjer.jpg', [bc], [(l, SITE + UI[l]['base']) for l in UI] + [('nb', SITE + '/rad/')]) + H + \
        f'<main class="lp rhub">{nav}<h1>{e(u["hub_h1"])}</h1><p class="lead">{e(u["hub_lead"])}</p><div class="rgrid">{cards}</div><p class="more"><a href="{u["landing"]}">{e(u["landing_name"])}</a></p></main>{F}{SC}</body></html>'
    p = os.path.join(ROOT, u['base'].strip('/')); os.makedirs(p, exist_ok=True)
    open(os.path.join(p, 'index.html'), 'w', encoding='utf-8').write(page); return url

if __name__ == '__main__':
    urls = []
    for lang in UI:
        urls.append(hub(lang))
        for key in T: urls.append(build(key, lang))
    sm = os.path.join(ROOT, 'sitemap.xml'); s = open(sm, encoding='utf-8').read()
    add = ''.join(f'<url><loc>{x}</loc><lastmod>2026-11-22</lastmod></url>\n' for x in urls if f'<loc>{x}</loc>' not in s)
    if add: open(sm, 'w', encoding='utf-8').write(s.replace('</urlset>', add + '</urlset>'))
    print('ok', len(urls))
