import { Suspense } from 'react'
import ResultaatContent from './ResultaatContent'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Jouw resultaat — Lumé Skincare',
  description: 'Jouw persoonlijke skincare aanbeveling op basis van de Lumé huidquiz.',
}

export default function ResultaatPage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center" style={{ backgroundColor: 'var(--lume-cream)' }}>
        <p style={{ color: 'var(--lume-stone)' }}>Jouw resultaat laden…</p>
      </div>
    }>
      <ResultaatContent />
    </Suspense>
  )
}
