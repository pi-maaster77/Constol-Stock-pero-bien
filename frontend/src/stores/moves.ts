// frontend/src/stores/moves.ts

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getMoves, movesAdjust, movesIn, movesOut } from '@/api/moves'

import type { Move, MoveIn, MoveOut, MoveAdjust, MoveAdjustRead, MoveDetail, MoveInRead, MoveOutRead } from '../types/move'
import { useNotificationsStore } from './notifications'
import type { ISODateString } from '@/types/ISODatingFormat'



export const useMovesStore = defineStore('moves', () => {
    const moves = ref<Move[]>([])
    const movesCount = computed(() => moves.value.length)

    function isAxiosError(error: unknown): error is {
        response?: { data?: { message?: string } }
        message?: string
    } {
        return typeof error === 'object' && error !== null
    }

    async function optimistic(fn: Function, request: Function) {
      const backup = [...moves.value]
      const notify = useNotificationsStore()

      try {
        fn()
        await request()
      } 
      catch (e: unknown) {
        moves.value.splice(0, moves.value.length, ...backup)
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
            const res = await getMoves()
            console.log("movimientos obtenidos:", res)
            moves.value.splice(0, moves.value.length, ...res as Move[])
            console.log("movimientos en store:", moves.value)
        })
    }
    
    function getMoveByID(id: number): Move | undefined {
        return moves.value.find(m => m.id === id) as Move| undefined
    }
    
    function set(value: Move[]) {
        moves.value.splice(0, moves.value.length, ...value)
    }

    function movesInStore(move: Omit<Move, 'id'>) {
        optimistic(() => {
            const tempID = Math.max(0, ...moves.value.map(p => p.id)) + 1
            moves.value.push({ id: tempID, ...move } as Move)
        }, async () => {
            const res = await movesIn([{
                date: move.date as ISODateString,
                details: move.details as unknown as MoveIn['details']
            }])
            console.log(res)
            load()
        })
    }

    function movesOutStore(move: Omit<Move, 'id'>) {
        optimistic(() => {
            const tempID = Math.max(0, ...moves.value.map(p => p.id)) + 1
            moves.value.push({ id: tempID, ...move } as Move)
        }
        , async () => {
            const res = await movesOut([{
                date: move.date as ISODateString,
                details: move.details as unknown as MoveOut['details']
            }])
            console.log(res)
            load()
        })
    }

    function movesAdjustStore(move: Omit<Move, 'id'>) {
        optimistic(() => {
            const tempID = Math.max(0, ...moves.value.map(p => p.id)) + 1
            moves.value.push({ id: tempID, ...move } as Move)
        }
        , async () => {
            const res = await movesAdjust([{
                date: move.date as ISODateString,
                details: move.details as unknown as MoveAdjust['details']
            }])
            console.log(res)
            load()
        })
    }

    return {moves, movesCount, load, getMoveByID, set, movesInStore, movesOutStore, movesAdjustStore } 
})
