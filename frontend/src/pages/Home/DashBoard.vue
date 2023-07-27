<template lang="pug">
  div.orderstats.pa-0
    v-row.ma-0.pl-4.pb-0.pt-1
      v-col(cols=7)
        span.title {{ $t('home.status.statistic') }}
      //v-col
      //  span.pl-10.title {{ $t('home.status.rank') }}
    v-row.ma-0.px-0.pb-4.justify-space-evenly(row wrap)
      .orderstats__item.text-center.px-3.py-1(v-for='(item, idx) in stats', :class='[item.class]', :key='item.class')
        div.d-block.router-item.pointer(v-if="item.to" @click ="goToOrder(item.to)")
          .normal-mode
            div.orderstats__item__title {{item.title}}
            .orderstats__item__content
              v-icon.mb-1(:color='item.color' large) {{item.icon}}
              //span.ml-4(v-if='!loading') {{item.count}}
              //v-progress-circular.ml-1(v-else, :width='2' color='rgba(0, 0, 0, 0.32)' indeterminate='')
              span.ml-4 {{item.count}}
        v-menu(
          v-else
          offset-x
        )
          template(v-slot:activator='{on}')
            .normal-mode(v-on='on').pointer
              .orderstats__item__title {{item.title}}
              .orderstats__item__content
                v-icon.mb-1(:color='item.color' large) {{item.icon}}
                //span.ml-4(v-if='!loading') {{item.count}}
                span.ml-4 {{item.count}}
                //v-progress-circular.ml-1(v-else, :width='2' color='rgba(0, 0, 0, 0.32)' indeterminate='')
          //template
          //  v-list.list-date(v-if="item.list_date")
          //    v-list-item(v-for="(date, idx) in item.list_date" :key="idx" @click="goToDate(date.auction_date, date.cst_ids)" link)
          //      v-list-item-title {{moment(date.auction_date).format($t('common.time_full_format'))}}
          //        span.primary--text.pl-3.bold--text {{ date.count }}
          //        span(v-if="item?.unit" ) {{$t(item?.unit)}}
            v-list.list-date(v-else)
              span.ml-2.grey--text {{ $t('common.no_data') }}
</template>

<script>
import {computed, getCurrentInstance, ref, toRefs, onMounted, watch} from 'vue'
import {api} from '@/plugins'
import {urlPath, endpoints} from "@/utils";
import router from '@/router'
import moment from "moment";

