import type { Pakket } from '@/components/products/PakketCard'

export const pakketten: Pakket[] = [
  {
    id: 'essentials',
    naam: 'Lumé Essentials',
    tagline: 'De perfecte basisroutine voor een gezonde, uitgebalanceerde huid.',
    prijs: 55,
    huidtype: 'Normale & gecombineerde huid',
    kleur: '#E8F0E8',
    producten: [
      'Gentle Foaming Cleanser (150ml)',
      'Hydrating Toner met Niacinamide (120ml)',
      'Daily Moisture Cream SPF30 (50ml)',
    ],
    shopifyHandle: 'lume-essentials',
  },
  {
    id: 'balance',
    naam: 'Lumé Balance',
    tagline: 'Gericht op het kalmeren en herstellen van gevoelige of onrustige huid.',
    prijs: 75,
    huidtype: 'Gevoelige & droge huid',
    kleur: '#F0E0D6',
    badge: 'Bestseller',
    producten: [
      'Soothing Milk Cleanser (150ml)',
      'Centella Repair Serum (30ml)',
      'Ceramide Barrier Cream (50ml)',
      'SPF50 Mineral Shield (30ml)',
    ],
    shopifyHandle: 'lume-balance',
  },
  {
    id: 'glow',
    naam: 'Lumé Glow',
    tagline: 'Gerichte aanpak voor een egale teint en zichtbaar stralende huid.',
    prijs: 95,
    huidtype: 'Vette & vlekgevoelige huid',
    kleur: '#FAF6F1',
    producten: [
      'Clarifying Gel Cleanser (150ml)',
      'Niacinamide + Zinc Serum (30ml)',
      'Peptide Renewal Moisturizer (50ml)',
      'AHA/BHA Exfoliant 2× per week (100ml)',
      'SPF50 Mattifying Shield (30ml)',
    ],
    shopifyHandle: 'lume-glow',
  },
]
