"""Clean up

Revision ID: 608b94210d78
Revises: 01e5b95d7cd2
Create Date: 2019-05-04 18:22:46.339673

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '608b94210d78'
down_revision = '01e5b95d7cd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_progression_data')
    op.drop_constraint('game_user_id_fkey', 'game', type_='foreignkey')
    op.drop_column('game', 'playlist')
    op.drop_column('game', 'user_id')
    op.drop_column('game', 'mode')
    op.add_column('stat', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('stat', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_constraint('_name_mode_uc', 'stat', type_='unique')
    op.drop_constraint('stat_user_id_fkey', 'stat', type_='foreignkey')
    op.drop_column('stat', 'updated')
    op.drop_column('stat', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stat', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('stat', sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_foreign_key('stat_user_id_fkey', 'stat', 'user', ['user_id'], ['id'])
    op.create_unique_constraint('_name_mode_uc', 'stat', ['user_id', 'name', 'mode'])
    op.drop_column('stat', 'updated_at')
    op.drop_column('stat', 'created_at')
    op.add_column('game', sa.Column('mode', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('game', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('game', sa.Column('playlist', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('game_user_id_fkey', 'game', 'user', ['user_id'], ['id'])
    op.create_table('user_progression_data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('kills_total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('wins_total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('matchesplayed_total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hoursplayed_total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastmodified_total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('kills_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop1_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop10_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop25_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('matchesplayed_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('minutesplayed_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastmodified_solo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('kills_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop1_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop5_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop12_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('matchesplayed_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('minutesplayed_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastmodified_duo', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('kills_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop1_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop3_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('placetop6_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('matchesplayed_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('minutesplayed_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastmodified_squad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_progression_data_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_progression_data_pkey')
    )
    # ### end Alembic commands ###
