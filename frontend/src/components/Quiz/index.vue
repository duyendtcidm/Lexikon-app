<template lang="pug">
  v-card.ma-auto.mt-5(max-width='800' elevation='4')
    v-card-title.justify-center.rounded-card.mb-1(style='background-color: #81D4FA' primary-title='')
      h1.font-weight-thin Multiple Choice Quiz
    v-card-text.pt-2(primary-title='')
      p Currently answering question Nr: {{currentIndex}}
    //v-img.white--text.align-end(height='200px' src='../assets/multiple_choice.jpg')
    v-spacer
    v-card(style='background-color: #E1F5FE')
      v-card-text()
        //h4.justify-center.font-italic {{currentQuestion.content}}
      v-spacer
    v-card-actions(rules='required')
      v-radio-group(v-model='answered')
        v-radio(v-for='n in this.choices' :key='n' :label='`${n}`' :value='n')
    v-card-actions(v-if="!isShowAnswer").d-flex.justify-space-around
      v-btn(@click='skip' elevation='2' color='error' size='x-large')
        | {{$t('test.quiz.button.skip')}}
      v-btn.white--text(@click='submit' elevation='2' color='green' size='x-large')
        | {{$t('test.quiz.button.submit')}}
    v-card-actions(v-if="isShowAnswer").d-flex.justify-space-around
      span hihihi
      v-btn.white--text(@click='next' elevation='2' color='green' size='x-large')
        | {{$t('test.quiz.button.next')}}
</template>

<script>
import {defineComponent, getCurrentInstance, onMounted, ref, toRefs} from 'vue'

export default defineComponent ({
  components: {

  },
  props: {
    quizes: {
      type: Array,
      required: false
    }
  },
  setup(props) {
    const questions = ref()
    const currentIndex = ref(1)
    const currentQuestion = ref({})
    const answered = ref(false)
    const choices = ref()
    const isShowAnswer = ref(false)
    console.log(questions[currentIndex.value].value)

    const skip = () => {
      currentIndex.value += 1
      currentQuestion.value = questions[currentIndex.value].value

    }
    const getColorAnswer = (isCorrect) => {
      if (isCorrect)
        return 'green'
      else return 'red'
    }
    const submit = () => {
      isShowAnswer.value = true

    }
    const next = () => {
      isShowAnswer.value = false
      currentQuestion.value = questions[currentIndex.value].value
      choices.value = currentQuestion.value[choices]
      console.log('currentQuestion.value', currentQuestion.value)

    }

    onMounted(() => {
      questions.value = props.quizes
      currentQuestion.value = questions[currentIndex.value].value
    })

    return {
      questions,
      currentIndex,
      currentQuestion,
      answered,
      choices,
      isShowAnswer,
      skip,
      submit,
      next
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common'
.question-part
  margin: auto
  width: 700px
.choice
  width: 100%
  button
    width: 40%
.right-answer
  background-color: green
  color: green
.wrong-answer
  background-color: red


</style>