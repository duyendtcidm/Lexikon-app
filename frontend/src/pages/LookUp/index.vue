<template lang="pug">
  div.loop-up
    header-bar
    //div.auction_date__panel.px-2
    //  v-dialog(
    //    ref="dialog"
    //    persistent
    //    width="90vw"
    //    max-width="500px"
    //    v-model="isOpenDatePicker"
    //  )
    //    //:return-value.sync="auctionDate"
    //    template(v-slot:activator="{ on, attrs }")
    //      v-text-field.pa-0.pr-1(
    //        :label="$t('common.auction_date')"
    //        readonly
    //        hide-details
    //        append-icon="mdi-calendar"
    //        v-bind="attrs"
    //        v-on="on"
    //        :value="moment(auctionDate).format($t('common.time_full_format_date'))"
    //        @click:append="isOpenDatePicker = true"
    //        color="primary"
    //      )
    //    v-date-picker(full-width scrollable locale="ja-jp" color="primary" header-color="primary" v-model="auctionDate")
    //      v-spacer
    //      v-btn.white--text(dark text color="red" @click="isOpenDatePicker = false")
    //        span {{$t('common.cancel')}}
    //      v-btn(dark text color="primary" @click="selectAuctionDate()")
    //        span {{$t('common.ok')}}
    v-row.py-4.d-flex.justify-center
      v-col(cols="4")
        v-text-field(
          outlined
          dense
          hide-details
          :label="$t('look_up.word_search')"
          :value="searchInfo"
          @input="handleSearchInput"
          color="primary"
        )
          template(v-slot:append)
            v-btn(color="primary" plain @click="onDraw")
              v-icon mdi-square-edit-outline
            v-btn.mr-0(color="primary" plain @click="onSearch(searchInfo)")
              v-icon mdi-magnify
    v-spacer
    //div.learnt-words.px-2
    //  div.static-header-learnt
    //    v-list-item.px-0
    //      v-list-item-title.bold--text
    //        v-row.ma-0.pa-0(justify="center") {{$t('look_up.learnt_words')}}
    //    v-text-field.pb-2(
    //      dense
    //      hide-details
    //      solo
    //      :label="$t('look_up.word_search')"
    //      prepend-inner-icon="mdi-magnify"
    //      v-model="searchInfoNewWord"
    //      @input="searchNewWords()"
    //      style="width: 100%"
    //      color="primary"
    //    )
    //  v-list(dense)
    //    v-list-item-group(v-if="!loading.newWords" color="primary")
    //      template(v-for="(word, index) in searchedNewWords")
    //        v-list-item(:key="index")
    //            span {{word.word}}
    //        v-divider
    //    v-skeleton-loader(
    //      v-else
    //      type="list-item,divider, list-item, divider, list-item, divider"
    //    )
    div.content
      div.word-detail(v-if="'foundedWord'")
        h1.mb-1.blue--text {{exampleWord.word}}
        span {{exampleWord.pitch}}
        br
        span.mr-5 {{$t('common.level')}}: {{exampleWord.level}}
        span {{$t('common.theme')}}: {{exampleWord.theme}}
        div.meaning(v-for="(meaning, index) in exampleWord.word_meaning")
          div.seperate-infor
            div.inner-seperate
              h3 {{meaning.meaning}}
              span {{meaning.type}}
            v-list(lines="two" v-for="(example, index) in meaning.sentences")
              v-list-item-title {{example.sentence}}
              v-list-item-subtitle {{example.meaning}}
      div.word-detail(v-else-if="'foundedGrammer'")
      div.word-detail(v-else)
        span.font-italic(:style="{'margin-top': '100px'}") {{$t('common.no_data')}}

      //div.kanji
      //  h3 hihi





</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import HeaderBar from "@/components/HeaderBar/index.vue";

export default defineComponent ({
  components: {
    HeaderBar
  },
  setup() {
    const instance = getCurrentInstance()
    const { $toast, $root } = instance.proxy
    // const auctionDate = ref(auctionDateValue || moment(new Date()).format('YYYY-MM-DD'))
    const isOpenDatePicker = ref(false)

    const searchInfo = ref('')
    const searchInfoNewWord = ref('')
    // const searchedNewWords = ref([])
    const data = ref({
      searchedNewWords: {},
      isFound: 'noData'
    })
    const searchedNewWords = [
      {
        code: 1,
        word: "hana",
        meaning: "hoa"
      },
      {
        code: 1,
        word: "hana",
        meaning: "hoa"
      },
        {
        code: 1,
        word: "hana",
        meaning: "hoa"
      }
    ]

    const loading = ref({
      searchResult: true,
      newWords: false
    })

    const exampleWord = {
      code: '1',
      word: '自然',
      kanji: 'tự nhiên',
      level: 'N5',
      pitch: 'shi／zen‾',
      theme: 'Life',
      word_meaning: [
        {
          id : 1,
          type: 'Danh từ',
          meaning: 'Thiên nhiên, tự nhiên',
          sentences: [
            {
              id : 11,
              sentence: '人間 は 自然 の 一部 である',
              meaning: 'Con người là một phần của thiên nhiên.'
            },
            {
              id : 12,
              sentence: '自然 を 教師 としなさい。',
              meaning: 'Hãy để thiên nhiên là người thầy của chúng ta.'
            }
          ]
        },
          {
          id : 2,
          type: 'Trạng từ',
          meaning: 'Một cách tự nhiên',
          sentences: [
            {
              id : 13,
              sentence: '自然 に 治 ります。',
              meaning: 'Để nó lành một cách tự nhiên.'
            },
            {
              id : 14,
              sentence: 'メグ の 髪 は 自然 に カール する。',
              meaning: 'Mái tóc của Meg quăn tự nhiên.'
            }
          ]
        },
      ]
    }

    const handleSearchInput = (input) => {
      searchInfo.value = input
      console.log('searchInfo', searchInfo)
    }

    const onDraw = () => {
      console.log('hero')
    }
    const onSearch = (searchInfo) => {
      console.log(searchInfo)
    }
    
    const searchNewWords = () => {
      console.log('searchInfoNewWord', searchInfoNewWord.value)
    }
    
    return {
      // isOpenDatePicker,
      // selectAuctionDate,
      searchInfo,
      handleSearchInput,
      onDraw,
      onSearch,
      searchInfoNewWord,
      searchNewWords,
      searchedNewWords,
      loading,
      exampleWord
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'
::v-deep
  .v-btn:not(.v-btn--round).v-size--default
    min-width: 30px
    padding: 0px 8px
  .v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__append-inner
    margin-top: 3px

.auction_date__panel
  position: fixed
  top: 5px
  float: left
  width: 12%
  height: calc(100vh - 160px)
  margin-top: 80px
  margin-left: 30px
  padding-top: 5px
.learnt-words
  position: fixed
  margin-top: 0px
  float: left
  width: 15%
  border-style: solid
  border-width: 1px
  border-color: #bdbdbd
  height: calc(100vh - 160px)
  margin-left: 20px
  background-color: white
  overflow-y: scroll
.static-header-learnt
  position: sticky
  top: 0
  z-index: 10
  background-color: #FFFFFF
.content
  display: flex
  justify-content: space-between
  width: 80%
  float: right
.word-detail
  width: 70%
  margin-top: 20px
  //background-color: #66ABF2
.seperate-infor
  border-top: 3px solid #5d2fc1
  margin-top: 20px
  padding: 10px 20px 0px
.inner-seperate
  border-bottom: 1px solid #fec400
.kanji
  width: 25%
  background-color: #13CE66
  margin-right: 30px

</style>