"""empty message

Revision ID: 0fa8ef06b2d0
Revises: 4c14a0db6cc4
Create Date: 2016-01-23 14:38:27.556455

"""

# revision identifiers, used by Alembic.
revision = '0fa8ef06b2d0'
down_revision = '4c14a0db6cc4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('manufacturers', sa.String(length=50), nullable=False))
    op.create_index(op.f('ix_server_manufacturers'), 'server', ['manufacturers'], unique=False)
    op.drop_index('ix_server_manufactures', table_name='server')
    op.drop_column('server', 'manufactures')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('manufactures', mysql.VARCHAR(length=50), nullable=False))
    op.create_index('ix_server_manufactures', 'server', ['manufactures'], unique=False)
    op.drop_index(op.f('ix_server_manufacturers'), table_name='server')
    op.drop_column('server', 'manufacturers')
    ### end Alembic commands ###
