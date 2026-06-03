'use client'

import { useSearchParams } from 'next/navigation'
import Link from 'next/link'
import { Check, RotateCcw } from 'lucide-react'
import { pakketten } from '@/lib/pakketten'
import PakketCard from '@/components/products/PakketCard'

export default function ResultaatContent() {
  const params = useSearchParams()
  const pakketId = params.get('pakket') || 'balance'
  const aanbevolen = pakketten.find((p) => p.id === pakketId) || pakketten[1]
  const overige = pakketten.filter((p) => p.id !== pakketId)

  return (
    <section className="min-h-screen py-16 px-6" style={{ backgroundColor: 'var(--lume-cream)' }}>
      <div className="max-w-6xl mx-auto">
        {/* Result header */}
        <div className="text-center mb-16">
          <div
            className="inline-flex items-center gap-2 text-xs font-medium uppercase tracking-widest mb-6 px-4 py-2 rounded-pill"
            style={{ backgroundColor: 'var(--lume-mist)', color: 'var(--lume-sage)' }}
          >
            <Check size={12} />
            Jouw analyse is klaar
          </div>
          <h1
            className="text-4xl md:text-5xl mb-4"
            style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
          >
            Wij raden jou aan:
          </h1>
          <p className="text-base" style={{ color: 'rgba(44,37,32,0.65)' }}>
            Op basis van jouw antwoorden is dit jouw persoonlijke routine.
          </p>
        </div>

        {/* Recommended pakket */}
        <div className="max-w-md mx-auto mb-20">
          <PakketCard pakket={aanbevolen} featured />
          <div className="mt-6 text-center">
            <Link
              href={`/quiz`}
              className="inline-flex items-center gap-2 text-sm"
              style={{ color: 'rgba(44,37,32,0.55)' }}
            >
              <RotateCcw size={13} />
              Quiz opnieuw doen
            </Link>
          </div>
        </div>

        {/* Other options */}
        <div>
          <h2
            className="text-2xl text-center mb-8"
            style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
          >
            Andere opties voor jou
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-3xl mx-auto">
            {overige.map((p) => (
              <PakketCard key={p.id} pakket={p} />
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
