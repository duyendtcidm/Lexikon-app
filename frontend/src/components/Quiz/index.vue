<template lang="pug">
  v-card.pa-6.ma-auto.mt-5(max-width='1000' elevation='4')
    v-card-title.justify-center.rounded-card.mb-1(style='background-color: #81D4FA' primary-title='')
      h1.font-weight-thin {{requirement}}
    //  Show timer
    v-card-text.pt-2
      h3 {{$t('test.quiz.question_no')}}: {{currentIndex}}
      v-spacer
      h3 {{$t('test.quiz.correct_ratio')}}: {{correctRatio}} %
    v-img.ma-auto(height='35%' width="35%" src='@/assets/sakura.jpeg')
    v-spacer
    v-card(style='background-color: #E1F5FE')
      v-card-text()
        h3.justify-center {{currentQuestion.content}}
      v-spacer
    v-card-actions(rules='required')
      v-radio-group(v-model='answered' :disabled="isShowAnswer")
        div(v-for='(n, idx) in choices' :key='n')
          v-row
            v-col(cols="2")
              v-icon(v-if="isShowAnswer && idx == currAnswer" color="green") mdi-check
            v-col
              v-radio(:label='`${n}`' :value='n')
    v-card-actions(v-if="!isShowAnswer").d-flex.justify-space-around
      v-btn(
        @click='skip'
        elevation='2'
        color='error'
        x-large
      )
        | {{$t('test.quiz.button.skip')}}
      v-btn.white--text(
        @click='submit'
        elevation='2'
        color='green'
        x-large
        :disabled="!answered"
      )
        | {{$t('test.quiz.button.submit')}}
    v-card-actions.right-answer(v-if="isShowAnswer && isCorrect").d-flex.justify-space-around
      v-list.right-answer
        div(v-for="(explain, idx) in explanation" )
          span(v-if="explain !== ''") {{idx}}. {{explain}}
      v-btn.white--text(
        @click='next'
        elevation='2'
        color='green'
        x-large
      )
        | {{$t('test.quiz.button.next')}}
    v-card-actions.wrong-answer(v-if="isShowAnswer && !isCorrect").d-flex.justify-space-around
      v-list.wrong-answer
        div(v-for="(explain, idx) in explanation" )
          span(v-if="explain !== ''") {{idx}}. {{explain}}
              //span(v-else-if="idx === currAnswer") hello {{idx}}. {{explain}}
              //span {{idx}} {{currAnswer}} {{idx == currAnswer}}
      v-btn.white--text(
        @click='next'
        elevation='2'
        color='red'
        x-large
      )
        span(v-if="currentIndex < numberQuestion") {{$t('test.quiz.button.next')}}
        span(v-else) {{$t('test.quiz.button.retest')}}
</template>

<script>
import {defineComponent, getCurrentInstance, onMounted, ref, toRefs, watch} from 'vue'

export default defineComponent ({
  props: {
    quizes: {
      type: Array,
      required: true,
      default: []
    },
    amount: {
      type: Number,
      required: true,
      default: 0
    },
    questionType: {
      type: String,
      required: true,
    }
  },
  setup(props, {emit}) {
    const questions = ref()
    const requirement = ref()
    const currentIndex = ref(1)
    const numberQuestion = ref()
    const currentQuestion = ref({})
    const currAnswer = ref()
    const answered = ref(false)
    const choices = ref({})
    const explanation = ref({})
    const isShowAnswer = ref(false)
    const isCorrect = ref(false)
    const correctRatio = ref('0.00')
    const currCorrectQuestion = ref(0)

    const skip = () => {
      isShowAnswer.value = true
      questions.value[currentIndex.value-1]['isCorrect'] = 'false'
    }
    const submit = () => {
      isShowAnswer.value = true
      if (answered.value === choices.value[questions.value[currentIndex.value-1]['answer']]){
        isCorrect.value = true
        currCorrectQuestion.value += 1
        questions.value[currentIndex.value-1]['isCorrect'] = 'true'
      } else {
        questions.value[currentIndex.value-1]['isCorrect'] = 'false'
      }
    }
    const next = () => {
      isShowAnswer.value = false
      isCorrect.value = false
      currentIndex.value = currentIndex.value + 1
      if (currentIndex.value <= numberQuestion.value){
        currentQuestion.value = questions.value[currentIndex.value-1]
        choices.value = currentQuestion.value['choices']
        explanation.value = currentQuestion.value['explanation']
        currAnswer.value = currentQuestion.value['answer']
      } else {
        emit('on-finish', questions.value)
      }
    }

    onMounted(() => {
      questions.value = props.quizes
      requirement.value = props.questionType
      numberQuestion.value = props.amount
      currentQuestion.value = questions.value[currentIndex.value-1]
      choices.value = currentQuestion.value['choices']
      explanation.value = currentQuestion.value['explanation']
      currAnswer.value = currentQuestion.value['answer']
    })

    watch(
      () => currentIndex.value,
      () => {
        correctRatio.value = (currCorrectQuestion.value / (currentIndex.value - 1) * 100).toFixed(2)
      }
    )

    return {
      questions,
      requirement,
      currentIndex,
      currentQuestion,
      numberQuestion,
      correctRatio,
      currAnswer,
      answered,
      choices,
      explanation,
      isShowAnswer,
      isCorrect,
      skip,
      submit,
      next
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common'
::v-deep v-list
  padding: 0
::v-deep v-list-item
  min-height: 30px
.question-part
  margin: auto
  width: 700px
.choice
  width: 100%
  button
    width: 40%
.right-answer
  background-color: rgba(184, 252, 184, 0.81)
  border-radius: 5px
  color: green
.wrong-answer
  background-color: rgb(255, 178, 178)
  border-radius: 5px


</style>