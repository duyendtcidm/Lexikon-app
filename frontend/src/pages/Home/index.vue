<template lang="pug">
  div
    //img.welcome(v-if="" src='@/assets/welcom.png')
    div(style="max-width: 1380px; margin: auto;").mt-8
      v-row.ml-2.justify-center.content
        dash-board(
          :remainDates="remainDates"
          :remainDatesCount="remainDatesCount"
          :unconfirmSaleResultDatesCount="unconfirmSaleResultDatesCount"
          :unconfirmSaleResultDates="unconfirmSaleResultDates"
        )
        v-col(cols="7").pl-0.mt-2
          calendar.mb-4(
            :loading="loading"
            :remainDates="remainDates"
            :unconfirmSaleResultDates="unconfirmSaleResultDates"
          )
          // @on-chosenDate="updateChosenDate"
          //j-dashboard
        v-col.mt-2
          div(v-for="menu in menus" :key="menu.title")
            v-row
              v-icon(size="50px") {{ menu.icon }}
              //span.title {{ menu.title }}
            v-row.line.ml-3.pl-4.mb-3
              v-col.mt-0.mb-0.ml-0.justify-right.row(v-for="child in menu.children" :key="child.title")
                v-btn.button(:style="'background-color:' + child.color")
                  router-link.link(
                    style="text-decoration: none; color: inherit;"
                    :to="{ path: `${child.path}` }"
                  )
                    .d-flex.justify-center.mb-1
                      v-icon(color="white").icon-child {{child.icon}}
                    span.d-flex.justify-center.title-child
                      | {{(child.title)}}
</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import DashBoard from './DashBoard'
import Calendar from './Calendar'
import {api} from "@/plugins";

export default defineComponent ({
  components: {
    DashBoard,
    Calendar
  },
  setup() {
    const auth_token = localStorage.getItem("auth_token")
    const auth_token_type = localStorage.getItem("auth_token_type")
    const token = auth_token_type + " " + auth_token
    //  fetch data from get user api
    api
      .get(`/users`, {
        headers: { Authorization: token },
      })
      .then((response) => {
        console.log('response', response);
      })
      .catch((error) => {
        console.log(error);
      })
     const instance = getCurrentInstance()
    const { $root } = instance.proxy
    const chosenDate = ref('')
    const menus = [
      {
        title: $root.$t('menu.look_up_and_practice.title'),
        icon: 'mdi-flower-pollen',
        children: [
          {
            title: $root.$t('menu.look_up_and_practice.look_up'),
            icon: 'mdi-text-box-search-outline',
            color: 'grey',
            path: `/look_up/`
          },
          {
            title: $root.$t('menu.look_up_and_practice.practice'),
            icon: 'mdi-note-edit-outline',
            color: 'orange',
            path: `/practice/`
          }
        ]
      }
    ]
    const loading = ref(true)
    const remainDates = ref([])
    const remainDatesCount = ref()
    const unconfirmSaleResultDates = ref([])
    const unconfirmSaleResultDatesCount = ref()

    const updateChosenDate = (date) => {
        chosenDate.value = date
    }

    return {
      menus,
      loading,
      remainDates,
      remainDatesCount,
      unconfirmSaleResultDates,
      unconfirmSaleResultDatesCount,
      // getRemaining,
      // getUnconfirmed,
      chosenDate,
      updateChosenDate
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'
@media (max-width: 1200px)
  .welcome
    width: 0
    display: none
@media (max-width: 1920px)
  .welcome
    width: 500px
    position: absolute
    margin-left: 10%
  //.content
  //  margin-top: 98px
.title
  font-size: 20px !important
  font-weight: bold
  color: $rough-black
  margin-top: 15px
  margin-left: 10px
.line
  border-width: 0 0 0 3px
  border-style: solid
  border-color: rgba(111, 152, 111, 0.3)
.icon-child
  font-size: 45px
  margin-top: 5px
.title-child
  font-size: 1vmax
  font-weight: bold
.button
  box-shadow: rgba(0, 0, 0, 0.37) 1px 2px 4px
  color: white
  height: 100px !important
  width: 7vw
  min-width: 100px !important
  border-radius: 10px
  padding: 20px
  transition: all 0.5s
  cursor: pointer
  margin: 5px

.button div
  cursor: pointer
  display: inline-block
  position: relative
  transition: 0.5s

.button div:after
  content: '\00bb'
  position: absolute
  opacity: 0
  top: 0
  right: -20px
  transition: 0.5s
  font-size: 34px

.button:hover div
  padding-right: 25px

.button:hover div:after
  opacity: 1
  right: 0

</style>