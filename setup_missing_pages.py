#!/usr/bin/env python3
"""
setup_missing_pages.py
Fixes footers on all pages, adds cookie banner, and creates all missing pages.
"""
import os, re, glob

BASE = '/home/user/Scorio-NL'

# ─────────────────────────────────────────────────────────────
# CORRECT FOOTER (with working links)
# ─────────────────────────────────────────────────────────────
NEW_FOOTER = '''  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/" class="logo">Scorio<span class="logo-dot"></span></a>
          <p class="footer-tagline">De slimste SEO scan tool voor Nederlandse ondernemers.</p>
          <div class="footer-socials">
            <a href="#" class="social-link" aria-label="LinkedIn">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
            <a href="#" class="social-link" aria-label="Twitter / X">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.748l7.73-8.835L1.254 2.25H8.08l4.253 5.622zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Product</h4>
          <ul>
            <li><a href="/#hoe-het-werkt">Hoe het werkt</a></li>
            <li><a href="/#prijzen">Prijzen</a></li>
            <li><a href="/">Gratis scan</a></li>
            <li><a href="/api/">API</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Bedrijf</h4>
          <ul>
            <li><a href="/over-ons/">Over ons</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/contact/">Contact</a></li>
            <li><a href="/affiliate/">Affiliate programma</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Legal</h4>
          <ul>
            <li><a href="/privacy/">Privacybeleid</a></li>
            <li><a href="/voorwaarden/">Algemene voorwaarden</a></li>
            <li><a href="/cookies/">Cookiebeleid</a></li>
            <li><a href="/avg/">AVG</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copyright">© 2026 Scorio.nl — KVK: 12345678 — Gemaakt in Nederland 🇳🇱</p>
        <div class="footer-payment">
          <div class="footer-pay-badge">
            <svg width="24" height="16" viewBox="0 0 40 26" fill="none" aria-hidden="true"><rect width="40" height="26" rx="4" fill="#CC0066"/><text x="20" y="17" text-anchor="middle" font-size="9" font-weight="900" fill="white" font-family="sans-serif">iDEAL</text></svg>
            iDEAL
          </div>
          <div class="footer-pay-badge">
            <svg width="24" height="16" viewBox="0 0 40 26" fill="none" aria-hidden="true"><rect width="40" height="26" rx="4" fill="#635BFF"/><text x="20" y="17" text-anchor="middle" font-size="9" font-weight="900" fill="white" font-family="sans-serif">stripe</text></svg>
            Stripe
          </div>
        </div>
      </div>
    </div>
  </footer>'''

# ─────────────────────────────────────────────────────────────
# COOKIE BANNER HTML + inline JS
# ─────────────────────────────────────────────────────────────
COOKIE_BANNER = '''
  <!-- Cookie Banner -->
  <div class="cookie-banner" id="cookie-banner" role="dialog" aria-label="Cookie melding">
    <div class="cookie-banner-inner">
      <p class="cookie-text"><span aria-hidden="true">🍪</span> Scorio gebruikt cookies voor analytics en een betere ervaring. <a href="/cookies/" class="cookie-link">Lees ons cookiebeleid.</a></p>
      <div class="cookie-actions">
        <button class="btn btn-ghost btn-sm" id="cookie-minimal">Alleen noodzakelijk</button>
        <button class="btn btn-accent btn-sm" id="cookie-accept">Alles accepteren</button>
      </div>
    </div>
  </div>
  <script>
  (function(){
    var b=document.getElementById('cookie-banner');
    if(!b)return;
    var c=localStorage.getItem('cookie_consent');
    if(c){document.body.classList.add(c==='all'?'cookies-accepted':'cookies-minimal');b.style.display='none';return;}
    b.style.display='';
    document.getElementById('cookie-accept').addEventListener('click',function(){localStorage.setItem('cookie_consent','all');document.body.classList.add('cookies-accepted');b.style.display='none';});
    document.getElementById('cookie-minimal').addEventListener('click',function(){localStorage.setItem('cookie_consent','minimal');document.body.classList.add('cookies-minimal');b.style.display='none';});
  })();
  </script>'''

# ─────────────────────────────────────────────────────────────
# HELPER: build a complete page
# ─────────────────────────────────────────────────────────────
def HEADER(active_nav=''):
    nav_items = [
        ('/hoe-het-werkt.html', 'Hoe het werkt'),
        ('/prijzen.html', 'Prijzen'),
        ('/blog/', 'Blog'),
    ]
    links = ''
    for href, label in nav_items:
        cls = ' class="active"' if href in active_nav else ''
        links += f'          <a href="{href}"{cls}>{label}</a>\n'
    return f'''  <header class="site-header" id="top">
    <div class="container">
      <div class="header-inner">
        <a href="/" class="logo">Scorio<span class="logo-dot"></span></a>
        <nav class="nav-links" role="navigation" aria-label="Hoofdmenu">
{links}        </nav>
        <div class="header-actions">
          <a href="#" class="btn btn-ghost btn-sm">Inloggen</a>
          <a href="/#hero-form" class="btn btn-accent btn-sm">Gratis scannen</a>
        </div>
        <button class="mobile-menu-btn" aria-label="Menu openen">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <button class="mobile-close-btn" aria-label="Menu sluiten">✕</button>
  </header>'''


