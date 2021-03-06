"""empty message

Revision ID: 672fc4e15fc5
Revises: eafc1b0e40ec
Create Date: 2019-03-09 06:41:05.722187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '672fc4e15fc5'
down_revision = 'eafc1b0e40ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('playlist', sa.String(), nullable=True))
    op.alter_column('game', 'game_type', type_=sa.String(), new_column_name='mode')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('game', 'mode', type_=sa.VARCHAR(length=6), new_column_name='game_type')
    op.drop_column('game', 'playlist')
    # ### end Alembic commands ###
