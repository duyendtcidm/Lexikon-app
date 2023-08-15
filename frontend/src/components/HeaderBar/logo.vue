<template lang="pug">
  router-link.logo(
    v-if="currentMember.role !== 'admin'"
    :to='{name: "home.title"}'
  )
    v-row
      img.py-2.ma-0(width='230px' alt='lexikon logo' src='@/assets/logo-header.png')
  router-link.logo(
    v-else
    :to='{name: "content.question.title"}'
  )
    v-row
      img.py-2.ma-0(width='230px' alt='lexikon logo' src='@/assets/logo-header.png')
</template>

<script>
import {computed, defineComponent, onMounted, ref} from "vue"

const Logo = defineComponent({
  setup() {
    const currentMember = ref({})
    currentMember.value = JSON.parse(localStorage.getItem("current_user"))
    return {
      currentMember
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