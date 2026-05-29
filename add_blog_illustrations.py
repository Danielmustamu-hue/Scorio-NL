#!/usr/bin/env python3
"""Add SVG illustrations to Scorio.nl blog cards and article heroes."""

import re, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SVG DEFINITIONS — Blog Cards (inline, 200×130 viewBox)
# ============================================================

SVG_SPEED = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M28 96 A72 72 0 0 1 172 96" stroke="rgba(255,255,255,0.12)" stroke-width="10" stroke-linecap="round"/>
  <path d="M28 96 A72 72 0 0 1 80 30" stroke="#F59E0B" stroke-width="10" stroke-linecap="round"/>
  <line x1="100" y1="96" x2="50" y2="48" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="100" cy="96" r="7" fill="white" fill-opacity="0.9"/>
  <circle cx="100" cy="96" r="3.5" fill="#F59E0B"/>
  <line x1="100" y1="27" x2="100" y2="36" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="144" y1="52" x2="138" y2="58" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="56" y1="52" x2="62" y2="58" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" stroke-linecap="round"/>
  <text x="18" y="116" fill="rgba(255,255,255,0.38)" font-size="9" font-family="system-ui,sans-serif">Traag</text>
  <text x="152" y="116" fill="rgba(255,255,255,0.38)" font-size="9" font-family="system-ui,sans-serif">Snel</text>
  <path d="M162 18 L155 31 L162 31 L155 46" stroke="rgba(255,255,255,0.58)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M176 28 L169 40 L176 40 L169 54" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_MOBILE = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="68" y="12" width="64" height="106" rx="11" stroke="white" stroke-width="2" stroke-opacity="0.9"/>
  <rect x="75" y="24" width="50" height="80" rx="3" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>
  <line x1="88" y1="121" x2="112" y2="121" stroke="white" stroke-width="2.5" stroke-opacity="0.7" stroke-linecap="round"/>
  <line x1="83" y1="36" x2="117" y2="36" stroke="rgba(255,255,255,0.55)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="83" y1="47" x2="111" y2="47" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="83" y1="57" x2="117" y2="57" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M80 78 L87 85 L102 68" stroke="#5B4FE8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="22" y="68" width="9" height="28" rx="2" fill="rgba(255,255,255,0.35)"/>
  <rect x="36" y="55" width="9" height="41" rx="2" fill="rgba(255,255,255,0.52)"/>
  <rect x="50" y="42" width="9" height="54" rx="2" fill="rgba(255,255,255,0.68)"/>
  <circle cx="160" cy="32" r="2.5" fill="rgba(255,255,255,0.45)"/>
  <circle cx="170" cy="52" r="1.5" fill="rgba(255,255,255,0.3)"/>
  <circle cx="157" cy="58" r="1.5" fill="rgba(255,255,255,0.35)"/>
  <circle cx="167" cy="72" r="2" fill="rgba(255,255,255,0.2)"/>
</svg>'''

SVG_SEARCH = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="18" y="52" width="128" height="30" rx="15" stroke="white" stroke-width="2" stroke-opacity="0.85"/>
  <line x1="36" y1="62" x2="36" y2="72" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-linecap="round"/>
  <line x1="46" y1="67" x2="92" y2="67" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-linecap="round"/>
  <circle cx="130" cy="67" r="8" stroke="rgba(255,255,255,0.55)" stroke-width="1.5"/>
  <line x1="135" y1="73" x2="142" y2="80" stroke="rgba(255,255,255,0.55)" stroke-width="2" stroke-linecap="round"/>
  <circle cx="158" cy="42" r="24" stroke="white" stroke-width="2.5" stroke-opacity="0.9"/>
  <line x1="176" y1="60" x2="188" y2="73" stroke="white" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="148" y1="42" x2="168" y2="42" stroke="rgba(255,255,255,0.45)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="158" y1="32" x2="158" y2="52" stroke="rgba(255,255,255,0.45)" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="22" cy="28" r="3" fill="rgba(255,255,255,0.5)"/>
  <circle cx="42" cy="20" r="2" fill="rgba(255,255,255,0.35)"/>
  <circle cx="62" cy="26" r="2.5" fill="rgba(255,255,255,0.4)"/>
  <line x1="22" y1="28" x2="42" y2="20" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
  <line x1="42" y1="20" x2="62" y2="26" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
  <line x1="18" y1="95" x2="98" y2="95" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-linecap="round"/>
  <line x1="18" y1="106" x2="135" y2="106" stroke="rgba(255,255,255,0.18)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="18" y1="117" x2="78" y2="117" stroke="rgba(255,255,255,0.13)" stroke-width="1.5" stroke-linecap="round"/>
</svg>'''

