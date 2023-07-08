import axios from 'axios'
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// import { TOKEN_KEY } from '@/utils/constants'
// import { Auth } from 'aws-amplify'

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL
})

api.interceptors.request.use(
  async (config: any) => {
    if ('Cypress' in window) {
      return config
    }

    // const token = await Auth.currentSession().then((res: any) => {
    //   const accessToken = res.getAccessToken()
    //   return accessToken.getJwtToken()
    // })

    // if (token) {
    //   // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    //   // @ts-ignore
    //   config.headers.Authorization = `Bearer ${token}`
    //   localStorage.setItem(TOKEN_KEY, token)
    // }
    return config
  },
  (error: any) => {
    return Promise.reject(error)
  }
)

export default api