<template lang="pug">
  v-card.mx-auto.mt-5(max-width='800' elevation='4')
    v-card-title.justify-center.rounded-card.mb-1(style='background-color: #81D4FA' primary-title='')
      h1.font-weight-thin Multiple Choice Quiz
    v-card-text.pt-2(primary-title='')
      p Currently answering question Nr:{{this.currentIndex +1}}
    //v-img.white--text.align-end(height='200px' src='../assets/multiple_choice.jpg')
    v-spacer
    v-card(style='background-color: #E1F5FE')
      v-card-text()
        //v-if='loading'
        h4.justify-center.font-italic Data is being loaded one moment please...
      v-card-text()
        //v-else=''
        h4.justify-center.font-italic {{this.currentQuestion}}
      v-spacer
      v-card-actions(rules='required')
        v-radio-group(v-model='answered')
          v-radio(v-for='n in this.shuffledAnswers' :key='n' :label='`${n}`' :value='n')
    v-card-actions.d-flex.justify-space-around
      v-btn(@click='skip' elevation='2' color='error' size='x-large')
        | Exit
      v-btn(@click='next' elevation='2' color='green' size='x-large')
        | Next
</template>

<script>
import {defineComponent, getCurrentInstance, ref, toRefs} from 'vue'
import { PRACTICE_HEADER } from '../index'

export default defineComponent ({
  components: {

  },
  props: {
    quizes: {
      type: Object,
      required: false
    }
  },
  setup(props) {
    const questions = toRefs(props.quizes)
    const currentIndex = ref(1)
    const currentQuestion = ref(false)
    const answered = ref(false)
    const shuffledAnswers = ref(false)

    const skip = () => {

    }
    const next = () => {

    }

    return {
      questions,
      currentIndex,
      currentQuestion,
      answered,
      shuffledAnswers,
      skip,
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