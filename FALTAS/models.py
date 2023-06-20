from app import db

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
