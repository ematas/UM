"""empty message

Revision ID: 6036445771c5
Revises: 70de669640b3
Create Date: 2021-08-29 14:15:17.203925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6036445771c5'
down_revision = '70de669640b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tratamiento', 'num_campo',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('tratamiento', 'diferencia_porcentaje')
    op.drop_column('tratamiento', 'dL_offset')
    op.drop_column('tratamiento', 'y_isoc')
    op.drop_column('tratamiento', 'sc_isoc')
    op.drop_column('tratamiento', 'tpr')
    op.drop_column('tratamiento', 'dW_offset')
    op.drop_column('tratamiento', 'oar')
    op.drop_column('tratamiento', 'um_hoja')
    op.drop_column('tratamiento', 'error_redondeo_de_um')
    op.drop_column('tratamiento', 'porcentaje_normalizacion')
    op.drop_column('tratamiento', 'f_cunya_fuera_eje')
    op.drop_column('tratamiento', 'x_isoc')
    op.drop_column('tratamiento', 'campo_equivalente')
    op.drop_column('tratamiento', 'dosis_referencia')
    op.drop_column('tratamiento', 'error_verificacion')
    op.drop_column('tratamiento', 'um_aria')
    op.drop_column('tratamiento', 'aria_pinnacle')
    op.drop_column('tratamiento', 'sp_isoc')
    op.drop_column('tratamiento', 'pdd_10')
    op.drop_column('tratamiento', 'dosis_cGy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tratamiento', sa.Column('dosis_cGy', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('pdd_10', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('sp_isoc', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('aria_pinnacle', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('um_aria', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('error_verificacion', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('dosis_referencia', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('campo_equivalente', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('x_isoc', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('f_cunya_fuera_eje', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('porcentaje_normalizacion', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('error_redondeo_de_um', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('um_hoja', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('oar', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('dW_offset', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('tpr', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('sc_isoc', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('y_isoc', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('dL_offset', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('tratamiento', sa.Column('diferencia_porcentaje', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.alter_column('tratamiento', 'num_campo',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
