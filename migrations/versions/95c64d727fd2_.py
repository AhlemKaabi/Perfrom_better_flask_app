"""empty message

Revision ID: 95c64d727fd2
Revises: 
Create Date: 2021-10-08 19:10:41.474159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95c64d727fd2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rampagents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rampagents_email'), 'rampagents', ['email'], unique=True)
    op.create_index(op.f('ix_rampagents_first_name'), 'rampagents', ['first_name'], unique=False)
    op.create_index(op.f('ix_rampagents_last_name'), 'rampagents', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rampagents_last_name'), table_name='rampagents')
    op.drop_index(op.f('ix_rampagents_first_name'), table_name='rampagents')
    op.drop_index(op.f('ix_rampagents_email'), table_name='rampagents')
    op.drop_table('rampagents')
    # ### end Alembic commands ###
