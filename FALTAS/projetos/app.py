from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastros.db'
db = SQLAlchemy(app)

class Cadastro(db.Model):
    __tablename__ = 'cadastro'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10))
    nome = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    loja = db.Column(db.String(100))
    salario = db.Column(db.Float)

    def __init__(self, codigo, nome, cargo, loja, salario):
        self.codigo = codigo
        self.nome = nome
        self.cargo = cargo
        self.loja = loja
        self.salario = salario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    codigo = request.form['codigo']
    nome = request.form['nome']
    cargo = request.form['cargo']
    loja = request.form['loja']
    salario = request.form['salario']

    novo_cadastro = Cadastro(codigo=codigo, nome=nome, cargo=cargo, loja=loja, salario=salario)
    db.session.add(novo_cadastro)
    db.session.commit()

    return "Cadastro realizado com sucesso!"

@app.route('/empregados')
def listar_empregados():
    empregados = Cadastro.query.all()
    return render_template('cadastros.html', empregados=empregados)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
