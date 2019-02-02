"""empty message

Revision ID: 19342a5b0b77
Revises: 23b21cdc0dfb
Create Date: 2018-12-31 03:00:14.665831+00:00

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '19342a5b0b77'
down_revision = '23b21cdc0dfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('edit_request_messages', sa.Column('author_id', sa.Integer(), nullable=False))
    op.drop_constraint('edit_request_messages_parent_id_fkey', 'edit_request_messages', type_='foreignkey')
    op.create_foreign_key(None, 'edit_request_messages', 'users', ['author_id'], ['id'])
    op.drop_column('edit_request_messages', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('edit_request_messages', sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'edit_request_messages', type_='foreignkey')
    op.create_foreign_key('edit_request_messages_parent_id_fkey', 'edit_request_messages', 'edit_request_messages', ['parent_id'], ['id'])
    op.drop_column('edit_request_messages', 'author_id')
    # ### end Alembic commands ###
