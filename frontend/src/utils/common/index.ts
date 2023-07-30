// import router from '../../router'
// import Store from '../../store'
// import { api, i18n } from '@/plugins'
// import Vue, { getCurrentInstance } from "vue";
// import { endpoints, showError, query, convertToWidthCharacter } from '@/utils'
// import { TaxType } from '@/utils/constants'
// import moment from 'moment'
// import _ from 'lodash'

export const backPage = () => {
    history.back()
}

export const moveCursor = (event: any, $refs: any, list_states: any, focusInput: any) => {
    /*
    * event: keydown event
    * list_states: array reference name exp ['code', 'untg', 'name', 'yomi', 'name_short', 'name_eng']
    * focusInput: reference name is focusing exp name
    * */
    let index = list_states.findIndex((state: any) => state === focusInput)
    if ((event.keyCode === 13 || event.keyCode === 9) && index !== list_states.length - 1) {
        event.preventDefault()
        focusInput = list_states[index + 1]
    }

    if ($refs[focusInput]) {
        if (Object.keys($refs[focusInput]).includes('focus')) $refs[focusInput].focus()
        if (Object.keys($refs[focusInput]).includes('activateMenu')) $refs[focusInput].activateMenu()
    }
    else if ($refs?.master_dialog.$refs[focusInput]) {
        $refs?.master_dialog.$refs[focusInput]?.focus()
    }
    return focusInput
}