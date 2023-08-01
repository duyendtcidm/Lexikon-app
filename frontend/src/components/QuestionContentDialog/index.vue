<template lang="pug">
  div
    dialog-container(
      ref="dialog_container"
      :label="isAdd ? $t('content.question.add') : $t('content.question.edit')"
      :mode="isAdd ? 'create' : 'update'"
      :loading="loading"
      :width="1100"
      :height="'85vh'"
      @on-close="closeDialog"
      @on-update="update"
      @on-create="create"
      @on-typing="onTyping"
      v-model="show"
    )
      validation-observer(
        ref="observer"
        v-slot="{ invalid }"
      )
        .container
          div
            div.multiple-tag
              .title-children
                h3 {{ $t('content.question.basic_information.title') }}
              .content
                validation-provider(:name="$t('content.question.basic_information.code')" :rules={regex: '^[0-9]*$'} v-slot="{ errors }")
                  v-text-field#code(
                    ref="code" type='number' hide-spin-buttons :error-messages="errors" :label="$t('content.question.basic_information.code')"
                    v-model="questionData.code" @focus="onClickInput('code')"
                  )
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.basic_information.name')")
                  v-text-field#name(
                    ref="name" :error-messages="errors"
                    v-model="questionData.name"
                    @focus="onClickInput('name')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.basic_information.name')}}
                      span.red--text *
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.basic_information.type')")
                  v-text-field#type(
                    ref="type"
                    :error-messages="errors"
                    :label="$t('content.question.basic_information.type')"
                    v-model="questionData.type"
                    @focus="onClickInput('type')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.basic_information.type')}}
                      span.red--text *
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.basic_information.level')")
                  v-text-field#level(
                    ref="level"
                    :error-messages="errors"
                    v-model="questionData.level"
                    @focus="onClickInput('level')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.basic_information.level')}}
                      span.red--text *
               
          div
            div.multiple-tag
              .title-children
                h3 {{ $t('content.question.choices.title') }}
              .content
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.choices.content')")
                  v-text-field#content(
                    ref="content"
                    :error-messages="errors"
                    v-model="questionData.content"
                    @focus="onClickInput('content')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.choices.content')}}
                      span.red--text *
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.choices.choice_1')")
                  v-text-field#choice_1(
                    ref="choice_1"
                    :error-messages="errors"
                    v-model="questionData.choices[1]"
                    @focus="onClickInput('choice_1')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.choices.choice_1')}}
                      span.red--text *
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.choices.choice_2')")
                  v-text-field#choice_2(
                    ref="choice_2"
                    :error-messages="errors"
                    v-model="questionData.choices[2]"
                    @focus="onClickInput('choice_2')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.choices.choice_2')}}
                      span.red--text *
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.choices.choice_3')")
                  v-text-field#choice_3(
                    ref="choice_3"
                    :error-messages="errors"
                    v-model="questionData.choices[3]"
                    @focus="onClickInput('choice_3')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.choices.choice_3')}}
                      span.red--text *
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.choices.choice_4')")
                  v-text-field#choice_4(
                    ref="choice_4"
                    :error-messages="errors"
                    v-model="questionData.choices[4]"
                    @focus="onClickInput('choice_4')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.choices.choice_4')}}
                      span.red--text *
          div
            div.multiple-tag
              .title-children
                h3 {{ $t('content.question.explanation.title') }}
              .content
                validation-provider(rules="required" v-slot="{ errors }" :name="$t('content.question.explanation.answer')")
                  v-text-field#answer(
                    ref="answer"
                    type='number' hide-spin-buttons
                    :error-messages="errors"
                    v-model="questionData.answer"
                    @focus="onClickInput('answer')"
                  )
                    template(v-slot:label)
                      span {{$t('content.question.explanation.answer')}}
                      span.red--text *
                v-text-field#explanation_1(
                  ref="explanation_1"
                  :label="$t('content.question.explanation.explanation_1')"
                  v-model="questionData.explanation[1]"
                  @focus="onClickInput('explanation_1')"
                )
                v-text-field#explanation_2(
                  ref="explanation_2"
                  :label="$t('content.question.explanation.explanation_2')"
                  v-model="questionData.explanation[2]"
                  @focus="onClickInput('explanation_2')"
                )
                v-text-field#explanation_3(
                  ref="explanation_3"
                  :label="$t('content.question.explanation.explanation_3')"
                  v-model="questionData.explanation[3]"
                  @focus="onClickInput('explanation_3')"
                )
                v-text-field#explanation_4(
                  ref="explanation_4"
                  :label="$t('content.question.explanation.explanation_4')"
                  v-model="questionData.explanation[4]"
                  @focus="onClickInput('explanation_4')"
                )


</template>

