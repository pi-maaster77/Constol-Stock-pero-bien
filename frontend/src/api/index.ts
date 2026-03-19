// frontend/src/api/index.ts

import axios from 'axios'
const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const apiClient = axios.create({
  baseURL: apiUrl,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient
