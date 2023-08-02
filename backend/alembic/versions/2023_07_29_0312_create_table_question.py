"""create_table_question

Revision ID: 4
Revises: 3
Create Date: 2023-07-29 03:12:40.785848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4'
down_revision = '3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
        CREATE TABLE IF NOT EXISTS question  (
            id BIGSERIAL NOT NULL,
            code BIGINT,
            name TEXT, 
            type TEXT,
            search_str TEXT,
            content TEXT,
            choices JSON DEFAULT '{}',
            answer BIGINT,
            explanation JSON DEFAULT '{}',
            level_id BIGSERIAL,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
            created_by BIGINT,
            modified_at TIMESTAMP WITH TIME ZONE,
            modified_by BIGINT,
            deleted_at TIMESTAMP WITH TIME ZONE,
            deleted_by BIGINT,
            active BOOLEAN DEFAULT TRUE,
            CONSTRAINT pkey_question PRIMARY KEY (id)
        )    
    ''')

    op.execute('''
            CREATE TABLE IF NOT EXISTS answered_question  (
                id  BIGSERIAL NOT NULL,
                user_id BIGINT NOT NULL,  
                question_id BIGINT, 
                status BIGINT,
                created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
                created_by BIGINT,
                modified_at TIMESTAMP WITH TIME ZONE,
                modified_by BIGINT,
                deleted_at TIMESTAMP WITH TIME ZONE,
                deleted_by BIGINT,
                active BOOLEAN DEFAULT TRUE,
                CONSTRAINT pkey_answered_question PRIMARY KEY (id)
            )
        ''')


def downgrade() -> None:
    op.execute('''DROP TABLE IF EXISTS question CASCADE ''')
    op.execute('''DROP TABLE IF EXISTS answered_question CASCADE ''')
