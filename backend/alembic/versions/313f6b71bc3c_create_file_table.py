"""Create file table

Revision ID: 313f6b71bc3c
Revises: 
Create Date: 2023-06-23 15:24:22.727576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313f6b71bc3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_filename', sa.String(), nullable=True),
    sa.Column('storage_filename', sa.String(), nullable=True),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('content_type', sa.String(), nullable=True),
    sa.Column('size', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###