<template lang="pug">
  div.home-page
    div(style="max-width: 1380px; margin: auto;").mt-8
      v-row.ml-2.justify-center.content
        dash-board(:date="chosenDate")
        v-col(cols="7").pl-15.mt-2
          calendar.mb-4(
            :loading="loading"
            @on-chosenDate="updateChosenDate"
          )
        v-col.mt-2.pl-10.pr-10
          div(v-for="menu in menus" :key="menu.title")
            v-row
              v-icon(size="60px") {{ menu.icon }}
              span.title {{ menu.title }}
            v-row.line.ml-3.pl-4.mb-3
              v-col.mt-0.mb-0.ml-0.row(v-for="child in menu.children" :key="child.title")
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
    const instance = getCurrentInstance()
    const { $root } = instance.proxy
    const chosenDate = ref('')
    const menus = [
      {
        title: $root.$t('menu.look_up_and_practice.title'),
        icon: 'mdi-account-school-outline',
        children: [
          {
            title: $root.$t('menu.look_up_and_practice.look_up'),
            icon: 'mdi-text-box-search-outline',
            color: 'grey',
            path: `/look_up`
          },
          {
            title: $root.$t('menu.look_up_and_practice.practice'),
            icon: 'mdi-note-edit-outline',
            color: 'orange',
            path: `/practice`
          },
            {
            title: $root.$t('menu.look_up_and_practice.exam'),
            icon: 'mdi-alpha-j-box-outline',
            color: 'rgb(184 54 49)',
            path: `/test`
          }
        ]
      }
      //   {
      //   title: $root.$t('menu.rank.ranking'),
      //   icon: 'mdi-cannabis',
      //   children: [
      //     {
      //       title: $root.$t('ranking.title'),
      //       icon: 'mdi-podium',
      //       color: 'rgb(30 82 146)',
      //       path: `/ranking`
      //     }
      //   ]
      // }
    ]
    const loading = ref(true)

    const updateChosenDate = (date) => {
      chosenDate.value = date
    }

    return {
      menus,
      loading,
      chosenDate,
      updateChosenDate
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'
//@media (max-width: 1200px)
//  .welcome
//    width: 0
//    display: none
//@media (max-width: 1920px)
//  .welcome
//    width: 500px
//    position: absolute
//    margin-left: 10%
  //.content
  //  margin-top: 98px
.home-page
  padding: 0 80px 0 80px
.title
  font-size: 20px !important
  font-weight: bold
  color: $rough-black
  margin-top: 15px
  margin-left: 10px
.line
  border-width: 0 0 0 4px
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
  width: 8vw
  min-width: 150px !important
  border-radius: 10px
  padding: 30px
  transition: all 0.5s
  cursor: pointer
  margin: 10px

.button div
  cursor: pointer
  //display: inline-block
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