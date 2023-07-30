<template lang="pug">
  v-btn(@click="onRender") hellooo

</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import {api, i18n} from '@/plugins'

export default defineComponent({

  setup() {
    const level = 'N3'
    const amount = 15
    const question_type = 'hiragana'
    const onRender = async (searchInfo) => {
      try {
        const { data } = await api.get(`/test/get_question_to_practice?level=${level}&amount=${amount}&question_type=${question_type}` )
        console.log(data)
      } catch (e) {
        console.log('hihi', e)
      }
    }

    return {
      onRender
    }
  }

})

</script>

<style lang="sass" scoped>

</style>