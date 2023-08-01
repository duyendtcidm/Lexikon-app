<template lang="pug">
  .home
    search-component(
      :search-info="searchInfo"
      :search-text="$t('content.question.search')"
      @inputting="handleSearchInput"
      @open-add-dialog="onClickOpenAddDialog"
    )
    item-list(
      :headers="questionContentHeaders"
      :items="questions"
      :actions="actions"
      @on-delete="openConfirmDelete"
      @on-update="onClickOpenUpdateDialog"
    )

    question-content-dialog(
      :show="isShowQuestionContentDialog"
      :question="curQuestion"
      :is-add="isAdd"
      @on-close="isShowQuestionContentDialog =false"
      @on-reload="reload"
    )
    confirm-delete-dialog(
      :show-dialog="isShowConfirmDelete"
      @on-close="onDelete"
    )

</template>

<script>
import {defineComponent, getCurrentInstance, onMounted, ref} from "vue"
import { SearchComponent, ItemList, QuestionContentDialog, ConfirmDeleteDialog } from "@/components"
import { questionContentHeader } from './index'
import router from "@/router"
import { api } from '@/plugins'
import { showError } from '@/utils'
import { debounce } from 'lodash'
export default defineComponent({
  components:{
    SearchComponent,
    ItemList,
    QuestionContentDialog,
    ConfirmDeleteDialog
  },
  setup() {
    const instance = getCurrentInstance()
    const { $toast, $root } = instance.proxy
    const questionContentHeaders = ref(questionContentHeader)
    const { search: searchInfoValue, untg: untgId } = router.currentRoute.query
    const searchInfo = ref(searchInfoValue || '')
    const isShowConfirmDelete = ref(false)
    const curQuestion = ref({})
    const isShowQuestionContentDialog = ref(false)
    const isAdd = ref(false) // add or edit
    const questions = ref([])

    const actions = ref([
      {
        id: 1,
        text: 'common.edit',
        icon: 'mdi-pencil',
        action: 'on-update',
        disabled: false,
        color: 'gray'
      },
      {
        id: 2,
        text: 'common.delete',
        icon: 'mdi-delete-empty',
        action: 'on-delete',
        disabled: false,
        color: 'red'
      }
    ])
    
    const onClickOpenUpdateDialog = (question) => {
      isAdd.value = false
      curQuestion.value = question
      isShowQuestionContentDialog.value = true
    }

    const openConfirmDelete = (question) => {
      isShowConfirmDelete.value = true
      curQuestion.value = question
    }

    const onClickOpenAddDialog = () => {
      isAdd.value = true
      isShowQuestionContentDialog.value = true
    }
   
    const deleteAPI = async () => {
      try {
        await api.delete(`/content/question/${curQuestion.value.id}`)
        await getQuestion()
        $toast.success($root.$t('common.msg.delete_successful'))
      } catch (e) {
        showError(e, $toast, $root.$t('common.msg.delete_failed'))
      }
    }

    const onDelete = (mode) => {
      isShowConfirmDelete.value = false
      if (mode === 'delete') {
        deleteAPI()
      }
    }

    const reload = () => {
      getQuestion()
    }

    const getQuestion = async () => {
      try {
        const { data } = await api.get(`/content/question/?search_input=${searchInfo.value}`)
        questions.value = data
      } catch (e) {
        showError(e, $toast, $root.$t('common.msg.get_data_failed'))
      }
    }

    const handleSearchInput = debounce((value) => {
      searchInfo.value = value
      getQuestion()
    }, 500)

    onMounted(() => {
      getQuestion()
    })


    return {
      questions,
      questionContentHeaders,
      actions,
      searchInfo,
      handleSearchInput,
      openConfirmDelete,
      onClickOpenUpdateDialog,
      onClickOpenAddDialog,
      isShowQuestionContentDialog,
      isAdd,
      curQuestion,
      reload,
      isShowConfirmDelete,
      onDelete
    }
  }
})

</script>

<style lang="sass" scoped>
@import '@/style/css/common.sass'
.home
  width: 100%
</style>