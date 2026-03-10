// frontend/src/api/discount_bulk.ts

import type { components } from '@/types/api'
import axios from 'axios'
import config from './config.json'

const { apiUrl } = config

type DiscountReturn = components['schemas']['DiscountBulk']
type DiscountCreate = components['schemas']['DiscountBulkCreate']
type DiscountUpdate = components['schemas']['DiscountBulkUpdate']

const paths = {
  discount: '/discount_bulk/',
  discountByID: (id: number) => `/discount_bulk/${id}`,
}

export const getDiscount = async (): Promise<DiscountReturn[]> => {
  const response = await axios.get(`${apiUrl}${paths.discount}`)
  return response.data
}

export const getDiscountByID = async (id: number): Promise<DiscountReturn> => {
  const response = await axios.get(`${apiUrl}${paths.discountByID(id)}`)
  return response.data
}

export const createDiscount = async (product: DiscountCreate): Promise<DiscountReturn> => {
  const response = await axios.post(`${apiUrl}${paths.discount}`, product)
  return response.data
}

export const updateDiscount = async (
  id: number,
  product: DiscountUpdate,
): Promise<DiscountReturn> => {
  const response = await axios.patch(`${apiUrl}${paths.discountByID(id)}`, product)
  return response.data
}

export const deleteDiscount = async (id: number): Promise<DiscountReturn> => {
  const response = await axios.delete(`${apiUrl}${paths.discountByID(id)}`)
  return response.data
}
