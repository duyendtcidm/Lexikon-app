<template lang="pug">
  div
    v-menu.black--text(ref='profileVMenu' v-model='isOpened' left offset-y)
      template(v-slot:activator='{on}')
        v-toolbar-items
          v-btn.profile-btn(v-on='on' text)
            v-list-item
              v-list-item-avatar
                img.icon(src="@/assets/student.png")
              v-list-item-content.d-none.d-lg-flex.text-left
                v-list-item-title.title-text
                  | {{ currentMember.name }}
      template
        v-list(dense nav)
          v-list-item
            v-list-item-content.text-center
              h3 {{ currentMember.name }}
          v-list-item(:to='{name: "Logout"}' @click="logout")
            v-list-item-icon
              v-icon.primary--text mdi-logout-variant
            v-list-item-content
              v-list-item-title.rough-black {{$t('common.logout')}}
</template>
<script>
import { defineComponent, getCurrentInstance, ref, onMounted } from 'vue'
import { api } from "@/plugins/index.ts";
import * as urlPath from "@/utils/urlPath";

const Profile = defineComponent({
  setup() {
    const isOpened = ref(false)
    const instance = getCurrentInstance()
    const { $toast, $root } = instance.proxy
    const currentMember = ref({})

    const logout = () => {
      // remove token form local storage
      localStorage.removeItem("auth_token");
      localStorage.removeItem("auth_token_type");
      $root.$router.replace({name: urlPath.LOG_IN.name})
    }
    // create new
    const getCurrentMember = async () => {
      // try {
        const { data } = await api.get(`/users/`)
        currentMember.value = data[0]
      // } catch (e) {
      //   $toast.error($root.$t('error_code.failed_to_load_current_member'))
      // }
    }

    onMounted(() => {
      getCurrentMember()
    })

    return {
      logout,
      currentMember,
      isOpened
    }
  }
})
export default Profile
</script>

<style scoped lang="sass">
@import '@/style/css/common.sass'
.content
  max-width: 500px
// Adjust padding to make it look balanced
.v-btn.profile-btn
  margin-left: 8px

  .v-list-item
    max-width: 196px
    padding: 0

    .v-list-item__avatar
      margin-right: 5px

.title-text
  color: $rough-black
</style>