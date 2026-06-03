'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { ArrowRight, ArrowLeft, Check } from 'lucide-react'
import { quizVragen, bepaalPakket, type QuizAntwoorden } from './quizLogic'

export default function QuizWizard() {
  const router = useRouter()
  const [stap, setStap] = useState(0)
  const [antwoorden, setAntwoorden] = useState<Partial<QuizAntwoorden>>({})
  const [geselecteerd, setGeselecteerd] = useState<string | null>(null)

  const vraag = quizVragen[stap]
  const isLaatste = stap === quizVragen.length - 1
  const voortgang = ((stap) / quizVragen.length) * 100

  function selecteerOptie(value: string) {
    setGeselecteerd(value)
  }

  function volgende() {
    if (!geselecteerd) return
    const nieuweAntwoorden = { ...antwoorden, [vraag.id]: geselecteerd }
    setAntwoorden(nieuweAntwoorden)

    if (isLaatste) {
      const pakket = bepaalPakket(nieuweAntwoorden as QuizAntwoorden)
      router.push(`/resultaat?pakket=${pakket}`)
    } else {
      setStap(stap + 1)
      setGeselecteerd(null)
    }
  }

  function vorige() {
    if (stap > 0) {
      setStap(stap - 1)
      setGeselecteerd(antwoorden[quizVragen[stap - 1].id as keyof QuizAntwoorden] || null)
    }
  }

  return (
    <div className="max-w-2xl mx-auto">
      {/* Progress */}
      <div className="mb-10">
        <div className="flex justify-between text-xs mb-3 font-medium" style={{ color: 'rgba(44,37,32,0.5)' }}>
          <span>Vraag {stap + 1} van {quizVragen.length}</span>
          <span>{Math.round(voortgang)}% voltooid</span>
        </div>
        <div className="h-1 rounded-full" style={{ backgroundColor: 'var(--lume-border)' }}>
          <div
            className="h-1 rounded-full transition-all duration-500"
            style={{ width: `${voortgang}%`, backgroundColor: 'var(--lume-terra)' }}
          />
        </div>
      </div>

      {/* Question */}
      <h2
        className="text-3xl md:text-4xl mb-8"
        style={{ fontFamily: 'Cormorant Garamond, serif', color: 'var(--lume-stone)' }}
      >
        {vraag.vraag}
      </h2>

      {/* Options */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-10">
        {vraag.opties.map((optie) => {
          const selected = geselecteerd === optie.value
          return (
            <button
              key={optie.value}
              onClick={() => selecteerOptie(optie.value)}
              className="text-left p-5 rounded-card transition-all flex items-start justify-between gap-4"
              style={{
                border: selected ? '2px solid var(--lume-terra)' : '1px solid var(--lume-border)',
                backgroundColor: selected ? 'var(--lume-blush)' : 'white',
              }}
            >
              <div>
                <p className="font-medium text-sm" style={{ color: 'var(--lume-stone)' }}>{optie.label}</p>
                {optie.beschrijving && (
                  <p className="text-xs mt-1" style={{ color: 'rgba(44,37,32,0.55)' }}>{optie.beschrijving}</p>
                )}
              </div>
              {selected && (
                <div
                  className="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5"
                  style={{ backgroundColor: 'var(--lume-terra)' }}
                >
                  <Check size={11} color="white" />
                </div>
              )}
            </button>
          )
        })}
      </div>

      {/* Navigation */}
      <div className="flex items-center justify-between">
        <button
          onClick={vorige}
          disabled={stap === 0}
          className="flex items-center gap-2 text-sm font-medium transition-opacity disabled:opacity-30"
          style={{ color: 'var(--lume-stone)' }}
        >
          <ArrowLeft size={16} />
          Vorige
        </button>

        <button
          onClick={volgende}
          disabled={!geselecteerd}
          className="flex items-center gap-2 px-6 py-3 text-sm font-medium text-white rounded-btn transition-opacity hover:opacity-90 disabled:opacity-40"
          style={{ backgroundColor: 'var(--lume-terra)' }}
        >
          {isLaatste ? 'Bekijk mijn resultaat' : 'Volgende'}
          <ArrowRight size={16} />
        </button>
      </div>
    </div>
  )
}
