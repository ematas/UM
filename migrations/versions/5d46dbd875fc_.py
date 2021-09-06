"""empty message

Revision ID: 5d46dbd875fc
Revises: 5e6b12ef42e3
Create Date: 2021-08-22 17:04:42.811849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d46dbd875fc'
down_revision = '5e6b12ef42e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tratamiento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dni_paciente', sa.Integer(), nullable=True),
    sa.Column('fecha_tto', sa.DateTime(), nullable=True),
    sa.Column('tecnico', sa.String(length=250), nullable=True),
    sa.Column('serie_numero', sa.Integer(), nullable=True),
    sa.Column('dosis_total', sa.Integer(), nullable=True),
    sa.Column('numero_sesiones', sa.Integer(), nullable=True),
    sa.Column('porcentaje_pauta', sa.Integer(), nullable=True),
    sa.Column('Movimientos', sa.String(length=250), nullable=True),
    sa.Column('tac_lateral', sa.Float(), nullable=True),
    sa.Column('tac_ant_post', sa.Float(), nullable=True),
    sa.Column('tac_sup_inf', sa.Float(), nullable=True),
    sa.Column('iso_lateral', sa.Float(), nullable=True),
    sa.Column('iso_ant_post', sa.Float(), nullable=True),
    sa.Column('iso_sup_inf', sa.Float(), nullable=True),
    sa.Column('norm_lateral', sa.Float(), nullable=True),
    sa.Column('norm_ant_post', sa.Float(), nullable=True),
    sa.Column('norm_sup_inf', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['dni_paciente'], ['persona.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tratamiento')
    # ### end Alembic commands ###