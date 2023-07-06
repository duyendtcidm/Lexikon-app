<template lang="pug">
  div.practice-page
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
          template(v-slot:no-data)
            span {{ $t('practice.no_data') }}
    v-row
      QuestionDialog



</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import { PRACTICE_HEADER } from './index'
import QuestionDialog from "@/components/QuestionDialog/index.vue";

export default defineComponent ({
  components: {
    QuestionDialog
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
.practice-page
  padding: 40px 60px 0px
::v-deep .v-data-table > .v-data-table__wrapper
  overflow-x: auto
  overflow-y: hidden
  > table
    > tbody > tr > td
      font-size: 16px !important
    > thead > tr > th
      color: white !important
      font-weight: bold
      font-size: 16px !important
      .v-input--selection-controls__input
        margin-right: 0px !important


</style>