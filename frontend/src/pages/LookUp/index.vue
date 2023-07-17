<template lang="pug">
  div.look-up
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
            //v-btn(color="primary" plain @click="onDraw")
            //  v-icon mdi-square-edit-outline
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
      div.word-detail(v-if="dataType.word")
        h1.mb-1.blue--text {{searchedWord.name}}
        span {{searchedWord.yomi}}
        span.green--text 「{{searchedWord.kanji}}」
        br
        span.mr-5 {{$t('common.level')}}: {{searchedWord.level}}
        div.meaning(v-for="(meaning, index) in searchedWord.meanings")
          div.seperate-infor
            div.inner-seperate
              h3 {{meaning.mean}}
              span {{meaning.type}}
            v-list-item-title.mt-3 {{meaning.sen_1}}
            v-list-item-subtitle {{meaning.mean_1}}
            v-list-item-title.mt-3 {{meaning.sen_2}}
            v-list-item-subtitle {{meaning.mean_2}}
        div.seperate-infor
          div.mt-2(v-for="reference in references" v-if="Object.keys(searchedWord[reference]).length" )
            h4 {{$t('look_up.reference.'+reference)}}
            div.pl-4(v-for="(value, name, index) in searchedWord[reference]")
              span {{ name }}: {{ value }}
      div.word-detail(v-else-if="dataType.grammar")
      div.word-detail(v-else-if="dataType.not_found")
        p.not-found
          span(:style="{'font-size': '30px'}") {{$t('common.no_data')}}
          br
          span {{$t('common.no_data_note')}}
      div.word-detail.intro(v-else)
        h2.blue--text {{$t('look_up.intro.hello')}}
        h3.blue--text {{$t('look_up.intro.about')}}
        h3.blue--text.mt-3 {{$t('look_up.intro.thanks')}}
      //div.kanji
      //  h3 hihi



</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import {api, i18n} from '@/plugins'

export default defineComponent ({
  setup() {
    const instance = getCurrentInstance()
    const { $toast, $root } = instance.proxy
    // const auctionDate = ref(auctionDateValue || moment(new Date()).format('YYYY-MM-DD'))
    const isOpenDatePicker = ref(false)

    const searchInfo = ref('')
    const searchInfoNewWord = ref('')
    // const searchedNewWords = ref([])
    const dataType = ref({
      word: false,
      grammar: false,
      not_found: false
    })
    const references = ['synonym', 'synonym', 'antonym', 'kanren', 'usage_pattern', 'compound_word', 'common_word']
    const searchedWord = ref({})
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

    const handleSearchInput = (input) => {
      searchInfo.value = input
    }

    const onDraw = () => {
      console.log('hero')
    }

    const defineDataType = (type) => {

      if (type === 'word') {
        dataType.value.word = true
        dataType.value.grammar = false
        dataType.value.not_found = false
      } else if (type === 'grammar') {
        dataType.value.word = false
        dataType.value.grammar = true
        dataType.value.not_found = false
      }
    }
    const onSearch = async (searchInfo) => {
      try {
        const { data } = await api.get(`/look_up/new_word/?search_input=${searchInfo}` )
        if (data.length) {
          searchedWord.value = data[0]
          defineDataType('word')
        } else
          dataType.value.not_found = true
      } catch (e) {
        console.log('hihi', e)
      }
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
      references,
      dataType,
      searchedWord
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
.look-up
  background-color: #f7f7f7
  height: 100vh
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
  //display: flex
  //justify-content: space-between
  //float: right
  width: 60%
  margin: auto
.word-detail
  width: 100%
  margin-top: 20px
.intro
  padding: 40px
  margin-top: 50px
  border-radius: 10px
  background-color: #c3e0ff

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
.not-found
  margin-top: 100px
  color: orange
  font-weight: bold

</style>