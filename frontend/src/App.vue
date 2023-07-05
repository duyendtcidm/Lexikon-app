<template lang="pug">
  v-app
    header-bar.center
    //(
    //  :back="enableBack"
    //)
    v-main
      router-view
  //Register

</template>

<script>
import {defineComponent, ref, watch, getCurrentInstance, computed, onMounted, onUnmounted} from 'vue'
import { HeaderBar } from './components'

const App = defineComponent({
  components: {
    HeaderBar
  },
  setup() {
    const instance = getCurrentInstance()
    // const { $root, $store, $toast } = instance.proxy
    const enableBack = ref(false)

    return {

    }
  }

})
export default App
</script>
