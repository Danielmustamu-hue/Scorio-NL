const SHOPIFY_STOREFRONT_URL = process.env.NEXT_PUBLIC_SHOPIFY_STOREFRONT_URL || ''
const SHOPIFY_STOREFRONT_TOKEN = process.env.NEXT_PUBLIC_SHOPIFY_STOREFRONT_TOKEN || ''

async function shopifyFetch<T>(query: string, variables?: Record<string, unknown>): Promise<T> {
  const response = await fetch(SHOPIFY_STOREFRONT_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Shopify-Storefront-Access-Token': SHOPIFY_STOREFRONT_TOKEN,
    },
    body: JSON.stringify({ query, variables }),
    next: { revalidate: 60 },
  })

  if (!response.ok) {
    throw new Error(`Shopify API error: ${response.statusText}`)
  }

  const { data, errors } = await response.json()
  if (errors) throw new Error(errors[0].message)
  return data as T
}

export interface ShopifyProduct {
  id: string
  title: string
  handle: string
  description: string
  priceRange: { minVariantPrice: { amount: string; currencyCode: string } }
  images: { edges: { node: { url: string; altText: string } }[] }
  variants: { edges: { node: { id: string; title: string; price: { amount: string } } }[] }
}

export async function getProductByHandle(handle: string): Promise<ShopifyProduct | null> {
  if (!SHOPIFY_STOREFRONT_URL) return null

  const query = `
    query GetProduct($handle: String!) {
      productByHandle(handle: $handle) {
        id title handle description
        priceRange { minVariantPrice { amount currencyCode } }
        images(first: 5) { edges { node { url altText } } }
        variants(first: 10) { edges { node { id title price { amount } } } }
      }
    }
  `

  const data = await shopifyFetch<{ productByHandle: ShopifyProduct }>(query, { handle })
  return data.productByHandle
}

export async function createCheckout(variantId: string, quantity = 1): Promise<string> {
  const query = `
    mutation CreateCart($variantId: ID!, $quantity: Int!) {
      cartCreate(input: {
        lines: [{ merchandiseId: $variantId, quantity: $quantity }]
      }) {
        cart { checkoutUrl }
        userErrors { field message }
      }
    }
  `

  const data = await shopifyFetch<{ cartCreate: { cart: { checkoutUrl: string } } }>(query, {
    variantId,
    quantity,
  })

  return data.cartCreate.cart.checkoutUrl
}
