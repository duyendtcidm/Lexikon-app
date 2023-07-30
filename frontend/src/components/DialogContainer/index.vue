<template lang="pug">
  div
    v-dialog(
      persistent
      scrollable
      :content-class="isOnMobile ? 'align-bottom' : ''"
      :value="value"
      :width="width ? width : ''"
      :max-width="width ? '': '500'"
      @input="dialog => $emit('input', dialog)"
      @keydown="onTyping"
      transition="dialog-bottom-transition"
    )
      v-card(:height="isOnMobile ? '500px' : height")
        v-card-title.primary
          v-btn(v-if="isBack" icon dark @click="close()")
            v-icon mdi-keyboard-backspace
          span.white--text {{label}}
          v-spacer
          v-btn(icon dark @click="close()")
            v-icon mdi-close

        v-card-text.relative-card
          div#div_top.invisible
          slot
        slot(name="actions")
          v-card-actions(v-if="showBottom")
            v-row(v-if="isConfirm")
              v-col(cols="6")
                v-btn.relative-btn(
                  :large="!$vuetify.breakpoint.xsOnly"
                  block
                  color="rough_black"
                  :loading="loading"
                  @click="close()"
                )
                  | {{$t('common.cancel')}}
              v-col(cols="6")
                v-btn.relative-btn(
                  :large="!$vuetify.breakpoint.xsOnly"
                  dark
                  block
                  color="red"
                  :loading="loading"
                  @click="deleteItem()"
                )
                  | {{$t('common.delete')}}
            v-row.pa-0.ma-0(v-if="!isConfirm")
              v-col.px-0(:cols="6" v-if="showDeleteBtn && mode === 'edit'" )
                v-btn.relative-btn(
                  ref="delete_btn"
                  :large="!$vuetify.breakpoint.xsOnly"
                  dark
                  block
                  color="red"
                  :loading="loading"
                  @click="showConfirmDelete = true"
                )
                  | {{$t('common.delete')}}
              v-col(:cols="showDeleteBtn && mode === 'edit' ? 6 : 12")
                v-btn.relative-btn(
                  ref="save_btn"
                  v-if="!isConfirm"
                  :large="!$vuetify.breakpoint.xsOnly"
                  dark
                  block
                  color="primary"
                  :loading="loading"
                  @click="mode === 'create' ? create() : update()"
                )
                  | {{saveBtnLabel ? saveBtnLabel : $t('common.save')}}
    confirm-delete-dialog(
      :itemLabel="itemLabel"
      :showDialog="showConfirmDelete"
      @on-close="(param) => confirmDelete(param)"
    )
</template>

<script>
import {defineComponent, ref, watch} from 'vue'
import ConfirmDeleteDialog from '../ConfirmDeleteDialog/index'
export default defineComponent ({
  name: 'DialogContainer',
  props: {
    value: {
      type: Boolean,
      required: true
    },
    mode: {
      type: String,
      default: null
    },
    label: {
      type: String,
      default: ''
    },
    loading: {
      type: Boolean,
      default: false
    },
    isBack: {
      type: Boolean,
      required: false,
      default: false
    },
    showBottom: {
      type: Boolean,
      default: true
    },
    isConfirm: {
      type: Boolean,
      default: false,
      required: false
    },
    height: {
      type: String,
      default: null
    },
    showActionButton: {
      type: Boolean,
      default: false
    },
    showDeleteBtn: {
      type: Boolean,
      default: false
    },
    width: {
      type: Number,
      required: false
    },
    itemLabel: {
      type: String,
      required: false
    },
    saveBtnLabel: {
      type: String,
      required: false
    },
    isOnMobile: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  components: {
    ConfirmDeleteDialog
  },
  setup(props, {emit}) {
    const showConfirmDelete = ref(false)

    const close = () => {
      emit('on-close')
    }

    const create = () => {
      emit('on-create')
    }

    const deleteItem = () => {
      showConfirmDelete.value = true
    }

    const confirmDelete = (param) => {
      if (param === 'delete') {
        emit('on-delete')
      }
      showConfirmDelete.value = false
    }

    const update = () => {
      emit('on-update')
    }

    const onTyping = (event) => {
      if (event.keyCode === 27) {
        // Press ES
        close()
      }
      emit('on-typing', event)
    }

    watch(
      () => props.value,
      () => {
        document.getElementById('div_top')?.scrollIntoView()
      }
    )

    return {
      showConfirmDelete,
      close,
      create,
      deleteItem,
      update,
      confirmDelete,
      onTyping
    }
  }
})

</script>

<style lang="sass" scoped>
@import '@/style/css/common.sass'

.v-dialog > *
  width: auto
  @include relative-fontsize-2

.relative-btn
  @include relative-fontsize-2

.v-card
  ::v-deep .v-card__title
    position: sticky
    top: 0
    z-index: 999

  ::v-deep .v-card__actions
    position: sticky
    background-color: white
    bottom: 0
    z-index: 999

.v-dialog--scrollable > .v-card > .v-card__text
  padding-bottom: 0

  span
    @include relative-fontsize-2
</style>

<style scoped lang="sass">
@import '@/style/css/common.sass'
.relative-card
  input, label, span
    @include relative-fontsize

::v-deep .v-dialog.align-bottom
  position: absolute
  bottom: 0
  bottom: calc((100vh - 150px - 500px) / 2) !important
  width: 350px !important
.invisible
  height: 1px
</style>
