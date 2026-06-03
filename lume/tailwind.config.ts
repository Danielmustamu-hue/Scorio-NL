import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'lume-cream': '#FAF6F1',
        'lume-stone': '#2C2520',
        'lume-terra': '#C4856A',
        'lume-sage': '#8FAF8F',
        'lume-blush': '#F0E0D6',
        'lume-mist': '#E8F0E8',
        'lume-border': '#E8E0D8',
      },
      fontFamily: {
        cormorant: ['Cormorant Garamond', 'serif'],
        inter: ['Inter', 'sans-serif'],
      },
      borderRadius: {
        card: '12px',
        btn: '8px',
        pill: '24px',
      },
    },
  },
  plugins: [],
}

export default config
