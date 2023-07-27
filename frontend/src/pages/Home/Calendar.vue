<template lang="pug">
  div.chart-container
    v-row
      v-col.catalog-calendar(cols="12")
        v-sheet.pa-2
          v-row.px-4.pt-1.pb-2
            v-col.pa-0.ma-0(cols="12")
              div.button-calendar
                span.mr-4.title {{ $t('home.calendar.title')}}
                v-btn(outlined, @click="setToday") {{ $t('home.today') }}
                v-btn(fab, small, text, @click="prev(focus)")
                  v-icon(small) mdi-chevron-left
                v-btn(fab, small, text, @click="next(focus)")
                  v-icon(small) mdi-chevron-right
                span.header-text(v-if="$refs.calendar") {{ $refs.calendar.title }}
        v-row(no-gutters)
          v-col.catalog-calendar__left(cols="12", md="7")
            v-sheet(height="310")
              v-calendar.pa-0(
                ref="calendar",
                v-model="clickedDay",
                :weekdays="weekdays",
                locale="vi"
                type="month",
                @change="updateRange"
              )
                template(v-slot:day="day")
                  div.pointer.date-cell(
                    @click='clickEvent(day)'
                  )
                    div.status-div
                      v-icon(
                        size="20"
                        :style="{ color: STATUS_ICONS[getStatusForDay(day)]?.color, opacity: getStatusForDay(day) !== null ? 1 : 0.01 }"
                      ) {{ getStatusForDay(day) ? STATUS_ICONS[getStatusForDay(day)]?.icon : 'mdi-text-box-search-outline' }}
                template(v-slot:day-label="day")
                  v-btn(
                    v-if='clickedDay === day.date'
                    :style='{"background-color": "#d9d9d9", "float": "left"}'
                    fab icon x-small
                    @click='clickEvent(day)'
                  )
                    | {{ day.day }}
                  v-btn(
                    v-else-if='today === day.date'
                    :style='{"border": "1px solid gray", "float": "left"}'
                    fab icon x-small
                    @click='clickEvent(day)'
                  )
                    | {{ day.day }}
                  v-btn(
                    v-else
                    :style='{"float": "left"}'
                    fab icon x-small
                    @click='clickEvent(day)'
                  )
                    | {{ day.day }}
          v-col.catalog-calendar__right(cols="12", md="5")
            v-list
              v-subheader(v-if='clickedDay')
                v-icon mdi-calendar-search
                span.pl-3 {{ clickedDay }}
              template(v-if="!noData")
                div(v-for="key in Object.keys(dateDetails)")
                  v-list-item-content.py-1.my-0.ml-8(v-if="dateDetails[key].length > 0")
                    v-list-item-title
                      v-icon(
                        size="18"
                        :style="'color:' + STATUS_ICONS[key]?.color"
                        ) {{STATUS_ICONS[key]?.icon}}
                      span.ml-1.bold--text.primary--text {{$t('home.calendar.' + STATUS_ICONS[key]?.title)}}
                      span.ml-2 {{dateDetails[key].length}}
                      span.ml-2 {{$t('home.calendar.unit')}}
              template(v-else)
                span.ml-5.grey--text {{ $t('common.no_data')}}
</template>

<script lang="js">
import {DateTime} from "luxon"
import {endpoints, urlPath} from "@/utils"
import {api} from "@/plugins"
import {getCurrentInstance, toRefs, ref, onMounted} from "vue"
import router from "../../router"
import moment from "moment"

