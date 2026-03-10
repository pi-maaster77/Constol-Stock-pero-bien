// frontend/src/types/product.ts

import type { components } from '@/types/api'

export type Product = components['schemas']['ProductReturn']
export type ProductCreate = components['schemas']['ProductCreate']
export type ProductUpdate = components['schemas']['ProductPatch']
