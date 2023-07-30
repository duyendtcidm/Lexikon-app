<template lang="pug">
  common-table(
    :headers="headers"
    :items="items"
    @on-click="onClickNextIcon"
    :max-width="maxWidth"
  )
    //template(v-slot:name="{item}")
    //  div(v-if="isShowView")
    //    v-icon(medium).mr-2 mdi-folder-open-outline
    //    span.link-text {{ item.name }}
    //  div(v-else) {{ item.name }}
    //template(v-slot:name_display="{item}")
    //  div(v-if="isShowView")
    //    v-icon(medium).mr-2 mdi-folder-open-outline
    //    span.link-text {{ item.name_display }}
    //  div(v-else) {{ item.name_display }}
    //template(v-if="isShowDestination" v-slot:is_default="{item}")
    //  div(v-if="item.is_default")
    //    span {{$t('payment_destination.is_default')}}
    //template(v-if="isShowDestination" v-slot:account_type="{item}")
    //  span {{ convertAccountType(item.account_type) }}
    template(v-slot:action="{item}")
      v-menu(
        left
        offset-y
        min-width="9vw"
      )
        template(v-slot:activator='{on}')
          v-btn(v-on='on' icon)
            v-icon(medium) mdi-dots-vertical
        v-list
          v-list-item(v-for="(action, i) in actions" :key="i" link @click="emitAction(action.action, item)")
            v-icon.pr-3(:color="action.color") {{ action.icon }}
            v-list-item-title {{ $t(action.text) }}
</template>
<script>
import { defineComponent } from 'vue'
import CommonTable from '../CommonTable/index'

const JMasterItemList = defineComponent({
  props: {
    maxWidth: {
      type: Number,
      default: 1000,
      required: false
    },
    items: {
      type: Array,
      required: true
    },
    headers: {
      type: Array,
      required: true
    },
    actions: {
      type: Array,
      required: true,
      default: () => []
    }
  },
  components: {
    CommonTable
  },
  setup(props, { emit }) {
    // Click to open unit of each group
    const onClickNextIcon = (item) => {
      emit('go-to-master-detail', item)
    }

    // emit all action (on-update, on-delete)
    const emitAction = (action, item) => {
      emit(action, item)
    }
    return {
      onClickNextIcon,
      emitAction
    }
  }
})

export default JMasterItemList
</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'
.home
  width: 100%

.btn
  border: 0px

.link-text
  color: blue
  text-decoration: underline

::v-deep table > thead > tr > th > span
  color: white !important
  font-size: 16px

::v-deep table > tbody > tr > td
  font-size: 16px !important
</style>
