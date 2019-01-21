"""empty message

Revision ID: c223a894722e
Revises: f8e8da0f724d
Create Date: 2019-01-21 21:38:48.598540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c223a894722e'
down_revision = 'f8e8da0f724d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('game_type', sa.String(length=6), nullable=True))
    op.add_column('game', sa.Column('time_played', sa.Integer(), nullable=True))
    op.add_column('game', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'game', 'user', ['user_id'], ['id'])
    op.drop_column('game', 'gametype')
    op.drop_column('game', 'timeplayed')
    op.drop_column('game', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('uid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('game', sa.Column('timeplayed', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('game', sa.Column('gametype', sa.VARCHAR(length=6), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'game', type_='foreignkey')
    op.drop_column('game', 'user_id')
    op.drop_column('game', 'time_played')
    op.drop_column('game', 'game_type')
    # ### end Alembic commands ###