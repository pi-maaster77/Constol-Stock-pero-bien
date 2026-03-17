// frontend/src/api/moves.ts

import type { components, paths } from '@/types/api'
import axios from 'axios'
import config from './config.json'
import type { MoveAdjust } from '@/types/move'
type Path = keyof paths
const { apiUrl } = config

type MovesIn = components['schemas']['MovesIn']
type MovesOut = components['schemas']['MovesOut']

const paths = {
  movesIn: '/moves/in' as Path,
  movesOut: '/moves/out' as Path,
  movesAdjust: '/moves/adjust' as Path,
  moves: '/moves/' as Path,
}

export const movesIn = async (movesInData: MovesIn): Promise<MovesIn> => {
  const response = await axios.post(`${apiUrl}${paths.movesIn}`, movesInData)
  return response.data
}

export const movesOut = async (movesOutData: MovesOut): Promise<MovesOut> => {
  const response = await axios.post(`${apiUrl}${paths.movesOut}`, movesOutData)
  return response.data
}

export const movesAdjust = async (movesAdjustData: MoveAdjust): Promise<MoveAdjust> => {
  const response = await axios.post(`${apiUrl}${paths.movesAdjust}`, movesAdjustData)
  return response.data
}

export const getMoves = async (): Promise<(MovesIn | MovesOut | MoveAdjust)[]> => {
  const response = await axios.get(`${apiUrl}${paths.moves}`)
  return response.data
}
