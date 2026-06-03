export default function LumeLogo({ light = false }: { light?: boolean }) {
  const color = light ? '#FFFFFF' : '#2C2520'
  return (
    <svg
      width="120"
      height="36"
      viewBox="0 0 120 36"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      aria-label="Lumé"
    >
      {/* Botanical leaves */}
      <path
        d="M8 18 C8 12 13 8 13 8 C13 8 14 14 11 18 C14 18 18 15 20 10 C20 10 22 16 18 20 C16 22 13 22 8 18Z"
        fill={light ? '#8FAF8F' : '#8FAF8F'}
        opacity="0.9"
      />
      {/* Lumé text */}
      <text
        x="26"
        y="26"
        fontFamily="Georgia, 'Cormorant Garamond', serif"
        fontStyle="italic"
        fontWeight="400"
        fontSize="26"
        fill={color}
        letterSpacing="1"
      >
        Lumé
      </text>
    </svg>
  )
}
