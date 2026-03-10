// frontend/src/stores/notifications.ts

import { defineStore } from 'pinia'
import type { NotificationType } from '../types/notifications'

interface Notification {
  type: NotificationType
  text: string
  timeout: number
}

export const useNotificationsStore = defineStore('notificaciones', {
  state: () => ({
    notifications: [] as Notification[],
  }),

  actions: {
    push(type: NotificationType, text: string, timeout = 4000) {
      const n: Notification = { type, text, timeout }
      this.notifications.push(n)

      setTimeout(() => {
        const i = this.notifications.indexOf(n)
        if (i !== -1) this.notifications.splice(i, 1)
      }, timeout)
    },

    clear(i: number) {
      this.notifications.splice(i, 1)
    },
  },
})
