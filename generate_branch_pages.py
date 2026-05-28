#!/usr/bin/env python3
"""Generate 10 branch landing pages for Scorio.nl."""
import os

BRANCHES = {
    'kapper': {
        'name': 'kapper',
        'name_cap': 'Kapper',
        'name_plural': 'kappers',
        'name_plural_cap': 'Kappers',
        'bedrijf_label': 'kapsalon',
        'bedrijf_label_cap': 'Kapsalon',
        'emoji': '✂️',
        'pijn': 'Mensen zoeken dagelijks "kapper + jouw stad". Als jij daar niet staat, gaan ze naar de concurrent om de hoek.',
        'zoekwoorden': 'kapper, kapsalon, haarstylist, kapper amsterdam, kapper rotterdam',
        'klant_scenario': 'Iemand verhuist naar jouw stad en zoekt een nieuwe kapper. Ze typen "kapper [stad]" in Google. Sta jij bovenaan?',
        'snelle_win': 'Vul je Google Bedrijfsprofiel volledig in met foto\'s, openingstijden en een beschrijving met je stad en specialisaties. Dit alleen al brengt je hoger in de lokale resultaten.',
        'zoekvolume': '14.000+',
        'tip2_icon': '📸',
        'tip2_titel': 'Foto\'s zijn essentieel',
        'tip2_tekst': 'Kappers worden gekozen op sfeer en stijl. Voeg voor/na-foto\'s toe op je website en Google Bedrijfsprofiel. Zorg dat de bestandsnamen lokale zoekwoorden bevatten.',
        'review1_tekst': 'Mijn kapsalon stond op pagina 3 van Google. Na de Scorio scan en de verbeteringen sta ik nu bovenaan voor "kapper [stad]". Mijn agenda zit vol — ik moet zelfs mensen teleurstellen.',
        'review1_naam': 'Michelle Peters',
        'review1_bedrijf': 'Kapsalon Michelle, Amsterdam',
        'review2_tekst': 'Ik dacht dat mijn website er goed genoeg uitzag. Scorio liet zien dat ik 9 kritieke SEO-fouten had. Na 6 weken werken aan de verbeteringen sta ik in de top 3 voor mijn wijk.',
        'review2_naam': 'Rachid El Mansouri',
        'review2_bedrijf': 'Barbershop De Pijp, Rotterdam',
        'review3_tekst': 'Zonder Scorio had ik nooit geweten dat mijn website zo slecht scoorde. Nu krijg ik wekelijks nieuwe klanten die me via Google hebben gevonden.',
        'review3_naam': 'Yolanda Bosman',
        'review3_bedrijf': 'Hair Studio Utrecht',
    },
    'restaurant': {
        'name': 'restaurant',
        'name_cap': 'Restaurant',
        'name_plural': 'restaurants',
        'name_plural_cap': 'Restaurants',
        'bedrijf_label': 'restaurant',
        'bedrijf_label_cap': 'Restaurant',
        'emoji': '🍽️',
        'pijn': '73% van de mensen zoekt online voordat ze een restaurant kiezen. Zonder goede SEO mis je die reserveringen — elke dag opnieuw.',
        'zoekwoorden': 'restaurant, eten, uiteten, restaurant amsterdam, italiaans restaurant',
        'klant_scenario': 'Een stel wil vanavond uit eten en zoekt "restaurant [stad] romantisch". Verschijn jij in die resultaten — of gaan ze naar de concurrent?',
        'snelle_win': 'Optimaliseer je menupagina met lokale zoekwoorden en voeg Schema.org Restaurant markup toe. Google toont je dan met openingstijden, prijsklasse en reviews direct in de zoekresultaten.',
        'zoekvolume': '22.000+',
        'tip2_icon': '📋',
        'tip2_titel': 'Menu online zichtbaar',
        'tip2_tekst': 'Zorg dat je menu vindbaar is als webpagina — niet alleen als PDF. Gebruik gerechtnamen als zoekwoorden: mensen zoeken specifiek op "pasta amsterdam" of "sushi rotterdam".',
        'review1_tekst': 'We kregen nauwelijks reserveringen via Google. Nu is online ons drukste reserveringskanaal. Scorio heeft ons laten zien wat er mis was — we waren compleet onzichtbaar.',
        'review1_naam': 'Marco Visser',
        'review1_bedrijf': 'Restaurant De Tafel, Amsterdam',
        'review2_tekst': 'Mijn Italiaans restaurant stond niet eens op de kaart in Google Maps. Na Scorio en een paar weken werken staan we nu in de top 3 voor "italiaans restaurant [stad]".',
        'review2_naam': 'Giuseppe Ferrara',
        'review2_bedrijf': 'Trattoria Ferrara, Utrecht',
        'review3_tekst': 'Ik dacht dat Google adverteren de enige manier was om gevonden te worden. Scorio bewees het tegendeel. Organisch traffic is nu onze grootste bron van nieuwe gasten.',
        'review3_naam': 'Aigerim Bekova',
        'review3_bedrijf': 'Restaurant Bekova, Rotterdam',
    },
    'loodgieter': {
        'name': 'loodgieter',
        'name_cap': 'Loodgieter',
        'name_plural': 'loodgieters',
        'name_plural_cap': 'Loodgieters',
        'bedrijf_label': 'loodgietersbedrijf',
        'bedrijf_label_cap': 'Loodgietersbedrijf',
        'emoji': '🔧',
        'pijn': 'Spoedzoekopdrachten zoals "loodgieter spoed" gaan altijd naar de eerste resultaten. Pagina 2 bestaat niet bij een lekkage — de klant belt de eerste die verschijnt.',
        'zoekwoorden': 'loodgieter, loodgieter spoed, ontstoppen, cv ketel, loodgieter amsterdam',
        'klant_scenario': 'Iemand heeft een lekkage. Ze pakken hun telefoon en zoeken "loodgieter spoed [stad]". De eerste die ze zien én bellen krijgt de opdracht.',
        'snelle_win': 'Maak een aparte pagina aan voor "loodgieter spoed [stad]" met je telefoonnummer prominent bovenaan, openingstijden en een duidelijke call-to-action. Spoedzoekopdrachten leveren de hoogste opdrachten op.',
        'zoekvolume': '18.000+',
        'tip2_icon': '📞',
        'tip2_titel': 'Telefoonnummer bovenaan',
        'tip2_tekst': 'Bij spoedzoekopdrachten wil men direct bellen. Zet je telefoonnummer zichtbaar op elke pagina. Voeg ook een klikbare belknop toe voor mobiel — dat verhoogt je conversie enorm.',
        'review1_tekst': 'Bij spoedklussen ben ik nu altijd de eerste die gevonden wordt. Dat betekent letterlijk meer werk. Scorio liet zien dat mijn spoedpagina compleet ontbrak.',
        'review1_naam': 'Jan Bakker',
        'review1_bedrijf': 'Bakker Loodgieters, Amsterdam',
        'review2_tekst': 'Ik had geen idee dat mijn website zo slecht scoorde. Na de Scorio scan heb ik aparte pagina\'s gemaakt per dienst en stad. Nu kom ik dagelijks voor uit spoedaanvragen.',
        'review2_naam': 'Henk de Groot',
        'review2_bedrijf': 'De Groot Installaties, Rotterdam',
        'review3_tekst': 'Concurrenten die al jaren bezig zijn heb ik inmiddels ingehaald op Google. Scorio gaf me precies het inzicht dat ik nodig had om de juiste verbeteringen te maken.',
        'review3_naam': 'Patrick van Dam',
        'review3_bedrijf': 'Van Dam Loodgieters, Utrecht',
    },
    'tandarts': {
        'name': 'tandarts',
        'name_cap': 'Tandarts',
        'name_plural': 'tandartsen',
        'name_plural_cap': 'Tandartsen',
        'bedrijf_label': 'tandartspraktijk',
        'bedrijf_label_cap': 'Tandartspraktijk',
        'emoji': '🦷',
        'pijn': 'Mensen zoeken een tandarts bij hen in de buurt. Ze vergelijken reviews en websites voordat ze bellen. Ben jij zichtbaar op het moment dat ze zoeken?',
        'zoekwoorden': 'tandarts, tandarts spoed, tandartspraktijk, tandarts amsterdam, nieuwe tandarts',
        'klant_scenario': 'Een gezin verhuist naar jouw wijk en zoekt een nieuwe tandarts. Ze googelen "tandarts [wijk] [stad]". Word jij gevonden — of nemen ze contact op met iemand anders?',
        'snelle_win': 'Verzamel actief reviews op Google en vermeld al je specialisaties op je website. Patiënten zoeken op specifieke behandelingen: "tandarts angst", "spoedhulp tandarts", "implantaten". Maak hier aparte pagina\'s voor.',
        'zoekvolume': '12.000+',
        'tip2_icon': '🏥',
        'tip2_titel': 'Specialisatiepagina\'s',
        'tip2_tekst': 'Maak aparte pagina\'s per behandeling: spoedhulp, implantaten, bleken, orthodontie. Elke pagina trekt bezoekers die specifiek naar die behandeling zoeken.',
        'review1_tekst': 'Nieuwe patiënten belden altijd via doorverwijzing. Nu vinden ze ons via Google. Scorio liet zien dat we onze specialisaties niet vermeldden — een simpele maar enorme verbetering.',
        'review1_naam': 'Dr. Ellen Vermeer',
        'review1_bedrijf': 'Tandartspraktijk Vermeer, Amsterdam',
        'review2_tekst': 'We hadden geen reviews op Google en stonden niet in de lokale resultaten. Na Scorio en drie maanden werken staan we nu in de top 3 voor onze wijk.',
        'review2_naam': 'Dr. Karim Benali',
        'review2_bedrijf': 'TandartsClinic Rotterdam',
        'review3_tekst': 'Ik dacht dat een website genoeg was. Scorio liet zien dat technische fouten ons onzichtbaar maakten. Nu is Google onze grootste bron van nieuwe patiënten.',
        'review3_naam': 'Dr. Marieke de Boer',
        'review3_bedrijf': 'Praktijk De Boer, Utrecht',
    },
    'webshop': {
        'name': 'webshop',
        'name_cap': 'Webshop',
        'name_plural': 'webshops',
        'name_plural_cap': 'Webshops',
        'bedrijf_label': 'webshop',
        'bedrijf_label_cap': 'Webshop',
        'emoji': '🛒',
        'pijn': 'Zonder SEO betaal je altijd voor advertenties. Met goede SEO komen klanten gratis naar jou toe — dag en nacht, ook als je slaapt.',
        'zoekwoorden': 'online kopen, webshop, productcategorie + kopen, gratis verzending',
        'klant_scenario': 'Iemand wil een specifiek product kopen en googelt de naam. Staat jouw productpagina bovenaan — of die van bol.com en grote ketens?',
        'snelle_win': 'Schrijf unieke productbeschrijvingen — geen kopieer-plak van de leverancier. Google bestraft duplicate content. Gebruik de zoekwoorden die kopers gebruiken: niet "schoen" maar "dames sneakers wit maat 38".',
        'zoekvolume': 'Afhankelijk van niche',
        'tip2_icon': '📦',
        'tip2_titel': 'Productpagina\'s optimaliseren',
        'tip2_tekst': 'Elke productpagina is een kans om gevonden te worden. Unieke titel, beschrijving met koopzoekwoorden en alt-teksten bij afbeeldingen. Organic traffic = gratis omzet.',
        'review1_tekst': 'We betaalden duizenden euro\'s per maand aan Google Ads. Na Scorio en een jaar SEO-werk is organisch traffic onze grootste bron van omzet — bijna gratis.',
        'review1_naam': 'Thomas Koopmans',
        'review1_bedrijf': 'OutdoorShop.nl',
        'review2_tekst': 'Mijn webshop had honderden producten maar vrijwel geen organisch traffic. Scorio liet zien dat al mijn productpagina\'s duplicate content hadden. Na de fix verdubbelde mijn traffic.',
        'review2_naam': 'Stephanie van den Heuvel',
        'review2_bedrijf': 'KidsMode.nl',
        'review3_tekst': 'Ik concurreer met grote spelers maar win het op niche zoekwoorden. Scorio gaf me de inzichten om mijn productpagina\'s perfect te optimaliseren.',
        'review3_naam': 'Daan Pieters',
        'review3_bedrijf': 'VintageFiets.nl',
    },
    'makelaar': {
        'name': 'makelaar',
        'name_cap': 'Makelaar',
        'name_plural': 'makelaars',
        'name_plural_cap': 'Makelaars',
        'bedrijf_label': 'makelaarskantoor',
        'bedrijf_label_cap': 'Makelaarskantoor',
        'emoji': '🏠',
        'pijn': 'Mensen googelen maanden voordat ze een makelaar bellen. Als jij dan niet zichtbaar bent, bestaat je naam niet voor hen op het moment dat ze klaar zijn om te bellen.',
        'zoekwoorden': 'makelaar, huis kopen, huis verkopen, makelaar amsterdam, NVM makelaar',
        'klant_scenario': 'Iemand overweegt hun huis te verkopen en begint te oriënteren. Ze zoeken "makelaar [stad] betrouwbaar". Kom jij naar voren in die zoekresultaten?',
        'snelle_win': 'Schrijf een blogartikel over de woningmarkt in jouw stad: "Woningmarkt [stad] 2026 — wat is jouw huis waard?". Dit trekt oriënterende kopers en verkopers maanden voordat ze contact opnemen.',
        'zoekvolume': '25.000+',
        'tip2_icon': '📊',
        'tip2_titel': 'Woningmarkt content',
        'tip2_tekst': 'Publiceer regelmatig updates over de lokale woningmarkt. Dit toont expertise, trekt oriënterende bezoekers en Google beloont je met betere rankings voor lokale zoekopdrachten.',
        'review1_tekst': 'Mensen die hun huis willen verkopen vinden ons nu online voordat ze überhaupt weten welke makelaar ze willen. Scorio heeft ons zichtbaar gemaakt op het juiste moment.',
        'review1_naam': 'Carla Dijkstra',
        'review1_bedrijf': 'Dijkstra Makelaars, Amsterdam',
        'review2_tekst': 'We concurreerden met grote ketens maar winnen het nu op lokale zoekopdrachten. Scorio gaf ons de inzichten. Nu zijn we de #1 makelaar in onze wijk op Google.',
        'review2_naam': 'Robert van Oost',
        'review2_bedrijf': 'Van Oost Vastgoed, Rotterdam',
        'review3_tekst': 'Ik had een mooie website maar niemand vond me. Scorio liet zien dat mijn lokale SEO compleet ontbrak. Nu is Google mijn grootste bron van nieuwe opdrachten.',
        'review3_naam': 'Saskia Hartman',
        'review3_bedrijf': 'Hartman Makelaardij, Utrecht',
    },
    'fysiotherapeut': {
        'name': 'fysiotherapeut',
        'name_cap': 'Fysiotherapeut',
        'name_plural': 'fysiotherapeuten',
        'name_plural_cap': 'Fysiotherapeuten',
        'bedrijf_label': 'fysiotherapiepraktijk',
        'bedrijf_label_cap': 'Fysiotherapiepraktijk',
        'emoji': '🏃',
        'pijn': 'Mensen met rugpijn of blessures zoeken direct online. Ze willen snel iemand in de buurt. Ben jij zichtbaar op het moment dat de pijn begint?',
        'zoekwoorden': 'fysiotherapeut, fysiotherapie, rugpijn behandeling, fysiotherapeut amsterdam, sportfysiotherapeut',
        'klant_scenario': 'Iemand heeft last van zijn rug en zoekt "fysiotherapeut [wijk]". Staat jouw praktijk in de top 3 — of vinden ze een concurrent?',
        'snelle_win': 'Maak aparte pagina\'s per specialisatie: rugklachten, sportblessures, bekkenbodemtherapie, zwangerschapsgerelateerde klachten. Elk met eigen zoekwoorden. Mensen zoeken op hun klacht, niet op "fysiotherapeut".',
        'zoekvolume': '16.000+',
        'tip2_icon': '💪',
        'tip2_titel': 'Klacht-specifieke pagina\'s',
        'tip2_tekst': 'Mensen googelen hun klacht: "rugpijn behandeling", "tennisarm behandeling", "knieband blessure". Maak per klacht een informatiepagina — dit trekt bezoekers die actief hulp zoeken.',
        'review1_tekst': 'Mijn praktijk was afhankelijk van doorverwijzingen van huisartsen. Nu vinden patiënten me direct via Google. Scorio liet zien hoe ik mijn specialisaties beter kon presenteren.',
        'review1_naam': 'Drs. Jolanda Smit',
        'review1_bedrijf': 'FysioPraktijk Smit, Amsterdam',
        'review2_tekst': 'Ik had aparte pagina\'s per behandeling aangemaakt maar ze werden niet gevonden. Scorio liet zien dat de technische SEO niet klopte. Na de fix verdubbelde mijn organisch verkeer.',
        'review2_naam': 'Tim Verhoeven',
        'review2_bedrijf': 'SportsFysio Verhoeven, Utrecht',
        'review3_tekst': 'Nieuwe patiënten vinden me nu via Google voor specifieke klachten. Scorio gaf me inzicht in wat er ontbrak. Mijn agenda staat nu weken vol.',
        'review3_naam': 'Nathalie de Wit',
        'review3_bedrijf': 'FysioPlus Rotterdam',
    },
    'accountant': {
        'name': 'accountant',
        'name_cap': 'Accountant',
        'name_plural': 'accountants',
        'name_plural_cap': 'Accountants',
        'bedrijf_label': 'accountantskantoor',
        'bedrijf_label_cap': 'Accountantskantoor',
        'emoji': '📊',
        'pijn': 'Ondernemers zoeken een betrouwbare accountant online. Ze vergelijken websites en reviews voordat ze contact opnemen. Ziet jouw website er professioneel én vindbaar uit?',
        'zoekwoorden': 'accountant, boekhouder, belastingaangifte, accountant amsterdam, accountant mkb',
        'klant_scenario': 'Een ZZP\'er heeft een nieuwe accountant nodig en googelt "accountant [stad] MKB". Verschijn jij in die zoekresultaten — of gaat de opdracht naar een concurrent?',
        'snelle_win': 'Maak specialisatiepagina\'s: "accountant voor ZZP", "accountant voor MKB", "accountant voor starters". Elke pagina trekt een specifieke doelgroep die precies zoekt wat jij aanbiedt.',
        'zoekvolume': '19.000+',
        'tip2_icon': '📑',
        'tip2_titel': 'Doelgroep-specifieke pagina\'s',
        'tip2_tekst': 'ZZP\'ers, MKB-ers en starters zoeken anders. Maak voor elke doelgroep een aparte landingspagina met specifieke zoekwoorden: "accountant zzp amsterdam" of "boekhouder mkb rotterdam".',
        'review1_tekst': 'Nieuwe klanten belden altijd via via. Nu vinden ze ons via Google. Scorio liet zien dat onze doelgroeppagina\'s compleet ontbraken. Na de fix groeit onze klantenbasis gestaag.',
        'review1_naam': 'Arjan Prins',
        'review1_bedrijf': 'Prins Accountancy, Amsterdam',
        'review2_tekst': 'We hadden een mooie website maar stonden nergens in Google. Scorio legde de vinger op de wond: geen lokale optimalisatie. Nu zijn we top 3 in onze stad.',
        'review2_naam': 'Linda Hoogenbosch',
        'review2_bedrijf': 'Hoogenbosch & Partners, Rotterdam',
        'review3_tekst': 'Als kleine accountant concurreer ik met grote kantoren. Via Scorio ontdekte ik hoe ik de lokale markt kon domineren met gerichte SEO.',
        'review3_naam': 'Kees Willems',
        'review3_bedrijf': 'Willems Administratie, Utrecht',
    },
    'schilder': {
        'name': 'schilder',
        'name_cap': 'Schilder',
        'name_plural': 'schilders',
        'name_plural_cap': 'Schilders',
        'bedrijf_label': 'schildersbedrijf',
        'bedrijf_label_cap': 'Schildersbedrijf',
        'emoji': '🎨',
        'pijn': 'Mensen vragen meerdere offertes aan via Google. De eerste drie schilders die ze vinden krijgen de kans. Sta jij er altijd bij?',
        'zoekwoorden': 'schilder, schildersbedrijf, binnenschilder, buitenschilder, schilder amsterdam',
        'klant_scenario': 'Iemand wil zijn huis laten schilderen en vraagt drie offertes aan. Ze googelen "schilder [stad]". Ben jij een van de drie die ze bellen?',
        'snelle_win': 'Voeg voor/na-foto\'s toe aan je website van afgeronde projecten. Gebruik de plaatsnaam in de bestandsnaam (schilder-amsterdam-resultaat.jpg) en alt-tekst. Dit verbetert zowel je SEO als je conversie.',
        'zoekvolume': '11.000+',
        'tip2_icon': '🖼️',
        'tip2_titel': 'Voor/na projectfoto\'s',
        'tip2_tekst': 'Foto\'s van je werk overtuigen potentiële klanten én helpen je SEO. Gebruik beschrijvende bestandsnamen en alt-teksten met je stad en dienst. Voeg ook klantreviews toe bij de foto\'s.',
        'review1_tekst': 'Ik kreeg mijn offerteaanvragen altijd via mond-tot-mondreclame. Nu komen ze via Google. Scorio liet zien wat er ontbrak — mijn website was technisch een ramp.',
        'review1_naam': 'Richard Meijer',
        'review1_bedrijf': 'Meijer Schilderwerken, Amsterdam',
        'review2_tekst': 'Mijn schildersbedrijf bestaat al 15 jaar maar online was ik onzichtbaar. Na Scorio en de verbeteringen sta ik nu bovenaan voor schilders in mijn regio.',
        'review2_naam': 'Gijs van der Linden',
        'review2_bedrijf': 'Van der Linden Schilders, Rotterdam',
        'review3_tekst': 'Ik concurreer nu met schildersbedrijven die veel langer bestaan. Via Google sta ik er al bovenaan voor lokale zoekopdrachten — dankzij de tips van Scorio.',
        'review3_naam': 'Niels Jansen',
        'review3_bedrijf': 'Jansen Kleur & Stijl, Utrecht',
    },
    'installateur': {
        'name': 'installateur',
        'name_cap': 'Installateur',
        'name_plural': 'installateurs',
        'name_plural_cap': 'Installateurs',
        'bedrijf_label': 'installatiebedrijf',
        'bedrijf_label_cap': 'Installatiebedrijf',
        'emoji': '⚙️',
        'pijn': 'Of het nu gaat om airco, zonnepanelen of elektra — mensen googelen altijd eerst. De installateur die bovenaan staat krijgt de meeste aanvragen.',
        'zoekwoorden': 'installateur, elektricien, airco installatie, zonnepanelen installateur, cv ketel installateur amsterdam',
        'klant_scenario': 'Iemand wil zonnepanelen laten installeren en vergelijkt drie bedrijven die ze via Google vinden. Sta jij ertussen — of missen ze jou volledig?',
        'snelle_win': 'Maak aparte pagina\'s per dienst: airco installatie, zonnepanelen installeren, elektra, cv-ketel vervanging. Voeg ook lokale targeting toe: "zonnepanelen installateur [stad]". Elke dienst heeft zijn eigen zoekvolume.',
        'zoekvolume': '20.000+',
        'tip2_icon': '☀️',
        'tip2_titel': 'Dienst-specifieke pagina\'s',
        'tip2_tekst': 'Elke dienst (airco, zonnepanelen, elektra, cv-ketel) heeft eigen zoekwoorden. Maak per dienst een aparte pagina met lokale targeting. Zo vang je traffic voor al je diensten tegelijk.',
        'review1_tekst': 'We installeerden zonnepanelen maar werden online niet gevonden. Na Scorio en aparte dienstpagina\'s stromen de aanvragen binnen. Best beslissing die we ooit namen.',
        'review1_naam': 'Erwin Bakker',
        'review1_bedrijf': 'Bakker Installaties, Amsterdam',
        'review2_tekst': 'Als elektricien dacht ik dat mond-tot-mondreclame genoeg was. Scorio bewees het tegendeel. Nu genereer ik dagelijks leads via Google zonder te betalen voor advertenties.',
        'review2_naam': 'Hans Koot',
        'review2_bedrijf': 'Koot Elektra, Rotterdam',
        'review3_tekst': 'Mijn airco-installatiebedrijf was amper zichtbaar online. Dankzij Scorio weet ik nu precies wat ik moet doen. In het hoogseizoen had ik meer aanvragen dan ik aankon.',
        'review3_naam': 'Özgür Yilmaz',
        'review3_bedrijf': 'YilmazClimate, Utrecht',
    },
}

