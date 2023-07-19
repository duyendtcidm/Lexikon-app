<template lang="pug">
  div.practice-page
    v-row.ma-0.pa-0.px-2.invoice_table
      v-col(:cols="12")
        v-data-table(
          :headers="PRACTICE_HEADER.filter(h => h.isVisible)"
          :items="searchedWords"
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
          template(v-slot:item.index="{ item }")
            span {{searchedWords.findIndex((word) => word.name === item.name) + 1}}
          template(v-slot:item.action="{ item }")
            v-menu(bottom left min-width="9vw")
              template(v-slot:activator='{ on }')
                v-btn(
                  color='primary',
                  dark,
                  class='mr-auto',
                  v-on='on',
                  icon,
                  max-height="20px"
                  max-width="20px"
                )
                  v-icon mdi-dots-vertical
              v-list
                v-list-item(@click="")
                  v-icon.pr-3 mdi-pencil
                  v-list-item-title {{$t('practice.title')}}
                v-list-item(@click="")
                  v-icon.pr-3(color="red" ) mdi-delete-outline
                  v-list-item-title {{$t('common.delete')}}
            span.pa-2
</template>

<script>
import {defineComponent, getCurrentInstance, onMounted, ref, watch} from 'vue'
import { PRACTICE_HEADER } from './index'
import QuestionDialog from "@/components/QuestionDialog/index.vue";
import {api} from "@/plugins";

export default defineComponent ({
  components: {
    QuestionDialog
  },
  setup() {
    const searchedWords = ref([])
    const getWord = async () => {
      // Date object
      const date = new Date();
      let currentDay= String(date.getDate()).padStart(2, '0');
      let currentMonth = String(date.getMonth()+1).padStart(2,"0");
      let currentYear = date.getFullYear();
      let currentDate = `${currentYear}-${currentMonth}-${currentDay}`;
      const { data } = await api.get(`/practice/?current_date=${currentDate}` )
      searchedWords.value = data
    }

    onMounted(() => {
      getWord()
    })

    return {
      PRACTICE_HEADER,
      searchedWords
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
  padding-left: 15px !important
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