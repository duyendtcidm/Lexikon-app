<template lang="pug">
  v-dialog(
    scrollable
    persistent
    max-width='500'
    v-model="value"
  )
    v-card.white-bg(height="400" )
      v-card-title.primary
        span.white--text {{ item.name }}
        v-spacer
        v-btn(icon dark @click="reset('close')")
          v-icon mdi-close

      v-card-text(:style="{'line-height': 5}").mb-4
        v-row.fix-row.ma-0.pa-0
          v-col.pa-0.ma-0(cols="3")
            span {{$t('practice.exercise.yomi')}} :
          v-col.pa-0(cols="5")
            //validation-provider(rules="required" v-slot="{ errors }" :name="$t('practice.exercise.yomi')")
            //  v-text-field#yomi(
            //    :error-messages="errors"
            //    v-model="yomi"
            //  )
            v-text-field#yomi(
              autofocus
              v-model="yomi"
              :disabled="checked"
            )
          v-col.py-0.pl-5(cols="4" v-if="checked" )
            span(v-if="item.yomi.trim().toLowerCase()===yomi.trim().toLowerCase()" ).green--text {{item.yomi}}
            span(v-else).red--text {{item.yomi}}
        v-row.fix-row.ma-0.pa-0
          v-col.pa-0.ma-0(cols="3")
            span {{$t('practice.exercise.kanji')}} :
          v-col.pa-0(cols="5")
            //validation-provider(rules="required" v-slot="{ errors }" :name="$t('practice.exercise.kanji')")
            //  v-text-field#kanji(
            //    :error-messages="errors"
            //    v-model="kanji"
            //  )
            v-text-field#kanji(
              v-model="kanji"
              :disabled="checked"
            )
          v-col.py-0.pl-5(cols="4" v-if="checked" )
            span(v-if="item.kanji.trim().toLowerCase()===kanji.trim().toLowerCase()" ).green--text {{item.kanji}}
            span(v-else).red--text {{item.kanji}}
        v-row.fix-row.ma-0.pa-0
          v-col.pa-0.ma-0(cols="3")
            span {{$t('practice.exercise.meanings')}} :
          v-col.pa-0(cols="5")
            //validation-provider(rules="required" v-slot="{ errors }" :name="$t('practice.exercise.meanings')")
            //  v-text-field#meanings(
            //    :error-messages="errors"
            //    v-model="meanings"
            //  )
            v-text-field#meanings(
              v-model="meanings"
              :disabled="checked"
            )
          v-col.py-0.pl-5(cols="4" v-if="checked" )
            span(v-if="item.meanings.trim().toLowerCase()===meanings.trim().toLowerCase()" ).green--text {{item.meanings}}
            span(v-else).red--text {{item.meanings}}
        //div(v-if="Object.keys(item.synonym).length" v-for="(name, value) in item.synonym")
        //  v-row.fix-row.ma-0.pa-0
        //    v-col.pa-0.ma-0(cols="4")
        //      span {{name}} :
        //    v-col.pa-0(cols="8")
        //      validation-provider(rules="required" v-slot="{ errors }")
        //        v-text-field#meanings(
        //          :error-messages="errors"
        //        )
        //div(v-if="Object.keys(item.antonym).length" )
        //  span jk
        //  div(v-for="(value, name, idx) in item.antonym")
        //    v-row.fix-row.ma-0.pa-0
        //      v-col.pa-0.ma-0(cols="4")
        //        span {{name}} :
        //      v-col.pa-0(cols="8")
        //        validation-provider(rules="required" v-slot="{ errors }")
        //          v-text-field#meanings(
        //            :error-messages="errors"
        //          )
      v-card-actions
        div.mb-1.action-btn(v-if="!checked")
          v-btn.relative-btn.ma-2.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            width="40%"
            @click="reset('cancel')"
          )
            span.blue--text {{$t('common.cancel')}}
          v-btn.relative-btn.ma-2.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            color="primary"
            width="40%"
            @click="checkResults"
          )
            | {{$t('practice.check')}}
        div.action-btn(v-else)
          v-btn.relative-btn.ma-2.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            color="primary"
            width="40%"
            @click="reset('ok')"
          )
            | {{$t('common.ok')}}
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'

const Question = defineComponent({
  props: {
    value: {
      type: Boolean,
      required: true
    },
    item: {
      type: Object,
      required: true
     }
  },
  setup(props, { emit }) {
    const checked = ref(false)
    const kanji = ref('')
    const yomi = ref('')
    const meanings = ref('')
    const isPass = ref(false)
    const checkResults = () => {
      let count = 3
      let correct = 0
      if (kanji.value && kanji.value.trim().toLowerCase() === props.item.kanji.trim().toLowerCase()) correct++
      if (yomi.value && yomi.value.trim().toLowerCase() === props.item.yomi.trim().toLowerCase()) correct++
      if (meanings.value && meanings.value.trim().toLowerCase() === props.item.meanings.trim().toLowerCase()) correct++
      checked.value = true
      isPass.value = (correct / count * 100 > 80)
    }

    const reset = (type:any) => {
      checked.value=false
      kanji.value = ''
      yomi.value = ''
      meanings.value = ''
      if (type === 'ok')
        emit('on-ok', isPass)
      else emit('on-close')
    }
    watch(
      () => props.item,
      () => {
        checked.value = false
      }
    )

    return {
      kanji,
      yomi,
      meanings,
      checked,
      isPass,
      reset,
      checkResults
    }
  }
})

export default Question
</script>


<style scoped lang="sass">
.fix-row
  justify-content: center
  align-items: center
  height: 40px !important
  font-size: 16px
.action-btn
  width: 100%
  display: flex
  justify-content: space-around
</style>
