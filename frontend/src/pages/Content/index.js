// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import { i18n } from '@/plugins'
export const questionContentHeader = [
    {
        text: '',
        align: 'start',
        sortable: false,
        width: 5,
        class: 'primary'
    },
    {
        text: i18n.t('common.code'),
        sortable: false,
        value: 'code',
        width: 80,
        class: 'primary'
    },
    {
        text: i18n.t('content.question.name'),
        sortable: false,
        value: 'name',
        width: 150,
        class: 'primary'
    },
    {
        text: i18n.t('content.question.type'),
        sortable: false,
        value: 'type',
        class: 'primary'
    },
    {
        text: i18n.t('content.question.content'),
        sortable: false,
        value: 'content',
        class: 'primary'
    },
    {
        text: '',
        align: 'right',
        sortable: false,
        value: 'action',
        class: 'primary'
    }
]
