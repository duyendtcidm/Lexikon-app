<template lang="pug">
  router-link.logo(
    :to='{name: "home.title"}'
  )
    v-row
      //img.py-2.ma-0(v-if="!isIPad" alt='lexikon logo' src='@/assets/hana-logo.png')
      img.py-2.ma-0(width='230px' alt='lexikon logo' src='@/assets/logo-header.png')
      //img(v-else alt='jfga logo' src='@/assets/hana-logo-2.png')
</template>

<script>
import {computed, defineComponent, onMounted, ref} from "vue"

const Logo = defineComponent({
  setup(){

    // check screen is mobile or ipad (not PC)
    // const isIPad = computed(() => {
    //   return (screen.width <= 820 && screen.width >= 600)
    // })

    return {

    }
  }
})
export default Logo

</script>

<style scoped lang="sass">
.logo
  text-decoration: none
  text-align: center
  position: relative
  img
    width: 230px !important
    @media (max-width: 820px)
      width: 96px
    @media (max-width: 600px)
      width: 140px
      margin-top: 5px !important
      padding-bottom: 0 !important

.test-div
  margin-top: 10px
  margin-left: 10px
  height: 30px
  @media (max-width: 820px)
    margin-top: 18px
    margin-left: 20px
  @media (max-width: 600px)
    margin-top: 0
    margin-left: 20px
  .test-text
    letter-spacing: 10px
    padding-top: 3px
    padding-left: 7px
    padding-right: 7px
    font-size: 28px
    font-weight: bold
    color: white
    border-radius: 4px
    @media (max-width: 820px)
      font-size: 18px
      letter-spacing: 4px
      padding-top: 3px
    @media (max-width: 600px)
      font-size: 10px
      padding-top: 3px

</style>