def BREADCRUMB(crumbs):
    # crumbs: list of (label, href) — last item has no href
    items = []
    for i, (label, href) in enumerate(crumbs):
        if i < len(crumbs) - 1:
            items.append(f'<li><a href="{href}">{label}</a></li><li><span class="breadcrumb-sep" aria-hidden="true">/</span></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
    inner = '\n        '.join(items)
    return f'''  <nav class="breadcrumb" aria-label="Broodkruimelpad">
    <div class="container">
      <ol class="breadcrumb-list">
        {inner}
      </ol>
    </div>
  </nav>'''


def full_page(title, meta_desc, canonical_path, breadcrumbs, content, active_nav='', extra_head=''):
    canonical = f'https://www.scorio.nl{canonical_path}'
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta_desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Scorio.nl" />
  <meta property="og:locale" content="nl_NL" />
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='%235B4FE8'/><text x='16' y='22' text-anchor='middle' font-size='16' font-weight='900' fill='white' font-family='sans-serif'>S</text></svg>" />
{extra_head}</head>
<body>
{COOKIE_BANNER}
{HEADER(active_nav)}
{BREADCRUMB(breadcrumbs)}
  <main>
{content}
  </main>
{NEW_FOOTER}
  <script src="/js/main.js"></script>
</body>
</html>'''


# ─────────────────────────────────────────────────────────────
# PATCH EXISTING FILES
# ─────────────────────────────────────────────────────────────
def patch_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace footer
    content = re.sub(
        r'<footer class="site-footer".*?</footer>',
        NEW_FOOTER,
        content,
        flags=re.DOTALL
    )

    # 2. Add cookie banner after <body> if not already present
    if 'id="cookie-banner"' not in content:
        content = re.sub(
            r'(<body[^>]*>)',
            r'\1\n' + COOKIE_BANNER,
            content,
            count=1
        )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  patched: {path}')
    else:
        print(f'  unchanged: {path}')


def patch_all_existing():
    patterns = [
        f'{BASE}/index.html',
        f'{BASE}/hoe-het-werkt.html',
        f'{BASE}/prijzen.html',
        f'{BASE}/blog/*.html',
        f'{BASE}/seo-check-*/index.html',
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    files = sorted(set(files))
    print(f'Patching {len(files)} existing files...')
    for f in files:
        patch_file(f)


# ─────────────────────────────────────────────────────────────
# NEW PAGES CONTENT
# ─────────────────────────────────────────────────────────────

def privacy_content():
    return '''    <section style="padding: 48px 0 var(--section-gap);">
      <div class="container">
        <div style="max-width: 760px; margin: 0 auto;">
          <span class="section-label">Legal</span>
          <h1 style="font-size: clamp(2rem, 4vw, 2.8rem); margin-bottom: 16px;">Privacybeleid</h1>
          <p style="color: var(--muted); margin-bottom: 48px;"><em>Laatste update: mei 2026</em></p>

          <div class="glass-card" style="padding: 32px; margin-bottom: 48px;">
            <p style="line-height: 1.8; color: rgba(232,232,240,0.85);">Scorio.nl hecht veel waarde aan de bescherming van jouw persoonsgegevens. In dit privacybeleid leggen we uit welke gegevens we verzamelen, waarom we dat doen en hoe we daarmee omgaan. We voldoen volledig aan de Algemene Verordening Gegevensbescherming (AVG / GDPR).</p>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">1. Wie zijn wij?</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 12px;">Scorio.nl is een dienst van <strong>[BEDRIJFSNAAM]</strong>, gevestigd in Nederland.</p>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.75); line-height: 2;">
            <li>📧 E-mail: <a href="mailto:privacy@scorio.nl" style="color: var(--primary-light);">privacy@scorio.nl</a></li>
            <li>📋 KVK: 12345678</li>
            <li>📍 Adres: Nederland</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">2. Welke gegevens verzamelen we?</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> E-mailadres (bij aanmelden of PDF download)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> Website URL (bij het uitvoeren van een scan)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> Betalingsgegevens (verwerkt via Stripe — wij slaan geen betaalgegevens op)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> Gebruiksdata (via Google Analytics — alleen met toestemming)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> IP-adres (automatisch via server logs, geanonimiseerd)</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">3. Waarom verzamelen we deze gegevens?</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Om de SEO scan uit te voeren</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Om het PDF rapport te versturen</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Om je abonnement te beheren</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Om je te informeren over je account</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Om onze dienst te verbeteren</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">4. Grondslag voor verwerking</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Uitvoering van de overeenkomst</strong> — voor scan, rapport en abonnement</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Gerechtvaardigd belang</strong> — voor beveiliging en fraudepreventie</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Toestemming</strong> — voor analytics cookies en marketing e-mails</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">5. Hoe lang bewaren we gegevens?</h2>
          <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; margin-bottom: 8px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.875rem;">
              <thead><tr style="border-bottom: 1px solid var(--border);">
                <th style="padding: 14px 20px; text-align: left; color: var(--muted); font-weight: 600;">Gegevenstype</th>
                <th style="padding: 14px 20px; text-align: left; color: var(--muted); font-weight: 600;">Bewaartermijn</th>
              </tr></thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px;">Accountgegevens</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">Zolang account actief is</td></tr>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px;">Scanresultaten</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">12 maanden</td></tr>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px;">Factuurgegevens</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">7 jaar (wettelijke bewaarplicht)</td></tr>
                <tr><td style="padding: 14px 20px;">Analytics data</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">26 maanden</td></tr>
              </tbody>
            </table>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">6. Delen we gegevens met derden?</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 16px;">Wij delen gegevens alleen met de volgende partijen, uitsluitend voor het uitvoeren van onze dienst:</p>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Stripe</strong> — betalingsverwerking</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Supabase</strong> — database hosting (EU)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Google Analytics</strong> — gebruiksstatistieken (alleen met toestemming)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light);">→</span> <strong>Resend</strong> — e-mail verzending</li>
          </ul>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.7); margin-top: 16px; padding: 16px; background: rgba(0,200,150,0.08); border-left: 3px solid var(--accent); border-radius: 4px;"><strong style="color: var(--accent);">Wij verkopen nooit persoonsgegevens aan derden.</strong></p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">7. Jouw rechten (AVG)</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 16px;">Op grond van de AVG heb je de volgende rechten:</p>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Recht op inzage in je gegevens</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Recht op correctie van onjuiste gegevens</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Recht op verwijdering ("recht om vergeten te worden")</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Recht op beperking van verwerking</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Recht op dataportabiliteit</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent);">✓</span> Recht van bezwaar</li>
          </ul>
          <p style="margin-top: 16px; line-height: 1.8; color: rgba(232,232,240,0.75);">Stuur een e-mail naar <a href="mailto:privacy@scorio.nl" style="color: var(--primary-light);">privacy@scorio.nl</a> om een recht uit te oefenen. We reageren binnen 30 dagen.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">8. Cookies</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8);">Voor meer informatie over cookies verwijzen we naar ons <a href="/cookies/" style="color: var(--primary-light);">cookiebeleid</a>.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">9. Beveiliging</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8);">We gebruiken SSL/HTTPS encryptie voor alle communicatie. Wachtwoorden worden gehashed opgeslagen (nooit leesbaar). Toegang tot persoonsgegevens is beperkt tot medewerkers die dit strikt nodig hebben.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">10. Wijzigingen in dit beleid</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8);">We kunnen dit privacybeleid wijzigen. Bij wezenlijke wijzigingen informeren we je via e-mail. De datum van de laatste update staat bovenaan dit document.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">11. Klachten</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8);">Ben je niet tevreden over hoe wij omgaan met jouw gegevens? Je kunt een klacht indienen bij de <a href="https://www.autoriteitpersoonsgegevens.nl" target="_blank" rel="noopener noreferrer" style="color: var(--primary-light);">Autoriteit Persoonsgegevens</a>.</p>

          <div style="margin-top: 48px; padding: 28px; background: rgba(91,79,232,0.08); border: 1px solid rgba(91,79,232,0.2); border-radius: 16px; text-align: center;">
            <p style="margin-bottom: 16px; font-size: 0.9rem; color: rgba(232,232,240,0.75);">Vragen over dit privacybeleid?</p>
            <a href="mailto:privacy@scorio.nl" class="btn btn-accent">Stuur een e-mail →</a>
          </div>
        </div>
      </div>
    </section>'''


def voorwaarden_content():
    return '''    <section style="padding: 48px 0 var(--section-gap);">
      <div class="container">
        <div style="max-width: 760px; margin: 0 auto;">
          <span class="section-label">Legal</span>
          <h1 style="font-size: clamp(2rem, 4vw, 2.8rem); margin-bottom: 16px;">Algemene Voorwaarden</h1>
          <p style="color: var(--muted); margin-bottom: 48px;"><em>Laatste update: mei 2026 — Van toepassing op alle gebruik van Scorio.nl</em></p>

          <h2 style="font-size: 1.3rem; margin: 0 0 16px;">1. Definities</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2; margin-bottom: 32px;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> <span><strong>Scorio.nl</strong> — de dienst aangeboden door [BEDRIJFSNAAM], geregistreerd in Nederland (KVK: 12345678)</span></li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> <span><strong>Gebruiker</strong> — iedereen die de dienst van Scorio.nl gebruikt</span></li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> <span><strong>Abonnement</strong> — betaalde toegang tot uitgebreide functies van Scorio.nl</span></li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> <span><strong>Rapport</strong> — het door Scorio gegenereerde SEO analyse rapport</span></li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">2. Toepasselijkheid</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 32px;">Deze algemene voorwaarden zijn van toepassing op alle gebruik van Scorio.nl en alle overeenkomsten die voortvloeien uit het gebruik van onze dienst. Door gebruik te maken van Scorio.nl ga je akkoord met deze voorwaarden.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">3. De dienst</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2; margin-bottom: 32px;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> Scorio.nl biedt geautomatiseerde SEO analyse van websites</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> Resultaten zijn indicatief van aard en dienen als richtlijn</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> We garanderen geen specifieke Google-rankings of resultaten</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> We behouden het recht de dienst te wijzigen of te beëindigen</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> We streven naar een uptime van 99,5%, maar geven geen garantie</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">4. Abonnementen en betaling</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2; margin-bottom: 32px;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> Abonnementen worden maandelijks of jaarlijks vooruit gefactureerd</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> Betaling via iDEAL of creditcard (verwerkt door Stripe)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> Prijzen zijn exclusief BTW voor zakelijke gebruikers (21%)</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--primary-light); flex-shrink:0;">→</span> Bij niet-betaling wordt de toegang na een herinnering geblokkeerd</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">5. Gratis proefperiode</h2>
          <ul style="list-style: none; padding: 0; color: rgba(232,232,240,0.8); line-height: 2.2; margin-bottom: 32px;">
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent); flex-shrink:0;">✓</span> 14 dagen gratis voor Starter, Pro en Agency abonnementen</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent); flex-shrink:0;">✓</span> Na de proefperiode automatisch verlengd tenzij je opzegt</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent); flex-shrink:0;">✓</span> Opzeggen kan eenvoudig via je accountpagina</li>
            <li style="display: flex; gap: 10px;"><span style="color: var(--accent); flex-shrink:0;">✓</span> Geen creditcard vereist voor de gratis scan</li>
          </ul>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">6. Opzegging</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 32px;">Opzeggen kan altijd via je accountinstellingen. Opzegging gaat in aan het einde van de lopende betaalde periode. Er vindt geen terugbetaling plaats van reeds betaalde bedragen voor de lopende periode.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">7. Aansprakelijkheid</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 16px;">Scorio.nl is niet aansprakelijk voor indirecte schade, gevolgschade of gederfde winst. Onze totale aansprakelijkheid is beperkt tot het bedrag dat je in de afgelopen drie maanden hebt betaald voor de dienst. Rapporten zijn indicatief — we geven geen garantie op specifieke zoekresultaten.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">8. Intellectueel eigendom</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 32px;">Alle content, software en functionaliteit van Scorio.nl is eigendom van [BEDRIJFSNAAM]. De gegenereerde rapporten zijn bestemd voor eigen gebruik van de gebruiker. Reproductie of doorverkoop van rapporten zonder toestemming is niet toegestaan.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">9. Toepasselijk recht</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 16px;">Op deze voorwaarden is Nederlands recht van toepassing. Geschillen die niet in goed overleg worden opgelost, worden voorgelegd aan de bevoegde rechter in Nederland.</p>

          <div style="margin-top: 48px; padding: 28px; background: rgba(91,79,232,0.08); border: 1px solid rgba(91,79,232,0.2); border-radius: 16px;">
            <p style="margin-bottom: 8px; font-size: 0.9rem; color: rgba(232,232,240,0.75);">Vragen over onze algemene voorwaarden?</p>
            <a href="/contact/" style="color: var(--primary-light);">Neem contact op →</a>
          </div>
        </div>
      </div>
    </section>'''


def cookies_content():
    return '''    <section style="padding: 48px 0 var(--section-gap);">
      <div class="container">
        <div style="max-width: 760px; margin: 0 auto;">
          <span class="section-label">Legal</span>
          <h1 style="font-size: clamp(2rem, 4vw, 2.8rem); margin-bottom: 16px;">Cookiebeleid</h1>
          <p style="color: var(--muted); margin-bottom: 48px;"><em>Laatste update: mei 2026</em></p>

          <h2 style="font-size: 1.3rem; margin: 0 0 16px;">1. Wat zijn cookies?</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 32px;">Cookies zijn kleine tekstbestanden die op je apparaat worden opgeslagen wanneer je een website bezoekt. Ze helpen de website te onthouden wie je bent en wat je voorkeuren zijn, zodat je een betere ervaring krijgt bij een volgend bezoek.</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">2. Welke cookies gebruiken wij?</h2>
          <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; margin-bottom: 32px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.825rem;">
              <thead>
                <tr style="border-bottom: 1px solid var(--border);">
                  <th style="padding: 14px 16px; text-align: left; color: var(--muted); font-weight: 600;">Naam</th>
                  <th style="padding: 14px 16px; text-align: left; color: var(--muted); font-weight: 600;">Type</th>
                  <th style="padding: 14px 16px; text-align: left; color: var(--muted); font-weight: 600;">Doel</th>
                  <th style="padding: 14px 16px; text-align: left; color: var(--muted); font-weight: 600;">Duur</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border);">
                  <td style="padding: 12px 16px; font-family: monospace; font-size: 0.8rem;">_ga</td>
                  <td style="padding: 12px 16px;"><span class="badge badge-primary" style="font-size: 0.7rem;">Analytisch</span></td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">Google Analytics bezoekersidentificatie</td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">2 jaar</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border);">
                  <td style="padding: 12px 16px; font-family: monospace; font-size: 0.8rem;">_gid</td>
                  <td style="padding: 12px 16px;"><span class="badge badge-primary" style="font-size: 0.7rem;">Analytisch</span></td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">Google Analytics sessie</td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">24 uur</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border);">
                  <td style="padding: 12px 16px; font-family: monospace; font-size: 0.8rem;">stripe_mid</td>
                  <td style="padding: 12px 16px;"><span class="badge badge-accent" style="font-size: 0.7rem;">Functioneel</span></td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">Betalingsverwerking Stripe</td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">1 jaar</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border);">
                  <td style="padding: 12px 16px; font-family: monospace; font-size: 0.8rem;">sb-auth-token</td>
                  <td style="padding: 12px 16px;"><span class="badge badge-accent" style="font-size: 0.7rem;">Functioneel</span></td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">Inloggen en sessie</td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">Sessie</td>
                </tr>
                <tr>
                  <td style="padding: 12px 16px; font-family: monospace; font-size: 0.8rem;">cookie_consent</td>
                  <td style="padding: 12px 16px;"><span class="badge badge-accent" style="font-size: 0.7rem;">Functioneel</span></td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">Cookie voorkeur onthouden</td>
                  <td style="padding: 12px 16px; color: rgba(232,232,240,0.7);">1 jaar</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">3. Typen cookies</h2>

          <div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 32px;">
            <div style="background: rgba(0,200,150,0.08); border: 1px solid rgba(0,200,150,0.2); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--accent);">Noodzakelijk</strong>
              <p style="margin: 8px 0 0; font-size: 0.875rem; color: rgba(232,232,240,0.75); line-height: 1.6;">Altijd actief. Zonder deze cookies werkt de website niet correct. Je kunt deze cookies niet weigeren.</p>
            </div>
            <div style="background: rgba(91,79,232,0.08); border: 1px solid rgba(91,79,232,0.2); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--primary-light);">Analytisch</strong>
              <p style="margin: 8px 0 0; font-size: 0.875rem; color: rgba(232,232,240,0.75); line-height: 1.6;">Alleen actief met jouw toestemming. Helpen ons begrijpen hoe bezoekers de website gebruiken, zodat we kunnen verbeteren.</p>
            </div>
            <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--muted);">Marketing</strong>
              <p style="margin: 8px 0 0; font-size: 0.875rem; color: rgba(232,232,240,0.5); line-height: 1.6;">Scorio.nl maakt geen gebruik van marketingcookies voor advertentiedoeleinden.</p>
            </div>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">4. Cookie toestemming beheren</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 16px;">Bij je eerste bezoek tonen we een cookiebanner. Je kunt kiezen voor "Alles accepteren" of "Alleen noodzakelijk". Je keuze wordt opgeslagen in je browser.</p>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 16px;">Wil je je keuze herzien? Klik op de onderstaande knop om de banner opnieuw te tonen:</p>
          <button onclick="localStorage.removeItem(\'cookie_consent\'); location.reload();" class="btn btn-ghost btn-sm">Cookie instellingen opnieuw instellen</button>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">5. Meer informatie</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8);">Vragen over ons cookiebeleid? Stuur een e-mail naar <a href="mailto:privacy@scorio.nl" style="color: var(--primary-light);">privacy@scorio.nl</a>. Meer informatie over cookies vind je op <a href="https://www.veiliginternetten.nl" target="_blank" rel="noopener noreferrer" style="color: var(--primary-light);">veiliginternetten.nl</a>.</p>
        </div>
      </div>
    </section>'''


def avg_content():
    return '''    <section style="padding: 48px 0 var(--section-gap);">
      <div class="container">
        <div style="max-width: 760px; margin: 0 auto;">
          <span class="section-label">Legal</span>
          <h1 style="font-size: clamp(2rem, 4vw, 2.8rem); margin-bottom: 16px;">AVG &amp; GDPR Compliance</h1>
          <p style="color: rgba(232,232,240,0.75); line-height: 1.8; margin-bottom: 48px;">Scorio.nl neemt de bescherming van persoonsgegevens serieus en voldoet volledig aan de Algemene Verordening Gegevensbescherming (AVG / GDPR), de Europese privacywetgeving die sinds 25 mei 2018 van kracht is.</p>

          <h2 style="font-size: 1.3rem; margin: 0 0 16px;">1. Wat is de AVG?</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8); margin-bottom: 32px;">De Algemene Verordening Gegevensbescherming (AVG) is de Europese wet die de verwerking van persoonsgegevens reguleert. De AVG geldt voor alle organisaties die persoonsgegevens verwerken van EU-inwoners. In het Engels heet deze wet de General Data Protection Regulation (GDPR).</p>

          <h2 style="font-size: 1.3rem; margin: 40px 0 20px;">2. Hoe voldoen wij aan de AVG?</h2>
          <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px;">
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Privacybeleid aanwezig en up-to-date</strong><br><span style="font-size: 0.85rem; color: var(--muted);">Volledig uitgewerkt privacybeleid beschikbaar via /privacy/</span></div>
            </div>
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Cookie toestemming via banner</strong><br><span style="font-size: 0.85rem; color: var(--muted);">Alleen analytische cookies na expliciete toestemming</span></div>
            </div>
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Gegevensminimalisatie</strong><br><span style="font-size: 0.85rem; color: var(--muted);">We verzamelen alleen gegevens die strikt noodzakelijk zijn</span></div>
            </div>
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Verwerkersovereenkomsten met alle sub-processors</strong><br><span style="font-size: 0.85rem; color: var(--muted);">Stripe, Supabase, Google, Resend, Vercel</span></div>
            </div>
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Beveiligde dataopslag</strong><br><span style="font-size: 0.85rem; color: var(--muted);">SSL/HTTPS encryptie, gehashte wachtwoorden</span></div>
            </div>
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Recht op verwijdering geïmplementeerd</strong><br><span style="font-size: 0.85rem; color: var(--muted);">Verzoek indienen via privacy@scorio.nl</span></div>
            </div>
            <div style="display: flex; gap: 16px; align-items: flex-start; padding: 16px; background: rgba(0,200,150,0.08); border-radius: 12px;">
              <span style="color: var(--accent); font-weight: 700; flex-shrink: 0;">✓</span>
              <div><strong>Data breach procedure aanwezig</strong><br><span style="font-size: 0.85rem; color: var(--muted);">Melding bij AP binnen 72 uur indien vereist</span></div>
            </div>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">3. Sub-processors</h2>
          <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; margin-bottom: 40px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">
              <thead><tr style="border-bottom: 1px solid var(--border);">
                <th style="padding: 14px 20px; text-align: left; color: var(--muted); font-weight: 600;">Partij</th>
                <th style="padding: 14px 20px; text-align: left; color: var(--muted); font-weight: 600;">Locatie</th>
                <th style="padding: 14px 20px; text-align: left; color: var(--muted); font-weight: 600;">Doel</th>
              </tr></thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px; font-weight: 600;">Stripe</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">VS / EU</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">Betalingsverwerking</td></tr>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px; font-weight: 600;">Supabase</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">VS / EU</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">Database &amp; authenticatie</td></tr>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px; font-weight: 600;">Google Analytics</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">VS</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">Gebruiksstatistieken</td></tr>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 14px 20px; font-weight: 600;">Resend</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">VS</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">E-mail verzending</td></tr>
                <tr><td style="padding: 14px 20px; font-weight: 600;">Vercel</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">VS / EU</td><td style="padding: 14px 20px; color: rgba(232,232,240,0.7);">Website hosting &amp; CDN</td></tr>
              </tbody>
            </table>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">4. Jouw rechten uitoefenen</h2>
          <div class="glass-card" style="padding: 32px; text-align: center; background: linear-gradient(135deg, rgba(91,79,232,0.12), rgba(0,200,150,0.06));">
            <p style="font-size: 1rem; margin-bottom: 8px; font-weight: 600;">Wil je je gegevens inzien, aanpassen of verwijderen?</p>
            <p style="font-size: 0.875rem; color: var(--muted); margin-bottom: 24px;">We reageren binnen 30 dagen op alle privacy verzoeken.</p>
            <a href="mailto:privacy@scorio.nl" class="btn btn-accent">Stuur een privacy verzoek →</a>
          </div>

          <h2 style="font-size: 1.3rem; margin: 40px 0 16px;">5. Autoriteit Persoonsgegevens</h2>
          <p style="line-height: 1.8; color: rgba(232,232,240,0.8);">Heb je een klacht over onze gegevensverwerking? Je kunt een klacht indienen bij de <a href="https://www.autoriteitpersoonsgegevens.nl" target="_blank" rel="noopener noreferrer" style="color: var(--primary-light);">Autoriteit Persoonsgegevens</a>.</p>
        </div>
      </div>
    </section>'''


def over_ons_content():
    return '''    <section style="padding: 48px 0 64px;">
      <div class="container">
        <div class="text-center" style="max-width: 680px; margin: 0 auto 80px;">
          <span class="section-label">🇳🇱 Gemaakt in Nederland</span>
          <h1 class="section-heading">Wij geloven dat elke ondernemer gevonden moet worden</h1>
          <p class="section-sub">Scorio is gebouwd voor de Nederlandse MKB'er die geen SEO-expert is maar wel wil groeien via Google.</p>
        </div>
      </div>
    </section>

    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; margin-bottom: 80px;">
          <div>
            <span class="section-label">Ons verhaal</span>
            <h2 class="section-heading" style="font-size: clamp(1.6rem, 3vw, 2.2rem);">Waarom Scorio bestaat</h2>
            <p style="color: rgba(232,232,240,0.8); line-height: 1.9; margin-bottom: 20px;">Elke dag spreken we ondernemers die een prachtig product of dienst hebben — maar online onzichtbaar zijn.</p>
            <p style="color: rgba(232,232,240,0.8); line-height: 1.9; margin-bottom: 20px;">Niet omdat ze niets doen. Maar omdat bestaande SEO tools te complex, te duur of gewoon niet in het Nederlands zijn.</p>
            <p style="color: rgba(232,232,240,0.8); line-height: 1.9; margin-bottom: 20px;">Scorio lost dat op. Geen jargon, geen overweldigende dashboards. Gewoon een duidelijk rapport met concrete acties in begrijpelijk Nederlands.</p>
            <p style="color: rgba(232,232,240,0.8); line-height: 1.9;">Gemaakt voor de kapper in Amsterdam, de loodgieter in Rotterdam en de webshop eigenaar in Eindhoven.</p>
          </div>
          <div>
            <div class="glass-card" style="padding: 40px; background: linear-gradient(135deg, rgba(91,79,232,0.15), rgba(0,200,150,0.08)); text-align: center;">
              <span style="font-size: 3rem; display: block; margin-bottom: 20px;" aria-hidden="true">🎯</span>
              <h3 style="font-size: 1.1rem; margin-bottom: 12px;">Onze missie</h3>
              <p style="color: rgba(232,232,240,0.8); line-height: 1.7; font-style: italic; font-size: 1.05rem;">"Elke Nederlandse ondernemer helpen gevonden te worden door de mensen die nu naar hem zoeken."</p>
            </div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 80px;">
          <div class="glass-card" style="padding: 32px; text-align: center;">
            <span style="font-size: 2.5rem; display: block; margin-bottom: 16px;" aria-hidden="true">🎯</span>
            <h3 style="margin-bottom: 12px;">Eenvoud</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.7;">Geen jargon. Gewoon duidelijke uitleg en concrete acties die elke ondernemer zelf kan uitvoeren.</p>
          </div>
          <div class="glass-card" style="padding: 32px; text-align: center;">
            <span style="font-size: 2.5rem; display: block; margin-bottom: 16px;" aria-hidden="true">🇳🇱</span>
            <h3 style="margin-bottom: 12px;">Nederlands</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.7;">Gebouwd voor de Nederlandse markt. iDEAL, Nederlandse content, lokale focus en Dutch support.</p>
          </div>
          <div class="glass-card" style="padding: 32px; text-align: center;">
            <span style="font-size: 2.5rem; display: block; margin-bottom: 16px;" aria-hidden="true">💪</span>
            <h3 style="margin-bottom: 12px;">Eerlijk</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.7;">We vertellen wat er echt mis is. Geen mooipraterij, wel oplossingen. Transparant over mogelijkheden én beperkingen.</p>
          </div>
        </div>

        <div style="text-align: center; margin-bottom: 80px;">
          <span class="section-label">Het team</span>
          <h2 class="section-heading" style="font-size: clamp(1.5rem, 3vw, 2rem); margin-bottom: 48px;">Het team achter Scorio</h2>
          <div style="display: inline-block; max-width: 280px;">
            <div style="width: 120px; height: 120px; background: linear-gradient(135deg, var(--primary), var(--accent)); border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 900; color: #fff;">S</div>
            <h3 style="margin-bottom: 4px;">[Jouw naam]</h3>
            <p style="color: var(--muted); font-size: 0.875rem; margin-bottom: 12px;">Oprichter &amp; Developer</p>
            <p style="font-size: 0.85rem; color: rgba(232,232,240,0.7); line-height: 1.7;">[Korte bio — vul zelf in. Bijv.: SEO-expert met 8 jaar ervaring, gefocust op het Nederlandse MKB.]</p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 64px;">
          <div class="glass-card" style="padding: 28px; text-align: center;">
            <span style="font-size: 2rem; font-weight: 900; color: var(--primary-light); display: block; margin-bottom: 8px;">2.400+</span>
            <span style="font-size: 0.85rem; color: var(--muted);">Websites gescand</span>
          </div>
          <div class="glass-card" style="padding: 28px; text-align: center;">
            <span style="font-size: 2rem; font-weight: 900; color: var(--primary-light); display: block; margin-bottom: 8px;">4,8/5</span>
            <span style="font-size: 0.85rem; color: var(--muted);">Gemiddelde beoordeling</span>
          </div>
          <div class="glass-card" style="padding: 28px; text-align: center;">
            <span style="font-size: 2rem; font-weight: 900; color: var(--primary-light); display: block; margin-bottom: 8px;">100%</span>
            <span style="font-size: 0.85rem; color: var(--muted);">Gemaakt in Nederland</span>
          </div>
        </div>

        <div style="text-align: center;">
          <p style="color: var(--muted); margin-bottom: 20px;">Vragen of feedback?</p>
          <a href="/contact/" class="btn btn-accent">Neem contact op →</a>
        </div>
      </div>
    </section>'''


def contact_content():
    return '''    <section style="padding: 48px 0 var(--section-gap);">
      <div class="container">
        <div class="text-center" style="margin-bottom: 64px;">
          <span class="section-label">Contact</span>
          <h1 class="section-heading">Neem contact op</h1>
          <p class="section-sub">We reageren altijd binnen één werkdag. Liever direct een scan? <a href="/" style="color: var(--primary-light);">Ga dan naar de homepage →</a></p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start;">

          <!-- Contact form -->
          <div class="glass-card" style="padding: 40px;">
            <h2 style="font-size: 1.2rem; margin-bottom: 28px;">Stuur een bericht</h2>
            <form action="mailto:info@scorio.nl" method="POST" enctype="text/plain" novalidate>
              <div style="display: flex; flex-direction: column; gap: 20px;">
                <div>
                  <label for="contact-naam" style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; color: rgba(232,232,240,0.8);">Naam *</label>
                  <input type="text" id="contact-naam" name="naam" required placeholder="Jouw naam" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
                </div>
                <div>
                  <label for="contact-email" style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; color: rgba(232,232,240,0.8);">E-mailadres *</label>
                  <input type="email" id="contact-email" name="email" required placeholder="jouw@email.nl" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
                </div>
                <div>
                  <label for="contact-onderwerp" style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; color: rgba(232,232,240,0.8);">Onderwerp *</label>
                  <select id="contact-onderwerp" name="onderwerp" required style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box; appearance: none;">
                    <option value="" disabled selected>Kies een onderwerp</option>
                    <option value="vraag">Vraag over de dienst</option>
                    <option value="technisch">Technisch probleem</option>
                    <option value="factuur">Factuur of betaling</option>
                    <option value="privacy">Privacy verzoek</option>
                    <option value="samenwerking">Samenwerking</option>
                    <option value="anders">Anders</option>
                  </select>
                </div>
                <div>
                  <label for="contact-bericht" style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; color: rgba(232,232,240,0.8);">Bericht *</label>
                  <textarea id="contact-bericht" name="bericht" required rows="6" placeholder="Jouw bericht..." style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box; resize: vertical;"></textarea>
                </div>
                <button type="submit" class="btn btn-accent" style="width: 100%;">Verstuur bericht →</button>
                <p style="font-size: 0.775rem; color: var(--muted); text-align: center;">Dit opent je e-mailprogramma. Liever direct mailen? <a href="mailto:info@scorio.nl" style="color: var(--primary-light);">info@scorio.nl</a></p>
              </div>
            </form>
          </div>

          <!-- Contact info -->
          <div style="display: flex; flex-direction: column; gap: 20px;">
            <div class="glass-card" style="padding: 28px; display: flex; gap: 20px; align-items: flex-start;">
              <span style="font-size: 1.8rem;" aria-hidden="true">📧</span>
              <div>
                <h3 style="font-size: 1rem; margin-bottom: 8px;">E-mail</h3>
                <a href="mailto:info@scorio.nl" style="color: var(--primary-light); text-decoration: none;">info@scorio.nl</a>
                <p style="font-size: 0.825rem; color: var(--muted); margin-top: 4px;">Reactietijd: binnen 1 werkdag</p>
              </div>
            </div>
            <div class="glass-card" style="padding: 28px; display: flex; gap: 20px; align-items: flex-start;">
              <span style="font-size: 1.8rem;" aria-hidden="true">🕐</span>
              <div>
                <h3 style="font-size: 1rem; margin-bottom: 8px;">Bereikbaarheid</h3>
                <p style="color: rgba(232,232,240,0.8); font-size: 0.875rem;">Maandag t/m vrijdag</p>
                <p style="color: rgba(232,232,240,0.8); font-size: 0.875rem;">9:00 — 17:00 uur</p>
              </div>
            </div>
            <div class="glass-card" style="padding: 28px; display: flex; gap: 20px; align-items: flex-start;">
              <span style="font-size: 1.8rem;" aria-hidden="true">📍</span>
              <div>
                <h3 style="font-size: 1rem; margin-bottom: 8px;">Gevestigd in</h3>
                <p style="color: rgba(232,232,240,0.8); font-size: 0.875rem;">Nederland 🇳🇱</p>
                <p style="font-size: 0.8rem; color: var(--muted); margin-top: 4px;">KVK: 12345678</p>
              </div>
            </div>
            <div class="glass-card" style="padding: 28px; display: flex; gap: 20px; align-items: flex-start;">
              <span style="font-size: 1.8rem;" aria-hidden="true">❓</span>
              <div>
                <h3 style="font-size: 1rem; margin-bottom: 8px;">Veelgestelde vragen</h3>
                <p style="font-size: 0.825rem; color: var(--muted); margin-bottom: 12px;">Vind snel een antwoord in onze FAQ.</p>
                <a href="/#faq" style="color: var(--primary-light); font-size: 0.85rem;">Bekijk de FAQ →</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''


