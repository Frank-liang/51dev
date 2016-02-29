"""empty message

Revision ID: e9cdedc2f06d
Revises: fa0f00412a65
Create Date: 2016-01-23 11:56:34.875878

"""

# revision identifiers, used by Alembic.
revision = 'e9cdedc2f06d'
down_revision = 'fa0f00412a65'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('os', sa.String(length=30), nullable=True))
    op.create_index(op.f('ix_server_os'), 'server', ['os'], unique=False)
    op.drop_column('server', 'os_version')
    op.drop_column('server', 'os_type')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('os_type', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('server', sa.Column('os_version', mysql.VARCHAR(length=10), nullable=True))
    op.drop_index(op.f('ix_server_os'), table_name='server')
    op.drop_column('server', 'os')
    ### end Alembic commands ###
