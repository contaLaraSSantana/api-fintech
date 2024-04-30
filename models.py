from main import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(255))

class Receitas(db.Model):
    id_receitas = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Float(10.2))
    datas = db.Column(db.Date)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

class Despesas(db.Model):
    id_despesas = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Float(10.2))
    datas = db.Column(db.Date)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

class Poupanca(db.Model):
    id_poupanca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Float(10.2))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
