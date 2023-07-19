// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import {i18n} from '@/plugins'
export const PRACTICE_HEADER = [
    {
        text: '',
        align: 'center',
        width: 10,
        value: 'index',
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.word_or_grammar'),
        align: 'left',
        value: 'name',
        width: 250,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.meaning'),
        align: 'left',
        value: 'meanings',
        width: 300,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.level'),
        align: 'center',
        value: 'level',
        width: 140,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.status'),
        align: 'center',
        value: 'status',
        width: 140,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.score'),
        align: 'center',
        value: 'score',
        width: 140,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.note'),
        align: 'left',
        value: 'note',
        width: 150,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        align: 'end',
        value: 'action',
        class: 'primary',
        isVisible: true,
        sortable : false
    }
]
