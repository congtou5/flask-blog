"""avatar hash

Revision ID: 49d83a917ff4
Revises: 4e08371dbae0
Create Date: 2015-12-25 21:53:09.341000

"""

# revision identifiers, used by Alembic.
revision = '49d83a917ff4'
down_revision = '4e08371dbae0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
