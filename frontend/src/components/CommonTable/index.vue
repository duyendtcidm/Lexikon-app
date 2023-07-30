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
      slot(name="name" :item="item")
    template(v-slot:item.name_display="{ item }")
        slot(name="name_display" :item="item")
    template(v-slot:item.action="{ item }")
      slot(name="action" :item="item")
    template(v-slot:no-data)
      span {{ $t('common.no_data') }}
    template(v-slot:item.box="{ item }")
      span {{numberToString(item.box)}}
    template(v-slot:item.stem="{ item }")
      span {{numberToString(item.stem)}}
    template(v-slot:item.amount="{ item }")
      span {{numberToString(item.amount)}}
    template(v-slot:item.sale_amount="{ item }")
      span {{numberToString(item.sale_amount)}}
    template(v-slot:item.remaining_pot="{ item }")
      span {{numberToString(item.remaining_pot)}}
    template(v-slot:item.remaining_cut="{ item }")
      span {{numberToString(item.remaining_cut)}}
    template(v-slot:item.remaining="{ item }")
      span {{numberToString(item.remaining)}}
    template(v-slot:item.sale_stem="{ item }")
      span {{numberToString(item.sale_stem)}}
    template(v-slot:item.tax_amount="{ item }")
      span {{numberToString(item.tax_amount)}}
    template(v-slot:item.sale_amount_with_tax="{ item }")
      span {{numberToString(item.sale_amount_with_tax)}}
    template(v-slot:item.usage_fee="{ item }")
      span {{numberToString(item.usage_fee)}}
    template(v-slot:item.fee_amount="{ item }")
      span {{numberToString(item.fee_amount)}}
    template(v-slot:item.deduction_amount="{ item }")
      span {{numberToString(item.deduction_amount)}}
    template(v-slot:item.total_amount="{ item }")
      span {{numberToString(item.total_amount)}}
    template(v-slot:item.fee="{ item }")
      span {{numberToString(item.fee)}}
    template(v-slot:item.total_amount_closed_ar="{ item }")
      span {{numberToString(item.total_amount_closed_ar)}}
    template(v-slot:item.tax_amount_rate="{ item }")
      span {{numberToString(item.tax_amount_rate)}}
    template(v-slot:item.tax_amount_rate2="{ item }")
      span {{numberToString(item.tax_amount_rate2)}}
    template(v-slot:item.customer="{ item }")
      span {{item.customer.name_short}}
    template(v-slot:item.payment_destination="{ item }")
      span {{item.payment_destination.name}}
    template(v-slot:item.payment_method="{ item }")
      span {{item.payment_method.name}}
    template(v-slot:item.payment_date="{ item }")
      span {{moment(item.payment_date).format($root.$t(`common.time_month_date`))}}
    template(v-slot:item.is_default="{ item }")
      slot(name="is_default" :item="item")
    template(v-slot:item.account_type="{ item }")
      slot(name="account_type" :item="item")
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
