"""insert_data_word_table

Revision ID: 3
Revises: 2
Create Date: 2023-07-16 12:29:30.552654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3'
down_revision = '2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
        CREATE TABLE IF NOT EXISTS word_learning  (
            id  BIGSERIAL NOT NULL,
            user_id BIGINT NOT NULL,  
            word_id BIGINT, 
            status BIGINT,
            correct_times BIGINT,
            practice_times BIGINT,
            practice_date DATE,
            note TEXT,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
            created_by BIGINT,
            modified_at TIMESTAMP WITH TIME ZONE,
            modified_by BIGINT,
            deleted_at TIMESTAMP WITH TIME ZONE,
            deleted_by BIGINT,
            active BOOLEAN DEFAULT TRUE,
            CONSTRAINT pkey_word_learning PRIMARY KEY (id)
        );
    ''')


def downgrade() -> None:
    op.execute('''DROP TABLE IF EXISTS word_learning CASCADE ''')