SVG_AI = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="58" y="22" width="84" height="72" rx="13" stroke="white" stroke-width="2" stroke-opacity="0.9"/>
  <line x1="100" y1="22" x2="100" y2="10" stroke="white" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round"/>
  <circle cx="100" cy="7" r="4.5" stroke="#8B5CF6" stroke-width="2" fill="rgba(139,92,246,0.3)"/>
  <rect x="70" y="41" width="20" height="14" rx="5" stroke="#8B5CF6" stroke-width="2" fill="rgba(139,92,246,0.2)"/>
  <rect x="110" y="41" width="20" height="14" rx="5" stroke="#8B5CF6" stroke-width="2" fill="rgba(139,92,246,0.2)"/>
  <circle cx="80" cy="48" r="4" fill="#8B5CF6"/>
  <circle cx="120" cy="48" r="4" fill="#8B5CF6"/>
  <rect x="76" y="70" width="48" height="11" rx="5.5" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
  <line x1="85" y1="75" x2="115" y2="75" stroke="rgba(255,255,255,0.35)" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="24" cy="42" r="3.5" fill="rgba(139,92,246,0.65)"/>
  <circle cx="14" cy="64" r="2" fill="rgba(255,255,255,0.3)"/>
  <circle cx="28" cy="78" r="2.5" fill="rgba(139,92,246,0.45)"/>
  <line x1="24" y1="42" x2="58" y2="57" stroke="rgba(139,92,246,0.3)" stroke-width="1" stroke-dasharray="4 3"/>
  <circle cx="176" cy="38" r="3.5" fill="rgba(139,92,246,0.65)"/>
  <circle cx="186" cy="62" r="2" fill="rgba(255,255,255,0.3)"/>
  <circle cx="172" cy="76" r="2.5" fill="rgba(139,92,246,0.45)"/>
  <line x1="176" y1="38" x2="142" y2="53" stroke="rgba(139,92,246,0.3)" stroke-width="1" stroke-dasharray="4 3"/>
  <circle cx="38" cy="22" r="1.5" fill="rgba(255,255,255,0.6)"/>
  <circle cx="163" cy="22" r="2" fill="rgba(255,255,255,0.55)"/>
  <circle cx="182" cy="88" r="1.5" fill="rgba(255,255,255,0.35)"/>
</svg>'''

SVG_SHIELD = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M100 16 L150 36 L150 72 Q150 108 100 122 Q50 108 50 72 L50 36 Z" stroke="white" stroke-width="2.5" stroke-opacity="0.9" stroke-linejoin="round" fill="rgba(91,79,232,0.18)"/>
  <rect x="80" y="72" width="40" height="30" rx="5" stroke="white" stroke-width="2" stroke-opacity="0.85"/>
  <path d="M87 72 L87 61 Q87 48 100 48 Q113 48 113 61 L113 72" stroke="white" stroke-width="2" stroke-opacity="0.85"/>
  <circle cx="100" cy="82" r="4" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
  <line x1="100" y1="86" x2="100" y2="92" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-linecap="round"/>
  <path d="M80 38 L92 50 L118 25" stroke="#00C896" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="28" cy="38" r="2.5" fill="rgba(255,255,255,0.28)"/>
  <circle cx="18" cy="62" r="2" fill="rgba(255,255,255,0.2)"/>
  <circle cx="172" cy="38" r="2.5" fill="rgba(255,255,255,0.28)"/>
  <circle cx="182" cy="60" r="2" fill="rgba(255,255,255,0.2)"/>
</svg>'''