def affiliate_content():
    return '''    <section style="padding: 48px 0 64px;">
      <div class="container">
        <div class="text-center" style="max-width: 640px; margin: 0 auto;">
          <span class="section-label">💰 Affiliate Programma</span>
          <h1 class="section-heading">30% recurring commissie op elke betaalde klant</h1>
          <p class="section-sub">Verwijs ondernemers naar Scorio en verdien elke maand commissie zolang ze klant zijn. Geen plafond. Maandelijks uitbetaald.</p>
          <a href="#aanmelden" class="btn btn-accent btn-lg">Meld je nu aan →</a>
        </div>
      </div>
    </section>

    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 80px;">
          <div class="glass-card" style="padding: 32px; text-align: center;">
            <div style="width: 56px; height: 56px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-weight: 900; font-size: 1.2rem; color: #fff;">1</div>
            <h3 style="margin-bottom: 10px;">Meld je aan</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">Vul het formulier in en ontvang je unieke affiliate link binnen 24 uur.</p>
          </div>
          <div class="glass-card" style="padding: 32px; text-align: center;">
            <div style="width: 56px; height: 56px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-weight: 900; font-size: 1.2rem; color: #fff;">2</div>
            <h3 style="margin-bottom: 10px;">Deel jouw link</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">Deel je link met klanten, op je website, in je nieuwsbrief of op social media.</p>
          </div>
          <div class="glass-card" style="padding: 32px; text-align: center;">
            <div style="width: 56px; height: 56px; background: var(--accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-weight: 900; font-size: 1.2rem; color: #fff;">3</div>
            <h3 style="margin-bottom: 10px;">Verdien 30%</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">30% van elke betaling, elke maand opnieuw. Zolang jouw klant bij Scorio blijft.</p>
          </div>
        </div>

        <div class="glass-card" style="padding: 48px; margin-bottom: 80px;">
          <h2 style="font-size: 1.3rem; margin-bottom: 28px; text-align: center;">💰 Bereken jouw commissie</h2>
          <div style="max-width: 520px; margin: 0 auto;">
            <div style="margin-bottom: 24px;">
              <label style="display: flex; justify-content: space-between; font-size: 0.875rem; font-weight: 600; margin-bottom: 12px;">
                <span>Hoeveel Starter klanten verwijs je per maand?</span>
                <span id="starter-val" style="color: var(--primary-light);">5</span>
              </label>
              <input type="range" id="starter-slider" min="1" max="50" value="5" style="width: 100%; accent-color: var(--primary);" oninput="calcAff()" />
            </div>
            <div style="margin-bottom: 32px;">
              <label style="display: flex; justify-content: space-between; font-size: 0.875rem; font-weight: 600; margin-bottom: 12px;">
                <span>Hoeveel Pro klanten verwijs je per maand?</span>
                <span id="pro-val" style="color: var(--primary-light);">2</span>
              </label>
              <input type="range" id="pro-slider" min="0" max="30" value="2" style="width: 100%; accent-color: var(--primary);" oninput="calcAff()" />
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px;">
              <div style="background: rgba(91,79,232,0.12); border: 1px solid rgba(91,79,232,0.25); border-radius: 16px; padding: 20px; text-align: center;">
                <span id="maand-out" style="font-size: 2rem; font-weight: 900; color: var(--primary-light); display: block;">€20,70</span>
                <span style="font-size: 0.8rem; color: var(--muted);">Per maand</span>
              </div>
              <div style="background: rgba(0,200,150,0.1); border: 1px solid rgba(0,200,150,0.25); border-radius: 16px; padding: 20px; text-align: center;">
                <span id="jaar-out" style="font-size: 2rem; font-weight: 900; color: var(--accent); display: block;">€248</span>
                <span style="font-size: 0.8rem; color: var(--muted);">Per jaar</span>
              </div>
            </div>
            <p style="font-size: 0.775rem; color: var(--muted); text-align: center;">Berekend op Starter €9/mnd en Pro €29/mnd × 30% commissie</p>
          </div>
        </div>
        <script>
        function calcAff(){
          var s=parseInt(document.getElementById('starter-slider').value);
          var p=parseInt(document.getElementById('pro-slider').value);
          document.getElementById('starter-val').textContent=s;
          document.getElementById('pro-val').textContent=p;
          var m=s*9*0.3+p*29*0.3;
          document.getElementById('maand-out').textContent='€'+m.toFixed(2).replace('.',',');
          document.getElementById('jaar-out').textContent='€'+(m*12).toFixed(0);
        }
        </script>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 80px;">
          <div class="glass-card" style="padding: 24px;">
            <span style="font-size: 1.5rem; display: block; margin-bottom: 12px;" aria-hidden="true">🎨</span>
            <strong style="display: block; margin-bottom: 6px;">Webdesigners &amp; bureaus</strong>
            <p style="font-size: 0.825rem; color: var(--muted); line-height: 1.6;">Bied Scorio aan als extra dienst aan je klanten en verdien passief inkomen.</p>
          </div>
          <div class="glass-card" style="padding: 24px;">
            <span style="font-size: 1.5rem; display: block; margin-bottom: 12px;" aria-hidden="true">🔍</span>
            <strong style="display: block; margin-bottom: 6px;">SEO consultants</strong>
            <p style="font-size: 0.825rem; color: var(--muted); line-height: 1.6;">Gebruik Scorio als tool voor je klanten en verdien mee aan de abonnementen.</p>
          </div>
          <div class="glass-card" style="padding: 24px;">
            <span style="font-size: 1.5rem; display: block; margin-bottom: 12px;" aria-hidden="true">✍️</span>
            <strong style="display: block; margin-bottom: 6px;">Bloggers &amp; content creators</strong>
            <p style="font-size: 0.825rem; color: var(--muted); line-height: 1.6;">Schrijf over SEO voor ondernemers en verdien aan je lezers die Scorio proberen.</p>
          </div>
        </div>

        <div id="aanmelden" class="glass-card" style="padding: 48px; max-width: 600px; margin: 0 auto;">
          <h2 style="font-size: 1.3rem; margin-bottom: 28px; text-align: center;">Meld je aan als affiliate</h2>
          <form action="mailto:affiliate@scorio.nl" method="POST" enctype="text/plain" style="display: flex; flex-direction: column; gap: 18px;">
            <div>
              <label style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Naam *</label>
              <input type="text" name="naam" required placeholder="Jouw naam" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
            </div>
            <div>
              <label style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">E-mailadres *</label>
              <input type="email" name="email" required placeholder="jouw@email.nl" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
            </div>
            <div>
              <label style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Website of platform</label>
              <input type="url" name="website" placeholder="https://jouwwebsite.nl" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
            </div>
            <div>
              <label style="display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Hoe ga je Scorio promoten? *</label>
              <textarea name="promotie" required rows="4" placeholder="Bijv. via mijn blog, nieuwsbrief, klanten..." style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box; resize: vertical;"></textarea>
            </div>
            <button type="submit" class="btn btn-accent" style="width: 100%;">Aanmelden als affiliate →</button>
          </form>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--border); font-size: 0.8rem; color: var(--muted); line-height: 1.8;">
            <strong style="color: rgba(232,232,240,0.7);">Voorwaarden:</strong>
            30 dagen cookie tracking · Uitbetaling maandelijks via bankoverschrijving · Minimum €25 · Geldig voor Nederlandse klanten
          </div>
        </div>

      </div>
    </section>'''


