<template lang="pug">
  div.test-page
    v-card(v-if="!isRendered" ).mx-auto.mt-4(max-width='700' style='background-color: #fff' height='95%')
      v-card-title.justify-center.rounded-card.mb-1(style='background-color: #81D4FA')
        h1.font-weight-thin {{$t('test.test_type.title')}}
      v-img.white--text.align-end(height='150px' src='@/assets/quiz.jpg')
      v-spacer
      v-card-subtitle.mt-5
        h2.display-1 {{$t('test.test_type.subtitle')}}
      v-card-actions.standard
        v-text-field.text-field(
          v-model='amount'
          type='number'
          hide-spin-buttons
          :label="$t('test.test_type.amount')"
          outlined
          dense
        )
      //v-card-actions
      //  v-radio-group(
      //
      //    v-model='level'
      //  )
      //    v-radio(label='N1' value='N1')
      //    v-radio(label='N2' value='N2')
      //    v-radio(label='N3' value='N3')
      //    v-radio(label='N4' value='N4')
      //    v-radio(label='N5' value='N5')
      v-select.standard.px-2(
        v-model='level'
        :items='levelTypeItems'
        :label="$t('test.test_type.level')"
        dense
        outlined
      )
      v-select.standard.px-2(
        v-model='question_type'
        dense
        :items='questionTypeItems'
        :label="$t('test.test_type.type_question')"
        outlined
      )
      v-row.standard
        v-btn.ma-2.white--text(elevation='2' color='info' :disabled="!level || amount === '0' || !amount || !question_type" @click='onRender')
          //router-link(style='text-decoration: none; color: inherit;' to=`/test/?level=${level}&amount=${amount}&question_type=${question_type}`)
          | {{$t('test.start_test')}}
    div(v-if="isRendered")
      quiz(:quizes="questions")



</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import {api, i18n} from '@/plugins'
import { Quiz } from '@/components'

export default defineComponent({
  components: {
    Quiz,
  },

  setup() {
    const instance = getCurrentInstance()
    const { $toast, $root, $refs } = instance.proxy
    const level = ref('')
    const amount = ref(0)
    const question_type = ref('')
    const levelTypeItems = ['N1', 'N2', 'N3', 'N4', 'N5']
    const isRendered = ref(false)
    const questions = ref()

    const questionTypeItems = [
        'Lựa chọn cách đọc đúng của từ trong ngoặc',
        'Viết lại từ trong ngoặc bằng chữ hán',
        'Lựa chọn từ thích hợp điển vào chỗ trống',
        'Tìm từ đồng nghĩa với từ trong ngoặc',
        'Lựa chọn câu có cách sử dụng đúng của từ'
    ]

    const defineQuestionType = (question_type) => {
      if(question_type === 'Lựa chọn cách đọc đúng của từ trong ngoặc')
        return 'hiragana'
      else if (question_type === 'Viết lại từ trong ngoặc bằng chữ hán')
          return 'kanji'
      else if (question_type === 'Lựa chọn từ thích hợp điển vào chỗ trống')
          return 'missing_word'
      else if (question_type === 'Tìm từ đồng nghĩa với từ trong ngoặc')
          return 'synonym'
      else if (question_type === 'Lựa chọn câu có cách sử dụng đúng của từ')
          return 'true_meaning'
    }

    const onRender = async () => {
      isRendered.value = false
      try {
        const questionType = defineQuestionType(question_type.value)
        const { data } = await api.get(`/test/get_question_to_practice?level=${level.value}&amount=${amount.value}&question_type=${questionType}`)
        questions.value = data
        isRendered.value = true
      } catch (e) {
        console.log('hihi', e)
      }
    }

    return {
      level,
      amount,
      question_type,
      levelTypeItems,
      questionTypeItems,
      onRender,
      isRendered,
      questions
    }
  }

})

</script>

<style lang="sass" scoped>
.test-page
  height: 100%
  margin: auto
.rounded-card
  border-radius: 5px
.standard
  width: 50%
  margin: auto
  justify-content: center
</style>