export default {
  setup(props, {emit}) {
    const instance = getCurrentInstance()
    const {$refs, $root} = instance.proxy
    const weekdays = [0, 1, 2, 3, 4, 5, 6]
    const assignmentDates = ref([])
    const invoiceStatusCount = ref(0)
    const orders = ref([])
    const today = ref(null)
    const focus = ref(null)
    const start = ref(null)
    const end = ref(null)
    const clickedDay = ref(null)
    const noData = ref(false)
    const dateDetails = ref({})
    const calendarData = ref(null)

    const STATUS_ICONS = ref({
      0: {
        title: 'new_words',
        icon: 'mdi-text-box-search-outline',
        color: 'grey'
      },
      1: {
        title: 'doing_words',
        icon: 'mdi-note-edit-outline',
        color: 'orange'
      },
      2: {
        title: 'complete_words',
        icon: 'mdi-text-box-check-outline',
        color: 'green'
      }
    })

    const CALENDAR_STATUSES = {
        'new_words': 0,
        'doing_words': 1,
        'complete_words': 2
    }
    const prev = (date) => {
      $refs.calendar.prev()
      date = new Date(date)
      // getMonth return order of this month in [1,2,3,4,5,6,7,8,9,10,11,12]
      let month = (date.getMonth() === 0 ? 12 : date.getMonth()).toString().padStart(2, '0')
      let year = month === '01' ? date.getFullYear() - 1 : date.getFullYear()
      let day = new Date(year, month, 0).getDate()
      focus.value = year + '-' + month + '-' + day
    }

    const next = (date) => {
      $refs.calendar.next()
      date = new Date(date)
      let month = (date.getMonth() + 1 === 12 ? 1 : date.getMonth() + 2).toString().padStart(2, '0')
      let year = month === '01' ? date.getFullYear() +1 : date.getFullYear()
      focus.value = year + '-' + month + '-' + '01'
    }

    const getToday = () => {
      return DateTime.local().toFormat("yyyy-MM-dd")
    }

    const updateRange = (data) => {
      // Prevent useless trigger when click on date
      if (start.value && data.start && start.value === data.start) {
        return
      }
      start.value = data.start
      end.value = data.end
      getDates()
    }

    const getDates = async() => {
      await api
          .get(`/home/calendar?start_date=${start.value.date}&end_date=${end.value.date}`)
          .then((response) => {
            calendarData.value = response.data
          })
          .catch(err => console.error(err))
      dateDetails.value = getDateDetails(focus.value)
      if(clickedDay.value == null) {
        clickedDay.value = today.value
        clickEvent(today.value)
      }
    }

    const getDateDetails = (date) => {
      const details = {}
      details[CALENDAR_STATUSES.new_words] = calendarData.value?.new_words.filter((stat) => stat.created_at === date)
      details[CALENDAR_STATUSES.doing_words] = calendarData.value?.doing_words.filter((stat) => stat.created_at === date)
      details[CALENDAR_STATUSES.complete_words] = calendarData.value?.complete_words.filter((stat) => stat.created_at === date)
      noData.value = !Object.values(details).find((value) => value.length > 0)
      return details
    }
    const clickEvent = (day) => {
      noData.value = true
      clickedDay.value = day.date ? day.date : day
      emit('on-chosenDate', clickedDay.value)
      dateDetails.value = getDateDetails(clickedDay.value)
    }

    const setToday = () => {
      today.value = DateTime.local().toFormat("yyyy-MM-dd")
      focus.value = today.value
      clickedDay.value = today.value
      clickEvent(today.value)
    }

    // const goToDate = (key) => {
    //   let routeData = {
    //     name: urlPath.ORDER.name,
    //     query: {date: clickedDay.value}
    //   }
    //   key = parseInt(key)
    //   if (Object.values(CALENDAR_STATUSES.invoice).includes(key)) {
    //     routeData = {
    //       name: urlPath.INVOICE.name,
    //       query: {auction_date: clickedDay.value}
    //     }
    //   } else if (Object.values(CALENDAR_STATUSES.sale).includes(key)) {
    //     routeData = {
    //       name: urlPath.SALE.name,
    //       query: {auction_date: clickedDay.value, cst_id: dateDetails.value[key][0]['cst']}
    //     }
    //   } else if (Object.values(CALENDAR_STATUSES.billing).includes(key)) {
    //     routeData = {
    //       name: urlPath.BILL.name,
    //       query: {issue_date_from: null, issue_date_to: null,  created_at_from: clickedDay.value,  created_at_to: clickedDay.value}
    //     }
    //   } else if (Object.values(CALENDAR_STATUSES.deposit).includes(key)) {
    //     routeData = {
    //       name: urlPath.PAYMENT.name,
    //       query: {issue_date_from: null, issue_date_to: null, created_at_from: clickedDay.value, created_at_to: clickedDay.value}
    //     }
    //   }
    //   router.push(routeData).catch((err) => {
    //     // Ignore the vuex err regarding navigating to the page they are already on.
    //     if (
    //         err.name !== 'NavigationDuplicated' &&
    //         !err.message.includes('Avoided redundant navigation to current location')
    //     ) {
    //       // But print any other errors to the console
    //       console.log(err)
    //     }
    //   })
    // }
    const getStatusForDay = (date) => {
      const new_words = calendarData.value?.new_words.find((stat) => stat.created_at === date.date)
      const doing_words = calendarData.value?.doing_words.find((stat) => stat.created_at === date.date)
      const complete_words = calendarData.value?.complete_words.find((stat) => stat.created_at === date.date)
      if (new_words)
        return CALENDAR_STATUSES.new_words
      if (doing_words)
        return CALENDAR_STATUSES.doing_words
      if (complete_words)
        return CALENDAR_STATUSES.complete_words
      return null
    }
    onMounted(()=>{
      focus.value = today.value = getToday()
    })


    return {
      weekdays,
      assignmentDates,
      invoiceStatusCount,
      orders,
      today,
      focus,
      start,
      end,
      clickedDay,
      noData,
      moment,
      setToday,
      prev,
      next,
      getToday,
      updateRange,
      getDates,
      clickEvent,
      // goToDate,
      getStatusForDay,
      CALENDAR_STATUSES,
      dateDetails,
      STATUS_ICONS,
    }
  }
};
</script>