def api_content():
    return '''    <section style="padding: 48px 0 64px;">
      <div class="container">
        <div class="text-center" style="max-width: 640px; margin: 0 auto;">
          <span class="section-label">Developers</span>
          <h1 class="section-heading">Scorio API</h1>
          <div style="display: inline-flex; align-items: center; gap: 10px; padding: 10px 20px; background: rgba(245,158,11,0.12); border: 1px solid rgba(245,158,11,0.3); border-radius: 100px; margin-bottom: 24px;">
            <span style="width: 8px; height: 8px; background: #f59e0b; border-radius: 50; display: inline-block;"></span>
            <span style="font-size: 0.85rem; color: #f59e0b; font-weight: 600;">🔧 Binnenkort beschikbaar</span>
          </div>
          <p class="section-sub">De Scorio API stelt ontwikkelaars in staat om SEO scans te integreren in hun eigen applicaties, dashboards of workflows.</p>
        </div>
      </div>
    </section>

    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">

        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; margin-bottom: 80px;">
          <div class="glass-card" style="padding: 28px;">
            <span style="font-size: 1.8rem; display: block; margin-bottom: 12px;" aria-hidden="true">🔍</span>
            <h3 style="margin-bottom: 10px;">Website scans via API</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">Start een SEO scan met een simpele API call. Krijg de resultaten terug als gestructureerd JSON.</p>
          </div>
          <div class="glass-card" style="padding: 28px;">
            <span style="font-size: 1.8rem; display: block; margin-bottom: 12px;" aria-hidden="true">📊</span>
            <h3 style="margin-bottom: 10px;">Rapporten als JSON</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">Haal scan rapporten op als gestructureerde JSON data. Verwerk ze in jouw eigen dashboard of tool.</p>
          </div>
          <div class="glass-card" style="padding: 28px;">
            <span style="font-size: 1.8rem; display: block; margin-bottom: 12px;" aria-hidden="true">⚡</span>
            <h3 style="margin-bottom: 10px;">Bulk scans</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">Scan meerdere websites tegelijk. Ideaal voor bureaus en hosting providers met meerdere klanten.</p>
          </div>
          <div class="glass-card" style="padding: 28px;">
            <span style="font-size: 1.8rem; display: block; margin-bottom: 12px;" aria-hidden="true">🔔</span>
            <h3 style="margin-bottom: 10px;">Webhooks</h3>
            <p style="font-size: 0.875rem; color: var(--muted); line-height: 1.6;">Ontvang automatische notificaties wanneer een scan klaar is. Geen polling nodig.</p>
          </div>
        </div>

        <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 20px; padding: 28px; margin-bottom: 80px; font-family: monospace; font-size: 0.85rem; color: var(--accent); overflow-x: auto;">
          <div style="color: var(--muted); margin-bottom: 12px;"># Voorbeeld API call (binnenkort beschikbaar)</div>
          <div style="color: rgba(232,232,240,0.9);">POST https://api.scorio.nl/v1/scan</div>
          <div style="color: rgba(232,232,240,0.6); margin-top: 8px;">{</div>
          <div style="color: rgba(232,232,240,0.6); padding-left: 20px;">"url": "https://jouwwebsite.nl",</div>
          <div style="color: rgba(232,232,240,0.6); padding-left: 20px;">"api_key": "sk_live_..."</div>
          <div style="color: rgba(232,232,240,0.6);">}</div>
        </div>

        <div class="glass-card" style="padding: 48px; max-width: 560px; margin: 0 auto; background: linear-gradient(135deg, rgba(91,79,232,0.12), rgba(0,200,150,0.06));">
          <h2 style="font-size: 1.2rem; margin-bottom: 8px; text-align: center;">Meld je aan voor vroege toegang</h2>
          <p style="font-size: 0.875rem; color: var(--muted); text-align: center; margin-bottom: 28px;">We informeren je als eerste wanneer de API beschikbaar is.</p>
          <form action="mailto:api@scorio.nl" method="POST" enctype="text/plain" style="display: flex; flex-direction: column; gap: 16px;">
            <input type="text" name="naam" required placeholder="Jouw naam" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
            <input type="email" name="email" required placeholder="jouw@email.nl" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
            <input type="text" name="bedrijf" placeholder="Bedrijfsnaam (optioneel)" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box;" />
            <textarea name="usecase" rows="3" placeholder="Hoe wil je de API gebruiken?" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.06); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-family: var(--font-body); font-size: 0.9rem; outline: none; box-sizing: border-box; resize: vertical;"></textarea>
            <button type="submit" class="btn btn-accent" style="width: 100%;">Aanmelden voor vroege toegang →</button>
          </form>
        </div>

      </div>
    </section>'''


