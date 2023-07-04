<template lang="pug">
  div.register-page
    v-img.logo(
      :src="require('../../assets/logo-header.png')"
      width="18%"
    )
    h1.text-center.register-title {{$t('register.title')}}
    div.register-form
      validation-provider(rules="required" v-slot="{ errors }" :name="$t('common.user_name')")
        v-text-field(
          outlined
          dense
          :error-messages="errors"
          v-model="accountData.userName"
          color="primary"
        )
          template(v-slot:label)
            span {{$t('common.user_name')}}
            span.red--text *
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
      validation-provider(rules="required" v-slot="{ errors }" :name="$t('common.password')")
        v-text-field(
          outlined
          dense
          :error-messages="errors"
          v-model="accountData.password"
          color="primary"
        )
          template(v-slot:label)
            span {{$t('common.password')}}
            span.red--text *
      v-btn.hidden-sm-and-up.green-bg-btn.button(width="150px" dark icon @click="registerAccount()")
        v-icon mdi-plus
      v-btn.hidden-xs-only.button(width="150px" color="primary" dark @click="registerAccount()")
        v-icon mdi-plus
        span {{ $t('register.title') }}
</template>

<script>
import {defineComponent, ref, getCurrentInstance} from 'vue'
import {ValidationProvider, ValidationObserver} from 'vee-validate'

export default defineComponent({
  components: {
    ValidationProvider,
    ValidationObserver
  },
  setup() {
    const { $toast, $root } = getCurrentInstance().proxy
    const accountData = ref({
      userName: '',
      email: '',
      password: ''
    })

    const registerAccount = () => {
      if (accountData.value?.email) {
        const emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        if(!emailRegex.test(accountData.value?.email))
          return $toast.error($root.$t('master.msg.check_type_email'))
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
  margin-bottom: 30px
.logo
  margin: auto
::v-deep .theme--light.v-input
  width: 100%
.register-form
  margin: auto
  width: 20%
  display: flex
  height: 200px
  flex-direction: column
  justify-content: center
  align-items: center
.register-form span
  width: 100%
</style>