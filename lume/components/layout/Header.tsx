'use client'

import Link from 'next/link'
import { useState } from 'react'
import { Menu, X, ShoppingBag } from 'lucide-react'
import LumeLogo from '@/components/ui/LumeLogo'

export default function Header() {
  const [open, setOpen] = useState(false)

  return (
    <header
      style={{ borderBottom: '1px solid var(--lume-border)', backgroundColor: 'var(--lume-cream)' }}
      className="sticky top-0 z-50"
    >
      <div className="max-w-6xl mx-auto px-6 flex items-center justify-between h-16">
        <Link href="/" aria-label="Lumé home">
          <LumeLogo />
        </Link>

        {/* Desktop nav */}
        <nav className="hidden md:flex items-center gap-8 font-inter text-sm font-medium" style={{ color: 'var(--lume-stone)' }}>
          <Link href="/#pakketten" className="hover:opacity-60 transition-opacity">Pakketten</Link>
          <Link href="/quiz" className="hover:opacity-60 transition-opacity">Huidquiz</Link>
          <Link href="/blog" className="hover:opacity-60 transition-opacity">Blog</Link>
          <Link href="/over-ons" className="hover:opacity-60 transition-opacity">Over ons</Link>
        </nav>

        <div className="hidden md:flex items-center gap-4">
          <Link
            href="/quiz"
            className="px-5 py-2 text-sm font-medium text-white rounded-btn transition-opacity hover:opacity-90"
            style={{ backgroundColor: 'var(--lume-terra)' }}
          >
            Start de quiz
          </Link>
          <button aria-label="Winkelwagen" className="relative hover:opacity-60 transition-opacity">
            <ShoppingBag size={20} style={{ color: 'var(--lume-stone)' }} />
          </button>
        </div>

        {/* Mobile */}
        <button
          className="md:hidden"
          onClick={() => setOpen(!open)}
          aria-label="Menu"
        >
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      {open && (
        <div
          className="md:hidden border-t px-6 py-6 flex flex-col gap-5 text-sm font-medium"
          style={{ borderColor: 'var(--lume-border)', backgroundColor: 'var(--lume-cream)' }}
        >
          <Link href="/#pakketten" onClick={() => setOpen(false)}>Pakketten</Link>
          <Link href="/quiz" onClick={() => setOpen(false)}>Huidquiz</Link>
          <Link href="/blog" onClick={() => setOpen(false)}>Blog</Link>
          <Link href="/over-ons" onClick={() => setOpen(false)}>Over ons</Link>
          <Link
            href="/quiz"
            onClick={() => setOpen(false)}
            className="inline-block text-center px-5 py-3 text-sm font-medium text-white rounded-btn"
            style={{ backgroundColor: 'var(--lume-terra)' }}
          >
            Start de huidquiz
          </Link>
        </div>
      )}
    </header>
  )
}
