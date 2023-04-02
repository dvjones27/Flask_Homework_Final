"""empty message

Revision ID: 57a5e2a8e933
Revises: 146b7b4296cc
Create Date: 2023-03-15 17:08:53.129264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57a5e2a8e933'
down_revision = '146b7b4296cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.String(), nullable=False))
        batch_op.alter_column('vin',
               existing_type=sa.VARCHAR(length=17),
               nullable=True)
        batch_op.create_unique_constraint(None, ['vin'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('vin',
               existing_type=sa.VARCHAR(length=17),
               nullable=False)
        batch_op.drop_column('id')

    # ### end Alembic commands ###
