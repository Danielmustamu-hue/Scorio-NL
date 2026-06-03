import type { Metadata } from 'next'
import Link from 'next/link'
import { ArrowRight } from 'lucide-react'

export const metadata: Metadata = {
  title: 'Over ons — Lumé Skincare',
  description: 'Leer meer over het verhaal achter Lumé — clean skincare voor de Nederlandse vrouw.',
}

export default function OverOnsPage() {
  return (
    <section className="py-24 px-6" style={{ backgroundColor: 'var(--lume-cream)' }}>
      <div className="max-w-4xl mx-auto">
        <span
          className="inline-block text-xs font-medium uppercase tracking-widest mb-6 px-3 py-1 rounded-pill"
          style={{ backgroundColor: 'var(--lume-blush)', color: 'var(--lume-terra)' }}
        >
          Ons verhaal
        </span>

        <h1
          className="text-5xl md:text-6xl mb-8 leading-tight"
          style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
        >
          Skincare zonder ruis.
        </h1>

        <div className="prose max-w-none space-y-8">
          <p className="text-lg leading-relaxed" style={{ color: 'rgba(44,37,32,0.75)' }}>
            Lumé is ontstaan uit een eenvoudige frustratie: te veel producten, te weinig resultaat.
            De gemiddelde Nederlandse vrouw gebruikt dagelijks acht verschillende huidverzorgingsproducten.
            Wij geloven dat er een betere manier is.
          </p>

          <div
            className="p-8 rounded-card"
            style={{ backgroundColor: 'var(--lume-blush)', borderLeft: '3px solid var(--lume-terra)' }}
          >
            <blockquote
              className="text-2xl leading-relaxed"
              style={{ fontFamily: 'Cormorant Garamond, serif', fontStyle: 'italic', color: 'var(--lume-stone)' }}
            >
              &ldquo;Jouw huid heeft niet meer nodig dan wat écht werkt. Wij zorgen voor de rest.&rdquo;
            </blockquote>
          </div>

          <p className="text-base leading-relaxed" style={{ color: 'rgba(44,37,32,0.7)' }}>
            Elk Lumé product is ontwikkeld in samenwerking met dermatologen en formulisten.
            Geen marketing-ingrediënten in verwaarloosbare hoeveelheden — alleen actieve stoffen
            in bewezen werkzame concentraties.
          </p>

          <p className="text-base leading-relaxed" style={{ color: 'rgba(44,37,32,0.7)' }}>
            We zijn trots op wat we níet doen: geen parabenen, geen sulfaten, geen kunstmatige geurstoffen,
            geen overdreven verpakkingen. Lumé is geformuleerd voor de Nederlandse huid, getest door
            Nederlandse dermatologen, en gebouwd rondom het principe dat minder écht meer is.
          </p>
        </div>

        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            { cijfer: '3', label: 'Pakketten, zorgvuldig samengesteld' },
            { cijfer: '6', label: 'Kernactieve ingrediënten' },
            { cijfer: '100%', label: 'Vrij van parabenen & sulfaten' },
          ].map((stat) => (
            <div
              key={stat.cijfer}
              className="p-8 rounded-card text-center"
              style={{ border: '1px solid var(--lume-border)', backgroundColor: 'white' }}
            >
              <p
                className="text-5xl mb-2"
                style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-terra)' }}
              >
                {stat.cijfer}
              </p>
              <p className="text-sm" style={{ color: 'rgba(44,37,32,0.65)' }}>{stat.label}</p>
            </div>
          ))}
        </div>

        <div className="mt-16 text-center">
          <Link
            href="/quiz"
            className="inline-flex items-center gap-2 px-7 py-3.5 text-sm font-medium text-white rounded-btn transition-opacity hover:opacity-90"
            style={{ backgroundColor: 'var(--lume-terra)' }}
          >
            Start de huidquiz
            <ArrowRight size={16} />
          </Link>
        </div>
      </div>
    </section>
  )
}
