// frontend/src/types/move.ts

import type { components } from '@/types/api'

export type Move = components['schemas']['MoveRead']
export type MoveIn = components['schemas']['MovesIn']
export type MoveOut = components['schemas']['MovesOut']
export type MoveAdjust = components['schemas']['MovesAdjust']

export type MoveDetail = components['schemas']['MoveDetailRead']

export type MoveInRead = components['schemas']['MoveInRead']
export type MoveOutRead = components['schemas']['MoveOutRead']
export type MoveAdjustRead = components['schemas']['MoveAdjustRead']