SVG_WEBSHOP = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="52" y="58" width="96" height="58" rx="4" stroke="white" stroke-width="2" stroke-opacity="0.85"/>
  <path d="M44 58 L156 58 L143 36 L57 36 Z" stroke="white" stroke-width="2" stroke-opacity="0.7" stroke-linejoin="round" fill="rgba(245,158,11,0.2)"/>
  <rect x="82" y="82" width="36" height="34" rx="3" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
  <rect x="58" y="66" width="22" height="14" rx="3" stroke="rgba(255,255,255,0.38)" stroke-width="1.5"/>
  <rect x="120" y="66" width="22" height="14" rx="3" stroke="rgba(255,255,255,0.38)" stroke-width="1.5"/>
  <path d="M100 16 L103 26 L114 26 L106 32 L109 43 L100 37 L91 43 L94 32 L86 26 L97 26 Z" stroke="#F59E0B" stroke-width="1.5" stroke-linejoin="round" fill="rgba(245,158,11,0.22)"/>
  <circle cx="68" cy="22" r="2.5" fill="rgba(245,158,11,0.65)"/>
  <circle cx="132" cy="22" r="2.5" fill="rgba(245,158,11,0.65)"/>
  <circle cx="56" cy="30" r="1.5" fill="rgba(245,158,11,0.42)"/>
  <circle cx="144" cy="30" r="1.5" fill="rgba(245,158,11,0.42)"/>
</svg>'''

SVG_DOCUMENT = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="48" y="12" width="95" height="115" rx="8" stroke="white" stroke-width="2" stroke-opacity="0.85"/>
  <path d="M118 12 L143 37 L118 37 Z" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" stroke-linejoin="round" fill="rgba(255,255,255,0.08)"/>
  <line x1="63" y1="54" x2="133" y2="54" stroke="white" stroke-width="2" stroke-opacity="0.8" stroke-linecap="round"/>
  <line x1="63" y1="68" x2="133" y2="68" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="63" y1="79" x2="120" y2="79" stroke="rgba(255,255,255,0.38)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="63" y1="90" x2="133" y2="90" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="63" y1="101" x2="105" y2="101" stroke="rgba(255,255,255,0.24)" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="148" cy="98" r="20" stroke="#00C896" stroke-width="2.5"/>
  <line x1="161" y1="112" x2="172" y2="124" stroke="#00C896" stroke-width="3" stroke-linecap="round"/>
  <line x1="141" y1="98" x2="155" y2="98" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="148" y1="91" x2="148" y2="105" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" stroke-linecap="round"/>
</svg>'''

SVG_CHART = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="28" y1="18" x2="28" y2="100" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round"/>
  <line x1="28" y1="100" x2="178" y2="100" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round"/>
  <rect x="42" y="76" width="22" height="24" rx="3" fill="rgba(91,79,232,0.45)" stroke="#5B4FE8" stroke-width="1.5"/>
  <rect x="76" y="56" width="22" height="44" rx="3" fill="rgba(91,79,232,0.62)" stroke="#5B4FE8" stroke-width="1.5"/>
  <rect x="110" y="40" width="22" height="60" rx="3" fill="rgba(91,79,232,0.78)" stroke="#5B4FE8" stroke-width="1.5"/>
  <rect x="144" y="26" width="22" height="74" rx="3" fill="#5B4FE8" stroke="#5B4FE8" stroke-width="1.5"/>
  <polyline points="53,76 87,56 121,40 155,26" stroke="#00C896" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 3" fill="none"/>
  <circle cx="53" cy="76" r="3.5" fill="#00C896"/>
  <circle cx="87" cy="56" r="3.5" fill="#00C896"/>
  <circle cx="121" cy="40" r="3.5" fill="#00C896"/>
  <circle cx="155" cy="26" r="3.5" fill="#00C896"/>
  <line x1="28" y1="56" x2="34" y2="56" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="28" y1="76" x2="34" y2="76" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round"/>
