

from app import db


class Persona(db.Model):
    # clave primaria
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10))
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    fecha = db.Column(db.DateTime)
    tecnico = db.Column(db.String(250))
    serie_numero = db.Column(db.Integer)
    dosis_total = db.Column(db.Integer)
    numero_sesiones = db.Column(db.Integer)
    porcentaje_pauta = db.Column(db.Integer)
    Movimientos = db.Column(db.String(250))
    tac_lateral = db.Column(db.Float)
    tac_ant_post = db.Column(db.Float)
    tac_sup_inf = db.Column(db.Float)
    iso_lateral = db.Column(db.Float)
    iso_ant_post = db.Column(db.Float)
    iso_sup_inf = db.Column(db.Float)
    norm_lateral = db.Column(db.Float)
    norm_ant_post = db.Column(db.Float)
    norm_sup_inf = db.Column(db.Float)
    numero_campos = db.Column(db.Integer)
    #tratamientos = db.relationship('Tratamiento')

    # para poder obtener una represencación de esta clase
    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'DNI: {self.dni}'
            f'NOMBRE: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Fecha: {self.fecha}, '
            f'Técnico: {self.tecnico}'
            f'Serie Número: {self.serie_numero}, '
            f'Dosis Total: {self.dosis_total}, '
            f'Número Sesiones: {self.numero_sesiones}, '
            f'Porcentaje Pauta: {self.porcentaje_pauta}, '
            f'Movimientos: {self.Movimientos}, '
            f'Tac Lateral: {self.tac_lateral}, ' 
            f'Tac Ant. Post.: {self.tac_ant_post}, '
            f'Tac Sup. Inf.: {self.tac_sup_inf}, ' 
            f'ISO Lateral: {self.iso_lateral}, '
            f'ISO Ant. Post.: {self.iso_ant_post}, '
            f'ISO Sup. Inf.: {self.iso_sup_inf}, '
            f'Norm Lateral: {self.norm_lateral}, '
            f'Norm Ant. Post.: {self.norm_ant_post}, '
            f'Norm Sup. Inf.: {self.norm_sup_inf}'
        )


class Tratamiento(db.Model):
    # clave primaria
    id_campo = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer)
    #, db.ForeignKey('persona.id')
    # represencación de esta clase
    num_campo = db.Column(db.Integer)
    nombre_campo = db.Column(db.String(250))
    gantry = db.Column(db.Integer)
    colimador = db.Column(db.Integer)
    mesa = db.Column(db.Integer)
    energia = db.Column(db.String(250))
    dfp_a_norm = db.Column(db.Float)
    tecnica = db.Column(db.String(250))
    Y2 = db.Column(db.Float)
    Y1 = db.Column(db.Float)
    X2 = db.Column(db.Float)
    X1 = db.Column(db.Float)
    #calculado dL_offset = db.Column(db.Float)
    #calculado dW_offset = db.Column(db.Float)
    #calculado x_isoc = db.Column(db.Float)
    #calculado y_isoc = db.Column(db.Float)
    cuadrado_equi = db.Column(db.Float)
    porcentaje_bloqueo = db.Column(db.Float)
    #calculado campo_equivalente = db.Column(db.Float)
    conformacion = db.Column(db.String(250))
    prof_fisica = db.Column(db.Float)
    prof_equiv = db.Column(db.Float)
    cunyya = db.Column(db.String(250))
    dose_at_ref_frac = db.Column(db.Float)
    #calculado porcentaje_normalizacion = db.Column(db.Float)
    #calculado dosis_cGy = db.Column(db.Float)
    #calculado dosis_referencia = db.Column(db.Float)
    #calculado pdd_10 = db.Column(db.Float)
    #calculado sc_isoc = db.Column(db.Float)
    #calculado sp_isoc = db.Column(db.Float)
    #calculado tpr = db.Column(db.Float)
    #calculado f_cunya_fuera_eje = db.Column(db.Integer)
    #calculado oar = db.Column(db.Integer)
    #calculado um_hoja = db.Column(db.Float)
    um_pinnacle = db.Column(db.Float)
    #calculado diferencia_porcentaje = db.Column(db.Float)
    #calculado um_aria = db.Column(db.Integer)
    #calculado aria_pinnacle = db.Column(db.Float)
    #calculado error_verificacion = db.Column(db.Float)
    #calculado error_redondeo_de_um = db.Column(db.Float)
    
    def __str__(self):
        return (
            f'Id Campo: {self.id_campo}, '            
            f'Id Paciente: {self.id_paciente}, '
            f'Nº de Campo: {self.num_campo}, '
            f'Nº de Campo: {self.nombre_campo}, '
            f'Gantry: {self.gantry}, '
            f'Colimador: {self.colimador}, '
            f'Mesa: {self.mesa}, '
            f'Energía: {self.energia}, '
            f'DFP a norm: {self.dfp_a_norm}, '
            f'Técnica: {self.tecnica}, '
            f'Y2: {self.Y2}, '
            f'Y1: {self.Y1}, '
            f'X2: {self.X2}, '
            f'X1: {self.X1}, '
            # f'dL offset: {self.dL_offset}, '
            # f'dW offset: {self.dW_offset}, '
            # f'X isoc: {self.x_isoc}, '
            # f'Y isoc: {self.y_isoc}, '
            f'Cuadrado Equiv: {self.cuadrado_equi}, '
            f'% bloqueo: {self.porcentaje_bloqueo}, '
            # f'Campo Equiv: {self.campo_equivalente}, '
            f'Conformación: {self.conformacion}, '
            f'Prof. Física: {self. prof_fisica}, '
            f'Prof. Equiv: {self.prof_equiv}, '
            f'Cuña: {self.cunyya}, '
            f'Dose at Ref/Frac: {self.dose_at_ref_frac}, '            
            # f'% Normalización: {self.porcentaje_normalizacion}, '
            # f'Dosis (cGy): {self.dosis_cGy}, '
            # f'Dosis Referencia: {self.dosis_referencia}, '
            # f'PDD 10: {self.pdd_10}, '
            # f'Sc isoc: {self.sc_isoc}, '
            # f'Sp isoc: {self.sp_isoc}, '
            # f'TPR: {self.tpr}, '
            # f'F cuña fuera eje: {self.f_cunya_fuera_eje}, '
            # f'OAR: {self.oar}, '
            # f'UM Hoja: {self.um_hoja}, '
            f'UM Pinnacle: {self.um_pinnacle}, '
            # f'Dif (%): {self.diferencia_porcentaje}, '
            # f'UM ARIA: {self.um_aria}, '
            # f'ARIA-PINNACLE: {self.aria_pinnacle}, '
            # f'Error Verificación: {self.error_verificacion}, '
            # f'Error de Redondeo de UM: {self.error_redondeo_de_um}, '
        )
