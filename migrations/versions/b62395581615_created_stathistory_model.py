"""Created StatHistory model

Revision ID: b62395581615
Revises: 672fc4e15fc5
Create Date: 2019-03-14 22:37:57.524571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b62395581615'
down_revision = '672fc4e15fc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stat_id', sa.Integer(), nullable=True),
    sa.Column('placements', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('kills', sa.Integer(), nullable=True),
    sa.Column('matchesplayed', sa.Integer(), nullable=True),
    sa.Column('playersoutlived', sa.Integer(), nullable=True),
    sa.Column('minutesplayed', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stat_id'], ['stat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_history')
    # ### end Alembic commands ###
