"""empty message

Revision ID: 3553d253c34b
Revises: 4355a15f5532
Create Date: 2019-01-29 16:30:01.984952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3553d253c34b'
down_revision = '4355a15f5532'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_progression_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('kills_total', sa.Integer(), nullable=True),
    sa.Column('wins_total', sa.Integer(), nullable=True),
    sa.Column('matchesplayed_total', sa.Integer(), nullable=True),
    sa.Column('hoursplayed_total', sa.Integer(), nullable=True),
    sa.Column('lastmodified_total', sa.Integer(), nullable=True),
    sa.Column('kills_solo', sa.Integer(), nullable=True),
    sa.Column('placetop1_solo', sa.Integer(), nullable=True),
    sa.Column('placetop10_solo', sa.Integer(), nullable=True),
    sa.Column('placetop25_solo', sa.Integer(), nullable=True),
    sa.Column('matchesplayed_solo', sa.Integer(), nullable=True),
    sa.Column('minutesplayed_solo', sa.Integer(), nullable=True),
    sa.Column('lastmodified_solo', sa.Integer(), nullable=True),
    sa.Column('kills_duo', sa.Integer(), nullable=True),
    sa.Column('placetop1_duo', sa.Integer(), nullable=True),
    sa.Column('placetop5_duo', sa.Integer(), nullable=True),
    sa.Column('placetop12_duo', sa.Integer(), nullable=True),
    sa.Column('matchesplayed_duo', sa.Integer(), nullable=True),
    sa.Column('minutesplayed_duo', sa.Integer(), nullable=True),
    sa.Column('lastmodified_duo', sa.Integer(), nullable=True),
    sa.Column('kills_squad', sa.Integer(), nullable=True),
    sa.Column('placetop1_squad', sa.Integer(), nullable=True),
    sa.Column('placetop3_squad', sa.Integer(), nullable=True),
    sa.Column('placetop6_squad', sa.Integer(), nullable=True),
    sa.Column('matchesplayed_squad', sa.Integer(), nullable=True),
    sa.Column('minutesplayed_squad', sa.Integer(), nullable=True),
    sa.Column('lastmodified_squad', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_progression_data')
    # ### end Alembic commands ###
