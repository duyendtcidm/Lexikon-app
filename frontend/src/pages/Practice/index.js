// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import i18n from '../../plugins/i18n'
export const PRACTICE_HEADER = [
    {
        text: '',
        align: 'start',
        width: 5,
        value: 'index',
        class: 'primary',
        isVisible: true
    },
    {
        text: '',
        width: 5,
        value: 'data-table-select',
        class: 'primary',
        isVisible: true
    },
    {
        text: i18n.t('common.code'),
        align: 'center',
        value: 'word_code',
        width: 100,
        class: 'primary',
        isVisible: true
    },
    {
        text: i18n.t('practice.practice_header.word_or_grammar'),
        align: 'left',
        value: 'word_gram_name',
        width: 300,
        class: 'primary',
        isVisible: true
    },
    {
        text: i18n.t('practice.practice_header.level'),
        align: 'left',
        value: 'word_gram_level',
        width: 120,
        class: 'primary',
        isVisible: true
    },
    {
        text: i18n.t('practice.practice_header.status'),
        align: 'right',
        value: 'word_gram_status',
        width: 120,
        class: 'primary',
        isVisible: true
    },
    {
        text: i18n.t('practice.practice_header.score'),
        align: 'right',
        value: 'word_gram_score',
        width: 120,
        class: 'primary',
        isVisible: true
    },
    {
        text: i18n.t('practice.practice_header.remark'),
        align: 'left',
        value: 'word_gram_remark',
        width: 120,
        class: 'primary',
        isVisible: true
    }
]
