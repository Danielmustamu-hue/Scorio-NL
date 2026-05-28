#!/usr/bin/env python3
"""Generate 10 city landing pages for Scorio.nl."""
import os

CITIES = {
    'amsterdam': {
        'name': 'Amsterdam',
        'inwoners': '900.000+',
        'bedrijven': '130.000+',
        'zoekvolume_hint': 'drukste stad van Nederland',
        'lokale_tip': 'In Amsterdam is de online concurrentie enorm. Zonder goede SEO ben je onzichtbaar tussen duizenden bedrijven.',
        'branches': 'horeca, retail, creatieve sector en tech',
        'branches_voorbeelden': 'horecagelegenheid, modewinkel, creatief bureau of tech-startup',
        'review1_tekst': 'Als Amsterdamse fotograaf dacht ik dat mijn website goed was. Scorio liet zien dat ik 12 kritieke fouten had. Nu sta ik bovenaan voor "fotograaf amsterdam".',
        'review1_naam': 'Lisa van den Berg',
        'review1_bedrijf': 'Fotostudio Amsterdam',
        'review2_tekst': 'Mijn restaurant stond op pagina 3 van Google. Na de Scorio scan wist ik precies wat ik moest aanpakken. Nu sta ik in de top 3 in Amsterdam.',
        'review2_naam': 'Marco de Vries',
        'review2_bedrijf': 'Restaurant De Pijp, Amsterdam',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn boetiek staat nu bovenaan in Amsterdam-West.',
        'review3_naam': 'Nadia Khalil',
        'review3_bedrijf': 'Modeboetiek Amsterdam',
    },
    'rotterdam': {
        'name': 'Rotterdam',
        'inwoners': '650.000+',
        'bedrijven': '85.000+',
        'zoekvolume_hint': 'grootste havenstad van Europa',
        'lokale_tip': 'Rotterdam groeit snel digitaal. Lokale ondernemers die nu investeren in SEO pakken een grote voorsprong op de rest.',
        'branches': 'haven, logistiek, bouw en horeca',
        'branches_voorbeelden': 'transportbedrijf, bouwbedrijf, horecagelegenheid of logistiek dienstverlener',
        'review1_tekst': 'Ons transportbedrijf werd nauwelijks gevonden online. Na de Scorio scan en de verbeteringen kregen we 3x meer aanvragen via Google.',
        'review1_naam': 'Peter Smits',
        'review1_bedrijf': 'Smits Transport Rotterdam',
        'review2_tekst': 'Als aannemer in Rotterdam wist ik niet waar ik moest beginnen met SEO. Scorio gaf me een concrete actielijst. Binnen 3 maanden zit mijn agenda vol.',
        'review2_naam': 'Joost van der Berg',
        'review2_bedrijf': 'Van der Berg Aanneming Rotterdam',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn koffiebar staat nu bovenaan in Rotterdam-Zuid.',
        'review3_naam': 'Fatima Osman',
        'review3_bedrijf': 'Koffiebar Rotterdam',
    },
    'utrecht': {
        'name': 'Utrecht',
        'inwoners': '370.000+',
        'bedrijven': '60.000+',
        'zoekvolume_hint': 'centraal gelegen studentenstad',
        'lokale_tip': 'Utrecht heeft een jonge, digitaal vaardige bevolking. Ze zoeken alles online — ben jij zichtbaar wanneer zij naar jou zoeken?',
        'branches': 'zorg, onderwijs, tech en horeca',
        'branches_voorbeelden': 'kapsalon, tandartspraktijk, IT-bedrijf of restaurant',
        'review1_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn kapsalon staat nu bovenaan in Utrecht.',
        'review1_naam': 'Sandra Hoekstra',
        'review1_bedrijf': 'Kapsalon Utrecht',
        'review2_tekst': 'Als huisartsenpraktijk in Utrecht wilde ik beter gevonden worden. Dankzij Scorio weten we nu precies wat we moeten doen. Nieuw patiënten melden zich nu online aan.',
        'review2_naam': 'Dr. Erik Willems',
        'review2_bedrijf': 'Huisartsenpraktijk Utrecht-Oost',
        'review3_tekst': 'Mijn IT-bedrijf stond nergens in Google. Na de Scorio scan en drie maanden werken aan de aanbevelingen staan we nu op pagina 1 voor onze belangrijkste zoektermen.',
        'review3_naam': 'Thomas van Dijk',
        'review3_bedrijf': 'Van Dijk IT-consultancy Utrecht',
    },
    'den-haag': {
        'name': 'Den Haag',
        'inwoners': '550.000+',
        'bedrijven': '70.000+',
        'zoekvolume_hint': 'regeringsstad en internationale zone',
        'lokale_tip': 'Den Haag combineert internationale bedrijven met lokaal MKB. Lokale SEO is hier cruciaal om op te vallen in een competitieve markt.',
        'branches': 'overheid, juridisch, zakelijke diensten en horeca',
        'branches_voorbeelden': 'advocatenkantoor, accountantskantoor, zakelijk dienstverlener of horecagelegenheid',
        'review1_tekst': 'Als advocatenkantoor in Den Haag was online vindbaarheid essentieel. Scorio liet zien dat onze website tientallen technische fouten had. Nu staan we bovenaan.',
        'review1_naam': 'Mr. Ingrid van Leeuwen',
        'review1_bedrijf': 'Van Leeuwen Advocaten Den Haag',
        'review2_tekst': 'Ons accountantskantoor werd amper gevonden. Na de Scorio scan en gerichte verbeteringen kregen we binnen 2 maanden 40% meer website-aanvragen.',
        'review2_naam': 'Pieter Donkers',
        'review2_bedrijf': 'Donkers Accountants Den Haag',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn restaurant staat nu bovenaan in het Haagse centrum.',
        'review3_naam': 'Amira El-Hassan',
        'review3_bedrijf': 'Restaurant Den Haag Centrum',
    },
    'eindhoven': {
        'name': 'Eindhoven',
        'inwoners': '240.000+',
        'bedrijven': '35.000+',
        'zoekvolume_hint': 'technologiehoofdstad van Nederland',
        'lokale_tip': 'Eindhoven is de tech- en designhoofdstad van Nederland. Online zichtbaarheid is hier geen luxe maar een absolute noodzaak om te groeien.',
        'branches': 'tech, design, industrie en retail',
        'branches_voorbeelden': 'tech-startup, designbureau, industrieel bedrijf of retailzaak',
        'review1_tekst': 'Als designbureau in Eindhoven moesten we beter vindbaar zijn. Scorio liet zien waar we stonden. Nu genereren we dagelijks leads via Google.',
        'review1_naam': 'Bas Verhagen',
        'review1_bedrijf': 'Studio Verhagen Design Eindhoven',
        'review2_tekst': 'Ons tech-bedrijf was amper zichtbaar online. Na de Scorio scan en de verbeteringen staan we nu bovenaan voor onze belangrijkste zoekwoorden in Eindhoven.',
        'review2_naam': 'Kevin Martens',
        'review2_bedrijf': 'Martens Software Eindhoven',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn winkel staat nu bovenaan in Eindhoven voor onze niche.',
        'review3_naam': 'Loes de Bruijn',
        'review3_bedrijf': 'Designwinkel Eindhoven',
    },
    'groningen': {
        'name': 'Groningen',
        'inwoners': '230.000+',
        'bedrijven': '28.000+',
        'zoekvolume_hint': 'bruisende Noord-Nederlandse stad',
        'lokale_tip': 'Groningen heeft een actieve lokale economie. Veel zoekopdrachten komen van studenten en bewoners die diensten zoeken vlak in de buurt.',
        'branches': 'horeca, zorg, onderwijs en retail',
        'branches_voorbeelden': 'cafetaria, huisartsenpraktijk, studiecoach of winkel',
        'review1_tekst': 'Mijn cafetaria in Groningen werd nauwelijks gevonden online. Na de Scorio scan en verbeteringen staan we nu in de top 3 van Google voor onze buurt.',
        'review1_naam': 'Henk Bosman',
        'review1_bedrijf': 'Cafetaria Bosman Groningen',
        'review2_tekst': 'Als fysiotherapiepraktijk in Groningen wilde ik beter gevonden worden door mensen in de buurt. Scorio gaf me precies de inzichten die ik nodig had.',
        'review2_naam': 'Marieke Brouwer',
        'review2_bedrijf': 'FysioPraktijk Groningen-Noord',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn winkel staat nu bovenaan in Groningen.',
        'review3_naam': 'Sanne Tiemersma',
        'review3_bedrijf': 'Boekwinkel Groningen',
    },
    'tilburg': {
        'name': 'Tilburg',
        'inwoners': '220.000+',
        'bedrijven': '30.000+',
        'zoekvolume_hint': 'groeiende Brabantse stad',
        'lokale_tip': 'Tilburg groeit snel en de lokale ondernemersmarkt is competitief. Wie nu goed scoort in Google pakt een blijvende voorsprong op de concurrentie.',
        'branches': 'textiel, zorg, retail en bouw',
        'branches_voorbeelden': 'bouwbedrijf, kledingwinkel, zorgpraktijk of modeonderneming',
        'review1_tekst': 'Ons bouwbedrijf in Tilburg stond nergens in Google. Na de Scorio scan wisten we precies wat we moesten aanpakken. Nu komen aanvragen vanzelf binnen.',
        'review1_naam': 'Rob Peeters',
        'review1_bedrijf': 'Peeters Bouw Tilburg',
        'review2_tekst': 'Mijn kledingwinkel in Tilburg had veel concurrentie online. Dankzij Scorio ontdekte ik 15 verbeterpunten. Nu staan we bovenaan voor lokale zoekwoorden.',
        'review2_naam': 'Vivienne Claes',
        'review2_bedrijf': 'Modezaak Claes Tilburg',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn praktijk staat nu bovenaan in Tilburg.',
        'review3_naam': 'Drs. Annemarie Loos',
        'review3_bedrijf': 'Psychologenpraktijk Tilburg',
    },
    'almere': {
        'name': 'Almere',
        'inwoners': '215.000+',
        'bedrijven': '25.000+',
        'zoekvolume_hint': 'jongste grote stad van Nederland',
        'lokale_tip': 'Almere is een van de snelst groeiende steden van Nederland. Veel nieuwe bedrijven — maar weinig hebben hun SEO op orde. Jouw kans om op te vallen.',
        'branches': 'retail, bouw, zorg en zakelijke diensten',
        'branches_voorbeelden': 'bouwbedrijf, retailwinkel, zorgpraktijk of zakelijke dienstverlener',
        'review1_tekst': 'Mijn bouwbedrijf in Almere groeide snel maar we werden online amper gevonden. Na Scorio staan we nu in de top 3 van Google voor "aannemer Almere".',
        'review1_naam': 'Gerard Visser',
        'review1_bedrijf': 'Visser Bouw & Renovatie Almere',
        'review2_tekst': 'Als nieuwe ondernemer in Almere was online zichtbaarheid essentieel. Scorio gaf me de inzichten om snel te groeien — nu heb ik een volle agenda.',
        'review2_naam': 'Patricia Nguyen',
        'review2_bedrijf': 'Schoonheidssalon Almere',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn winkel staat nu bovenaan in Almere.',
        'review3_naam': 'Daan Mulder',
        'review3_bedrijf': 'Sportwinkel Almere',
    },
    'breda': {
        'name': 'Breda',
        'inwoners': '185.000+',
        'bedrijven': '28.000+',
        'zoekvolume_hint': 'strategisch gelegen Brabantse stad',
        'lokale_tip': 'Breda ligt centraal tussen Rotterdam, Antwerpen en Eindhoven. Goede lokale zichtbaarheid trekt klanten aan uit de hele regio.',
        'branches': 'logistiek, retail, horeca en zorg',
        'branches_voorbeelden': 'logistiek dienstverlener, retailzaak, restaurant of zorgpraktijk',
        'review1_tekst': 'Ons logistiek bedrijf in Breda werd niet gevonden via Google. Na de Scorio scan en de verbeteringen staan we nu bovenaan voor regionale zoekopdrachten.',
        'review1_naam': 'Arjan Verhoeven',
        'review1_bedrijf': 'Verhoeven Logistics Breda',
        'review2_tekst': 'Mijn restaurant in Breda had weinig online bezoekers. Scorio liet me zien wat er ontbrak. Nu staan we in de top 3 voor "restaurant breda centrum".',
        'review2_naam': 'Stephanie Janssen',
        'review2_bedrijf': 'Bistro Janssen Breda',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn praktijk staat nu bovenaan in Breda.',
        'review3_naam': 'Hanneke Schilders',
        'review3_bedrijf': 'Fysiotherapie Schilders Breda',
    },
    'nijmegen': {
        'name': 'Nijmegen',
        'inwoners': '180.000+',
        'bedrijven': '22.000+',
        'zoekvolume_hint': 'oudste stad van Nederland',
        'lokale_tip': 'Nijmegen heeft een sterke lokale economie met veel ZZP\'ers en MKB. Online concurrentie groeit snel — wees er vroeg bij en pak de topposities.',
        'branches': 'zorg, onderwijs, tech en horeca',
        'branches_voorbeelden': 'zorgpraktijk, tutorbedrijf, IT-dienstverlener of horecagelegenheid',
        'review1_tekst': 'Mijn zorgpraktijk in Nijmegen was amper zichtbaar online. Na de Scorio scan en 8 weken werken aan de verbeteringen komen nieuwe patiënten nu via Google.',
        'review1_naam': 'Dr. Judith van Rooij',
        'review1_bedrijf': 'Psychologenpraktijk Nijmegen',
        'review2_tekst': 'Als IT-bedrijf in Nijmegen hadden we een website die er goed uitzag maar slecht scoorde. Scorio gaf ons de inzichten. Nu genereren we structureel leads via SEO.',
        'review2_naam': 'Bart Hendriksen',
        'review2_bedrijf': 'Hendriksen IT Nijmegen',
        'review3_tekst': 'Ik dacht dat SEO alleen voor grote bedrijven was. Scorio bewees het tegendeel. Mijn eetcafé staat nu bovenaan in Nijmegen.',
        'review3_naam': 'Wouter Coppens',
        'review3_bedrijf': 'Eetcafé Coppens Nijmegen',
    },
}

