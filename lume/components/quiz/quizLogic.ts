export interface QuizVraag {
  id: string
  vraag: string
  opties: { label: string; value: string; beschrijving?: string }[]
}

export interface QuizAntwoorden {
  huidtype: string
  klacht: string
  gevoeligheid: string
  leeftijd: string
  doel: string
}

export const quizVragen: QuizVraag[] = [
  {
    id: 'huidtype',
    vraag: 'Hoe voelt jouw huid aan op het midden van de dag?',
    opties: [
      { label: 'Droog en strak', value: 'droog', beschrijving: 'Huid trekt vaak' },
      { label: 'Vettig en glimmend', value: 'vet', beschrijving: 'Vooral T-zone' },
      { label: 'Gemengd', value: 'gemengd', beschrijving: 'Vet op sommige plekken' },
      { label: 'Normaal en comfortabel', value: 'normaal', beschrijving: 'Geen extremen' },
    ],
  },
  {
    id: 'klacht',
    vraag: 'Wat is je grootste huidzorg op dit moment?',
    opties: [
      { label: 'Uitdroging', value: 'droog' },
      { label: 'Onzuiverheden & poriën', value: 'onzuiverheden' },
      { label: 'Roodheid & irritatie', value: 'gevoelig' },
      { label: 'Ongelijkmatige teint', value: 'teint' },
    ],
  },
  {
    id: 'gevoeligheid',
    vraag: 'Reageert je huid snel op nieuwe producten?',
    opties: [
      { label: 'Ja, vaak roodheid of irritatie', value: 'hoog' },
      { label: 'Soms, kleine reacties', value: 'matig' },
      { label: 'Zelden tot nooit', value: 'laag' },
    ],
  },
  {
    id: 'leeftijd',
    vraag: 'In welke leeftijdscategorie val je?',
    opties: [
      { label: '18–24', value: 'jong' },
      { label: '25–34', value: 'jong_volwassen' },
      { label: '35–44', value: 'volwassen' },
      { label: '45+', value: 'mature' },
    ],
  },
  {
    id: 'doel',
    vraag: 'Wat wil je het liefst bereiken met je huidverzorging?',
    opties: [
      { label: 'Hydrateren & beschermen', value: 'hydratie' },
      { label: 'Kalmeren & herstellen', value: 'kalmering' },
      { label: 'Stralen & egaliseren', value: 'glow' },
      { label: 'Anti-aging & stevig', value: 'antiaging' },
    ],
  },
]

export function bepaalPakket(antwoorden: QuizAntwoorden): string {
  const scores = { essentials: 0, balance: 0, glow: 0 }

  if (antwoorden.huidtype === 'droog') scores.balance += 3
  if (antwoorden.huidtype === 'vet') scores.glow += 3
  if (antwoorden.huidtype === 'gemengd') { scores.glow += 1; scores.essentials += 2 }
  if (antwoorden.huidtype === 'normaal') scores.essentials += 3

  if (antwoorden.klacht === 'droog') scores.balance += 2
  if (antwoorden.klacht === 'onzuiverheden') scores.glow += 2
  if (antwoorden.klacht === 'gevoelig') scores.balance += 2
  if (antwoorden.klacht === 'teint') scores.glow += 2

  if (antwoorden.gevoeligheid === 'hoog') scores.balance += 2
  if (antwoorden.gevoeligheid === 'laag') { scores.glow += 1; scores.essentials += 1 }

  if (antwoorden.doel === 'hydratie') scores.essentials += 2
  if (antwoorden.doel === 'kalmering') scores.balance += 2
  if (antwoorden.doel === 'glow') scores.glow += 2
  if (antwoorden.doel === 'antiaging') { scores.balance += 1; scores.glow += 1 }

  const winner = Object.entries(scores).sort((a, b) => b[1] - a[1])[0][0]
  return winner
}
