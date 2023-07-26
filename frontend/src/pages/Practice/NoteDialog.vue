<template lang="pug">
  v-dialog(
    scrollable
    persistent
    max-width='700'
    v-model="value"
  )
    v-card.white-bg
      v-card-title.primary
        span.white--text {{ $t(`practice.note.title`) }}

      v-card-text
        v-col.pb-0.pl-1.pr-0
          v-textarea.mt-2(
            v-if="value"
            outlined
            autofocus
            hide-details
            rows="3"
            :label="$t('practice.note.edit_note')"
            v-model="changedRemark"
          )

      v-card-actions
        v-row.mb-1(justify="center")
          v-btn.relative-btn.ma-2.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            width="40%"
            @click="$emit('on-close')"
          )
            span.blue--text {{$t('common.cancel')}}
          v-btn.relative-btn.ma-2.white--text(
            :large="!$vuetify.breakpoint.xsOnly"
            color="primary"
            width="40%"
            @click="updateRemark"
          )
            | {{$t('common.ok')}}
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'

const NoteDialog = defineComponent({
  props: {
    value: {
      type: Boolean,
      required: true
    },
    remark: {
      type: String,
      required: true
     }
  },
  setup(props, { emit }) {
    const changedRemark = ref('')
    const updateRemark = () => {
      emit('on-ok', changedRemark.value)
    }
    watch(
      () => props.remark,
      () => {
        changedRemark.value = props.remark
      }
    )

    return {
      changedRemark,
      updateRemark
    }
  }
})

export default NoteDialog
</script>

<style lang="sass"></style>
