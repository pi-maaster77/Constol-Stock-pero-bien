// frontend/src/stores/product.ts

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getProducts, getProductByID, createProduct, deleteProduct, updateProduct } from '@/api/product'

import type { Product } from '../types/product'
import { useNotificationsStore } from './notifications'



export const useProductsStore = defineStore('products', () => {
    const products = ref<Product[]>([])
    const productCount = computed(() => products.value.length)

    function isAxiosError(error: unknown): error is {
        response?: { data?: { message?: string } }
        message?: string
    } {
        return typeof error === 'object' && error !== null
    }

    async function optimistic(fn: Function, request: Function) {
      const backup = [...products.value]
      const notify = useNotificationsStore()

      try {
        fn()
        await request()
      } 
      catch (e: unknown) {
        products.value.splice(0, products.value.length, ...backup)
        console.error(e)

        let msg = 'Ocurrió un error inesperado'

        if (isAxiosError(e)) {
            msg =
            e.response?.data?.message ||
            e.message ||
            msg
        }
        notify.push('error', msg)
      }
    }

    function load (){
        optimistic(() => {}, async () => {
            const res = await getProducts()
            console.log(res)
            products.value.splice(0, products.value.length, ...res)
        })
    }
    
    function getProductByID(id: number): Product | undefined {
        return products.value.find(p => p.id === id)
    }
    
    function set(value: Product[]) {
        products.value.splice(0, products.value.length, ...value)
    }

    function create(product: Omit<Product, 'id'>) {
        optimistic(() => {
            const tempID = Math.max(0, ...products.value.map(p => p.id)) + 1
            products.value.push({ id: tempID, ...product })
        }, async () => {
            const res = await createProduct({
                bc: product.bc,
                name: product.name,
                unit_id: product.unit_id,
                price_formula: product.price_formula,
                public_price: product.public_price,
                expires: product.expires,
            })
            load()
        })
    }

    function updateByID(id: number, product: Omit<Product, 'id'>) {
        optimistic(() => {
            const index = products.value.findIndex(p => p.id === id)
            if (index !== -1) {
                products.value[index] = { id, ...product }
            }
        }, async () => {
            await updateProduct(id, {
                bc: product.bc,
                name: product.name,
                unit_id: product.unit_id,
                price_formula: product.price_formula,
                public_price: product.public_price,
                expires: product.expires,
            })
            load()
        })
    }

    function deleteByID(id: number) {
        optimistic(() => {
            const index = products.value.findIndex(p => p.id === id)
            if (index !== -1) {
                products.value.splice(index, 1)
            }
        }, async () => {
            await deleteProduct(id)
            load()
        })
    }
    return { products, productCount, load, getProductByID, set, create, updateByID, deleteByID }
})
