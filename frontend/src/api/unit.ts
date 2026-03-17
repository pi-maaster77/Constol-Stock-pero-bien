// frontend/src/api/unit.ts

import type { components, paths } from '@/types/api'
import axios from 'axios'
import config from './config.json'
type Path = keyof paths

import type { Unit, UnitCreate, UnitUpdate } from '@/types/unit'

const { apiUrl } = config

const paths = {
  units: '/unit/' as Path,
  unitByID: (id: number) => `/unit/${id}` as Path,
}

export const getUnit = async (): Promise<Unit[]> => {
  const response = await axios.get(`${apiUrl}${paths.units}`)
  return response.data
}

export const getUnitByID = async (id: number): Promise<Unit> => {
  const response = await axios.get(`${apiUrl}${paths.unitByID(id)}`)
  return response.data
}

export const createUnit = async (unit: UnitCreate): Promise<Unit> => {
  const response = await axios.post(`${apiUrl}${paths.units}`, unit)
  return response.data
}

export const updateProduct = async (id: number, product: UnitUpdate): Promise<Unit> => {
  const response = await axios.patch(`${apiUrl}${paths.unitByID(id)}`, product)
  return response.data
}
