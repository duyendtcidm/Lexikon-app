<template lang="pug">
  div.question-part
    div(v-for="(ques,idx) in questions" :key="idx")
      h4.mt-5.mb-2 {{ques.code}}. {{ques.content}}
      v-col.choice(cols="6" v-for="(choice,idx) in ques.choices")
        v-btn(
          :style="isShowAnswer&&isAnswered  ? 'right-answer' : 'wrong-answer' "
          dense
          color='white'
          @click="getClassAnswer(idx, ques)"
          )
          span {{choice}}
      div(v-if="isShowAnswer").explain
        span {{ques.explain}}
</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import { PRACTICE_HEADER } from '../index'

export default defineComponent ({
  components: {

  },
  setup() {
    const questions = [
    {
      id: 1,
      code: 1,
      type: 'pronunciation',
      content: 'とても(悲しい)話を聞いた。',
      choices: {
        1: 'おかしい',
        2: 'かなしい',
        3: 'きびしい',
        4: 'さびしい'
      },
      answer: '2',
      explain: "'1. お菓子:  kẹo' '2. 悲しい: buồn' '3. 厳しい: nghiêm túc' '4. 寂しい: cô đơn'"
    },
      {
      id: 1,
      code: 23,
      type: 'pronunciation',
      content: 'とても(悲しい)話を聞いた。',
      choices: {
        1: 'おかしい',
        2: 'かなしい',
        3: 'きびしい',
        4: 'さびしい'
      },
      answer: '2',
      explain: ''
      }
    ]
    const isShowAnswer = ref(false)
    const isAnswered = ref(false)
    const getClassAnswer = (choice, ques) => {
      isAnswered.value = true
      if (choice === ques.answer) {
        isShowAnswer.value = true
      } else {
        isShowAnswer.value = false
      }
    }

    return {
      questions,
      getClassAnswer,
      isShowAnswer,
      isAnswered
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