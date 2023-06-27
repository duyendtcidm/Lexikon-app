<!--<template lang="pug">-->
<!--  div-->
<!--    v-menu.black&#45;&#45;text(ref='profileVMenu' v-model='isOpened' left offset-y)-->
<!--      template(v-slot:activator='{on}')-->
<!--        v-toolbar-items-->
<!--          v-btn.profile-btn(v-on='on' text)-->
<!--            v-list-item-->
<!--              v-list-item-avatar-->
<!--                img.icon(src="@/assets/farmer_2.png")-->
<!--              v-list-item-content.d-none.d-lg-flex.text-left-->
<!--                v-list-item-title.title-text-->
<!--                  | {{ currentMember.name_short }}-->
<!--                v-list-item-subtitle.grey&#45;&#45;text-->
<!--                  | {{ currentMember.dept }}-->
<!--      template-->
<!--        v-list(dense nav)-->
<!--          v-list-item-->
<!--            v-list-item-content.text-center-->
<!--              h3 {{ currentMember.name }}-->
<!--              v-list-item-subtitle.text&#45;&#45;disabled-->
<!--                | ID: {{ currentMember.id }}-->
<!--          v-list-item(:to='{name: "Logout"}' @click="logout")-->
<!--            v-list-item-icon-->
<!--              v-icon.primary&#45;&#45;text mdi-logout-variant-->
<!--            v-list-item-content-->
<!--              v-list-item-title.rough-black Log out-->
<!--</template>-->
<!--<script>-->
<!--import { defineComponent, getCurrentInstance, ref, onMounted } from 'vue'-->
<!--import { Auth } from 'aws-amplify'-->
<!--import { api } from "@/plugins/index.ts";-->
<!--import { endpoints, showError } from "@/utils";-->

<!--const Profile = defineComponent({-->
<!--  setup() {-->
<!--    const isOpened = ref(false)-->
<!--    const instance = getCurrentInstance()-->
<!--    const { $toast, $root } = instance.proxy-->
<!--    const currentMember = ref({})-->

<!--    const logout = () => {-->
<!--      Auth.signOut()-->
<!--    }-->

<!--    // create new-->
<!--    const getCurrentMember = async () => {-->
<!--      try {-->
<!--        const isAuthenticated = await Auth.currentAuthenticatedUser()-->
<!--        .then(() => {-->
<!--          return true-->
<!--        })-->
<!--        .catch(() => {-->
<!--          return false-->
<!--        })-->

<!--        if (isAuthenticated) {-->
<!--          const { data } = await api.get(`${endpoints.MASTER_MEMBER}current`)-->
<!--          currentMember.value = data-->
<!--        }-->
<!--      } catch (e) {-->
<!--        showError(e, $toast, $root.$t('error_code.failed_to_load_current_member'))-->
<!--      }-->
<!--    }-->

<!--    onMounted(() => {-->
<!--      getCurrentMember()-->
<!--    })-->

<!--    return {-->
<!--      logout,-->
<!--      currentMember,-->
<!--      isOpened-->
<!--    }-->
<!--  }-->
<!--})-->
<!--export default Profile-->
<!--</script>-->

<!--<style scoped lang="sass">-->
<!--@import '@/style/css/common.sass'-->
<!--.content-->
<!--  max-width: 500px-->
<!--// Adjust padding to make it look balanced-->
<!--.v-btn.profile-btn-->
<!--  margin-left: 8px-->

<!--  .v-list-item-->
<!--    max-width: 196px-->
<!--    padding: 0-->

<!--    .v-list-item__avatar-->
<!--      margin-right: 5px-->

<!--.title-text-->
<!--  color: $rough-black-->
<!--</style>-->