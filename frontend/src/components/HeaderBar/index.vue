<template lang="pug">
  v-app-bar(app color="white" dark elevation="1")
    //v-row.ma-0.pa-0(v-if="!isMobile" align="center" justify="space-between")
    v-row.ma-0.pa-0(align="center" justify="space-between")
      v-col.ma-0.pa-0(cols="4")
        logo
      v-col.pa-0.ma-0(cols="4")
        v-row.pa-0(justify="center")
          v-btn(
            rounded
            v-if="back"
            icon
            color="primary"
            @click="goBack"
          )
            v-icon(large) mdi-keyboard-backspace
          v-toolbar-title.header-text.primary--text {{$t($route.name)}}


      v-col.ma-0.pa-0.pr-2(cols="4")
        v-row.ma-0(justify="end")
          h3.black--text profile
          //profile

    //v-row.ma-0.pa-0(v-else align="center" justify="space-between")
    //  portal-target(name="header-action")
    //  v-row.ma-0.pa-0(v-if="$route.path === '/'" align="center")
    //    v-col.ma-0.pa-0(cols="4")
    //      logo
    //    v-col.pl-0
    //      v-toolbar-title.header-mobile-text.primary--text(style="text-align: center") {{$t($route.query.gr_name) ? $t($route.query.gr_name) + $t('common.no_ja') + $t($route.name) : $t($route.name) }}
    //  v-btn(
    //    rounded
    //    v-if="back"
    //    icon
    //    color="primary"
    //    @click="goBack"
    //  )
    //    v-icon(large) mdi-keyboard-backspace
    //  v-row.ma-0.pa-0(justify="center" )
    //    v-col.ma-0.pa-0(align="center" )
    //      .header-mobile-text.primary--text
    //        portal-target(name="header-title")
    //      .sub-header-mobile-text.primary--text
    //        portal-target(name="header-sub-title")
      //

</template>

<script>
import {defineComponent} from 'vue'
import Logo from './logo.vue'
// import Profile from './profile.vue'
// import JNotifications from '../JNotifications/index.vue'
import { backPage } from '../../utils/common/index'

const HeaderBar = defineComponent({
  components: {
    Logo,
    // Profile
  },
  props: {
    back: {
      type: Boolean,
      required: false,
      default: false
    },
  //   isMobile: {
  //     type: Boolean,
  //     required: false,
  //     default: false
  //   }
  },
  setup(props) {
    const goBack = () => {
      backPage()
    }

    return {
      goBack
    }
  }
})
export default HeaderBar
</script>

<style lang="sass" scoped>
@import '@/style/css/common.sass'
.header-text
  font-size: 30px
  font-weight: bold
.header-mobile-text
  font-size: 20px
  font-weight: bold
.sub-header-mobile-text
  font-size: 16px
  font-weight: bold
::v-deep .v-toolbar__content
    padding-right: 0 !important
</style>