ALL_CITIES = [
    ('amsterdam', 'Amsterdam'),
    ('rotterdam', 'Rotterdam'),
    ('utrecht', 'Utrecht'),
    ('den-haag', 'Den Haag'),
    ('eindhoven', 'Eindhoven'),
    ('groningen', 'Groningen'),
    ('tilburg', 'Tilburg'),
    ('almere', 'Almere'),
    ('breda', 'Breda'),
    ('nijmegen', 'Nijmegen'),
]


def other_cities_links(current_slug):
    items = []
    for slug, name in ALL_CITIES:
        if slug != current_slug:
            items.append(f'<a href="/seo-check-{slug}/" class="city-link">{name}</a>')
    return '\n            '.join(items)


def generate_page(slug, d):
    stad = d['name']
    other_links = other_cities_links(slug)

    # Build FAQ schema
    faq_schema = f"""[
          {{
            "@type": "Question",
            "name": "Hoe kom ik bovenaan in Google in {stad}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Combineer technische SEO, lokale zoekwoorden ({stad} + jouw dienst) en een volledig Google Bedrijfsprofiel. Scorio laat zien wat bij jou als eerste aandacht nodig heeft."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Wat kost een SEO specialist in {stad}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "SEO bureaus in {stad} rekenen gemiddeld €500 tot €2000 per maand. Met Scorio doe je de analyse zelf voor €9 per maand en weet je precies wat je moet aanpakken."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Hoe lang duurt SEO in {stad}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Technische verbeteringen zie je binnen 2–4 weken terug. Voor betere rankings in {stad} reken je op 3 tot 6 maanden bij consistente inzet."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Werkt Scorio ook voor lokale bedrijven in {stad}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Absoluut. Scorio is speciaal gebouwd voor Nederlandse MKB’ers en ZZP’ers. We analyseren ook je lokale vindbaarheid in {stad} en geven concrete, uitvoerbare tips."
            }}
          }}
        ]"""

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Gratis SEO Check {stad} | Website Score Check | Scorio.nl</title>
  <meta name="description" content="Gratis SEO scan voor ondernemers in {stad}. Ontdek in 60 seconden hoe jouw website scoort en wat je kunt verbeteren. Download je PDF rapport. Geen registratie nodig." />
  <link rel="canonical" href="https://www.scorio.nl/seo-check-{slug}/" />
  <link rel="alternate" hreflang="nl" href="https://www.scorio.nl/seo-check-{slug}/" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Gratis SEO Check {stad} | Scorio.nl" />
  <meta property="og:description" content="Gratis SEO scan voor ondernemers in {stad}. Ontdek in 60 seconden hoe jouw website scoort en wat je kunt verbeteren." />
  <meta property="og:url" content="https://www.scorio.nl/seo-check-{slug}/" />
  <meta property="og:site_name" content="Scorio.nl" />
  <meta property="og:locale" content="nl_NL" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Gratis SEO Check {stad} | Scorio.nl" />
  <meta name="twitter:description" content="Gratis SEO scan voor ondernemers in {stad}. Resultaat in 60 seconden. Geen registratie." />

  <!-- Schema Markup -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebPage",
        "@id": "https://www.scorio.nl/seo-check-{slug}/#webpage",
        "name": "Gratis SEO Check {stad} | Scorio.nl",
        "description": "Gratis SEO scan voor ondernemers in {stad}. Ontdek in 60 seconden hoe jouw website scoort.",
        "url": "https://www.scorio.nl/seo-check-{slug}/",
        "inLanguage": "nl",
        "isPartOf": {{"@id": "https://www.scorio.nl/#website"}},
        "breadcrumb": {{"@id": "https://www.scorio.nl/seo-check-{slug}/#breadcrumb"}}
      }},
      {{
        "@type": "BreadcrumbList",
        "@id": "https://www.scorio.nl/seo-check-{slug}/#breadcrumb",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.scorio.nl/"}},
          {{"@type": "ListItem", "position": 2, "name": "SEO Check {stad}", "item": "https://www.scorio.nl/seo-check-{slug}/"}}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": {faq_schema}
      }},
      {{
        "@type": "WebSite",
        "@id": "https://www.scorio.nl/#website",
        "name": "Scorio.nl",
        "url": "https://www.scorio.nl",
        "description": "De #1 gratis SEO scan tool voor Nederlandse MKB-ondernemers.",
        "inLanguage": "nl"
      }}
    ]
  }}
  </script>

  <link rel="stylesheet" href="/css/style.css" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='%235B4FE8'/><text x='16' y='22' text-anchor='middle' font-size='16' font-weight='900' fill='white' font-family='sans-serif'>S</text></svg>" />
  <style>
    /* City page specific styles */
    .city-stats {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin: 48px 0;
    }}
    @media (max-width: 768px) {{
      .city-stats {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    .city-stat-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      text-align: center;
    }}
    .city-stat-num {{
      display: block;
      font-size: 1.8rem;
      font-weight: 900;
      color: var(--primary-light);
      line-height: 1;
      margin-bottom: 8px;
    }}
    .city-stat-lbl {{
      font-size: 0.8rem;
      color: var(--muted);
      line-height: 1.4;
    }}
    .urgency-visual {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin: 32px 0;
    }}
    .urgency-row {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 16px 20px;
      border-radius: 12px;
      font-size: 0.9rem;
    }}
    .urgency-row.bad {{ background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.2); }}
    .urgency-row.medium {{ background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.2); }}
    .urgency-row.good {{ background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.2); }}
    .urgency-dot {{ width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }}
    .urgency-dot.red {{ background: #ef4444; }}
    .urgency-dot.yellow {{ background: #f59e0b; }}
    .urgency-dot.green {{ background: #10b981; }}
    .urgency-label {{ font-weight: 700; min-width: 100px; }}
    .how-steps {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }}
    @media (max-width: 768px) {{
      .how-steps {{ grid-template-columns: 1fr; }}
    }}
    .how-step {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 32px 24px;
      text-align: center;
    }}
    .how-step-num {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--primary);
      color: #fff;
      font-weight: 900;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 20px;
    }}
    .how-step-icon {{
      font-size: 2rem;
      margin-bottom: 16px;
      display: block;
    }}
    .how-step h3 {{
      font-size: 1rem;
      margin-bottom: 8px;
    }}
    .how-step p {{
      font-size: 0.85rem;
      color: var(--muted);
      line-height: 1.6;
      margin: 0;
    }}
    .check-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 48px;
    }}
    @media (max-width: 768px) {{
      .check-grid {{ grid-template-columns: 1fr; }}
    }}
    @media (min-width: 769px) and (max-width: 1024px) {{
      .check-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    .check-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
    }}
    .check-card-icon {{
      font-size: 1.8rem;
      margin-bottom: 12px;
      display: block;
    }}
    .check-card h3 {{
      font-size: 0.95rem;
      margin-bottom: 8px;
    }}
    .check-card p {{
      font-size: 0.82rem;
      color: var(--muted);
      line-height: 1.6;
      margin: 0;
    }}
    .reviews-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }}
    @media (max-width: 900px) {{
      .reviews-grid {{ grid-template-columns: 1fr; }}
    }}
    .review-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 28px;
    }}
    .review-stars {{
      color: #f59e0b;
      font-size: 0.9rem;
      margin-bottom: 16px;
    }}
    .review-text {{
      font-size: 0.875rem;
      line-height: 1.7;
      color: rgba(232,232,240,0.85);
      margin-bottom: 20px;
    }}
    .review-author {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .review-avatar {{
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.8rem;
      color: #fff;
      flex-shrink: 0;
    }}
    .review-name {{
      font-weight: 700;
      font-size: 0.875rem;
    }}
    .review-company {{
      font-size: 0.775rem;
      color: var(--muted);
    }}
    .city-other-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 20px;
    }}
    .city-link {{
      padding: 8px 16px;
      border-radius: 100px;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border);
      color: var(--muted);
      text-decoration: none;
      font-size: 0.825rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .city-link:hover {{
      background: rgba(91,79,232,0.15);
      border-color: var(--primary);
      color: var(--primary-light);
    }}
    /* Scan modal */
    .scan-modal-overlay {{
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.7);
      backdrop-filter: blur(8px);
      display: flex; align-items: center; justify-content: center;
      z-index: 9999;
      opacity: 0; pointer-events: none;
      transition: opacity 0.3s;
    }}
    .scan-modal-overlay.active {{ opacity: 1; pointer-events: all; }}
    .scan-modal {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 48px;
      max-width: 480px;
      width: 90%;
      text-align: center;
    }}
    .scan-modal-spinner {{
      width: 64px; height: 64px;
      border: 4px solid var(--border);
      border-top-color: var(--primary);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      margin: 0 auto 24px;
    }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    .scan-modal-url {{
      color: var(--primary-light);
      font-weight: 700;
      word-break: break-all;
    }}
    .scan-progress {{
      height: 6px;
      background: rgba(255,255,255,0.08);
      border-radius: 100px;
      margin-top: 24px;
      overflow: hidden;
    }}
    .scan-progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--accent));
      border-radius: 100px;
      width: 0%;
      transition: width 0.3s ease;
    }}
  </style>
