from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify, flash, redirect

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
    return render_template('menu.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar_post():
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

@app.route('/excluir')
def exibir_formulario_exclusao():
    return render_template('excluir.html')

@app.route('/excluir', methods=['GET', 'POST'])
def excluir_registro():
    if request.method == 'POST':
        codigo = request.json.get('codigo')

        registro = Cadastro.query.filter_by(codigo=codigo).first()
        if registro:
            db.session.delete(registro)
            db.session.commit()
            return "Empregado excluído com sucesso!"
        else:
            return "Empregado não encontrado.", 404

    return render_template('excluir.html')


from flask import jsonify

@app.route('/buscar_empregado')
def buscar_empregado():
    codigo = request.args.get('codigo')

    # Busca o empregado com base no código fornecido
    empregado = Cadastro.query.filter_by(codigo=codigo).first()

    if empregado:
        # Se o empregado for encontrado, retorna os dados em formato JSON
        dados_empregado = {
            'codigo': empregado.codigo,
            'nome': empregado.nome,
            'cargo': empregado.cargo,
            'loja': empregado.loja,
            'salario': empregado.salario
        }
        return jsonify(dados_empregado), 200
    else:
        # Se o empregado não for encontrado, retorna uma mensagem de erro em formato JSON
        mensagem = {'erro': 'Empregado não encontrado'}
        return jsonify(mensagem), 404

# Rota para exibir a página de edição
@app.route('/editar', methods=['GET'])
def exibir_pagina_edicao():
    return render_template('editar.html')

from flask import jsonify

@app.route('/buscar_funcionario')
def obter_funcionario_por_codigo(codigo):
    # Lógica para buscar o funcionário no banco de dados com base no código
    # Substitua este exemplo pela sua própria lógica de busca
    funcionario = db.query(Cadastro).filter_by(codigo=codigo).first()

    if funcionario:
        return {
            'id': funcionario.id,
            'nome': funcionario.nome,
            'cargo': funcionario.cargo,
            'loja': funcionario.loja,
            'salario': funcionario.salario
        }

    return None

def editar_funcionario(funcionario_id, nome, cargo, loja, salario):
    # Lógica para atualizar os dados do funcionário no banco de dados
    # Substitua este exemplo pela sua própria lógica de edição
    funcionario = db.query(Cadastro).get(funcionario_id)

    if funcionario:
        funcionario.nome = nome
        funcionario.cargo = cargo
        funcionario.loja = loja
        funcionario.salario = salario
        db.commit()
        return True

    return False

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()