</svg>'''

SVG_MAP_PIN = '''<svg viewBox="0 0 200 130" width="148" height="96" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="62" r="56" stroke="rgba(0,200,150,0.12)" stroke-width="1.5"/>
  <circle cx="100" cy="62" r="42" stroke="rgba(0,200,150,0.18)" stroke-width="1.5"/>
  <circle cx="100" cy="62" r="28" stroke="rgba(0,200,150,0.28)" stroke-width="1.5"/>
  <path d="M100 18 Q124 18 124 44 Q124 64 100 84 Q76 64 76 44 Q76 18 100 18 Z" stroke="white" stroke-width="2.5" stroke-opacity="0.9" stroke-linejoin="round" fill="rgba(0,200,150,0.22)"/>
  <circle cx="100" cy="44" r="9" stroke="white" stroke-width="2" stroke-opacity="0.8"/>
  <rect x="22" y="72" width="15" height="26" rx="2" stroke="rgba(255,255,255,0.42)" stroke-width="1.5"/>
  <rect x="16" y="80" width="11" height="18" rx="2" stroke="rgba(255,255,255,0.28)" stroke-width="1.5"/>
  <rect x="163" y="72" width="15" height="26" rx="2" stroke="rgba(255,255,255,0.42)" stroke-width="1.5"/>
  <rect x="173" y="80" width="11" height="18" rx="2" stroke="rgba(255,255,255,0.28)" stroke-width="1.5"/>
  <line x1="12" y1="98" x2="188" y2="98" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
</svg>'''

SVG_FEATURED = '''<svg viewBox="0 0 200 200" width="200" height="200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="35" y="38" width="130" height="148" rx="10" stroke="white" stroke-width="3"/>
  <rect x="65" y="28" width="70" height="26" rx="9" stroke="white" stroke-width="3"/>
  <circle cx="100" cy="41" r="4" fill="white"/>
  <path d="M50 78 L60 90 L75 68" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="88" y1="79" x2="148" y2="79" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="88" y1="92" x2="132" y2="92" stroke="white" stroke-width="2" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M50 112 L60 124 L75 102" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="88" y1="113" x2="148" y2="113" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="88" y1="126" x2="128" y2="126" stroke="white" stroke-width="2" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M50 146 L60 158 L75 136" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="88" y1="147" x2="148" y2="147" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="88" y1="160" x2="120" y2="160" stroke="white" stroke-width="2" stroke-linecap="round" stroke-opacity="0.6"/>
  <circle cx="168" cy="42" r="14" stroke="white" stroke-width="2" stroke-opacity="0.4"/>
  <line x1="162" y1="42" x2="174" y2="42" stroke="white" stroke-width="2" stroke-opacity="0.4" stroke-linecap="round"/>
  <line x1="168" y1="36" x2="168" y2="48" stroke="white" stroke-width="2" stroke-opacity="0.4" stroke-linecap="round"/>
  <circle cx="30" cy="145" r="10" stroke="white" stroke-width="2" stroke-opacity="0.3"/>
  <path d="M26 145 L29 148 L36 141" stroke="white" stroke-width="2" stroke-opacity="0.3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# ============================================================
# HERO SVGS — Article heroes (large, centered in 280px banner)
# ============================================================