def not_found_page():
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pagina niet gevonden | Scorio.nl</title>
  <meta name="robots" content="noindex" />
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='%235B4FE8'/><text x='16' y='22' text-anchor='middle' font-size='16' font-weight='900' fill='white' font-family='sans-serif'>S</text></svg>" />
</head>
<body>
{COOKIE_BANNER}
{HEADER()}
  <main>
    <section style="padding: 80px 0 var(--section-gap); text-align: center;">
      <div class="container">
        <div style="max-width: 540px; margin: 0 auto;">
          <div style="font-size: 7rem; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 24px;">404</div>
          <h1 style="font-size: clamp(1.5rem, 3vw, 2rem); margin-bottom: 16px;">Deze pagina bestaat niet</h1>
          <p style="color: rgba(232,232,240,0.7); line-height: 1.7; margin-bottom: 40px;">De pagina die je zoekt is verplaatst of bestaat niet meer. Misschien is er een typefout in de URL?</p>

          <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; margin-bottom: 56px;">
            <a href="/" class="btn btn-accent btn-lg">Terug naar homepage →</a>
            <a href="/#hero-form" class="btn btn-ghost btn-lg">Gratis scan doen</a>
          </div>

          <div class="glass-card" style="padding: 32px; text-align: left;">
            <p style="font-size: 0.875rem; font-weight: 600; color: var(--muted); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.06em;">Misschien zoek je dit:</p>
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <a href="/prijzen.html" style="color: rgba(232,232,240,0.85); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: var(--primary-light);">→</span> Prijzen</a>
              <a href="/blog/" style="color: rgba(232,232,240,0.85); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: var(--primary-light);">→</span> Blog — SEO tips voor Nederlandse ondernemers</a>
              <a href="/contact/" style="color: rgba(232,232,240,0.85); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: var(--primary-light);">→</span> Contact</a>
              <a href="/hoe-het-werkt.html" style="color: rgba(232,232,240,0.85); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: var(--primary-light);">→</span> Hoe het werkt</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
{NEW_FOOTER}
  <script src="/js/main.js"></script>
