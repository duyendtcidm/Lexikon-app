<template lang="pug">

</template>

<script>
import { defineComponent, getCurrentInstance, ref } from 'vue'
import {api} from "@/plugins";

export default defineComponent ({
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




    return {
    }
  }
})

</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'

</style>