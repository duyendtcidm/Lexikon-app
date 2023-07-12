<template lang="pug">
  div.practice-page
    v-row.ma-0.pa-0.px-2.invoice_table
      v-col(:cols="12")
        v-data-table(
          :headers="PRACTICE_HEADER.filter(h => h.isVisible)"
          :items="searchWords"
          :items-per-page="-1"
          :single-select="false"
          fixed-header
          class="elevation-2"
          hide-default-footer
        )
          template(v-slot:header.status="{ header }")
            v-row.ma-0.pa-0(align="center")
              span {{header.text}}
          template(v-slot:header.data-table-select="{ on }")
            div.border-checkbox
              v-simple-checkbox(v-model="isSelectedAll" color="primary" v-on="on")
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
    const searchWords = ref([
      {
        "code": 1,
        "name": "人生",
        "meaning": "cuộc đời",
        "level": "N2",
        "status": "3",
        "score": "6:9",
        "remark": ""
      },
        {
        "code": 2,
        "name": "精算",
        "meaning": "tính toán",
        "level": "N2",
        "status": "5",
        "score": "5:5",
        "remark": ""
      },
        {
        "code": 3,
        "name": "微妙",
        "meaning": "tinh tế",
        "level": "N2",
        "status": "3",
        "score": "6:9",
        "remark": ""
      }
    ])

    return {
      PRACTICE_HEADER,
      searchWords
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
.invoice_table
  padding-top: 7px !important
  padding-left: 10px !important
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
.transmission-list
  background-color: white
  .v-list-item
    height: 48px
    &__icon
      // Reduce big margin between icon and text in default style
      margin-right: 16px

    &__title
      // Disable bold text caused by dense list style
      font-weight: normal
.col-send-type
  display: inline
  width: 50px
  font-size: 16px !important
.border-checkbox i
  background-color: white
  border-radius: 5px
.link-text
  color: blue
  text-decoration: underline
  cursor: pointer
.blur-progress-loader-div
  position: fixed
  top: 0
  left: 0
  height: 100vh
  width: 100vw
  opacity: 0.3
  background-color: lightblue
  z-index: 998
.progress_circle_loader-div
  position: fixed
  top: calc(50vh - 50px)
  left: calc(50vw - 50px)
  z-index: 999
.status-div
  height: 20px
  width: 44px
  display: flex
  flex-wrap: wrap
.status-div-more-2
  height: 35px
  width: 44px
  display: flex
  flex-wrap: wrap


</style>