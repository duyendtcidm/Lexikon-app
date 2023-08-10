<template lang="pug">
  div.test-page
    v-card(v-if="!isRendered" ).mx-auto.mt-4(max-width='800' style='background-color: #fff' height='95%')
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
      quiz(
        :quizes="questions"
        :amount="exactAmount"
        :questionType="question_type"
        :render="isRendered"
        @on-finish="updateStatus"
      )



</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import {api, i18n} from '@/plugins'
import { Quiz } from '@/components'
import {showError} from "@/utils";

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
    const exactAmount = ref(0)

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
        exactAmount.value = data.length
        if (data.length) {
          questions.value = data
          isRendered.value = true
        } else {
          $toast.error($root.$t('common.msg.get_data_question'))
        }
      } catch (e) {
        showError(e, $toast, $root.$t('common.msg.get_data_failed'))
      }
    }

    const generateStatus = (status, isCorrect) => {
      if(isCorrect === 'true')
        if (status)
          status += 1
        else status = 1
      else
        if (status)
          status = status > 0 ? status : 0
        else
          status = 0
      return status

    }

    const updateStatus = async (results) => {
      isRendered.value = false
      let answeredQuestions = []
      let newQuestions = []

      results.forEach((result) => {
        if (result['status']) {
          answeredQuestions.push({id: result.id, question_id: result.question_id, status: generateStatus(result['status'], result['isCorrect'])})
        } else {
          newQuestions.push({question_id: result.question_id, status: generateStatus(result['status'], result['isCorrect'])})
        }
      })
      let param = {
        tried: answeredQuestions,
        new: newQuestions
      }
      try {
        await api.put(`/test/update_status`, param)
        $toast.success($root.$t('test.msg.congratulation'))
        isRendered.value = false
      } catch (e) {
        showError(e, $toast, $root.$t('common.msg.get_data_failed'))
      }
    }

    return {
      level,
      amount,
      exactAmount,
      question_type,
      levelTypeItems,
      questionTypeItems,
      onRender,
      isRendered,
      questions,
      updateStatus
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