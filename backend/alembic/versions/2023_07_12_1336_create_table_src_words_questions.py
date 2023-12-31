"""create_table_src_words_questions

Revision ID: 2
Revises: 1
Create Date: 2023-07-12 13:36:09.217612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2'
down_revision = '1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    #  Create table word, grammar
    op.execute('''CREATE TABLE IF NOT EXISTS word
                (
                    id  BIGSERIAL NOT NULL,
                    code BIGINT,
                    name TEXT,
                    meanings JSON,
                    yomi TEXT,
                    kanji TEXT,
                    search_str TEXT,
                    level_id BIGINT,
                    synonym JSON DEFAULT '{}',
                    antonym JSON DEFAULT '{}',
                    kanren JSON DEFAULT '{}',
                    usage_pattern JSON DEFAULT '{}',
                    compound_word JSON DEFAULT '{}',
                    common_word JSON DEFAULT '{}',
                    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
                    created_by BIGINT,
                    modified_at TIMESTAMP WITH TIME ZONE,
                    modified_by BIGINT,
                    deleted_at TIMESTAMP WITH TIME ZONE,
                    deleted_by BIGINT,
                    active BOOLEAN DEFAULT TRUE,
                    CONSTRAINT pkey_word PRIMARY KEY (id)
                );''')
    op.execute('''CREATE UNIQUE INDEX IF NOT EXISTS word_unique_code ON level (code) WHERE active IS TRUE;''')
    op.execute('''
        UPDATE word
        SET search_str = concat(code, '|', lower(name), CASE
        WHEN yomi IS NOT NULL AND LENGTH(yomi) > 0 AND (yomi = ANY (array [name])) IS NOT TRUE
        THEN concat('|', yomi) END )
        WHERE TRUE;
    ''')



def downgrade() -> None:
    op.execute('''DROP INDEX IF EXISTS word_unique_code ''')
    op.execute('''DROP TABLE IF EXISTS word CASCADE ''')