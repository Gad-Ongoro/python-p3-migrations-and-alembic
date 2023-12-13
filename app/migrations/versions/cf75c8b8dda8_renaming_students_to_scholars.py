"""Renaming students to scholars

Revision ID: cf75c8b8dda8
Revises: 7d9e3f0badaa
Create Date: 2023-12-13 02:37:12.032992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf75c8b8dda8'
down_revision = '7d9e3f0badaa'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('students', 'scholars')


def downgrade():
    op.rename_table('scholars', 'students')
