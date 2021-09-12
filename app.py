from collections import namedtuple
from flask import Flask, render_template, request, session, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from forms import PersonaForm, TratamientoForm
from models import Persona, Tratamiento, Usuario

app = Flask(__name__)

app.secret_key = 'sermicro2012_sermicro2012'

'''Configuración de la BDD'''
USER_DB = 'postgres'
PASS_DB = 'sermicro2012'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
'''cadena de conexión completa: TIPO BD://usuario contraseña url_bd nombre'''
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

'''definimos varias variables para sqlalchemy funcionando con flask (integración flask-sqlalchemy)
   mapeo de objetos hacia la bdd'''

'''URL QUÉ VA A USAR SQLALCHEMY PARA CONECTARSE A LA BASE DE DATOS'''
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
'''optimizamos: qué no haga un trackeo de cada modificación hecha en la base de datos'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''inicializamos objeto de BD de sqlalchemy'''
db.init_app(app)

# agrego configuración de Flask Migrate: realizar migraciones y hacer mapeo de esta clase de python hacia
migrate = Migrate()  # creo objeto migrate
# inicializo este objeto usando los 2 objetos
migrate.init_app(app, db)

# configuración de flask-wtf para agregar
app.config['SECRET_KEY'] = 'sermicro2012'


# Ruta de inicio
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    if 'username' in session:
        return redirect(url_for('escritorio'))
    return render_template('login.html')


# opción para iniciar sesión en la app
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


# opción de sólo ver una persona (para lo qué recibiremos un parámetro)
@app.route('/ver/<int:id>', methods=['GET', 'POST'])
def ver(id):
    # precargo datos necesarios
    dL = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    dW = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    PDD10 = [78.1, 77.3, 83.8, 103.4, 103.5, 107.4, 107.6, 90.4]
    Sc_isoc = [1.010, 1.008, 1.012, 1.005, 1.006, 0.996, 0.997, 0.993]
    Sp_isoc = [0.988, 0.955, 0.989, 0.981, 0.969, 0.987, 0.971, 0.985]
    TPR = [86.110, 85.225, 90.001, 101.936, 102.053, 104.138, 104.325, 94.113]
    f_cunya_f_eje = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    oar = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    um_hoja = [45.72, 5.08, 51.11, 39.20, 5.05, 29.77, 3.92, 54.31]

    # CON RESPECTO AL PACIENTE
    # recuperamos la persona según id proporcionado
    # si no lo encuentra ese id nos devuelve el código de error 404
    persona = Persona.query.get_or_404(id)

    # cargo los Tratamientos (campos) a pasar al formulario
    camposQueTienePaciente = db.session.execute("SELECT * from tratamiento where id_paciente = :idid", {'idid': id})

    # veo cuántos campos tiene dado de alta (para poder iterar en el formulario)
    Record = namedtuple('Record', camposQueTienePaciente.keys())
    records = [Record(*r) for r in camposQueTienePaciente.fetchall()]
    numerocamposQueYaTiene = len(records)

    # ahora lo compartimos con nuestra página
    return render_template('detalle.html', persona=persona, numerocamposQueYaTiene=numerocamposQueYaTiene,
                           Record=Record, records=records, dL=dL, dW=dW, PDD10=PDD10, Sc_isoc=Sc_isoc, Sp_isoc=Sp_isoc,
                           TPR=TPR, f_cunya_f_eje=f_cunya_f_eje, oar=oar, um_hoja=um_hoja)


