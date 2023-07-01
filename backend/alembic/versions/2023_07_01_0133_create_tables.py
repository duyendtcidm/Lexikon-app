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
        
    ''')


def downgrade() -> None:
    pass
