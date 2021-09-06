from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

# formulario persona
class PersonaForm(FlaskForm):
    dni = StringField('DNI', validators=[DataRequired()])
    # nombre será un campo con etiqueta "nombre" y requerido
    nombre = StringField('Nombre', validators=[DataRequired()])
    # no requerido
    apellido = StringField('Apellido', validators=[DataRequired()])
    # requerido
    tecnico = StringField('Apellido', validators=[DataRequired()])
    serie_numero = IntegerField('Número de Serie', validators=[DataRequired()])
    dosis_total = IntegerField('Dosis Total', validators=[DataRequired()])
    numero_sesiones = IntegerField('Número de Sesiones', validators=[DataRequired()])
    porcentaje_pauta = FloatField('% Pauta', validators=[DataRequired()])
    Movimientos = StringField('Movimientos', validators=[DataRequired()])
    tac_lateral = FloatField('Tac Lateral', validators=[DataRequired()])
    tac_ant_post = FloatField('Tac Ant Post', validators=[DataRequired()])
    tac_sup_inf = FloatField('Tac Sup Inf', validators=[DataRequired()])
    iso_lateral = FloatField('Iso Lateral', validators=[DataRequired()])
    iso_ant_post = FloatField('Iso Ant Post', validators=[DataRequired()])
    iso_sup_inf = FloatField('Iso Sup Inf', validators=[DataRequired()])
    norm_lateral = FloatField('Norm Lateral', validators=[DataRequired()])
    norm_ant_post = FloatField('Norm Ant Post', validators=[DataRequired()])
    norm_sup_inf = FloatField('Norm Sup Inf', validators=[DataRequired()])
    numero_campos = IntegerField('Nº de Campos', validators=[DataRequired()])
    enviar = SubmitField('Enviar')


# formulario tratamiento
class TratamientoForm(FlaskForm):
    id_campo = IntegerField('Id Tratamiento')
    id_paciente = IntegerField('Id Paciente')
    num_campo = IntegerField('Número de Campo')
    nombre_campo = StringField('Nombre de Campo')
    gantry = IntegerField('Gantry')
    colimador = IntegerField('Colimador')
    mesa = IntegerField('Mesa')
    energia = StringField('Energía')
    dfp_a_norm = FloatField('DFP a norm')
    tecnica = StringField('Técnica')
    Y2 = FloatField('Y2')
    Y1 = FloatField('Y1')
    X2 = FloatField('X2')
    X1 = FloatField('X1')
    # dL_offset = db.Column(db.Float)
    # dW_offset = db.Column(db.Float)
    # x_isoc = db.Column(db.Float)
    # y_isoc = db.Column(db.Float)
    cuadrado_equi = FloatField('Cuadrado Equiv')
    porcentaje_bloqueo = FloatField('% bloqueo')
    # campo_equivalente = db.Column(db.Float)
    conformacion = StringField('Conformación')
    prof_fisica = FloatField('Prof. física')
    prof_equiv = FloatField('Prof. equiv.')
    cunyya = StringField('Cuña')
    dose_at_ref_frac = FloatField('Dose at Ref/Frac')
    #  porcentaje_normalizacion = db.Column(db.Float)
    # dosis_cGy = db.Column(db.Float)
    # dosis_referencia = db.Column(db.Float)
    # pdd_10 = db.Column(db.Float)
    # sc_isoc = db.Column(db.Float)
    # sp_isoc = db.Column(db.Float)
    # tpr = db.Column(db.Float)
    # f_cunya_fuera_eje = IntegerField('F cuña fuera de eje', validators=[DataRequired()])
    # oar = IntegerField('OAR', validators=[DataRequired()])
    # um_hoja = db.Column(db.Float)
    um_pinnacle = FloatField('UM Pinnacle')
    # diferencia_porcentaje = db.Column(db.Float)
    # um_aria = IntegerField('Número de Sesiones', validators=[DataRequired()])
    # aria_pinnacle = db.Column(db.Float)
    # error_verificacion = db.Column(db.Float)
    # error_redondeo_de_um = db.Column(db.Float)
    enviar = SubmitField('Enviar')



