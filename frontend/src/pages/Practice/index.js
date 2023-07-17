// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import {i18n} from '@/plugins'
export const PRACTICE_HEADER = [
    {
        text: '',
        align: 'start',
        width: 5,
        value: 'index',
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: '',
        width: 5,
        value: 'data-table-select',
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('common.code'),
        align: 'center',
        value: 'code',
        width: 100,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.word_or_grammar'),
        align: 'left',
        value: 'name',
        width: 200,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.meaning'),
        align: 'left',
        value: 'meaning',
        width: 200,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.level'),
        align: 'center',
        value: 'level',
        width: 120,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.status'),
        align: 'center',
        value: 'status',
        width: 100,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.score'),
        align: 'center',
        value: 'score',
        width: 120,
        class: 'primary',
        isVisible: true,
        sortable : false
    },
    {
        text: i18n.t('practice.practice_header.remark'),
        align: 'left',
        value: 'remark',
        width: 120,
        class: 'primary',
        isVisible: true,
        sortable : false
    }
]
