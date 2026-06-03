import Link from 'next/link'
import { Leaf, Shield, Package, ArrowRight } from 'lucide-react'
import PakketCard from '@/components/products/PakketCard'
import { pakketten } from '@/lib/pakketten'

export default function HomePage() {
  return (
    <>
      {/* HERO */}
      <section
        className="min-h-screen flex items-center"
        style={{ backgroundColor: 'var(--lume-cream)' }}
      >
        <div className="max-w-6xl mx-auto px-6 py-24 grid grid-cols-1 md:grid-cols-2 gap-12 items-center w-full">
          <div>
            <span
              className="inline-block text-xs font-medium uppercase tracking-widest mb-6 px-3 py-1 rounded-pill"
              style={{ backgroundColor: 'var(--lume-blush)', color: 'var(--lume-terra)' }}
            >
              Jouw huid, jouw routine.
            </span>
            <h1
              className="text-5xl md:text-6xl lg:text-7xl leading-tight mb-6"
              style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
            >
              Jouw huid verdient precies het goede.
            </h1>
            <p
              className="text-lg leading-relaxed mb-8 max-w-lg"
              style={{ color: 'rgba(44,37,32,0.7)', fontFamily: 'Inter, sans-serif' }}
            >
              Onze quiz analyseert jouw huidtype en stelt een persoonlijk verzorgingspakket samen.
              Wetenschappelijk onderbouwd. Zonder overbodige ingrediënten.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link
                href="/quiz"
                className="inline-flex items-center justify-center gap-2 px-7 py-3.5 text-sm font-medium text-white rounded-btn transition-opacity hover:opacity-90"
                style={{ backgroundColor: 'var(--lume-terra)' }}
              >
                Start de huidquiz
                <ArrowRight size={16} />
              </Link>
              <Link
                href="/#pakketten"
                className="inline-flex items-center justify-center px-7 py-3.5 text-sm font-medium rounded-btn transition-opacity hover:opacity-70"
                style={{ border: '1px solid var(--lume-stone)', color: 'var(--lume-stone)' }}
              >
                Bekijk pakketten
              </Link>
            </div>
          </div>

          <div className="relative">
            <div
              className="relative w-full overflow-hidden"
              style={{ aspectRatio: '4/5', borderRadius: '16px', backgroundColor: 'var(--lume-blush)' }}
            >
              <div
                className="absolute inset-0 flex items-center justify-center"
                style={{ color: 'rgba(44,37,32,0.2)' }}
              >
                <div className="text-center">
                  <div style={{ fontSize: '64px' }}>✦</div>
                  <p className="text-sm mt-2" style={{ fontFamily: 'Cormorant Garamond, serif', fontSize: '18px' }}>
                    Lumé Skincare
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* TRUST BAR */}
      <section style={{ backgroundColor: 'var(--lume-blush)' }}>
        <div className="max-w-6xl mx-auto px-6 py-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-0 md:divide-x" style={{ '--tw-divide-opacity': 1 } as React.CSSProperties}>
            {[
              { icon: <Leaf size={18} />, text: 'Vrij van parabenen & sulfaten' },
              { icon: <Shield size={18} />, text: 'Dermatologisch getoetst' },
              { icon: <Package size={18} />, text: 'Gratis verzending vanaf €50' },
            ].map(({ icon, text }) => (
              <div key={text} className="flex items-center justify-center gap-3 px-6 py-2">
                <span style={{ color: 'var(--lume-terra)' }}>{icon}</span>
                <span className="text-sm font-medium" style={{ color: 'var(--lume-stone)' }}>{text}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="py-24" style={{ backgroundColor: 'var(--lume-cream)' }}>
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2
              className="text-4xl md:text-5xl"
              style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
            >
              Van quiz tot routine in 5 minuten
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                nr: '01',
                titel: 'Vertel over je huid',
                tekst: 'Beantwoord 5 korte vragen over jouw huidtype, klachten en verzorgingsdoelen.',
              },
              {
                nr: '02',
                titel: 'Ontvang jouw advies',
                tekst: 'Onze logica matcht jouw profiel aan het beste pakket. Persoonlijk, niet generiek.',
              },
              {
                nr: '03',
                titel: 'Begin je nieuwe routine',
                tekst: 'Bestel direct. Gratis verzending, volgende dag in huis. Geen abonnement nodig.',
              },
            ].map((stap) => (
              <div
                key={stap.nr}
                className="p-8 rounded-card"
                style={{ border: '1px solid var(--lume-border)', backgroundColor: 'white' }}
              >
                <div
                  className="text-xs font-medium mb-4"
                  style={{ color: 'var(--lume-terra)', fontFamily: 'Inter, sans-serif', letterSpacing: '0.1em' }}
                >
                  {stap.nr}
                </div>
                <h3
                  className="text-2xl mb-3"
                  style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
                >
                  {stap.titel}
                </h3>
                <p className="text-sm leading-relaxed" style={{ color: 'rgba(44,37,32,0.65)' }}>
                  {stap.tekst}
                </p>
              </div>
            ))}
          </div>

          <div className="text-center mt-12">
            <Link
              href="/quiz"
              className="inline-flex items-center gap-2 px-7 py-3.5 text-sm font-medium text-white rounded-btn transition-opacity hover:opacity-90"
              style={{ backgroundColor: 'var(--lume-terra)' }}
            >
              Start nu de quiz
              <ArrowRight size={16} />
            </Link>
          </div>
        </div>
      </section>

      {/* PAKKETTEN */}
      <section
        id="pakketten"
        className="py-24"
        style={{ backgroundColor: 'var(--lume-blush)' }}
      >
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2
              className="text-4xl md:text-5xl mb-4"
              style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
            >
              Drie routines, één doel: een gezonde huid
            </h2>
            <p className="text-base" style={{ color: 'rgba(44,37,32,0.65)' }}>
              Of doe de quiz en ontdek welk pakket bij jou past.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {pakketten.map((pakket, i) => (
              <PakketCard key={pakket.id} pakket={pakket} featured={i === 1} />
            ))}
          </div>
        </div>
      </section>

      {/* INGREDIËNTEN FILOSOFIE */}
      <section className="py-24" style={{ backgroundColor: 'var(--lume-mist)' }}>
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
            <div>
              <span
                className="inline-block text-xs font-medium uppercase tracking-widest mb-4 px-3 py-1 rounded-pill"
                style={{ backgroundColor: 'var(--lume-blush)', color: 'var(--lume-terra)' }}
              >
                Onze filosofie
              </span>
              <h2
                className="text-4xl md:text-5xl mb-6 leading-tight"
                style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
              >
                Wij geloven in minder, beter.
              </h2>
              <p className="text-base leading-relaxed" style={{ color: 'rgba(44,37,32,0.7)' }}>
                Geen lange lijsten van ingrediënten die je niet kunt uitspreken. Geen marketingbuzz.
                Alleen wat je huid écht nodig heeft — in de juiste concentraties, wetenschappelijk onderbouwd.
              </p>
            </div>

            <div>
              <h3
                className="text-lg mb-6 font-medium"
                style={{ color: 'var(--lume-stone)', fontFamily: 'Cormorant Garamond, serif', fontSize: '22px' }}
              >
                Wat wél in onze producten zit:
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  { naam: 'Hyaluronzuur', beschrijving: 'Intensieve hydratatie diep in de huid' },
                  { naam: 'Niacinamide', beschrijving: 'Vermindert poriën en egalisert teint' },
                  { naam: 'Ceramiden', beschrijving: 'Herstelt de huidbarrière' },
                  { naam: 'Peptiden', beschrijving: 'Stimuleert collageenproductie' },
                  { naam: 'Centella Asiatica', beschrijving: 'Kalmeert en herstelt geïrriteerde huid' },
                  { naam: 'SPF50', beschrijving: 'Brede bescherming UVA/UVB' },
                ].map((ing) => (
                  <div
                    key={ing.naam}
                    className="p-4 rounded-card"
                    style={{ backgroundColor: 'white', border: '1px solid var(--lume-border)' }}
                  >
                    <p className="text-sm font-medium mb-1" style={{ color: 'var(--lume-stone)' }}>{ing.naam}</p>
                    <p className="text-xs leading-relaxed" style={{ color: 'rgba(44,37,32,0.6)' }}>{ing.beschrijving}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA BOTTOM */}
      <section className="py-24" style={{ backgroundColor: 'var(--lume-cream)' }}>
        <div className="max-w-2xl mx-auto px-6 text-center">
          <h2
            className="text-4xl md:text-5xl mb-6"
            style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
          >
            Klaar om je huid te leren kennen?
          </h2>
          <p className="text-base mb-8" style={{ color: 'rgba(44,37,32,0.65)' }}>
            Doe de quiz en ontdek in 5 minuten welk Lumé pakket bij jou past.
          </p>
          <Link
            href="/quiz"
            className="inline-flex items-center gap-2 px-8 py-4 text-sm font-medium text-white rounded-btn transition-opacity hover:opacity-90"
            style={{ backgroundColor: 'var(--lume-terra)' }}
          >
            Start de huidquiz
            <ArrowRight size={16} />
          </Link>
        </div>
      </section>
    </>
  )
}