<style scoped lang="sass">
@import '~vuetify/src/styles/settings/_variables'
.chart-container
  padding-top: 10px
  padding-left: 10px
  border: 1px solid lightgray
  border-radius: 5px
  background-color: white
  min-height: 450px

.title
  font-size: 20px
  font-weight: bold
.button-calendar
  font-size: 18px
  margin-top: -4px
.date-cell
  min-height: 100%
  min-width: 100%
  padding: 30px 0 0 30px
.status-div
  position: absolute
  height: 30px
  width: 44px
  display: flex
  flex-direction: row
  flex-wrap: wrap
.margin
  margin-top: -18px
::v-deep .v-calendar-weekly__day-label
  margin: 0 !important
::v-deep .v-calendar-weekly__day-label .v-btn
  font-size: 12px !important
::v-deep .v-calendar-weekly__week
  min-height: 20% !important
  border-left: #e0e0e0 1px solid
::v-deep .v-calendar-weekly
    border-left: 0 !important
::v-deep .v-calendar-weekly .v-calendar-weekly__head-weekday.v-outside
    border-left: #e0e0e0 1px solid
.catalog-calendar
  ::v-deep .f-panel__body
    padding: 0

    .catalog-calendar__left
      .day-label-info
        margin-top: 2px
        .day-label
          width: 28px
          height: 28px
          background-color: #0e68af

        .day-label--today
          border: 1px solid #9e9e9e

        .v-calendar-weekly
          border-top: none

      .catalog-calendar__right
        .v-list
          padding: 0
          overflow: hidden auto
          max-height: 326px

          .v-subheader
            padding: 0

            .v-icon
              margin: 0 8px 0 3px
              color: #9e9e9e

            span
              font-size: 14px

          .v-list-item
            .v-list-item__content
              span
                color: #689f38
                font-size: 14px
.dot
  height: 12px
  width: 12px
  border-radius: 50%
  display: inline-block
  transition: opacity ease .1s

.header-text
  text-align: center
  display: inline-flex
  align-items: center

.pointer
  cursor: pointer
</style>

