import Link from 'next/link'
import { Check } from 'lucide-react'

export interface Pakket {
  id: string
  naam: string
  tagline: string
  prijs: number
  huidtype: string
  kleur: string
  badge?: string
  producten: string[]
  shopifyHandle: string
}

export default function PakketCard({ pakket, featured = false }: { pakket: Pakket; featured?: boolean }) {
  return (
    <div
      className="relative flex flex-col rounded-card overflow-hidden transition-transform hover:-translate-y-1"
      style={{
        border: featured ? '2px solid var(--lume-terra)' : '1px solid var(--lume-border)',
        backgroundColor: 'white',
      }}
    >
      {pakket.badge && (
        <div
          className="absolute top-4 right-4 text-xs font-medium px-3 py-1 rounded-pill text-white"
          style={{ backgroundColor: 'var(--lume-terra)' }}
        >
          {pakket.badge}
        </div>
      )}

      {/* Color strip */}
      <div className="h-2 w-full" style={{ backgroundColor: pakket.kleur }} />

      <div className="p-8 flex flex-col flex-1">
        <div
          className="text-xs font-medium uppercase tracking-wider mb-2 rounded-pill inline-block px-3 py-1 self-start"
          style={{ backgroundColor: 'var(--lume-blush)', color: 'var(--lume-terra)' }}
        >
          {pakket.huidtype}
        </div>

        <h3
          className="text-2xl mt-2 mb-1"
          style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
        >
          {pakket.naam}
        </h3>
        <p className="text-sm mb-6 leading-relaxed" style={{ color: 'rgba(44,37,32,0.65)' }}>
          {pakket.tagline}
        </p>

        <ul className="space-y-2 mb-8 flex-1">
          {pakket.producten.map((p) => (
            <li key={p} className="flex items-center gap-2 text-sm" style={{ color: 'var(--lume-stone)' }}>
              <Check size={14} style={{ color: 'var(--lume-sage)', flexShrink: 0 }} />
              {p}
            </li>
          ))}
        </ul>

        <div className="flex items-end justify-between">
          <div>
            <p className="text-3xl font-light" style={{ fontFamily: 'Cormorant Garamond, serif' }}>
              €{pakket.prijs}
            </p>
            <p className="text-xs" style={{ color: 'rgba(44,37,32,0.5)' }}>incl. BTW &amp; gratis verzending</p>
          </div>
          <Link
            href={`/quiz`}
            className="px-5 py-2.5 text-sm font-medium rounded-btn transition-opacity hover:opacity-80"
            style={{
              backgroundColor: featured ? 'var(--lume-terra)' : 'transparent',
              color: featured ? 'white' : 'var(--lume-stone)',
              border: featured ? 'none' : '1px solid var(--lume-stone)',
            }}
          >
            {featured ? 'Kies dit pakket' : 'Meer info'}
          </Link>
        </div>
      </div>
    </div>
  )
}