</body>
</html>'''


# ─────────────────────────────────────────────────────────────
# COOKIE BANNER CSS (append to style.css)
# ─────────────────────────────────────────────────────────────
COOKIE_CSS = """

/* ============================================================
   Cookie Banner
   ============================================================ */
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #16162A;
  border-top: 1px solid rgba(255,255,255,0.1);
  z-index: 9000;
  padding: 16px 24px;
  box-shadow: 0 -4px 24px rgba(0,0,0,0.4);
}
.cookie-banner-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}
.cookie-text {
  font-size: 0.875rem;
  color: rgba(136,136,170,1);
  margin: 0;
  line-height: 1.6;
}
.cookie-link {
  color: #7B72FF;
  text-decoration: underline;
}
.cookie-actions {
  display: flex;
  gap: 10px;
  flex-shrink: 0;
}
@media (max-width: 600px) {
  .cookie-banner-inner { flex-direction: column; align-items: flex-start; }
}
"""


# ─────────────────────────────────────────────────────────────
# SITEMAP UPDATE
# ─────────────────────────────────────────────────────────────
NEW_SITEMAP_ENTRIES = """
  <!-- Bedrijfspagina's -->
  <url>
    <loc>https://www.scorio.nl/over-ons/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/over-ons/"/>
  </url>
  <url>
    <loc>https://www.scorio.nl/contact/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/contact/"/>
  </url>
  <url>
    <loc>https://www.scorio.nl/affiliate/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/affiliate/"/>
  </url>
  <url>
    <loc>https://www.scorio.nl/api/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/api/"/>
  </url>

  <!-- Legal pagina's -->
  <url>
    <loc>https://www.scorio.nl/privacy/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/privacy/"/>
  </url>
  <url>
    <loc>https://www.scorio.nl/voorwaarden/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/voorwaarden/"/>
  </url>
  <url>
    <loc>https://www.scorio.nl/cookies/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/cookies/"/>
  </url>
  <url>
    <loc>https://www.scorio.nl/avg/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/avg/"/>
  </url>
"""


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    # 1. Patch all existing HTML files
    patch_all_existing()

    # 2. Add cookie banner CSS to style.css
    css_path = os.path.join(BASE, 'css', 'style.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    if '.cookie-banner' not in css:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(COOKIE_CSS)
        print('✓ Cookie CSS added to style.css')

    # 3. Create new pages
    pages = [
        ('privacy', 'Privacybeleid | Scorio.nl',
         'Lees het privacybeleid van Scorio.nl. Hoe we omgaan met jouw persoonsgegevens, welke gegevens we verzamelen en jouw AVG-rechten.',
         '/privacy/',
         [('Home', '/'), ('Privacybeleid', '')],
         privacy_content()),
        ('voorwaarden', 'Algemene Voorwaarden | Scorio.nl',
         'De algemene voorwaarden van Scorio.nl. Van toepassing op alle gebruik van onze SEO scan dienst.',
         '/voorwaarden/',
         [('Home', '/'), ('Algemene Voorwaarden', '')],
         voorwaarden_content()),
        ('cookies', 'Cookiebeleid | Scorio.nl',
         'Ons cookiebeleid: welke cookies Scorio.nl gebruikt, waarvoor en hoe je je voorkeuren kunt beheren.',
         '/cookies/',
         [('Home', '/'), ('Cookiebeleid', '')],
         cookies_content()),
        ('avg', 'AVG & GDPR Compliance | Scorio.nl',
         'Hoe Scorio.nl voldoet aan de AVG/GDPR. Overzicht van onze privacymaatregelen, sub-processors en jouw rechten.',
         '/avg/',
         [('Home', '/'), ('AVG & GDPR', '')],
         avg_content()),
        ('over-ons', 'Over Scorio.nl | De Nederlandse SEO Tool',
         'Leer meer over Scorio.nl — de SEO scan tool gebouwd voor het Nederlandse MKB. Ons verhaal, missie en het team.',
         '/over-ons/',
         [('Home', '/'), ('Over ons', '')],
         over_ons_content()),
        ('contact', 'Contact | Scorio.nl',
         'Neem contact op met Scorio.nl. Stuur een bericht via ons contactformulier of mail direct naar info@scorio.nl.',
         '/contact/',
         [('Home', '/'), ('Contact', '')],
         contact_content()),
        ('affiliate', 'Affiliate Programma | Scorio.nl',
         'Verdien 30% recurring commissie als Scorio affiliate. Verwijs ondernemers en verdien elke maand zolang ze klant zijn.',
         '/affiliate/',
         [('Home', '/'), ('Affiliate programma', '')],
         affiliate_content()),
        ('api', 'API | Scorio.nl',
         'De Scorio API — integreer SEO scans in je eigen applicatie. Meld je aan voor vroege toegang.',
         '/api/',
         [('Home', '/'), ('API', '')],
         api_content()),
    ]

    for slug, title, meta_desc, canonical_path, crumbs, content in pages:
        dir_path = os.path.join(BASE, slug)
        os.makedirs(dir_path, exist_ok=True)
        html = full_page(title, meta_desc, canonical_path, crumbs, content)
        out = os.path.join(dir_path, 'index.html')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ Created: {out}')

    # 4. Create 404.html
    out404 = os.path.join(BASE, '404.html')
    with open(out404, 'w', encoding='utf-8') as f:
        f.write(not_found_page())
    print(f'✓ Created: {out404}')

    # 5. Update sitemap.xml
    sitemap_path = os.path.join(BASE, 'sitemap.xml')
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    if '/over-ons/' not in sitemap:
        sitemap = sitemap.replace('\n</urlset>', NEW_SITEMAP_ENTRIES + '\n</urlset>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap)
        print('✓ sitemap.xml updated')

    # 6. Update vercel.json (add 404 routing, keep existing headers)
    vercel_path = os.path.join(BASE, 'vercel.json')
    with open(vercel_path, 'r', encoding='utf-8') as f:
        import json
        vercel = json.load(f)

    if 'routes' not in vercel:
        vercel['routes'] = [
            {"handle": "filesystem"},
            {"src": "/(.*)", "dest": "/404.html", "status": 404}
        ]
        with open(vercel_path, 'w', encoding='utf-8') as f:
            json.dump(vercel, f, indent=2)
            f.write('\n')
        print('✓ vercel.json updated with 404 routing')

    print('\n✅ All done!')


if __name__ == '__main__':
    main()
