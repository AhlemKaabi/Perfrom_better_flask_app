"""empty message

Revision ID: 9d24ad919256
Revises: 7b1c080f50ef
Create Date: 2021-10-12 17:23:11.846290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d24ad919256'
down_revision = '7b1c080f50ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_flights_departure', table_name='flights')
    op.create_index(op.f('ix_flights_departure'), 'flights', ['departure'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_flights_departure'), table_name='flights')
    op.create_index('ix_flights_departure', 'flights', ['departure'], unique=False)
    # ### end Alembic commands ###