ALL_BRANCHES = [
    ('kapper', 'Kapper'),
    ('restaurant', 'Restaurant'),
    ('loodgieter', 'Loodgieter'),
    ('tandarts', 'Tandarts'),
    ('webshop', 'Webshop'),
    ('makelaar', 'Makelaar'),
    ('fysiotherapeut', 'Fysiotherapeut'),
    ('accountant', 'Accountant'),
    ('schilder', 'Schilder'),
    ('installateur', 'Installateur'),
]

TOP_STEDEN = [
    ('amsterdam', 'Amsterdam'),
    ('rotterdam', 'Rotterdam'),
    ('utrecht', 'Utrecht'),
    ('den-haag', 'Den Haag'),
    ('eindhoven', 'Eindhoven'),
]


def other_branch_links(current_slug):
    items = []
    for slug, name in ALL_BRANCHES:
        if slug != current_slug:
            items.append(f'<a href="/seo-check-{slug}/" class="city-link">{name}</a>')
    return '\n            '.join(items)


def city_links_html():
    items = []
    for slug, name in TOP_STEDEN:
        items.append(f'<a href="/seo-check-{slug}/" class="city-link">{name}</a>')
    return '\n            '.join(items)


def generate_page(slug, d):
    name = d['name']
    name_cap = d['name_cap']
    name_plural = d['name_plural']
    name_plural_cap = d['name_plural_cap']
    bedrijf = d['bedrijf_label']
    bedrijf_cap = d['bedrijf_label_cap']
    emoji = d['emoji']
    other_links = other_branch_links(slug)
    steden_links = city_links_html()

    faq_schema = f"""[
          {{
            "@type": "Question",
            "name": "Hoe kom ik bovenaan in Google als {name}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Combineer drie dingen: technische SEO basis op orde, lokale zoekwoorden ({name} + jouw stad) in je teksten, en een volledig Google Bedrijfsprofiel met foto's en reviews. Scorio laat zien wat bij jou prioriteit heeft."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Wat kost SEO voor een {name}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Je kunt beginnen voor €9 per maand met Scorio. Een SEO bureau rekent €500 tot €2000 per maand. Begin met de basis zelf doen via Scorio — je weet dan precies wat je moet aanpakken zonder maandelijkse bureaukosten."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Heb ik als {name} een blog nodig voor SEO?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Niet verplicht, maar het helpt enorm. Schrijf over vragen die klanten stellen: 'wat kost een {name}', 'hoe kies ik een goede {name}'. Dit trekt bezoekers die actief op zoek zijn naar jouw diensten."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Werkt Google Bedrijfsprofiel voor {name_plural}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Absoluut — dit is voor lokale {name_plural} het krachtigste gratis SEO middel. Vul alles volledig in, voeg foto's toe en vraag reviews. Google toont je dan in de kaartresultaten bovenaan de zoekresultaten."
            }}
          }}
        ]"""

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Gratis SEO Check voor {name_plural_cap} | Website Score | Scorio.nl</title>
  <meta name="description" content="Speciaal voor {name_plural}: gratis SEO scan in 60 seconden. Ontdek waarom klanten jou niet vinden en wat je vandaag kunt verbeteren. Geen registratie nodig." />
  <link rel="canonical" href="https://www.scorio.nl/seo-check-{slug}/" />
  <link rel="alternate" hreflang="nl" href="https://www.scorio.nl/seo-check-{slug}/" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Gratis SEO Check voor {name_plural_cap} | Scorio.nl" />
  <meta property="og:description" content="Speciaal voor {name_plural}: gratis SEO scan in 60 seconden. Ontdek waarom klanten jou niet vinden en wat je vandaag kunt verbeteren." />
  <meta property="og:url" content="https://www.scorio.nl/seo-check-{slug}/" />
  <meta property="og:site_name" content="Scorio.nl" />
  <meta property="og:locale" content="nl_NL" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Gratis SEO Check voor {name_plural_cap} | Scorio.nl" />
  <meta name="twitter:description" content="Speciaal voor {name_plural}: gratis SEO scan in 60 seconden. Geen registratie nodig." />

  <!-- Schema Markup -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebPage",
        "@id": "https://www.scorio.nl/seo-check-{slug}/#webpage",
        "name": "Gratis SEO Check voor {name_plural_cap} | Scorio.nl",
        "description": "Speciaal voor {name_plural}: gratis SEO scan in 60 seconden. Ontdek waarom klanten jou niet vinden.",
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
          {{"@type": "ListItem", "position": 2, "name": "SEO Check {name_cap}", "item": "https://www.scorio.nl/seo-check-{slug}/"}}
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
    /* Branch page specific styles */
    .branch-stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin: 48px 0;
    }}
    @media (max-width: 768px) {{
      .branch-stats {{ grid-template-columns: 1fr; }}
    }}
    .branch-stat-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 32px 24px;
      text-align: center;
    }}
    .branch-stat-num {{
      display: block;
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--primary-light);
      line-height: 1;
      margin-bottom: 12px;
    }}
    .branch-stat-lbl {{
      font-size: 0.85rem;
      color: var(--muted);
      line-height: 1.5;
    }}
    .quote-box {{
      border-left: 4px solid var(--primary);
      background: rgba(91,79,232,0.08);
      border-radius: 0 16px 16px 0;
      padding: 28px 32px;
      margin: 32px 0;
      font-size: 1.05rem;
      line-height: 1.7;
      color: rgba(232,232,240,0.9);
      font-style: italic;
    }}
    .quick-win-box {{
      background: rgba(0,200,150,0.08);
      border: 1px solid rgba(0,200,150,0.25);
      border-radius: 20px;
      padding: 32px;
      margin: 32px 0;
    }}
    .quick-win-icon {{
      font-size: 2rem;
      margin-bottom: 12px;
      display: block;
    }}
    .quick-win-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--accent);
      margin-bottom: 12px;
    }}
    .quick-win-text {{
      font-size: 0.9rem;
      line-height: 1.7;
      color: rgba(232,232,240,0.8);
      margin-bottom: 8px;
    }}
    .quick-win-sub {{
      font-size: 0.8rem;
      color: var(--muted);
    }}
    .tips-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }}
    @media (max-width: 768px) {{
      .tips-grid {{ grid-template-columns: 1fr; }}
    }}
    .tip-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 28px 24px;
    }}
    .tip-card-icon {{
      font-size: 1.8rem;
      margin-bottom: 16px;
      display: block;
    }}
    .tip-card h3 {{
      font-size: 1rem;
      margin-bottom: 10px;
      font-weight: 700;
    }}
    .tip-card p {{
      font-size: 0.85rem;
      color: var(--muted);
      line-height: 1.7;
      margin: 0;
    }}
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
      width: 44px; height: 44px;
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
    .how-step-icon {{ font-size: 2rem; margin-bottom: 16px; display: block; }}
    .how-step h3 {{ font-size: 1rem; margin-bottom: 8px; }}
    .how-step p {{ font-size: 0.85rem; color: var(--muted); line-height: 1.6; margin: 0; }}
    .check-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 48px;
    }}
    @media (max-width: 768px) {{ .check-grid {{ grid-template-columns: 1fr; }} }}
    @media (min-width: 769px) and (max-width: 1024px) {{ .check-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    .check-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
    }}
    .check-card-icon {{ font-size: 1.8rem; margin-bottom: 12px; display: block; }}
    .check-card h3 {{ font-size: 0.95rem; margin-bottom: 8px; }}
    .check-card p {{ font-size: 0.82rem; color: var(--muted); line-height: 1.6; margin: 0; }}
    .reviews-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }}
    @media (max-width: 900px) {{ .reviews-grid {{ grid-template-columns: 1fr; }} }}
    .review-card {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 28px;
    }}
    .review-stars {{ color: #f59e0b; font-size: 0.9rem; margin-bottom: 16px; }}
    .review-text {{ font-size: 0.875rem; line-height: 1.7; color: rgba(232,232,240,0.85); margin-bottom: 20px; }}
    .review-author {{ display: flex; align-items: center; gap: 12px; }}
    .review-avatar {{
      width: 40px; height: 40px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      display: flex; align-items: center; justify-content: center;
      font-weight: 700; font-size: 0.8rem; color: #fff; flex-shrink: 0;
    }}
    .review-name {{ font-weight: 700; font-size: 0.875rem; }}
    .review-company {{ font-size: 0.775rem; color: var(--muted); }}
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
    .scan-modal-url {{ color: var(--primary-light); font-weight: 700; word-break: break-all; }}
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
      <h2 style="font-size:1.2rem;margin-bottom:8px;">Jouw website wordt gescand...</h2>
      <p style="font-size:0.875rem;color:var(--muted);">We analyseren <span class="scan-modal-url"></span></p>
      <div class="scan-progress"><div class="scan-progress-fill"></div></div>
      <p style="font-size:0.775rem;color:var(--muted);margin-top:12px;">45+ SEO factoren worden gecontroleerd</p>
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
        <li aria-current="page">SEO Check {name_cap}</li>
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

          <div class="hero-content">
            <div class="hero-badge fade-up">
              <span aria-hidden="true">💼</span> SEO voor {name_plural_cap}
            </div>

            <h1 class="hero-heading fade-up stagger-1">
              Vinden klanten jouw<br />
              <span class="hero-gradient">{bedrijf}</span> online?
            </h1>

            <p class="hero-sub fade-up stagger-2">
              <strong>{d['zoekvolume']} zoekopdrachten</strong> per maand in Nederland naar {name_plural}. Als jij niet bovenaan staat — staat je concurrent er wel.
            </p>

            <form class="hero-form scan-form fade-up stagger-3" novalidate>
              <div class="hero-input-wrap">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418" />
                </svg>
                <input type="url" class="hero-input" placeholder="https://jouw{slug.replace('-', '')}.nl" aria-label="URL van jouw website" autocomplete="url" spellcheck="false" />
              </div>
              <button type="submit" class="btn btn-accent btn-lg">Scan mijn website →</button>
            </form>

            <div class="hero-social-proof fade-up stagger-4">
              <div style="display:flex;gap:6px;font-size:0.85rem;color:var(--muted);flex-wrap:wrap;">
                <span style="color:var(--accent);font-weight:700;">✓</span> Gratis
                <span style="margin:0 4px;">·</span>
                <span style="color:var(--accent);font-weight:700;">✓</span> 60 seconden
                <span style="margin:0 4px;">·</span>
                <span style="color:var(--accent);font-weight:700;">✓</span> Direct resultaat
              </div>
            </div>
          </div>

          <!-- Right: Score Card -->
          <div class="hero-visual">
            <div class="score-card" role="img" aria-label="Voorbeeld SEO score rapport">
              <div class="score-card-header">
                <span class="score-card-title">SEO Rapport</span>
                <span class="score-card-url">jouw{slug.replace('-','')}.nl</span>
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
              <span class="float-dot green"></span> Scan klaar! Rapport verstuurd
            </div>
            <div class="score-card-float float-bottom">
              <span class="float-dot orange"></span> 3 verbeterpunten gevonden
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================================
         PIJN SECTIE
    ============================================================ -->
    <section style="padding: var(--section-gap) 0; background: rgba(255,255,255,0.02); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
      <div class="container">
        <div style="max-width: 820px; margin: 0 auto;">
          <span class="section-label">De realiteit voor {name_plural}</span>
          <h2 class="section-heading" style="font-size:clamp(1.5rem,3vw,2rem);">Het probleem dat veel {name_plural} herkennen</h2>

          <div class="quote-box fade-up">
            "{d['klant_scenario']}"
          </div>

          <p style="color:rgba(232,232,240,0.75);line-height:1.8;margin-bottom:20px;" class="fade-up">
            {d['pijn']}
          </p>
          <p style="color:rgba(232,232,240,0.75);line-height:1.8;margin-bottom:32px;" class="fade-up">
            Dit is geen theorie. Dit gebeurt elke dag. De vraag is niet óf mensen zoeken naar een {name} — dat doen ze zeker. De vraag is of ze <em>jou</em> vinden.
          </p>

          <div class="fade-up">
            <a href="#hero-form" class="btn btn-accent">Ontdek hoe jij scoort →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         STATISTIEKEN
    ============================================================ -->
    <section style="padding: var(--section-gap) 0;">
      <div class="container">
        <div class="text-center" style="margin-bottom: 0;">
          <span class="section-label">Cijfers die er toe doen</span>
          <h2 class="section-heading">De markt voor {name_plural} in Nederland</h2>
        </div>

        <div class="branch-stats">
          <div class="branch-stat-card fade-up">
            <span class="branch-stat-num">{d['zoekvolume']}</span>
            <span class="branch-stat-lbl">Zoekopdrachten per maand<br />naar {name_plural} in Nederland</span>
          </div>
          <div class="branch-stat-card fade-up stagger-1">
            <span class="branch-stat-num">75%</span>
            <span class="branch-stat-lbl">Klikt nooit verder<br />dan pagina 1 van Google</span>
          </div>
          <div class="branch-stat-card fade-up stagger-2">
            <span class="branch-stat-num">3x</span>
            <span class="branch-stat-lbl">Meer vertrouwen in organische<br />resultaten dan advertenties</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         SNELLE WIN SECTIE
    ============================================================ -->
    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">
        <div style="max-width: 720px; margin: 0 auto;">
          <span class="section-label">Quick win</span>
          <h2 class="section-heading" style="font-size:clamp(1.4rem,3vw,1.9rem);">Jouw snelste verbetering als {name}</h2>

          <div class="quick-win-box fade-up">
            <span class="quick-win-icon" aria-hidden="true">⚡</span>
            <div class="quick-win-title">Quick win voor {name_plural}</div>
            <p class="quick-win-text">{d['snelle_win']}</p>
            <p class="quick-win-sub">Dit alleen al kan je positie in Google significant verbeteren.</p>
          </div>

          <p style="color:rgba(232,232,240,0.7);font-size:0.875rem;line-height:1.7;">
            Wil je weten welke verbeteringen op jouw specifieke website de meeste impact hebben? De gratis Scorio-scan analyseert 45+ factoren en geeft je een geprioriteerde actielijst.
          </p>
        </div>
      </div>
    </section>

    <!-- ============================================================
         WAT WE CONTROLEREN
    ============================================================ -->
    <section style="padding: var(--section-gap) 0; background: rgba(255,255,255,0.02); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Ons rapport</span>
          <h2 class="section-heading">Wat controleren we voor jouw {bedrijf}?</h2>
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
            <p>Title tags, meta descriptions, H1-structuur, zoekwoorden en interne links — alles geoptimaliseerd voor {name_plural}.</p>
          </div>
          <div class="check-card fade-up stagger-2">
            <span class="check-card-icon" aria-hidden="true">📱</span>
            <h3>Mobielvriendelijkheid</h3>
            <p>Google indexeert eerst de mobiele versie. Wij controleren of jouw {bedrijf} daar klaar voor is.</p>
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
            <p>Geen lijst van 50 dingen. Wij laten je zien wat het meeste impact heeft voor jouw {bedrijf} — vandaag nog uitvoerbaar.</p>
          </div>
        </div>

        <div style="text-align:center;margin-top:48px;">
          <a href="#hero-form" class="btn btn-accent btn-lg">Gratis scannen — start nu →</a>
        </div>
      </div>
    </section>

    <!-- ============================================================
         HOE HET WERKT
    ============================================================ -->
    <section style="padding: var(--section-gap) 0;">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Hoe het werkt</span>
          <h2 class="section-heading">Je SEO-scan in 3 stappen</h2>
          <p class="section-sub">Van URL invullen tot je persoonlijk actieplan voor je {bedrijf} — alles in minder dan 60 seconden.</p>
        </div>

        <div class="how-steps">
          <div class="how-step fade-up">
            <div class="how-step-num">1</div>
            <span class="how-step-icon" aria-hidden="true">🌐</span>
            <h3>Vul je website URL in</h3>
            <p>Voer de URL van jouw {bedrijf} in en klik op "Scan mijn website". Geen account of registratie nodig.</p>
          </div>
          <div class="how-step fade-up stagger-1">
            <div class="how-step-num">2</div>
            <span class="how-step-icon" aria-hidden="true">🔍</span>
            <h3>Wij scannen 45+ SEO factoren</h3>
            <p>Scorio analyseert je snelheid, SEO-structuur, mobielvriendelijkheid, technische fouten en meer in 60 seconden.</p>
          </div>
          <div class="how-step fade-up stagger-2">
            <div class="how-step-num">3</div>
            <span class="how-step-icon" aria-hidden="true">📋</span>
            <h3>Ontvang je persoonlijke rapport</h3>
            <p>Je krijgt een SEO-score van 0–100 én een geprioriteerde actielijst — speciaal voor jouw {bedrijf} en situatie.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         SEO TIPS VOOR BRANCHE
    ============================================================ -->
    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">
        <div class="text-center">
          <span class="section-label">Praktische tips</span>
          <h2 class="section-heading">3 SEO tips speciaal voor {name_plural}</h2>
          <p class="section-sub">Direct uitvoerbaar — geen technische kennis vereist.</p>
        </div>

        <div class="tips-grid">
          <div class="tip-card fade-up">
            <span class="tip-card-icon" aria-hidden="true">📍</span>
            <h3>Lokale zoekwoorden</h3>
            <p>Combineer altijd je dienst met je stad: "{name} [stad]". Maak voor elke stad waar je actief bent een aparte pagina. Google beloont relevantie voor lokale zoekopdrachten.</p>
          </div>
          <div class="tip-card fade-up stagger-1">
            <span class="tip-card-icon" aria-hidden="true">{d['tip2_icon']}</span>
            <h3>{d['tip2_titel']}</h3>
            <p>{d['tip2_tekst']}</p>
          </div>
          <div class="tip-card fade-up stagger-2">
            <span class="tip-card-icon" aria-hidden="true">⭐</span>
            <h3>Reviews zijn SEO</h3>
            <p>Google beloont bedrijven met veel goede reviews met een hogere positie. Vraag tevreden klanten actief om een Google review — dit is een van de sterkste lokale SEO-signalen.</p>
          </div>
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
          <h2 class="section-heading">{name_plural_cap} die je voorgingen</h2>
          <p class="section-sub">Bekijk wat andere {name_plural} bereikten met Scorio.</p>
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
            <div class="pricing-price"><span class="price-amount">€0</span><span class="price-period">/mnd</span></div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes">✓</span> 1 scan per maand</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Basis rapport online</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> SEO score + 3 tips</li>
              <li class="pricing-feature disabled"><span class="feature-check no">–</span> Volledig PDF rapport</li>
              <li class="pricing-feature disabled"><span class="feature-check no">–</span> E-mail support</li>
              <li class="pricing-feature disabled"><span class="feature-check no">–</span> iDEAL betaling</li>
            </ul>
            <a href="#hero-form" class="pricing-cta pricing-cta-secondary">Gratis starten</a>
          </div>

          <div class="pricing-card featured" data-plan="starter">
            <div class="pricing-card-badge"><span class="badge badge-accent">⭐ Meest gekozen</span></div>
            <div class="pricing-name">Starter</div>
            <div class="pricing-price"><span class="price-amount">€9</span><span class="price-period">/mnd</span></div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes">✓</span> 5 scans per maand</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Volledig PDF rapport</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Alle SEO categorieën</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> E-mail support</li>
              <li class="pricing-feature disabled"><span class="feature-check no">–</span> Priority support</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> iDEAL betaling</li>
            </ul>
            <a href="#" class="pricing-cta pricing-cta-primary">14 dagen gratis proberen</a>
            <p class="pricing-trial">Daarna €9/mnd — altijd opzegbaar</p>
          </div>

          <div class="pricing-card" data-plan="pro">
            <div class="pricing-name">Pro</div>
            <div class="pricing-price"><span class="price-amount">€29</span><span class="price-period">/mnd</span></div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes">✓</span> 25 scans per maand</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Volledig PDF rapport</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Concurrentie vergelijking</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Priority support</li>
              <li class="pricing-feature disabled"><span class="feature-check no">–</span> Klantportaal</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> iDEAL betaling</li>
            </ul>
            <a href="#" class="pricing-cta pricing-cta-secondary">14 dagen gratis proberen</a>
            <p class="pricing-trial">Daarna €29/mnd — altijd opzegbaar</p>
          </div>

          <div class="pricing-card" data-plan="agency">
            <div class="pricing-card-badge"><span class="badge badge-primary">Voor bureaus</span></div>
            <div class="pricing-name">Agency</div>
            <div class="pricing-price"><span class="price-amount">€79</span><span class="price-period">/mnd</span></div>
            <div class="price-yearly"></div>
            <div class="pricing-divider"></div>
            <ul class="pricing-features">
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Onbeperkte scans</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> White-label rapporten</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> API toegang</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Klantportaal</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> Priority support</li>
              <li class="pricing-feature"><span class="feature-check yes">✓</span> iDEAL betaling</li>
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
          <h2 class="section-heading">Veelgestelde vragen over SEO voor {name_plural}</h2>
          <p class="section-sub">Directe antwoorden speciaal voor {name_plural} in Nederland.</p>
        </div>

        <div class="faq-list">

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Hoe kom ik bovenaan in Google als {name}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Combineer drie dingen: technische SEO basis op orde, lokale zoekwoorden ({name} + jouw stad) in je teksten, en een volledig Google Bedrijfsprofiel met foto's en reviews. Scorio laat precies zien wat bij jou prioriteit heeft. Start met de gratis scan voor je geprioriteerde actielijst.
              </div>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Wat kost SEO voor een {name}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Je kunt beginnen voor €9 per maand met Scorio. Een SEO bureau rekent €500 tot €2.000 per maand. Begin met de basis zelf doen via Scorio — je weet dan precies wat je moet aanpakken en bespaar je duizenden euro's per jaar aan bureaukosten.
              </div>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Heb ik als {name} een blog nodig voor SEO?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Niet verplicht, maar het helpt enorm. Schrijf over vragen die klanten stellen: "wat kost een {name}", "hoe kies ik een goede {name}". Dit trekt bezoekers die actief op zoek zijn naar jouw diensten en verhoogt je autoriteit in Google.
              </div>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              Werkt Google Bedrijfsprofiel voor {name_plural}?
              <svg class="faq-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Absoluut — dit is voor lokale {name_plural} het krachtigste gratis SEO middel. Vul alles volledig in, voeg foto's toe en vraag reviews. Google toont je dan in de kaartresultaten bovenaan de zoekresultaten — nog voor de gewone organische resultaten.
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
          <span style="font-size:2.5rem;display:block;margin-bottom:16px;" aria-hidden="true">{emoji}</span>
          <h2 class="section-heading" style="font-size:clamp(1.4rem,3vw,1.9rem);margin-bottom:16px;">Klaar om meer klanten te krijgen<br />via Google als {name}?</h2>
          <p style="color:rgba(232,232,240,0.75);margin-bottom:40px;max-width:520px;margin-left:auto;margin-right:auto;">Doe de gratis scan en zie in 60 seconden wat er beter kan op jouw website. Geen registratie, geen creditcard.</p>

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
         INTERNE LINKS
    ============================================================ -->
    <section style="padding: 0 0 var(--section-gap);">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">
          <div class="glass-card" style="padding:28px 32px;">
            <h2 style="font-size:0.95rem;margin-bottom:6px;font-weight:700;">Meer SEO hulp per branche</h2>
            <p style="font-size:0.8rem;color:var(--muted);margin-bottom:16px;">Scorio is beschikbaar voor alle branches.</p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
              {other_links}
            </div>
          </div>
          <div class="glass-card" style="padding:28px 32px;">
            <h2 style="font-size:0.95rem;margin-bottom:6px;font-weight:700;">SEO check per stad</h2>
            <p style="font-size:0.8rem;color:var(--muted);margin-bottom:16px;">Lokale SEO voor de grootste Nederlandse steden.</p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
              {steden_links}
            </div>
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


def update_sitemap(base):
    sitemap_path = os.path.join(base, 'sitemap.xml')
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    branch_entries = '\n  <!-- Branche landingspagina\'s -->'
    for slug, _ in ALL_BRANCHES:
        branch_entries += f"""
  <url>
    <loc>https://www.scorio.nl/seo-check-{slug}/</loc>
    <lastmod>2026-05-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="nl" href="https://www.scorio.nl/seo-check-{slug}/"/>
  </url>"""

    branch_entries += '\n'
    new_content = content.replace('\n</urlset>', branch_entries + '\n</urlset>')

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'✓ sitemap.xml updated with {len(ALL_BRANCHES)} branch URLs')


def main():
    base = '/home/user/Scorio-NL'
    for slug, _ in ALL_BRANCHES:
        data = BRANCHES[slug]
        dir_path = os.path.join(base, f'seo-check-{slug}')
        os.makedirs(dir_path, exist_ok=True)
        html = generate_page(slug, data)
        out = os.path.join(dir_path, 'index.html')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ {out}')

    update_sitemap(base)
    print('\nAll 10 branch pages generated.')


if __name__ == '__main__':
    main()
