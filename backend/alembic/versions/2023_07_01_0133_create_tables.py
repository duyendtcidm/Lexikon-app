"""create_tables

Revision ID: 1
Revises: 
Create Date: 2023-07-01 01:33:06.269109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
        CREATE TABLE users
        (
            id  BIGSERIAL NOT NULL,
            code BIGINT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT,
            level BIGINT,
            role TEXT,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
            created_by BIGINT,
            modified_at TIMESTAMP WITH TIME ZONE,
            modified_by BIGINT,
            deleted_at TIMESTAMP WITH TIME ZONE,
            deleted_by BIGINT,
            active BOOLEAN DEFAULT TRUE,
            CONSTRAINT pkey_learner PRIMARY KEY (id)
        );''')
    op.execute('''CREATE UNIQUE INDEX IF NOT EXISTS user_unique_code ON users (code) WHERE active IS TRUE;''')
    op.execute('''CREATE UNIQUE INDEX IF NOT EXISTS user_unique_email ON users (email) WHERE active IS TRUE;''')

    op.execute('''CREATE TABLE level
        (
            id  BIGSERIAL NOT NULL,
            code BIGINT,
            name TEXT,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
            created_by BIGINT,
            modified_at TIMESTAMP WITH TIME ZONE,
            modified_by BIGINT,
            deleted_at TIMESTAMP WITH TIME ZONE,
            deleted_by BIGINT,
            active BOOLEAN DEFAULT TRUE,
            CONSTRAINT pkey_level PRIMARY KEY (id)
        );''')
    op.execute('''CREATE UNIQUE INDEX IF NOT EXISTS level_unique_code ON level (code) WHERE active IS TRUE;''')
    op.execute('''CREATE UNIQUE INDEX IF NOT EXISTS level_unique_name ON level (name) WHERE active IS TRUE;''')
    op.execute('''INSERT INTO level(code, name) VALUES (1, 'N1'), (2, 'N2'), (3, 'N3'), (4, 'N4'), (5, 'N5');''')

def downgrade() -> None:
    op.execute('''DROP INDEX IF EXISTS level_unique_name ''')
    op.execute('''DROP INDEX IF EXISTS level_unique_code ''')
    op.execute('''DROP TABLE IF EXISTS level CASCADE ''')
    op.execute('''DROP INDEX IF EXISTS user_unique_code ''')
    op.execute('''DROP INDEX IF EXISTS user_unique_email ''')
    op.execute('''DROP TABLE IF EXISTS users CASCADE''')
