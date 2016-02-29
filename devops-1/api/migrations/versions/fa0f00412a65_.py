"""empty message

Revision ID: fa0f00412a65
Revises: None
Create Date: 2016-01-22 00:15:35.981273

"""

# revision identifiers, used by Alembic.
revision = 'fa0f00412a65'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cabinet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('idc_id', sa.String(length=10), nullable=False),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_cabinet_idc_id'), 'cabinet', ['idc_id'], unique=False)
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_name', sa.String(length=50), nullable=False),
    sa.Column('superior', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('idc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('idc_name', sa.String(length=30), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('user_interface', sa.String(length=50), nullable=False),
    sa.Column('user_phone', sa.String(length=20), nullable=False),
    sa.Column('rel_cabinet_num', sa.Integer(), nullable=False),
    sa.Column('pack_cabinet_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_idc_name'), 'idc', ['name'], unique=True)
    op.create_table('ip_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=20), nullable=False),
    sa.Column('mac', sa.String(length=20), nullable=False),
    sa.Column('device', sa.String(length=20), nullable=False),
    sa.Column('serve_id', sa.Integer(), nullable=False),
    sa.Column('swich_id', sa.Integer(), nullable=False),
    sa.Column('swich_port', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ip_info_serve_id'), 'ip_info', ['serve_id'], unique=False)
    op.create_index(op.f('ix_ip_info_swich_id'), 'ip_info', ['swich_id'], unique=False)
    op.create_table('manufacture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('power',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('server_power', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_name', sa.String(length=20), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('module_letter', sa.String(length=10), nullable=False),
    sa.Column('dev_interface', sa.String(length=100), nullable=True),
    sa.Column('op_interface', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_pid'), 'product', ['pid'], unique=False)
    op.create_table('raid',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('raidtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplier', sa.Integer(), nullable=True),
    sa.Column('manufactures', sa.String(length=50), nullable=False),
    sa.Column('manufacture_date', sa.Date(), nullable=True),
    sa.Column('server_type', sa.String(length=20), nullable=True),
    sa.Column('st', sa.String(length=60), nullable=True),
    sa.Column('assets_no', sa.String(length=60), nullable=True),
    sa.Column('idc_id', sa.Integer(), nullable=True),
    sa.Column('cabinet_id', sa.Integer(), nullable=True),
    sa.Column('cabinet_pos', sa.String(length=10), nullable=True),
    sa.Column('expire', sa.Date(), nullable=True),
    sa.Column('ups', sa.Integer(), nullable=True),
    sa.Column('parter', sa.String(length=50), nullable=True),
    sa.Column('parter_type', sa.String(length=50), nullable=True),
    sa.Column('server_up_time', sa.Date(), nullable=True),
    sa.Column('os_type', sa.String(length=20), nullable=True),
    sa.Column('os_version', sa.String(length=10), nullable=True),
    sa.Column('hostname', sa.String(length=32), nullable=False),
    sa.Column('inner_ip', sa.String(length=32), nullable=False),
    sa.Column('mac_address', sa.String(length=32), nullable=True),
    sa.Column('ip_info', sa.String(length=300), nullable=True),
    sa.Column('server_cpu', sa.String(length=250), nullable=True),
    sa.Column('server_disk', sa.String(length=250), nullable=True),
    sa.Column('server_mem', sa.String(length=250), nullable=True),
    sa.Column('raid', sa.String(length=10), nullable=True),
    sa.Column('raid_card_type', sa.String(length=50), nullable=True),
    sa.Column('remote_card', sa.String(length=32), nullable=True),
    sa.Column('remote_cardip', sa.String(length=32), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.Column('last_op_time', sa.Time(), nullable=True),
    sa.Column('last_op_people', sa.Integer(), nullable=True),
    sa.Column('monitor_mail_group', sa.String(length=32), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('server_purpose', sa.Integer(), nullable=True),
    sa.Column('trouble_resolve', sa.Integer(), nullable=True),
    sa.Column('op_interface_other', sa.Integer(), nullable=True),
    sa.Column('dev_interface', sa.Integer(), nullable=True),
    sa.Column('check_update_time', sa.Time(), nullable=True),
    sa.Column('vm_status', sa.Integer(), nullable=False),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.Column('host', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_server_host'), 'server', ['host'], unique=False)
    op.create_index(op.f('ix_server_hostname'), 'server', ['hostname'], unique=False)
    op.create_index(op.f('ix_server_idc_id'), 'server', ['idc_id'], unique=False)
    op.create_index(op.f('ix_server_inner_ip'), 'server', ['inner_ip'], unique=False)
    op.create_index(op.f('ix_server_manufactures'), 'server', ['manufactures'], unique=False)
    op.create_index(op.f('ix_server_server_purpose'), 'server', ['server_purpose'], unique=False)
    op.create_index(op.f('ix_server_service_id'), 'server', ['service_id'], unique=False)
    op.create_index(op.f('ix_server_st'), 'server', ['st'], unique=False)
    op.create_index(op.f('ix_server_status'), 'server', ['status'], unique=False)
    op.create_index(op.f('ix_server_supplier'), 'server', ['supplier'], unique=False)
    op.create_index(op.f('ix_server_vm_status'), 'server', ['vm_status'], unique=False)
    op.create_table('servertype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('manufactures_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_servertype_manufactures_id'), 'servertype', ['manufactures_id'], unique=False)
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('switch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('switch_name', sa.String(length=50), nullable=False),
    sa.Column('switch_type', sa.String(length=50), nullable=False),
    sa.Column('manager_ip', sa.String(length=50), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('idc_id', sa.Integer(), nullable=True),
    sa.Column('cabinet_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('expire', sa.Date(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.Column('manufacturers', sa.Integer(), nullable=True),
    sa.Column('last_op_time', sa.Time(), nullable=True),
    sa.Column('last_op_people', sa.Integer(), nullable=True),
    sa.Column('switch_port_nums', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_switch_cabinet_id'), 'switch', ['cabinet_id'], unique=False)
    op.create_index(op.f('ix_switch_idc_id'), 'switch', ['idc_id'], unique=False)
    op.create_index(op.f('ix_switch_status'), 'switch', ['status'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('deparment_id', sa.Integer(), nullable=True),
    sa.Column('is_leader', sa.Integer(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_deparment_id'), 'user', ['deparment_id'], unique=False)
    op.create_index(op.f('ix_user_is_leader'), 'user', ['is_leader'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_is_leader'), table_name='user')
    op.drop_index(op.f('ix_user_deparment_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_switch_status'), table_name='switch')
    op.drop_index(op.f('ix_switch_idc_id'), table_name='switch')
    op.drop_index(op.f('ix_switch_cabinet_id'), table_name='switch')
    op.drop_table('switch')
    op.drop_table('supplier')
    op.drop_table('status')
    op.drop_index(op.f('ix_servertype_manufactures_id'), table_name='servertype')
    op.drop_table('servertype')
    op.drop_index(op.f('ix_server_vm_status'), table_name='server')
    op.drop_index(op.f('ix_server_supplier'), table_name='server')
    op.drop_index(op.f('ix_server_status'), table_name='server')
    op.drop_index(op.f('ix_server_st'), table_name='server')
    op.drop_index(op.f('ix_server_service_id'), table_name='server')
    op.drop_index(op.f('ix_server_server_purpose'), table_name='server')
    op.drop_index(op.f('ix_server_manufactures'), table_name='server')
    op.drop_index(op.f('ix_server_inner_ip'), table_name='server')
    op.drop_index(op.f('ix_server_idc_id'), table_name='server')
    op.drop_index(op.f('ix_server_hostname'), table_name='server')
    op.drop_index(op.f('ix_server_host'), table_name='server')
    op.drop_table('server')
    op.drop_table('raidtype')
    op.drop_table('raid')
    op.drop_index(op.f('ix_product_pid'), table_name='product')
    op.drop_table('product')
    op.drop_table('power')
    op.drop_table('manufacture')
    op.drop_index(op.f('ix_ip_info_swich_id'), table_name='ip_info')
    op.drop_index(op.f('ix_ip_info_serve_id'), table_name='ip_info')
    op.drop_table('ip_info')
    op.drop_index(op.f('ix_idc_name'), table_name='idc')
    op.drop_table('idc')
    op.drop_table('department')
    op.drop_index(op.f('ix_cabinet_idc_id'), table_name='cabinet')
    op.drop_table('cabinet')
    ### end Alembic commands ###
