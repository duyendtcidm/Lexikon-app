<template lang="pug">
  div
    v-row.ma-0.pa-0.px-2.invoice_table
      v-col(:cols="12")
        v-data-table(

          :headers="PRACTICE_HEADER.filter(h => h.isVisible)"
          :items-per-page="-1"
          :single-select="false"
          fixed-header
          class="elevation-2"
          hide-default-footer

        )
          template(v-slot:header.status="{ header }")
            v-row.ma-0.pa-0(align="center")
              span {{header.text}}



</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import { PRACTICE_HEADER } from './index'

export default defineComponent ({
  components: {

  },
  setup() {




    return {
      PRACTICE_HEADER
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'


</style>