export default {
  name: 'JOrderStatus',
  props: {
    remainDatesCount: {
      type: Number,
      default: 0
    },
    remainDates: {
      type: Array,
      default: null
    },
    unconfirmSaleResultDatesCount: {
      type: Number,
      default: 0
    },
    unconfirmSaleResultDates: {
      type: Array,
      default: null
    }
  },
  setup(props, {$emit}) {
    const vm = getCurrentInstance().proxy
    const { $toast, $root } = vm
    const statusLink = ref('')
    const {
      remainDatesCount,
      remainDates,
      unconfirmSaleResultDatesCount,
      unconfirmSaleResultDates
    } = toRefs(props)

    const loading = ref(true)

    const stats = computed(() => {
      const stats = [
        {
          title: vm.$t('home.status.level.n1'),
          icon: "mdi-party-popper",
          color: 'primary',
          count: 5,
          to: 'q=~%28match_status~%28~%27new%29%29'
        },
        {
          title: vm.$t('home.status.level.n2'),
          icon: "mdi-bullseye-arrow",
          color: 'primary',
          count: 15,
          to: 'q=~%28match_status~%28~%27confirming%29%29'
        },
        {
          title: vm.$t('home.status.level.n3'),
          icon: "mdi-speedometer",
          color: 'primary',
          count: 20,
          to: 'q=~%28match_status~%28~%27confirmed%29%29'
        },
          {
          title: vm.$t('home.status.level.n4'),
          icon: "mdi-fire",
          color: 'primary',
          count: 30,
          to: 'q=~%28match_status~%28~%27confirmed%29%29'
        },
          {
          title: vm.$t('home.status.level.n5'),
          icon: "mdi-baby-carriage",
          color: 'primary',
          count: 40,
          to: 'q=~%28match_status~%28~%27confirmed%29%29'
        },

        // {
        //   title: vm.$t('home.calendar.registered_but_not_fixed'),
        //   icon: "mdi-warehouse",
        //   class: 'orderstats__unconfirm',
        //   color: 'grey',
        //   count: unconfirmSaleResultDatesCount.value || 0,
        //   list_date: unconfirmSaleResultDates.value,
        //   unit: "home.calendar.unit.sale"
        // },
        // {
        //   title: vm.$t('home.calendar.urizan'),
        //   icon: "mdi-warehouse",
        //   class: 'orderstats__remaining',
        //   color: 'red',
        //   count: remainDatesCount.value || 0,
        //   list_date: remainDates.value,
        //   unit: "home.calendar.unit.sale"
        // }
      ]
      return stats
    })

    // Get data orders
    // const getOrders = async () => {
    //   const defaultFields = [
    //     'new_count',
    //     'confirming_count',
    //     'invoiceable_count',
    //     'invoiced_count'
    //   ]
    //   api.get(`${endpoints.HOME}orders/_stats`, {
    //     params: {
    //       fields: defaultFields.join(',')
    //     }
    //   })
    //       .then(async response => {
    //         stats.value[0].count = response.data.new_count
    //         stats.value[1].count = response.data.confirming_count
    //         stats.value[2].count = response.data.invoiceable_count
    //         stats.value[3].count = response.data.invoiced_count
    //       })
    //       .catch(err => console.error(err))
    //       .finally(() => {
    //         loading.value = false
    //       })
    // }

    // Go to Order page filter by STATUS ORDER
    // const goToOrder = (status) => {
    //   router
    //       .push({
    //         name: urlPath.ORDER.name,
    //         query: {status: status}
    //       })
    //       .catch((err) => {
    //         // Ignore the vuex err regarding navigating to the page they are already on.
    //         if (
    //             err.name !== 'NavigationDuplicated' &&
    //             !err.message.includes('Avoided redundant navigation to current location')
    //         ) {
    //           // But print any other errors to the console
    //           console.log(err)
    //         }
    //       })
    // }

    // Go to SALE page filter by Auction Date
    // const goToDate = async (auctionDate, cstIds) => {
    //   try {
    //     const { data } = await api.get(`${endpoints.HOME}cst_ord?ids=${cstIds}`)
    //     router
    //       .push({
    //         name: urlPath.SALE.name,
    //         query: {auction_date: auctionDate, cst_id: data.__data__?.id}
    //       })
    //       .catch((err) => {
    //         // Ignore the vuex err regarding navigating to the page they are already on.
    //         if (
    //             err.name !== 'NavigationDuplicated' &&
    //             !err.message.includes('Avoided redundant navigation to current location')
    //         ) {
    //           // But print any other errors to the console
    //           console.log(err)
    //         }
    //       })
    //   } catch (e) {
    //     $toast.error($root.$t('common.msg.redirect_failed'))
    //   }
    // }

    // watch(props, () => {
    //   getOrders()
    // })

    return {
      loading,
      stats,
      // goToDate,
      moment,
      statusLink,
      // goToOrder
    }
  }
}
</script>

<style scoped lang="sass">
@import '~vuetify/src/styles/settings/_variables'
.justify-space-evenly
  justify-content: space-evenly

.title
  font-size: 20px
  font-weight: bold

.right-border
  border-right: solid rgba(111, 152, 111, 0.3)
  padding-right: 54px !important

.orderstats
  border: 1px solid lightgray
  border-radius: 5px
  background-color: white
  width: 100%
  height: 100%

  .v-badge
    display: inline

  @media #{map-get($display-breakpoints, 'xs-only')}
    &__item
      margin-top: 10px
  @media #{map-get($display-breakpoints, 'sm-and-down')}
    &__item
      margin-bottom: 16px !important

  &__item
    .router-item
      text-decoration: none

    &__title
      text-decoration: underline
      color: darkgreen

    &__content
      font-size: 32px

      span
        color: rgba(0, 0, 0, 0.81)

  &__remaining
    .orderstats__item__title
      color: red !important
      text-decoration: underline

  &__unconfirm
    .orderstats__item__title
      color: #282828 !important
      text-decoration: underline

.list-date
  max-height: 200px
  overflow-y: auto

.pointer
  cursor: pointer
</style>
