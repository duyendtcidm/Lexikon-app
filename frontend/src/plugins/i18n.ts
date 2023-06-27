import Vue from "vue"
import VueI18n from "vue-i18n"
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import vi from "../locale/vi.json"

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: "vi",
  messages: {
    vi
  },
  // dateTimeFormats: {
  //   "ja-JP": {
  //     short: {
  //       year: "numeric",
  //       month: "short",
  //       day: "numeric"
  //     },
  //     long: {
  //       year: 'numeric', month: 'short', day: 'numeric',
  //       weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: true
  //     }
  //   }
  // }
})

export default i18n