HERO_SVGS = {
    'trage-website-klanten-kosten': {
        'gradient': 'linear-gradient(135deg,#1a0f00 0%,#2d1900 50%,#150b00 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="340" height="187" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="M50 180 A150 150 0 0 1 350 180" stroke="rgba(255,255,255,0.1)" stroke-width="16" stroke-linecap="round"/>
  <path d="M50 180 A150 150 0 0 1 162 48" stroke="#F59E0B" stroke-width="16" stroke-linecap="round"/>
  <line x1="200" y1="180" x2="98" y2="85" stroke="white" stroke-width="4" stroke-linecap="round"/>
  <circle cx="200" cy="180" r="14" fill="white" fill-opacity="0.92"/>
  <circle cx="200" cy="180" r="7" fill="#F59E0B"/>
  <line x1="200" y1="48" x2="200" y2="64" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>
  <line x1="290" y1="92" x2="278" y2="104" stroke="rgba(255,255,255,0.3)" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="110" y1="92" x2="122" y2="104" stroke="rgba(255,255,255,0.3)" stroke-width="2.5" stroke-linecap="round"/>
  <text x="32" y="206" fill="rgba(255,255,255,0.38)" font-size="16" font-family="system-ui,sans-serif">Traag</text>
  <text x="342" y="206" fill="rgba(255,255,255,0.38)" font-size="16" font-family="system-ui,sans-serif">Snel</text>
  <path d="M330 30 L318 52 L330 52 L318 78" stroke="rgba(255,255,255,0.6)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M355 44 L343 64 L355 64 L343 88" stroke="rgba(255,255,255,0.35)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M372 58 L362 76 L372 76 L362 96" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',
    },
    'mobile-first-indexering': {
        'gradient': 'linear-gradient(135deg,#0D0726 0%,#1A1050 50%,#080414 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="300" height="165" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="140" y="15" width="120" height="190" rx="18" stroke="white" stroke-width="3" stroke-opacity="0.9"/>
  <rect x="150" y="30" width="100" height="152" rx="6" stroke="rgba(255,255,255,0.22)" stroke-width="2"/>
  <line x1="170" y1="208" x2="230" y2="208" stroke="white" stroke-width="4" stroke-opacity="0.7" stroke-linecap="round"/>
  <line x1="158" y1="46" x2="242" y2="46" stroke="rgba(255,255,255,0.55)" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="158" y1="62" x2="222" y2="62" stroke="rgba(255,255,255,0.32)" stroke-width="2" stroke-linecap="round"/>
  <line x1="158" y1="76" x2="242" y2="76" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-linecap="round"/>
  <line x1="158" y1="90" x2="208" y2="90" stroke="rgba(255,255,255,0.28)" stroke-width="2" stroke-linecap="round"/>
  <path d="M158 132 L172 148 L200 120" stroke="#00C896" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="44" y="65" width="18" height="56" rx="3" fill="rgba(255,255,255,0.35)"/>
  <rect x="68" y="44" width="18" height="77" rx="3" fill="rgba(255,255,255,0.52)"/>
  <rect x="92" y="24" width="18" height="97" rx="3" fill="rgba(255,255,255,0.68)"/>
  <rect x="116" y="8" width="16" height="113" rx="3" fill="rgba(255,255,255,0.82)"/>
  <circle cx="310" cy="50" r="4.5" fill="rgba(255,255,255,0.45)"/>
  <circle cx="332" cy="78" r="3" fill="rgba(255,255,255,0.3)"/>
  <circle cx="302" cy="92" r="3" fill="rgba(255,255,255,0.35)"/>
  <circle cx="325" cy="115" r="5" fill="rgba(255,255,255,0.2)"/>
  <circle cx="347" cy="48" r="2.5" fill="rgba(255,255,255,0.38)"/>
</svg>''',
    },
    'zoekwoorden-kiezen-lokaal-bedrijf': {
        'gradient': 'linear-gradient(135deg,#001a12 0%,#002d1e 50%,#000e08 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="360" height="198" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="195" cy="90" r="65" stroke="white" stroke-width="4" stroke-opacity="0.9"/>
  <line x1="150" y1="90" x2="240" y2="90" stroke="rgba(255,255,255,0.38)" stroke-width="2" stroke-linecap="round"/>
  <line x1="195" y1="48" x2="195" y2="132" stroke="rgba(255,255,255,0.38)" stroke-width="2" stroke-linecap="round"/>
  <line x1="244" y1="140" x2="290" y2="190" stroke="white" stroke-width="6.5" stroke-linecap="round"/>
  <rect x="18" y="50" width="145" height="32" rx="16" stroke="white" stroke-width="2.5" stroke-opacity="0.85"/>
  <line x1="36" y1="60" x2="36" y2="72" stroke="rgba(255,255,255,0.7)" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="46" y1="66" x2="102" y2="66" stroke="rgba(255,255,255,0.38)" stroke-width="2" stroke-linecap="round"/>
  <line x1="18" y1="100" x2="110" y2="100" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-linecap="round"/>
  <line x1="18" y1="114" x2="152" y2="114" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="18" y1="128" x2="82" y2="128" stroke="rgba(255,255,255,0.14)" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="42" cy="178" r="4.5" fill="rgba(0,200,150,0.65)"/>
  <circle cx="64" cy="162" r="3" fill="rgba(0,200,150,0.48)"/>
  <circle cx="85" cy="180" r="3.5" fill="rgba(0,200,150,0.52)"/>
  <line x1="42" y1="178" x2="64" y2="162" stroke="rgba(0,200,150,0.25)" stroke-width="1.2" stroke-dasharray="4 3"/>
  <line x1="64" y1="162" x2="85" y2="180" stroke="rgba(0,200,150,0.25)" stroke-width="1.2" stroke-dasharray="4 3"/>
</svg>''',
    },
    'https-ssl-certificaat-seo': {
        'gradient': 'linear-gradient(135deg,#0D0726 0%,#1A1050 50%,#080414 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="300" height="165" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="M200 20 L280 55 L280 118 Q280 183 200 208 Q120 183 120 118 L120 55 Z" stroke="white" stroke-width="3.5" stroke-opacity="0.9" stroke-linejoin="round" fill="rgba(91,79,232,0.15)"/>
  <rect x="168" y="126" width="64" height="52" rx="8" stroke="white" stroke-width="2.5" stroke-opacity="0.85"/>
  <path d="M178 126 L178 105 Q178 84 200 84 Q222 84 222 105 L222 126" stroke="white" stroke-width="2.5" stroke-opacity="0.85"/>
  <circle cx="200" cy="146" r="7" stroke="rgba(255,255,255,0.7)" stroke-width="2"/>
  <line x1="200" y1="153" x2="200" y2="165" stroke="rgba(255,255,255,0.7)" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M162 70 L180 90 L218 50" stroke="#00C896" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="52" cy="64" r="4" fill="rgba(255,255,255,0.26)"/>
  <circle cx="38" cy="94" r="3" fill="rgba(255,255,255,0.18)"/>
  <circle cx="348" cy="64" r="4" fill="rgba(255,255,255,0.26)"/>
  <circle cx="362" cy="92" r="3" fill="rgba(255,255,255,0.18)"/>
</svg>''',
    },
    'seo-webshops-7-fouten': {
        'gradient': 'linear-gradient(135deg,#1a0f00 0%,#261500 50%,#120800 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="360" height="198" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="80" y="98" width="240" height="100" rx="6" stroke="white" stroke-width="2.5" stroke-opacity="0.85"/>
  <path d="M65 98 L335 98 L315 56 L85 56 Z" stroke="white" stroke-width="2.5" stroke-opacity="0.7" stroke-linejoin="round" fill="rgba(245,158,11,0.18)"/>
  <rect x="150" y="144" width="100" height="54" rx="5" stroke="rgba(255,255,255,0.5)" stroke-width="2"/>
  <rect x="90" y="110" width="56" height="28" rx="4" stroke="rgba(255,255,255,0.38)" stroke-width="1.5"/>
  <rect x="254" y="110" width="56" height="28" rx="4" stroke="rgba(255,255,255,0.38)" stroke-width="1.5"/>
  <path d="M200 20 L205 37 L222 37 L210 47 L214 64 L200 55 L186 64 L190 47 L178 37 L195 37 Z" stroke="#F59E0B" stroke-width="2" stroke-linejoin="round" fill="rgba(245,158,11,0.22)"/>
  <circle cx="128" cy="32" r="5" fill="rgba(245,158,11,0.6)"/>
  <circle cx="272" cy="32" r="5" fill="rgba(245,158,11,0.6)"/>
  <circle cx="108" cy="46" r="3.5" fill="rgba(245,158,11,0.42)"/>
  <circle cx="292" cy="46" r="3.5" fill="rgba(245,158,11,0.42)"/>
</svg>''',
    },
    'meta-description-schrijven': {
        'gradient': 'linear-gradient(135deg,#001a12 0%,#002d1e 50%,#000e08 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="320" height="176" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="56" y="16" width="188" height="198" rx="12" stroke="white" stroke-width="3" stroke-opacity="0.85"/>
  <path d="M202 16 L244 58 L202 58 Z" stroke="rgba(255,255,255,0.35)" stroke-width="2" stroke-linejoin="round" fill="rgba(255,255,255,0.07)"/>
  <line x1="76" y1="80" x2="224" y2="80" stroke="white" stroke-width="2.5" stroke-opacity="0.8" stroke-linecap="round"/>
  <line x1="76" y1="97" x2="224" y2="97" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-linecap="round"/>
  <line x1="76" y1="112" x2="196" y2="112" stroke="rgba(255,255,255,0.38)" stroke-width="2" stroke-linecap="round"/>
  <line x1="76" y1="127" x2="224" y2="127" stroke="rgba(255,255,255,0.32)" stroke-width="2" stroke-linecap="round"/>
  <line x1="76" y1="142" x2="172" y2="142" stroke="rgba(255,255,255,0.25)" stroke-width="2" stroke-linecap="round"/>
  <line x1="76" y1="157" x2="224" y2="157" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="76" y1="172" x2="140" y2="172" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="316" cy="145" r="40" stroke="#00C896" stroke-width="3.5"/>
  <line x1="342" y1="172" x2="364" y2="196" stroke="#00C896" stroke-width="5.5" stroke-linecap="round"/>
  <line x1="300" y1="145" x2="332" y2="145" stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>
  <line x1="316" y1="129" x2="316" y2="161" stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/>
</svg>''',
    },
    'seo-gids-mkb-ondernemers-2026': {
        'gradient': 'linear-gradient(135deg,#0D0726 0%,#1A1050 50%,#080414 100%)',
        'svg': '''<svg viewBox="0 0 400 220" width="320" height="176" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="55" y="28" width="200" height="172" rx="12" stroke="white" stroke-width="3"/>
  <rect x="95" y="16" width="120" height="30" rx="10" stroke="white" stroke-width="3"/>
  <circle cx="155" cy="31" r="5" fill="white"/>
  <path d="M75 82 L88 98 L108 72" stroke="#00C896" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="120" y1="82" x2="228" y2="82" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-opacity="0.8"/>
  <line x1="120" y1="95" x2="192" y2="95" stroke="rgba(255,255,255,0.42)" stroke-width="2" stroke-linecap="round"/>
  <path d="M75 118 L88 134 L108 108" stroke="#00C896" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="120" y1="118" x2="228" y2="118" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-opacity="0.8"/>
  <line x1="120" y1="131" x2="182" y2="131" stroke="rgba(255,255,255,0.42)" stroke-width="2" stroke-linecap="round"/>
  <path d="M75 154 L88 170 L108 144" stroke="#F59E0B" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="120" y1="154" x2="228" y2="154" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-opacity="0.75"/>
  <line x1="120" y1="167" x2="197" y2="167" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-linecap="round"/>
  <circle cx="310" cy="66" r="22" stroke="white" stroke-width="2.5" stroke-opacity="0.32"/>
  <line x1="297" y1="66" x2="323" y2="66" stroke="rgba(255,255,255,0.32)" stroke-width="2" stroke-linecap="round"/>
  <line x1="310" y1="53" x2="310" y2="79" stroke="rgba(255,255,255,0.32)" stroke-width="2" stroke-linecap="round"/>
  <circle cx="330" cy="145" r="13" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
  <path d="M325 145 L329 149 L337 141" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',
    },
}

