import { i18n } from '@/plugins'

export const showError = (
    e, toast, defaultMessage = i18n.t('master.msg.get_data_failed')
) => {
  if (e.response?.data?.detail) {
    const { detail } = e.response.data
    if (detail?.msg) toast.error(detail?.msg)
    else if (detail?.error_code) toast.error(i18n.t(`error_code.${detail?.error_code}`))
    else if (detail?.used_in_assignment) toast.error(i18n.t(`used_in_assignment.${detail?.used_in_assignment}`))
    else if (detail?.used_in_ar) toast.error(i18n.t(`used_in_ar.${detail?.used_in_ar}`))
    else if (detail?.used_as_default_vrt) toast.error(i18n.t(`used_as_default_vrt.${detail?.used_as_default_vrt}`))
    else if (detail?.used_as_default_itm) toast.error(i18n.t(`used_as_default_itm.${detail?.used_as_default_itm}`))
    else if (detail?.used_in_master_customer) toast.error(i18n.t(`used_in_master_customer.${detail?.used_in_master_customer}`))
    else if (typeof detail === 'string') toast.error(detail)
    else toast.error(defaultMessage)
  } else {
    toast.error(defaultMessage)
  }
}

export const scrollTop = () => {
  window.scrollTo(0, 0)
}

export const scrollBottom = () => {
  window.setTimeout(() => {
    window.scrollTo(0, document.body.scrollHeight)
  }, 300)
}
