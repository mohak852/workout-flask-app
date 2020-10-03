"""empty message

Revision ID: d848d125836d
Revises: 
Create Date: 2020-10-03 02:00:25.978268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd848d125836d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workout', sa.Column('bodyWeight', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workout', 'bodyWeight')
    # ### end Alembic commands ###
