"""Added last_known_data_hash to User

Revision ID: 01e5b95d7cd2
Revises: fc0a25652261
Create Date: 2019-05-04 17:14:13.865750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01e5b95d7cd2'
down_revision = 'fc0a25652261'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('last_known_data_hash', sa.BigInteger(), nullable=True))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('user', 'wins_total')
    op.drop_column('user', 'placetop10_solo')
    op.drop_column('user', 'matchesplayed_duo')
    op.drop_column('user', 'minutesplayed_squad')
    op.drop_column('user', 'hoursplayed_total')
    op.drop_column('user', 'lastmodified_solo')
    op.drop_column('user', 'placetop3_squad')
    op.drop_column('user', 'lastmodified_total')
    op.drop_column('user', 'minutesplayed_duo')
    op.drop_column('user', 'kills_solo')
    op.drop_column('user', 'placetop1_solo')
    op.drop_column('user', 'matchesplayed_total')
    op.drop_column('user', 'matchesplayed_solo')
    op.drop_column('user', 'placetop1_squad')
    op.drop_column('user', 'placetop6_squad')
    op.drop_column('user', 'lastmodified_duo')
    op.drop_column('user', 'kills_squad')
    op.drop_column('user', 'kills_total')
    op.drop_column('user', 'minutesplayed_solo')
    op.drop_column('user', 'placetop12_duo')
    op.drop_column('user', 'placetop5_duo')
    op.drop_column('user', 'matchesplayed_squad')
    op.drop_column('user', 'kills_duo')
    op.drop_column('user', 'placetop1_duo')
    op.drop_column('user', 'placetop25_solo')
    op.drop_column('user', 'lastmodified_squad')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lastmodified_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop25_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop1_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('kills_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('matchesplayed_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop5_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop12_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('minutesplayed_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('kills_total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('kills_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('lastmodified_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop6_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop1_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('matchesplayed_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('matchesplayed_total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop1_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('kills_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('minutesplayed_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('lastmodified_total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop3_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('lastmodified_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('hoursplayed_total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('minutesplayed_squad', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('matchesplayed_duo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('placetop10_solo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('wins_total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'last_known_data_hash')
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###