# opción de sólo ver una persona (para lo qué recibiremos un parámetro)
@app.route('/altaCampo/<int:id>', methods=['GET', 'POST'])
def altaCampo(id):
    # recuperamos la persona según id proporcionado
    # si no lo encuentra ese id nos devuelve el código de error 404
    persona = Persona.query.get_or_404(id)

    # Para dar de alta un nuevo campo (tratamiento)
    tratamiento = Tratamiento()
    tratamientoForm = TratamientoForm(obj=tratamiento)

    # veo los campos qué tiene dado de alta este paciente
    camposQueTienePaciente = db.session.execute(
        "SELECT tratamiento.id_paciente from tratamiento where id_paciente = :idid", {'idid': id})
    # veo cuántos campos tiene dado de alta
    Record = namedtuple('Record', camposQueTienePaciente.keys())
    records = [Record(*r) for r in camposQueTienePaciente.fetchall()]
    camposQueYaTiene = len(records) + 1

    pacienteAfectado = persona.id
    totaldecampos = db.session.query(Tratamiento.id_campo).count()
    totaldecampos = totaldecampos + 1

    if request.method == 'POST':
        # si válido
        if tratamientoForm.validate_on_submit():
            # con los valores del formulario rellenamos la persona
            tratamientoForm.populate_obj(tratamiento)
            # ya listos para guardar info en BDD
            db.session.add(tratamiento)
            db.session.commit()
            return redirect(url_for('inicio'))

    # ahora lo compartimos con nuestra página
    return render_template('altaCampo.html', persona=persona, forma=tratamientoForm, camposQueYaTiene=camposQueYaTiene,
                           pacienteAfectado=pacienteAfectado, totaldecampos=totaldecampos)


@app.route('/agregar.html', methods=['GET', 'POST'])
def agregar():
    # creamos objeto tipo persona, nuestra clase de modelo
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    # si es método POST se hará la inserción
    if request.method == 'POST':
        # si válido
        if personaForm.validate_on_submit():
            # con los valores del formulario rellenamos la persona
            personaForm.populate_obj(persona)
            # ya listos para guardar info en BDD
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    # si es GET
    return render_template('agregar.html', forma=personaForm)


@app.route('/editar/<int:este>', methods=['GET', 'POST'])
def editar(este):
    # recuperamos el objeto persona a editar
    persona = Persona.query.get_or_404(este)
    # llenamos nuestro objeto personaForma con los datos recuperados
    personaForma = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            # volcamos lo del formulario a nuestro objeto tipo persona
            personaForma.populate_obj(persona)
            # guardamos
            db.session.commit()
            return redirect(url_for('inicio'))
    # le pasamos al formulario a la persona recuperada
    return render_template('editar.html', forma=personaForma)


# sólo será necesario un GET
@app.route('/eliminar/<int:este>')
def eliminar(este):
    persona = Persona.query.get_or_404(este)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))


@app.route('/escritorio', methods=['GET', 'POST'])
def escritorio():
    # Mostramos a los pacientes ordenados por ID
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()
    return render_template('index.html', personas=personas, total_personas=total_personas)


@app.route('/salir')
def salir():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route('/hacer_login', methods=['GET', 'POST'])
def hacer_login():
    correo = request.form["username"]
    palabra_secreta = request.form["password"]
    usuarios_que_tenemos = Usuario.query.all()
    for i in usuarios_que_tenemos:
        if correo == i.nombre_usuario and palabra_secreta == i.clave_usuario:
            session["username"] = correo
            session["rol"]=i.rol_usuario
            return redirect("/escritorio")
    else:
        # Si NO coincide, lo regresamos
        return redirect("/login")

'''
@app.route('/tratamiento.html/<int:este>', methods=['GET', 'POST'])
def tratamiento(este):
    # creamos objeto tipo tratamiento, clase de modelo
    tratamiento = Tratamiento()
    tratamientoForm = TratamientoForm(obj=tratamiento)
    # si es método POST se hará la inserción
    if request.method == 'POST':
        # si válido
        if tratamientoForm.validate_on_submit():
            # con los valores del formulario rellenamos la persona
            tratamientoForm.populate_obj(tratamiento)
            # ya listos para guardar info en BDD
            db.session.add(tratamiento)
            db.session.commit()
            return redirect(url_for('detalle.html'))
    # si es GET
    return render_template('tratamiento.html', forma=tratamientoForm)
'''