# ============================================================
# CSS ADDITIONS
# ============================================================

BLOG_SVG_CSS = '''
/* ============================================================
   BLOG CARD SVG ILLUSTRATIES
   ============================================================ */
.blog-card-img svg {
  flex-shrink: 0;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.35));
  transition: transform 0.4s ease;
}

.blog-card:hover .blog-card-img svg {
  transform: scale(1.06) translateY(-3px);
}

/* Article hero banner */
.article-hero-banner {
  width: 100%;
  height: 280px;
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 32px 0 40px;
  overflow: hidden;
}

.article-hero-banner svg {
  animation: heroFloat 4s ease-in-out infinite;
  filter: drop-shadow(0 8px 32px rgba(0,0,0,0.5));
}

@keyframes heroFloat {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-10px); }
}

@media (max-width: 600px) {
  .article-hero-banner { height: 200px; }
  .article-hero-banner svg { width: 80%; height: auto; }
}

@media print {
  .article-hero-banner { height: 180px; page-break-inside: avoid; }
  .article-hero-banner svg { animation: none; }
  .blog-card-img { height: 120px; }
}
'''

# ============================================================
# CARD CONFIGS — emoji → (gradient, svg_string)
# ============================================================

CARD_MAP = [
    ('⚡',  'linear-gradient(135deg,rgba(245,158,11,0.52)0%,rgba(160,80,0,0.2)100%)',   SVG_SPEED),
    ('📱',  'linear-gradient(135deg,rgba(91,79,232,0.52)0%,rgba(0,100,80,0.2)100%)',    SVG_MOBILE),
    ('🔑',  'linear-gradient(135deg,rgba(0,200,150,0.48)0%,rgba(0,80,60,0.2)100%)',     SVG_SEARCH),
    ('🤖',  'linear-gradient(135deg,rgba(139,92,246,0.58)0%,rgba(60,20,120,0.2)100%)', SVG_AI),
    ('🛡️', 'linear-gradient(135deg,rgba(91,79,232,0.52)0%,rgba(0,100,80,0.2)100%)',    SVG_SHIELD),
    ('🛒',  'linear-gradient(135deg,rgba(245,158,11,0.48)0%,rgba(80,50,0,0.2)100%)',   SVG_WEBSHOP),
    ('📝',  'linear-gradient(135deg,rgba(0,200,150,0.48)0%,rgba(0,100,60,0.2)100%)',   SVG_DOCUMENT),
    ('📊',  'linear-gradient(135deg,rgba(91,79,232,0.52)0%,rgba(139,92,246,0.2)100%)', SVG_CHART),
    ('🗺️', 'linear-gradient(135deg,rgba(0,200,150,0.48)0%,rgba(0,100,80,0.2)100%)',   SVG_MAP_PIN),
]

