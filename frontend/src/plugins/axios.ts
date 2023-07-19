import axios from 'axios'

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL
})

api.interceptors.request.use(
  async (config: any) => {
    if ('Cypress' in window) {
      return config
    }

    const token = localStorage.getItem("auth_token")
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error: any) => {
    return Promise.reject(error)
  }
)

export default api