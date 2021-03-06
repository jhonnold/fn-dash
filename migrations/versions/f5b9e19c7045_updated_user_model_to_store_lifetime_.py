"""Updated user model to store lifetime stats

Revision ID: f5b9e19c7045
Revises: 1e6a1110cb35
Create Date: 2019-01-14 19:22:40.754997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5b9e19c7045'
down_revision = '1e6a1110cb35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hoursplayed_total', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('kills_duo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('kills_solo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('kills_squad', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('kills_total', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('lastmodified_duo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('lastmodified_solo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('lastmodified_squad', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('lastmodified_total', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('matchesplayed_duo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('matchesplayed_solo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('matchesplayed_squad', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('matchesplayed_total', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop10_duo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop10_solo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop1_duo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop1_solo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop1_squad', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop25_duo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop25_solo', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop3_squad', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('placetop6_squad', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('wins_total', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'wins_total')
    op.drop_column('user', 'placetop6_squad')
    op.drop_column('user', 'placetop3_squad')
    op.drop_column('user', 'placetop25_solo')
    op.drop_column('user', 'placetop25_duo')
    op.drop_column('user', 'placetop1_squad')
    op.drop_column('user', 'placetop1_solo')
    op.drop_column('user', 'placetop1_duo')
    op.drop_column('user', 'placetop10_solo')
    op.drop_column('user', 'placetop10_duo')
    op.drop_column('user', 'matchesplayed_total')
    op.drop_column('user', 'matchesplayed_squad')
    op.drop_column('user', 'matchesplayed_solo')
    op.drop_column('user', 'matchesplayed_duo')
    op.drop_column('user', 'lastmodified_total')
    op.drop_column('user', 'lastmodified_squad')
    op.drop_column('user', 'lastmodified_solo')
    op.drop_column('user', 'lastmodified_duo')
    op.drop_column('user', 'kills_total')
    op.drop_column('user', 'kills_squad')
    op.drop_column('user', 'kills_solo')
    op.drop_column('user', 'kills_duo')
    op.drop_column('user', 'hoursplayed_total')
    # ### end Alembic commands ###
