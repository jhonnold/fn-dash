"""empty message

Revision ID: fc0a25652261
Revises: dba68d37092b
Create Date: 2019-05-04 14:02:21.602644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc0a25652261'
down_revision = 'dba68d37092b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('stat_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'game', 'stat', ['stat_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'game', type_='foreignkey')
    op.drop_column('game', 'stat_id')
    # ### end Alembic commands ###
