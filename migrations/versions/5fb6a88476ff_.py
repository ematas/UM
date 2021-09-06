"""empty message

Revision ID: 5fb6a88476ff
Revises: bd0891f4469c
Create Date: 2021-08-31 19:04:50.344223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fb6a88476ff'
down_revision = 'bd0891f4469c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tratamiento_id_paciente_fkey', 'tratamiento', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('tratamiento_id_paciente_fkey', 'tratamiento', 'persona', ['id_paciente'], ['id'])
    # ### end Alembic commands ###
