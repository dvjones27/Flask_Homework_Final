"""empty message

Revision ID: e6a2abaa3a50
Revises: 57a5e2a8e933
Create Date: 2023-03-15 19:19:20.954865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6a2abaa3a50'
down_revision = '57a5e2a8e933'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_token', sa.String(), nullable=False))
        batch_op.drop_constraint('car_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_token'], ['token'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('car_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.drop_column('user_token')

    # ### end Alembic commands ###