<script>
import {defineComponent, getCurrentInstance, ref, toRefs, watch} from 'vue'
import { showError, moveCursor} from '@/utils'
import { STATES, QUESTION_INIT } from './index'
import { api } from '@/plugins'
import moment from "moment/moment";
// import JConfirmDialog from '../JConfirmDialog/index'
import router from "@/router";
import DialogContainer from "@/components/DialogContainer/index.vue";
const CustomerDialog = defineComponent({
  component: {
    DialogContainer
  },
  props: {
    show: {
      type: Boolean,
      default: false
    },
    question: {
      type: Object,
      default: null
    },
    isAdd: {
      type: Boolean,
      default: false
    }
  },
  components: {
    DialogContainer
  },
  setup(props, { emit }) {
    moment.locale('ja')
    const instance = getCurrentInstance().proxy
    const { $toast, $root, $refs } = instance
    const loading = ref(false)
    const { question } = toRefs(props)
    let LIST_STATES = STATES
    const focusInput = ref('code')
    const questionData = ref({})
    const enterKeydown = ref(0)
    const {auction_date: auctionDateValue} = router.currentRoute.query
    const questions = ref([])

    const closeDialog = () => {
      loading.value = false
      emit('on-close')
    }

    const onFocus = (event, rf) => {
      focusInput.value = rf
      if (event.keyCode === 13 || event.keyCode === 9) {
        enterKeydown.value += 1
        if (enterKeydown.value === 2) {
          enterKeydown.value = 0
          $refs[focusInput.value].blur()
          focusInput.value = moveCursor(event, $refs, LIST_STATES, focusInput.value)
        }
      }
    }

    const onTyping = (event) => {
      const oldFocus = focusInput.value
      focusInput.value = moveCursor(event, $refs, LIST_STATES, focusInput.value)
      if (focusInput.value === LIST_STATES[LIST_STATES.length - 1] && event.keyCode === 13 && oldFocus === focusInput.value)
        $refs.dialog_container.$refs.save_btn.$el.click()
    }

    const onClickInput = (refName) => {
      focusInput.value = refName
    }

    const convertLevel = (level) => {
      if (level.trim().toLowerCase()=== 'n1') return 1
      if (level.trim().toLowerCase() === 'n2') return 2
      if (level.trim().toLowerCase() === 'n3') return 3
      if (level.trim().toLowerCase() === 'n4') return 4
      if (level.trim().toLowerCase() === 'n5') return 5
      return ''
    }

    const convertData = () => {
      Object.keys(questionData.value).forEach((key) => {
        if (key === 'level') {
          questionData.value[key] = convertLevel(questionData.value[key])
          Object.assign(questionData.value, {'level_id': questionData.value['level']})
        }
        if (questionData.value[key] === '') questionData.value[key] = null
      })
    }

    // UPDATE common customer
    const update = async () => {
      convertData()
      loading.value = true
      try {
        await api.put(`/content/`, questionData.value)
        closeDialog()
        $toast.success($root.$t('common.msg.update_successful'))
        emit('on-reload')
      } catch (e) {
        showError(e, $toast, $root.$t('common.msg.update_failed'))
      } finally {
        loading.value = false
      }
    }

    // CREATE common customer
    const create = async () => {
      convertData()
      loading.value = true
      try {
        const data = await api.post(`/content/`, questionData.value)
        closeDialog()
        $toast.success($root.$t('common.msg.create_successful'))
        emit('on-reload')
      } catch (e) {
        showError(e, $toast, $root.$t('common.msg.update_failed'))
      } finally {
        loading.value = false
      }
    }

    const init = async () => {
      focusInput.value = 'code'
      if (props.show) {
        if (props.isAdd) {
          questionData.value = JSON.parse(JSON.stringify(QUESTION_INIT))
        } else {
          await getQuestions()
          const data = await api.get(`/content/question/?question_id=${questionData.value.id}`)
        }
      }
    }


    const getQuestions = async () => {
        if (!props.isAdd){
          const {data} =  await api.get(`/content/question/`+ question.value['id'])
          questionData.value = data
        }
    }
     const getListQuestion = async () => {
       try {
         const {data} = await api.get(`/content/question/`)
         questions.value = data
       } catch (e) {
         showError(e, $toast, $root.$t('common.msg.get_data_failed'))
       }
     }
    watch(
      () => props.show,
      () => {
        if (props.show) {
            init()
            getListQuestion()
        }
      }
    )


    return {
      loading,
      onTyping,
      update,
      create,
      onClickInput,
      questionData,
      onFocus,
      closeDialog,
      questions,
      close
    }
  }
})

export default CustomerDialog
</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'
.container
  display: grid
  grid-gap: 25px
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))
.container > .multiple-tag, div > .multiple-tag
  object-fit: cover
  border: 1px solid #3c3c3c
  .title-children
    background-color: #1976d2
    color: white
    padding: 10px
    text-align: center
  .content
    padding: 10px
.auto-button
  padding-bottom: 4px
.list-item
  max-height: 550px
  overflow-y: auto
.item
  display: flex
  align-items: center
.item .code
  display: inline-block
  width: 100px
  text-align: left
  padding-left: 20px
.item .name
  display: inline-block
  width: calc(100% - 100px)
  text-align: left
  padding-right: 20px
.icon-list
  font-size: 20px
  display: inline-block
  justify-content: center
  align-items: center
.no-value
  color: gray
  font-style: italic
  text-align-last: center

</style>