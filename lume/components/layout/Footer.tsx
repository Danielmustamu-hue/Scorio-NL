import Link from 'next/link'
import LumeLogo from '@/components/ui/LumeLogo'

export default function Footer() {
  return (
    <footer
      style={{ backgroundColor: 'var(--lume-stone)', color: 'var(--lume-cream)' }}
      className="mt-24"
    >
      <div className="max-w-6xl mx-auto px-6 py-16">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <div className="md:col-span-1">
            <LumeLogo light />
            <p className="mt-4 text-sm leading-relaxed" style={{ color: 'rgba(250,246,241,0.65)' }}>
              Jouw huid, jouw routine. Wetenschappelijk onderbouwd skincare zonder overbodige ingrediënten.
            </p>
          </div>

          <div>
            <h4 className="font-inter font-medium text-sm mb-4" style={{ color: 'var(--lume-terra)' }}>Shop</h4>
            <ul className="space-y-3 text-sm" style={{ color: 'rgba(250,246,241,0.65)' }}>
              <li><Link href="/#pakketten" className="hover:text-white transition-colors">Alle pakketten</Link></li>
              <li><Link href="/quiz" className="hover:text-white transition-colors">Huidquiz</Link></li>
              <li><Link href="/resultaat" className="hover:text-white transition-colors">Mijn resultaat</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-inter font-medium text-sm mb-4" style={{ color: 'var(--lume-terra)' }}>Info</h4>
            <ul className="space-y-3 text-sm" style={{ color: 'rgba(250,246,241,0.65)' }}>
              <li><Link href="/over-ons" className="hover:text-white transition-colors">Over ons</Link></li>
              <li><Link href="/blog" className="hover:text-white transition-colors">Blog</Link></li>
              <li><Link href="/ingredienten" className="hover:text-white transition-colors">Ingrediënten</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-inter font-medium text-sm mb-4" style={{ color: 'var(--lume-terra)' }}>Klantenservice</h4>
            <ul className="space-y-3 text-sm" style={{ color: 'rgba(250,246,241,0.65)' }}>
              <li><Link href="/contact" className="hover:text-white transition-colors">Contact</Link></li>
              <li><Link href="/faq" className="hover:text-white transition-colors">Veelgestelde vragen</Link></li>
              <li><Link href="/bezorging" className="hover:text-white transition-colors">Bezorging &amp; retour</Link></li>
            </ul>
          </div>
        </div>

        <div
          className="pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs"
          style={{ borderTop: '1px solid rgba(250,246,241,0.15)', color: 'rgba(250,246,241,0.4)' }}
        >
          <p>© 2024 Lumé Skincare. Alle rechten voorbehouden.</p>
          <div className="flex gap-6">
            <Link href="/privacy" className="hover:text-white transition-colors">Privacybeleid</Link>
            <Link href="/voorwaarden" className="hover:text-white transition-colors">Algemene voorwaarden</Link>
            <Link href="/cookies" className="hover:text-white transition-colors">Cookies</Link>
          </div>
        </div>
      </div>
    </footer>
  )
}
