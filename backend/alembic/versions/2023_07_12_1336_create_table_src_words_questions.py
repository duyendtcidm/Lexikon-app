"""create_table_src_words_questions

Revision ID: 6d9f7cf32fa8
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
    op.execute('''CREATE TABLE word
                (
                    id  BIGSERIAL NOT NULL,
                    code BIGINT,
                    name TEXT,
                    meaning JSON[],
                    pronunciation TEXT,
                    kanji TEXT,
                    level BIGINT,
                    synonym JSON[],
                    antonym JSON[],
                    kanren JSON[],
                    antonym JSON[],
                    antonym JSON[],
                    antonym JSON[],
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

    op.execute('''CREATE TABLE grammar
                (
                    id  BIGSERIAL NOT NULL,
                    code BIGINT,
                    name TEXT,
                    structure TEXT,
                    usage JSON[],
                    kanji TEXT,
                    level BIGINT,
                    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
                    created_by BIGINT,
                    modified_at TIMESTAMP WITH TIME ZONE,
                    modified_by BIGINT,
                    deleted_at TIMESTAMP WITH TIME ZONE,
                    deleted_by BIGINT,
                    active BOOLEAN DEFAULT TRUE,
                    CONSTRAINT pkey_grammar PRIMARY KEY (id)
                );''')
    op.execute('''CREATE UNIQUE INDEX IF NOT EXISTS grammar_unique_code ON level (code) WHERE active IS TRUE;''')



def downgrade() -> None:
    op.execute('''DROP INDEX IF EXISTS grammar_unique_code ''')
    op.execute('''DROP TABLE IF EXISTS word CASCADE ''')
    op.execute('''DROP INDEX IF EXISTS grammar_unique_code ''')
    op.execute('''DROP TABLE IF EXISTS grammar CASCADE''')
