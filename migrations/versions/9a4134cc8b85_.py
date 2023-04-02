"""empty message

Revision ID: 9a4134cc8b85
Revises: bb9de79f0f28
Create Date: 2023-03-14 19:51:48.045448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a4134cc8b85'
down_revision = 'bb9de79f0f28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vin', sa.String(length=17), nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.VARCHAR(), server_default=sa.text("nextval('car_id_seq'::regclass)"), autoincrement=False, nullable=False))
        batch_op.drop_column('vin')

    # ### end Alembic commands ###