</head>
<body>

  <!-- Scan Modal -->
  <div class="scan-modal-overlay" role="dialog" aria-modal="true" aria-label="Website wordt gescand">
    <div class="scan-modal">
      <div class="scan-modal-spinner" aria-hidden="true"></div>
      <h2 style="font-size: 1.2rem; margin-bottom: 8px;">Jouw website wordt gescand...</h2>
      <p style="font-size: 0.875rem; color: var(--muted);">We analyseren <span class="scan-modal-url"></span></p>
      <div class="scan-progress">
        <div class="scan-progress-fill"></div>
      </div>
      <p style="font-size: 0.775rem; color: var(--muted); margin-top: 12px;">45+ SEO factoren worden gecontroleerd</p>
    </div>
  </div>

  <header class="site-header" id="top">
    <div class="container">
      <div class="header-inner">
        <a href="/" class="logo">Scorio<span class="logo-dot"></span></a>
        <nav class="nav-links" role="navigation" aria-label="Hoofdmenu">
          <a href="/hoe-het-werkt.html">Hoe het werkt</a>
          <a href="/prijzen.html">Prijzen</a>
          <a href="/blog/">Blog</a>
        </nav>
        <div class="header-actions">
          <a href="#" class="btn btn-ghost btn-sm">Inloggen</a>
          <a href="#hero-form" class="btn btn-accent btn-sm">Gratis scannen</a>
        </div>
        <button class="mobile-menu-btn" aria-label="Menu openen">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <button class="mobile-close-btn" aria-label="Menu sluiten">✕</button>
  </header>

  <!-- Breadcrumb -->
  <nav class="breadcrumb" aria-label="Broodkruimelpad">
    <div class="container">
      <ol class="breadcrumb-list">
        <li><a href="/">Home</a></li>
        <li><span class="breadcrumb-sep" aria-hidden="true">/</span></li>
        <li aria-current="page">SEO Check {stad}</li>
      </ol>
    </div>
  </nav>

  <main>

    <!-- ============================================================
         HERO
    ============================================================ -->
    <section class="hero" id="hero-form">
      <div class="container">
        <div class="hero-inner">

          <!-- Left: copy + form -->
          <div class="hero-content">
            <div class="hero-badge fade-up">
              <span aria-hidden="true">📍</span> SEO Check {stad}
            </div>

            <h1 class="hero-heading fade-up stagger-1">
              Hoe goed is jouw website<br />
              zichtbaar in <span class="hero-gradient">{stad}</span>?
            </h1>

            <p class="hero-sub fade-up stagger-2">
              In {stad} zijn er <strong>{d['bedrijven']}</strong> actieve bedrijven. Hoeveel van hen worden gevonden als mensen online zoeken? Doe de gratis scan en ontdek waar jij staat.
            </p>

            <form class="hero-form scan-form fade-up stagger-3" novalidate id="scan-form-hero">
              <div class="hero-input-wrap">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418" />
                </svg>
                <input
                  type="url"
                  class="hero-input"
                  placeholder="https://jouwbedrijf{slug.replace('-', '')}.nl"
                  aria-label="URL van jouw website"
                  autocomplete="url"
                  spellcheck="false"
                />
              </div>
              <button type="submit" class="btn btn-accent btn-lg">
                Scan mijn website →
              </button>
            </form>

            <div class="hero-social-proof fade-up stagger-4">
              <div style="display:flex;gap:6px;font-size:0.85rem;color:var(--muted);flex-wrap:wrap;">
                <span style="color:var(--accent);font-weight:700;">✓</span> Gratis
                <span style="margin:0 4px;">·</span>
                <span style="color:var(--accent);font-weight:700;">✓</span> Geen registratie
                <span style="margin:0 4px;">·</span>
                <span style="color:var(--accent);font-weight:700;">✓</span> Resultaat in 60 seconden
              </div>
            </div>
          </div>

          <!-- Right: Score Card -->
          <div class="hero-visual">
            <div class="score-card" role="img" aria-label="Voorbeeld SEO score rapport">
              <div class="score-card-header">
                <span class="score-card-title">SEO Rapport</span>
                <span class="score-card-url">jouwbedrijf.nl</span>
              </div>

              <div class="score-ring-wrap">
                <svg class="score-svg" viewBox="0 0 200 200" aria-hidden="true">
                  <circle class="ring-track" cx="100" cy="100" r="80" />
                  <circle class="ring-progress" cx="100" cy="100" r="80" />
                </svg>
                <div class="score-center">
                  <span class="score-number" data-target="74">0</span>
                  <span class="score-label-text">Jouw Score</span>
                </div>
              </div>

              <div class="score-metrics">
                <div class="metric-row">
                  <div class="metric-icon-wrap speed" aria-hidden="true">⚡</div>
                  <div class="metric-info">
                    <div class="metric-name">Snelheid</div>
                    <div class="metric-bar"><div class="metric-fill speed"></div></div>
                  </div>
                  <span class="metric-value">87</span>
                </div>
                <div class="metric-row">
                  <div class="metric-icon-wrap seo" aria-hidden="true">🔍</div>
                  <div class="metric-info">
                    <div class="metric-name">SEO</div>
                    <div class="metric-bar"><div class="metric-fill seo"></div></div>
                  </div>
                  <span class="metric-value">64</span>
                </div>
                <div class="metric-row">
                  <div class="metric-icon-wrap mobile" aria-hidden="true">📱</div>
                  <div class="metric-info">
                    <div class="metric-name">Mobiel</div>
                    <div class="metric-bar"><div class="metric-fill mobile"></div></div>
                  </div>
                  <span class="metric-value">91</span>
                </div>
              </div>
            </div>

            <div class="score-card-float float-top">
              <span class="float-dot green"></span>
              Scan klaar! Rapport verstuurd
            </div>
            <div class="score-card-float float-bottom">
              <span class="float-dot orange"></span>
              3 verbeterpunten gevonden
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================================
         STATS BAR
    ============================================================ -->
    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">
        <div class="city-stats">
          <div class="city-stat-card fade-up">
            <span class="city-stat-num">{d['inwoners']}</span>
            <span class="city-stat-lbl">Inwoners in {stad}</span>
          </div>
          <div class="city-stat-card fade-up stagger-1">
            <span class="city-stat-num">{d['bedrijven']}</span>
            <span class="city-stat-lbl">Actieve bedrijven</span>
          </div>
          <div class="city-stat-card fade-up stagger-2">
            <span class="city-stat-num">73%</span>
            <span class="city-stat-lbl">Zoekt lokaal via Google</span>
          </div>
          <div class="city-stat-card fade-up stagger-3">
            <span class="city-stat-num">Pagina 1</span>
            <span class="city-stat-lbl">Of je bestaat niet</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         LOKALE URGENTIE
    ============================================================ -->
    <section style="padding: var(--section-gap) 0;">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;">
          <div class="fade-up">
            <span class="section-label">Lokale SEO in {stad}</span>
            <h2 class="section-heading" style="font-size:clamp(1.6rem,3vw,2.2rem);">Waarom SEO in {stad} belangrijker is dan ooit</h2>
            <p style="color:rgba(232,232,240,0.75);line-height:1.8;margin-bottom:20px;">
              {d['lokale_tip']}
            </p>
            <p style="color:rgba(232,232,240,0.75);line-height:1.8;margin-bottom:20px;">
              Elke dag zoeken mensen in {stad} naar een {d['branches_voorbeelden']}. Ze openen Google, typen hun zoekopdracht in en klikken op één van de eerste drie resultaten.
            </p>
            <p style="color:rgba(232,232,240,0.75);line-height:1.8;margin-bottom:32px;">
              Als jouw website daar niet tussen staat, besta je digitaal niet. Je concurrent pakt die klant — elke dag opnieuw. SEO is niet voor grote bedrijven met grote budgetten. Het is voor elke ondernemer in {stad} die gevonden wil worden.
            </p>
            <a href="#hero-form" class="btn btn-accent">Scan mijn website gratis →</a>
          </div>

          <div class="fade-up stagger-2">
            <div class="urgency-visual">
              <div class="urgency-row bad">
                <div class="urgency-dot red"></div>
                <span class="urgency-label">Zonder SEO</span>
                <span style="color:rgba(232,232,240,0.6);">"Pagina 5 — niemand komt daar"</span>
              </div>
              <div class="urgency-row medium">
                <div class="urgency-dot yellow"></div>
                <span class="urgency-label">Gemiddeld</span>
                <span style="color:rgba(232,232,240,0.6);">"Pagina 2–3 — bijna goed genoeg"</span>
              </div>
              <div class="urgency-row good">
                <div class="urgency-dot green"></div>
                <span class="urgency-label">Met Scorio</span>
                <span style="color:rgba(232,232,240,0.6);">"Pagina 1 — hier gebeurt het"</span>
              </div>
            </div>

            <div class="glass-card" style="margin-top:24px;padding:28px;">
              <div style="font-size:0.8rem;color:var(--muted);margin-bottom:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;">Populaire branches in {stad}</div>
              <div style="display:flex;flex-wrap:wrap;gap:8px;">
                {" ".join([f'<span class="badge badge-primary">{b.strip()}</span>' for b in d['branches'].split(',')])}
              </div>
              <div style="margin-top:20px;padding-top:20px;border-top:1px solid var(--border);font-size:0.85rem;color:var(--muted);">
                In al deze sectoren is lokale SEO de #1 manier om nieuwe klanten te winnen.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         HOE HET WERKT
    ============================================================ -->
    <section style="padding: var(--section-gap) 0; background: rgba(255,255,255,0.02); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Hoe het werkt</span>
          <h2 class="section-heading">Je SEO-scan in 3 stappen</h2>
          <p class="section-sub">Van URL invullen tot je persoonlijk actieplan — alles in minder dan 60 seconden.</p>
        </div>

        <div class="how-steps">
          <div class="how-step fade-up">
            <div class="how-step-num">1</div>
            <span class="how-step-icon" aria-hidden="true">🌐</span>
            <h3>Vul je website URL in</h3>
            <p>Voer de URL van jouw {stad}se website in en klik op "Scan mijn website". Geen account nodig.</p>
          </div>
          <div class="how-step fade-up stagger-1">
            <div class="how-step-num">2</div>
            <span class="how-step-icon" aria-hidden="true">🔍</span>
            <h3>Wij scannen 45+ SEO factoren</h3>
            <p>Scorio analyseert je snelheid, SEO-structuur, mobielvriendelijkheid, technische fouten en meer.</p>
          </div>
          <div class="how-step fade-up stagger-2">
            <div class="how-step-num">3</div>
            <span class="how-step-icon" aria-hidden="true">📋</span>
            <h3>Ontvang je persoonlijke rapport</h3>
            <p>Je krijgt een SEO-score van 0–100 én een geprioriteerde actielijst — speciaal voor jouw situatie in {stad}.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         WAT WE CONTROLEREN
    ============================================================ -->
    <section style="padding: var(--section-gap) 0;">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Ons rapport</span>
          <h2 class="section-heading">Wat controleren we voor jou?</h2>
          <p class="section-sub">Elke scan analyseert 45+ factoren verdeeld over zes categorieën.</p>
        </div>

        <div class="check-grid">
          <div class="check-card fade-up">
            <span class="check-card-icon" aria-hidden="true">⚡</span>
            <h3>Snelheid &amp; Core Web Vitals</h3>
            <p>Laadtijd, LCP, INP en CLS — de drie officiële Google-rankingfactoren voor paginasnelheid.</p>
          </div>
          <div class="check-card fade-up stagger-1">
            <span class="check-card-icon" aria-hidden="true">🔍</span>
            <h3>On-page SEO</h3>
            <p>Title tags, meta descriptions, H1-structuur, zoekwoorden en interne links voor jouw {stad}se pagina's.</p>
          </div>
          <div class="check-card fade-up stagger-2">
            <span class="check-card-icon" aria-hidden="true">📱</span>
            <h3>Mobielvriendelijkheid</h3>
            <p>Google indexeert eerst de mobiele versie. Wij controleren of jouw site daar klaar voor is.</p>
          </div>
          <div class="check-card fade-up stagger-3">
            <span class="check-card-icon" aria-hidden="true">🔗</span>
            <h3>Links &amp; sitestructuur</h3>
            <p>Interne links, externe links, broken links en de algehele structuur van je website.</p>
          </div>
          <div class="check-card fade-up stagger-1">
            <span class="check-card-icon" aria-hidden="true">🛡️</span>
            <h3>Technische fouten</h3>
            <p>HTTPS, robots.txt, sitemap, indexeerbaarheid en andere technische SEO-factoren.</p>
          </div>
          <div class="check-card fade-up stagger-2">
            <span class="check-card-icon" aria-hidden="true">📋</span>
            <h3>Actielijst met prioriteiten</h3>
            <p>Geen lijst van 50 dingen. Wij laten je zien wat het meeste impact heeft — vandaag nog uitvoerbaar.</p>
          </div>
        </div>

        <div style="text-align:center;margin-top:48px;">
          <a href="#hero-form" class="btn btn-accent btn-lg">Gratis scannen — start nu →</a>
        </div>
      </div>
    </section>

    <!-- ============================================================
         SOCIAL PROOF / REVIEWS
    ============================================================ -->
    <section style="padding: var(--section-gap) 0; background: rgba(255,255,255,0.02); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Ervaringen</span>
          <h2 class="section-heading">Ondernemers in {stad} gingen je voor</h2>
          <p class="section-sub">Bekijk wat andere {stad}se ondernemers bereikten met Scorio.</p>
        </div>

        <div class="reviews-grid">
          <div class="review-card fade-up">
            <div class="review-stars">★★★★★</div>
            <p class="review-text">"{d['review1_tekst']}"</p>
            <div class="review-author">
              <div class="review-avatar">{d['review1_naam'][:2].upper()}</div>
              <div>
                <div class="review-name">{d['review1_naam']}</div>
                <div class="review-company">{d['review1_bedrijf']}</div>
              </div>
            </div>
          </div>
          <div class="review-card fade-up stagger-1">
            <div class="review-stars">★★★★★</div>
            <p class="review-text">"{d['review2_tekst']}"</p>
            <div class="review-author">
              <div class="review-avatar">{d['review2_naam'][:2].upper()}</div>
              <div>
                <div class="review-name">{d['review2_naam']}</div>
                <div class="review-company">{d['review2_bedrijf']}</div>
              </div>
            </div>
          </div>
          <div class="review-card fade-up stagger-2">
            <div class="review-stars">★★★★★</div>
            <p class="review-text">"{d['review3_tekst']}"</p>
            <div class="review-author">
              <div class="review-avatar">{d['review3_naam'][:2].upper()}</div>
              <div>
                <div class="review-name">{d['review3_naam']}</div>
                <div class="review-company">{d['review3_bedrijf']}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         PRICING
    ============================================================ -->
    <section class="pricing" id="prijzen">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Tarieven</span>
          <h2 class="section-heading">Eenvoudige, eerlijke prijzen</h2>
          <p class="section-sub">Begin gratis. Schaal op wanneer jij er klaar voor bent. Altijd opzegbaar.</p>
        </div>

        <div class="pricing-toggle">
          <span class="toggle-label toggle-monthly active">Maandelijks</span>
          <label class="toggle-switch" aria-label="Schakel naar jaarlijks factureren">
            <input type="checkbox" id="pricing-toggle" role="switch" />
            <span class="toggle-track"></span>
            <span class="toggle-thumb"></span>
          </label>
          <span class="toggle-label toggle-yearly">Jaarlijks</span>
          <span class="toggle-badge">2 maanden gratis</span>
        </div>

        <div class="pricing-grid">

          <div class="pricing-card" data-plan="free">
            <div class="pricing-name">Gratis</div>
            <div class="pricing-price">
              <span class="price-amount">€0</span>
              <span class="price-period">/mnd</span>
            </div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> 1 scan per maand</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Basis rapport online</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> SEO score + 3 tips</li>
              <li class="pricing-feature disabled"><span class="feature-check no" aria-label="Niet inbegrepen">–</span> Volledig PDF rapport</li>
              <li class="pricing-feature disabled"><span class="feature-check no" aria-label="Niet inbegrepen">–</span> E-mail support</li>
              <li class="pricing-feature disabled"><span class="feature-check no" aria-label="Niet inbegrepen">–</span> iDEAL betaling</li>
            </ul>
            <a href="#hero-form" class="pricing-cta pricing-cta-secondary">Gratis starten</a>
          </div>

          <div class="pricing-card featured" data-plan="starter">
            <div class="pricing-card-badge">
              <span class="badge badge-accent">⭐ Meest gekozen</span>
            </div>
            <div class="pricing-name">Starter</div>
            <div class="pricing-price">
              <span class="price-amount">€9</span>
              <span class="price-period">/mnd</span>
            </div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> 5 scans per maand</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Volledig PDF rapport</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Alle SEO categorieën</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> E-mail support</li>
              <li class="pricing-feature disabled"><span class="feature-check no" aria-label="Niet inbegrepen">–</span> Priority support</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> iDEAL betaling</li>
            </ul>
            <a href="#" class="pricing-cta pricing-cta-primary">14 dagen gratis proberen</a>
            <p class="pricing-trial">Daarna €9/mnd — altijd opzegbaar</p>
          </div>

          <div class="pricing-card" data-plan="pro">
            <div class="pricing-name">Pro</div>
            <div class="pricing-price">
              <span class="price-amount">€29</span>
              <span class="price-period">/mnd</span>
            </div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> 25 scans per maand</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Volledig PDF rapport</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Concurrentie vergelijking</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Priority support</li>
              <li class="pricing-feature disabled"><span class="feature-check no" aria-label="Niet inbegrepen">–</span> Klantportaal</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> iDEAL betaling</li>
            </ul>
            <a href="#" class="pricing-cta pricing-cta-secondary">14 dagen gratis proberen</a>
            <p class="pricing-trial">Daarna €29/mnd — altijd opzegbaar</p>
          </div>

          <div class="pricing-card" data-plan="agency">
            <div class="pricing-card-badge">
              <span class="badge badge-primary">Voor bureaus</span>
            </div>
            <div class="pricing-name">Agency</div>
            <div class="pricing-price">
              <span class="price-amount">€79</span>
              <span class="price-period">/mnd</span>
            </div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Onbeperkte scans</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> White-label rapporten</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> API toegang</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Klantportaal</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> Priority support</li>
              <li class="pricing-feature"><span class="feature-check yes" aria-label="Inbegrepen">✓</span> iDEAL betaling</li>
            </ul>
            <a href="#" class="pricing-cta pricing-cta-secondary">14 dagen gratis proberen</a>
            <p class="pricing-trial">Daarna €79/mnd — altijd opzegbaar</p>
          </div>

        </div>

        <div style="display:flex;justify-content:center;gap:16px;margin-top:32px;flex-wrap:wrap;">
          <div class="footer-pay-badge"><svg width="24" height="16" viewBox="0 0 40 26" fill="none" aria-hidden="true"><rect width="40" height="26" rx="4" fill="#CC0066"/><text x="20" y="17" text-anchor="middle" font-size="9" font-weight="900" fill="white" font-family="sans-serif">iDEAL</text></svg> iDEAL</div>
          <div class="footer-pay-badge"><svg width="24" height="16" viewBox="0 0 40 26" fill="none" aria-hidden="true"><rect width="40" height="26" rx="4" fill="#635BFF"/><text x="20" y="17" text-anchor="middle" font-size="9" font-weight="900" fill="white" font-family="sans-serif">stripe</text></svg> Stripe</div>
          <span style="font-size:0.8rem;color:var(--muted);align-self:center;">· 14 dagen gratis · Geen creditcard vereist · Altijd opzegbaar</span>
        </div>
      </div>
    </section>

    <!-- ============================================================
         FAQ
    ============================================================ -->
    <section class="faq">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Veelgestelde vragen</span>
          <h2 class="section-heading">Veelgestelde vragen over SEO in {stad}</h2>
          <p class="section-sub">Directe antwoorden op de meest gestelde SEO-vragen van ondernemers in {stad}.</p>
        </div>

        <div class="faq-list">

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Hoe kom ik bovenaan in Google in {stad}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Combineer technische SEO, lokale zoekwoorden ({stad} + jouw dienst) en een volledig Google Bedrijfsprofiel. Scorio laat precies zien wat bij jou als eerste aandacht nodig heeft. Begin met de gratis scan en gebruik de geprioriteerde actielijst als startpunt.
              </div>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Wat kost een SEO specialist in {stad}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                SEO bureaus in {stad} rekenen gemiddeld €500 tot €2.000 per maand. Met Scorio doe je de analyse zelf voor €9 per maand en weet je precies wat je moet aanpakken — zonder maandelijkse bureaukosten. Zo houdt je de regie en bespaar je duizenden euro's per jaar.
              </div>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Hoe lang duurt het voordat SEO werkt in {stad}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Technische verbeteringen zie je binnen 2–4 weken terug in Google Search Console. Voor betere rankings in {stad} reken je op 3 tot 6 maanden bij consistente inzet. Lokale verbeteringen via Google Bedrijfsprofiel kunnen al binnen enkele weken merkbaar zijn.
              </div>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Werkt Scorio ook voor lokale bedrijven in {stad}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Absoluut. Scorio is speciaal gebouwd voor Nederlandse MKB'ers en ZZP'ers. We analyseren ook je lokale vindbaarheid in {stad} en geven concrete tips voor je Google Bedrijfsprofiel, lokale zoekwoorden en NAP-consistentie. Precies wat jij nodig hebt om klanten in {stad} te bereiken.
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================================
         FINALE CTA
    ============================================================ -->
    <section style="padding: var(--section-gap) 0;">
      <div class="container">
        <div class="glass-card" style="padding:64px;text-align:center;max-width:720px;margin:0 auto;background:linear-gradient(135deg,rgba(91,79,232,0.15) 0%,rgba(0,200,150,0.08) 100%);">
          <span style="font-size:2.5rem;display:block;margin-bottom:16px;" aria-hidden="true">🚀</span>
          <h2 class="section-heading" style="font-size:clamp(1.5rem,3vw,2rem);margin-bottom:16px;">Klaar om beter gevonden te worden in {stad}?</h2>
          <p style="color:rgba(232,232,240,0.75);margin-bottom:40px;max-width:520px;margin-left:auto;margin-right:auto;">Doe de gratis scan — geen registratie, geen creditcard. Ontvang direct jouw persoonlijk SEO-rapport voor {stad}.</p>

          <form class="hero-form scan-form" novalidate style="max-width:520px;margin:0 auto 20px;">
            <div class="hero-input-wrap">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418" />
              </svg>
              <input type="url" class="hero-input" placeholder="https://jouwwebsite.nl" aria-label="URL van jouw website" autocomplete="url" spellcheck="false" />
            </div>
            <button type="submit" class="btn btn-accent btn-lg">Scan mijn website →</button>
          </form>

          <p style="font-size:0.8rem;color:var(--muted);">Of probeer <a href="/prijzen.html" style="color:var(--primary-light);">Starter 14 dagen gratis</a> — geen creditcard nodig</p>
        </div>
      </div>
    </section>

    <!-- ============================================================
         ANDERE STEDEN
    ============================================================ -->
    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">
        <div class="glass-card" style="padding:32px 40px;">
          <h2 style="font-size:1rem;margin-bottom:6px;font-weight:700;">SEO check in andere steden</h2>
          <p style="font-size:0.825rem;color:var(--muted);margin-bottom:20px;">Scorio is beschikbaar voor ondernemers in heel Nederland.</p>
          <div class="city-other-links">
            {other_links}
          </div>
        </div>
      </div>
    </section>

  </main>

  <footer class="site-footer" role="contentinfo">
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
            <li><a href="/hoe-het-werkt.html">Hoe het werkt</a></li>
            <li><a href="/prijzen.html">Prijzen</a></li>
            <li><a href="/#hero-form">Gratis scan</a></li>
            <li><a href="#">API</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Bedrijf</h4>
          <ul>
            <li><a href="#">Over ons</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Affiliate programma</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Legal</h4>
          <ul>
            <li><a href="#">Privacybeleid</a></li>
            <li><a href="#">Algemene voorwaarden</a></li>
            <li><a href="#">Cookies</a></li>
            <li><a href="#">AVG</a></li>
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
  </footer>

  <script src="/js/main.js"></script>
</body>
</html>"""
    return html


def main():
    base = '/home/user/Scorio-NL'
    for slug, name in ALL_CITIES:
        data = CITIES[slug]
        dir_path = os.path.join(base, f'seo-check-{slug}')
        os.makedirs(dir_path, exist_ok=True)
        html = generate_page(slug, data)
        out = os.path.join(dir_path, 'index.html')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ {out}')

    print('\nAll 10 city pages generated.')


if __name__ == '__main__':
    main()
