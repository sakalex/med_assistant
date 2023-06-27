"""User add field email

Revision ID: 1c846e801fd5
Revises: 27a8b061aff1
Create Date: 2023-06-25 11:53:39.627702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c846e801fd5'
down_revision = '27a8b061aff1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=256), nullable=False))
    op.drop_column('users', 'login')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('login', sa.VARCHAR(length=256), nullable=False))
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
