<template lang="pug">
  v-app
    header-bar.center(
      v-if="$root.$route.path !== '/register' && $root.$route.path !== '/log_in' && $root.$route.path !== '/forgot_password'"
      :back="enableBack"
    )
    v-main
      router-view
</template>

<script>
import {defineComponent, ref, watch, getCurrentInstance, computed, onMounted, onUnmounted} from 'vue'
import { HeaderBar } from './components'
import { urlPath } from './utils'
import { history } from "./store/history"
import router from "@/router";
import {api} from "@/plugins";

const App = defineComponent({
  components: {
    HeaderBar
  },
  setup() {
    const instance = getCurrentInstance()
    const { $root, $store, $toast } = instance.proxy
    const start = ref(true)
    const enableBack = ref(false)

    watch(
      () => $root.$route,
      () => {
        const { path } = $root.$route
        start.value = path !== '/'
        const isMainUrl = urlPath.DISABLE_NAVIGATION?.find((url) => url === path)
        enableBack.value = !isMainUrl
        // check histories
        if (history.state.histories.length > 1) {
          enableBack.value = !isMainUrl
        }
        else { enableBack.value = false }
      }
    )

    return {
      enableBack
    }
  }

})
export default App
</script>
