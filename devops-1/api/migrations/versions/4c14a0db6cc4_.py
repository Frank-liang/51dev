"""empty message

Revision ID: 4c14a0db6cc4
Revises: e9cdedc2f06d
Create Date: 2016-01-23 14:36:02.513479

"""

# revision identifiers, used by Alembic.
revision = '4c14a0db6cc4'
down_revision = 'e9cdedc2f06d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('uuid', sa.String(length=50), nullable=True))
    op.create_index(op.f('ix_server_uuid'), 'server', ['uuid'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_server_uuid'), table_name='server')
    op.drop_column('server', 'uuid')
    ### end Alembic commands ###
