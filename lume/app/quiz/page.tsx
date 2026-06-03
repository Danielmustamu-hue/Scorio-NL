import QuizWizard from '@/components/quiz/QuizWizard'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Huidquiz — Lumé Skincare',
  description: 'Beantwoord 5 vragen en ontdek welk Lumé skincare pakket bij jouw huidtype past.',
}

export default function QuizPage() {
  return (
    <section className="min-h-screen py-16 px-6" style={{ backgroundColor: 'var(--lume-cream)' }}>
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <span
            className="inline-block text-xs font-medium uppercase tracking-widest mb-4 px-3 py-1 rounded-pill"
            style={{ backgroundColor: 'var(--lume-blush)', color: 'var(--lume-terra)' }}
          >
            Jouw persoonlijke huidanalyse
          </span>
          <h1
            className="text-4xl md:text-5xl mb-4"
            style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
          >
            Ontdek jouw perfecte routine
          </h1>
          <p className="text-base" style={{ color: 'rgba(44,37,32,0.65)' }}>
            5 vragen. 5 minuten. Jouw persoonlijk verzorgingsadvies.
          </p>
        </div>

        <QuizWizard />
      </div>
    </section>
  )
}
