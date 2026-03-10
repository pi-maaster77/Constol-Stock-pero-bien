import axios from 'axios'
import config from './config.json'

const apiClient = axios.create({
  baseURL: config.apiUrl,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient
