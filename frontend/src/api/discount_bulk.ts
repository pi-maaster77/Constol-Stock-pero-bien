// frontend/src/api/discount_bulk.ts

import type { components, paths } from '@/types/api'
import axios from 'axios'
const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'
type Path = keyof paths

type DiscountReturn = components['schemas']['DiscountBulk']
type DiscountCreate = components['schemas']['DiscountBulkCreate']
type DiscountUpdate = components['schemas']['DiscountBulkUpdate']

const paths = {
  discount: '/discount_bulk/' as Path,
  discountByID: (id: number) => `/discount_bulk/${id}` as Path,
}

export const getDiscount = async (): Promise<DiscountReturn[]> => {
  const response = await axios.get(`${apiUrl}${paths.discount}`)
  return response.data
}

export const getDiscountByID = async (id: number): Promise<DiscountReturn> => {
  const response = await axios.get(`${apiUrl}${paths.discountByID(id)}`)
  return response.data
}

export const createDiscount = async (discount: DiscountCreate): Promise<DiscountReturn> => {
  const response = await axios.post(`${apiUrl}${paths.discount}`, discount)
  return response.data
}

export const updateDiscount = async (
  id: number,
  discount: DiscountUpdate,
): Promise<DiscountReturn> => {
  const response = await axios.patch(`${apiUrl}${paths.discountByID(id)}`, discount)
  return response.data
}

export const deleteDiscount = async (id: number): Promise<DiscountReturn> => {
  const response = await axios.delete(`${apiUrl}${paths.discountByID(id)}`)
  return response.data
}
