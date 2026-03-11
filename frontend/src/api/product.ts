// frontend/src/api/product.ts

import type { components } from '@/types/api'
import axios from 'axios'
import config from './config.json'

const { apiUrl } = config

type ProductReturn = components['schemas']['ProductReturn']
type ProductCreate = components['schemas']['ProductCreate']
type ProductUpdate = components['schemas']['ProductPatch']

const paths = {
  products: '/product/',
  productByID: (id: number) => `/product/${id}`,
  productByBC: (bc: string) => `/product/bc/${bc}`,
}

export const getProducts = async (): Promise<ProductReturn[]> => {
  const response = await axios.get(`${apiUrl}${paths.products}`)
  return response.data
}

export const getProductByID = async (id: number): Promise<ProductReturn> => {
  const response = await axios.get(`${apiUrl}${paths.productByID(id)}`)
  return response.data
}

export const getProductByBC = async (bc: string): Promise<ProductReturn> => {
  const response = await axios.get(`${apiUrl}${paths.productByBC(bc)}`)
  return response.data
}

export const createProduct = async (product: ProductCreate): Promise<ProductReturn> => {
  const response = await axios.post(`${apiUrl}${paths.products}`, product)
  console.log(response.data)
  return response.data
}

export const updateProduct = async (id: number, product: ProductUpdate): Promise<ProductReturn> => {
  const response = await axios.patch(`${apiUrl}${paths.productByID(id)}`, product)
  return response.data
}

export const deleteProduct = async (id: number): Promise<ProductReturn> => {
  const response = await axios.delete(`${apiUrl}${paths.productByID(id)}`)
  return response.data
}
