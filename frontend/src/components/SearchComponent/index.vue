<template lang="pug">
  div.mt-0.mx-2.search
    v-text-field.mb-1.input(
      :label="searchText"
      outlined
      dense
      v-model="searchInfoValue"
      prepend-inner-icon="mdi-magnify"
      @input="onInput()"
      color="primary"
    )
    div.pl-10
      v-btn.mr-2.hidden-sm-and-up.green-bg-btn.button(dark icon @click="onClickOpenAddDialog()")
        v-icon mdi-plus
      v-btn.mr-2.hidden-xs-only.button(color="primary" dark @click="onClickOpenAddDialog()")
        v-icon mdi-plus
        span {{ $t('common.add') }}


</template>

<script>
import {defineComponent, getCurrentInstance, ref, watch} from 'vue'
import {api} from "@/plugins/index.ts";
import {endpoints} from "@/utils";

export default defineComponent({
  props: {
    searchInfo: {
      type: String,
      required: true
    },
    searchText: {
      type: String,
      required: true
    }
  },
  setup(props, {emit}) {
    const instance = getCurrentInstance()
    const {$toast, $root} = instance.proxy
    const searchInfoValue = ref(props.searchInfo || '')
    const syncLoading = ref(false)
    const onInput = () => {
      emit('inputting', searchInfoValue.value)
    }

    // Click to open ADD dialog
    const onClickOpenAddDialog = () => {
      emit('open-add-dialog')
    }

    watch(
      () => props.searchInfo,
      () => {
        searchInfoValue.value = props.searchInfo
      }
    )

    return {
      onInput,
      searchInfoValue,
      onClickOpenAddDialog,
      syncLoading
    }
  }
})
</script>

<style lang="sass">
@import '@/style/css/common.sass'
.button
  height: 40px !important

.search
  max-width: 900px
  padding-top: 30px
  display: flex

  .divider
    background-color: var(--v-primary-base)

  .input
    .v-input__slot
      background: #ffffff
      min-height: 40px !important

    .v-input__slot:hover
      background: #ffffff !important

  .categories-list
    position: absolute
    left: 8px
    right: 8px
    z-index: 4
    overflow: auto
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.5)

    .category-title
      padding: 4px

      .v-icon
        color: var(--v-primary-base)
        padding: 2px !important

.v-application .mx-2
  margin: 0 auto !important

.green-bg-btn
  background-color: var(--v-primary-base)
  border-color: var(--v-primary-base)
</style>