<template lang="pug">
  div.register-page
    v-img.logo(
      :src="require('../../assets/logo-header.png')"
      width="18%"
    )
    h1.text-center.register-title {{$t('forgot_password.title')}}
    div.register-form
      validation-provider(rules="required|email" v-slot="{ errors }" :name="$t('common.email')")
        v-text-field(
          outlined
          dense
          ref="email"
          :error-messages="errors"
          v-model="accountData.email"
          color="primary"
        )
          template(v-slot:label)
            span {{$t('common.email')}}
            span.red--text *
      validation-provider(rules="required" v-slot="{ errors }" :name="$t('common.new_password')")
        v-text-field(
          type="password"
          outlined
          dense
          :error-messages="errors"
          v-model="accountData.password"
          color="primary"
        )
          template(v-slot:label)
            span {{$t('common.new_password')}}
            span.red--text *
      v-btn.hidden-sm-and-up.green-bg-btn.button(width="150px" dark icon @click="registerAccount()")
      v-btn.hidden-xs-only.button(width="150px" color="primary" dark @click="registerAccount()")
        span {{ $t('forgot_password.update') }}
      p.mt-6
        router-link.link(
          :to="{ path: `/log_in` }"
        )
          span.text-decoration-underline.ml-1 {{$t('log_in.title')}}
</template>

<script>
import {defineComponent, ref, getCurrentInstance} from 'vue'
import {api, i18n} from '@/plugins'
import { urlPath} from "@/utils" //endpoints
import router from "@/router";

export default defineComponent({
  setup() {
    const { $toast, $root } = getCurrentInstance().proxy
    const accountData = ref({})

    const registerAccount = async () => {
      if (accountData.value?.email) {
        const emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        if(!emailRegex.test(accountData.value?.email))
          return $toast.error($root.$t('master.msg.check_type_email'))
      }
      try {
        const { data } = await api.post(`auth/forgot-password/`, accountData.value)
        router.push({name: urlPath.LOG_IN.name})
        $toast.success(data.detail)
        setTimeout(() => {
            window.location.reload()
          }, 1000)
      } catch (e) {
        console.log('hihi', e)
      }
    }

    return {
      accountData,
      registerAccount
    }
  }
})
</script>

<style lang="sass" scoped>
@import '@/style/css/common.sass'
.register-page
  padding-top: 150px
.register-title
  margin-top: 50px
  margin-bottom: 70px
.logo
  margin: auto
::v-deep .theme--light.v-input
  width: 100%
.register-form
  margin: auto
  width: 25%
  display: flex
  height: 200px
  flex-direction: column
  justify-content: center
  align-items: center
.register-form span
  width: 100%
</style>