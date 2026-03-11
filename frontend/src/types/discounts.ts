// frontend/src/types/discounts.ts

import type { components } from '@/types/api'

export type Discount = components['schemas']['DiscountBulk']
export type DiscountCreate = components['schemas']['DiscountBulkCreate']
export type DiscountUpdate = components['schemas']['DiscountBulkUpdate']