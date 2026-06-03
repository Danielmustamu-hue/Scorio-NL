import type { Metadata } from 'next'
import Link from 'next/link'
import { ArrowRight } from 'lucide-react'

export const metadata: Metadata = {
  title: 'Blog — Lumé Skincare',
  description: 'Lees over huidverzorging, ingrediënten en routines op de Lumé blog.',
}

const artikelen = [
  {
    slug: 'hyaluronzuur-uitgelegd',
    titel: 'Hyaluronzuur: wat het is en waarom jouw huid het nodig heeft',
    categorie: 'Ingrediënten',
    datum: '12 november 2024',
    leestijd: '4 min',
    intro:
      'Hyaluronzuur is een van de meest besproken ingrediënten in skincare — maar wat doet het eigenlijk? We leggen het uit.',
  },
  {
    slug: 'ochtendroutine-opbouwen',
    titel: 'Hoe bouw je een effectieve ochtendroutine op in 3 stappen',
    categorie: 'Routines',
    datum: '5 november 2024',
    leestijd: '5 min',
    intro:
      'Een goede ochtendroutine hoeft niet ingewikkeld te zijn. Met de juiste stappen bescherm je je huid de hele dag.',
  },
  {
    slug: 'niacinamide-voordelen',
    titel: 'Niacinamide: het multi-talent in onze Lumé Balance formule',
    categorie: 'Ingrediënten',
    datum: '28 oktober 2024',
    leestijd: '6 min',
    intro:
      'Niacinamide doet meer dan je denkt: van porienverkleinend tot brightening. Alles over dit veelzijdige ingrediënt.',
  },
  {
    slug: 'spf-elke-dag',
    titel: 'Waarom je ook op bewolkte dagen SPF nodig hebt',
    categorie: 'Bescherming',
    datum: '20 oktober 2024',
    leestijd: '3 min',
    intro:
      'UV-straling dringt door wolken heen. We leggen uit waarom dagelijkse SPF het beste anti-aging product is dat bestaat.',
  },
]

export default function BlogPage() {
  return (
    <section className="py-24 px-6" style={{ backgroundColor: 'var(--lume-cream)' }}>
      <div className="max-w-6xl mx-auto">
        <div className="mb-16">
          <span
            className="inline-block text-xs font-medium uppercase tracking-widest mb-4 px-3 py-1 rounded-pill"
            style={{ backgroundColor: 'var(--lume-blush)', color: 'var(--lume-terra)' }}
          >
            Kennis & inspiratie
          </span>
          <h1
            className="text-5xl md:text-6xl"
            style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
          >
            Lumé Blog
          </h1>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {artikelen.map((artikel) => (
            <article
              key={artikel.slug}
              className="p-8 rounded-card flex flex-col"
              style={{ border: '1px solid var(--lume-border)', backgroundColor: 'white' }}
            >
              <div className="flex items-center gap-3 mb-4">
                <span
                  className="text-xs font-medium px-3 py-1 rounded-pill"
                  style={{ backgroundColor: 'var(--lume-mist)', color: 'var(--lume-sage)' }}
                >
                  {artikel.categorie}
                </span>
                <span className="text-xs" style={{ color: 'rgba(44,37,32,0.45)' }}>
                  {artikel.datum} · {artikel.leestijd}
                </span>
              </div>

              <h2
                className="text-2xl mb-3 leading-snug"
                style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
              >
                {artikel.titel}
              </h2>
              <p className="text-sm leading-relaxed mb-6 flex-1" style={{ color: 'rgba(44,37,32,0.65)' }}>
                {artikel.intro}
              </p>

              <Link
                href={`/blog/${artikel.slug}`}
                className="inline-flex items-center gap-2 text-sm font-medium transition-opacity hover:opacity-70"
                style={{ color: 'var(--lume-terra)' }}
              >
                Lees verder
                <ArrowRight size={14} />
              </Link>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}