# ============================================================
# FUNCTIONS
# ============================================================

def update_blog_index(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    for emoji, gradient, svg in CARD_MAP:
        old = f'<div class="blog-card-img" aria-hidden="true">{emoji}</div>'
        new = (
            f'<div class="blog-card-img" style="background:{gradient};" aria-hidden="true">\n'
            f'            {svg}\n'
            f'          </div>'
        )
        content = content.replace(old, new)

    # Featured article: replace the emoji span
    old_feat = '<span style="font-size: 4rem;" aria-hidden="true">🔍</span>'
    new_feat = f'<div aria-hidden="true" style="opacity:0.9">{SVG_FEATURED}</div>'
    content = content.replace(old_feat, new_feat)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('  ✓ blog/index.html — kaartillustraties bijgewerkt')


def add_hero_to_article(path):
    slug = os.path.basename(path).replace('.html', '')
    if slug not in HERO_SVGS:
        print(f'  - {slug}: geen hero config, overgeslagen')
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'article-hero-banner' in content:
        print(f'  - {slug}: hero al aanwezig')
        return

    cfg = HERO_SVGS[slug]
    hero_html = (
        '\n      <!-- Hero Banner -->\n'
        f'      <div class="article-hero-banner" style="background:{cfg["gradient"]};" aria-hidden="true">\n'
        f'        {cfg["svg"]}\n'
        '      </div>\n'
    )

    # Insert after </header> before <!-- Layout or <div class="article-layout">
    marker = re.search(r'</header>\s*\n\s*(?=<!--\s*Layout|<div class="article-layout")', content)
    if marker:
        insert_pos = marker.end() - len(re.search(r'\s*(?=<!--\s*Layout|<div class="article-layout")', content[marker.start():]).group())
        # Simpler: just replace the matched area
        new_content = content[:marker.start()] + '</header>\n' + hero_html + content[marker.end():]
        # Wait, marker.end() points to just before the Layout comment/div
        # Let me use a cleaner replacement:
        old_snippet = content[marker.start():marker.end()]
        content = content[:marker.start()] + '</header>\n' + hero_html + content[marker.end():]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  ✓ {slug}: hero banner toegevoegd')
    else:
        print(f'  ✗ {slug}: invoegpunt niet gevonden')


def update_css(style_path):
    with open(style_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'article-hero-banner' in content:
        print('  - CSS al bijgewerkt')
        return

    # Update blog-card-img block to remove font-size (SVGs don't need it)
    content = re.sub(
        r'(\.blog-card-img \{[^}]*?)font-size: 3rem;\n',
        r'\1font-size: 0;\n',
        content
    )
    # Also set height to 160px (from 180px) per spec
    content = re.sub(
        r'(\.blog-card-img \{[^}]*?)height: 180px;',
        r'\1height: 160px;',
        content
    )

    content = content.rstrip() + '\n\n' + BLOG_SVG_CSS + '\n'
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('  ✓ css/style.css bijgewerkt')


def main():
    print('1. Blog index illustraties...')
    update_blog_index(os.path.join(ROOT, 'blog', 'index.html'))

    print('2. Artikel hero banners...')
    for path in sorted(glob.glob(os.path.join(ROOT, 'blog', '*.html'))):
        if 'index' not in path:
            add_hero_to_article(path)

    print('3. CSS bijwerken...')
    update_css(os.path.join(ROOT, 'css', 'style.css'))

    print('\n✅ Klaar — alle blog illustraties toegevoegd!')

if __name__ == '__main__':
    main()
