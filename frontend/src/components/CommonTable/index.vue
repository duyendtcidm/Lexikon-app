<template lang="pug">
  v-data-table.main(
    v-model="selected"
    :headers="headersRef"
    :items="itemsRef"
    hide-default-footer
    :single-select="singleSelect"
    :item-key="itemKey ? itemKey : 'name'"
    :items-per-page="-1"
    class="elevation-2"
    :style="(maxWidth ? `max-width: ${maxWidth.toString()}px;` : '') + (width ? `width: ${width.toString()}px;` : '')"
    fixed-header
    :show-select="showSelect"
    checkbox-color="primary"
    mobile-breakpoint="0"
    @click:row="handleClick"
  )
    template(v-slot:header.data-table-select="{ props, on }")
      div.border-checkbox
        v-simple-checkbox(:value="props.value" v-on="on" color="primary")
    template(v-slot:item.name="{ item }")
      span {{ item.name }}
    template(v-slot:item.action="{ item }")
      slot(name="action" :item="item")
    template(v-slot:no-data)
      span {{ $t('common.no_data') }}


</template>
<script>
import {defineComponent, onMounted, ref, watch} from 'vue'
import { numberToString } from '@/utils'
import moment from "moment"

const CommonTable = defineComponent({
  props: {
    headers: {
      type: Array,
      required: true
    },
    items: {
      type: Array,
      required: true
    },
    maxWidth: {
      type: Number,
      default: 1000,
      required: false
    },
    width: {
      type: Number,
      default: null,
      required: false
    },
    showSelect: {
      type: Boolean,
      default: false,
      required: false
    },
    itemKey: {
      type: String,
      required: false
    }
  },
  setup(props, {emit}) {
    const headersRef = ref([])
    const itemsRef = ref([])
    const singleSelect = ref(false)
    const selected = ref([])

    const handleClick = (row) => {
      emit('on-click', row)
    }

    const generateTable = () => {
      headersRef.value = props.headers
      itemsRef.value = props.items
    }

    onMounted(() => {
      generateTable()
    })
    watch(props, () => {
      generateTable()
    })
    watch(selected, () => {
      emit('on-select', selected)
    })
    return {
      singleSelect,
      selected,
      headersRef,
      itemsRef,
      handleClick,
      numberToString,
      moment
    }
  }
})

export default CommonTable
</script>

<style scoped lang="sass">
.main
  margin: 0 auto
.text-start
  padding: 0
::v-deep table > thead > tr > th > span
  color: white !important
  font-size: 16px
.border-checkbox i
  background-color: white
  border-radius: 5px
</style>
