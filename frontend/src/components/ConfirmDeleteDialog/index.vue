<template lang="pug">
  confirm-dialog(
    :showDialog="showDialog"
    :messages="setMessage()"
    :is-delete-master = "isDeleteMaster"
    :cancel-text="$t('common.cancel')"
    :ok-text="okText?okText:$t('common.delete')"
    :color-confirm="'red'"
    @on-cancel="closeDialog('cancel')"
    @on-close="closeDialog('cancel')"
    @on-ok="closeDialog('delete')"
  )
</template>

<script>
import {defineComponent, getCurrentInstance, ref} from 'vue'
import ConfirmDialog from '../ConfirmDialog/index'

const ConfirmDeleteDialog = defineComponent({
  components: {
    ConfirmDialog
  },
  props: {
    showDialog: {
      type: Boolean,
      required: true
    },
    itemLabel: {
      type: String,
      required: false
    },
    messages: {
      type: String,
      required: false
    },
     okText: {
      type: String,
      required: false
    },
    isDeleteMaster: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  setup(props, {emit}) {
    const {$root} = getCurrentInstance().proxy
    const closeDialog = (param) => {
      emit('on-close', param)
    }

    const setMessage = () => {
      if (props.messages)
          return [props.messages]
      else
        return [props.itemLabel ? $root.$t('common.confirm_delete_label', {query: props.itemLabel ?? ''}) : $root.$t('common.confirm_delete')]
    }

    return {
      closeDialog,
      setMessage
    }
  }
})
export default ConfirmDeleteDialog
</script>
