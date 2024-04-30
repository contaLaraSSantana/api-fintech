from flask import Flask, request, jsonify
from main import app, db
from models import Receitas, Despesas, Usuario, Poupanca

@app.route('/Usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios_dic = []
    for usuario in usuarios:
        usuario_dic = {
            'id_usuario': usuario.id_usuario,
            'nome_usuario': usuario.nome_usuario,
            'email': usuario.email
        }
        usuarios_dic.append(usuario_dic)
    return jsonify(
        mensagem='Lista de Usuários',
        usuarios=usuarios_dic
    )

@app.route('/Usuarios', methods=['POST'])
def post_usuario():
    usuario_data = request.json
    novo_usuario = Usuario(
        nome_usuario=usuario_data.get('nome_usuario'),
        email=usuario_data.get('email'),
        senha=usuario_data.get('senha')
    )
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify(
        mensagem='Usuário cadastrado com sucesso',
        usuario={
            'id_usuario': novo_usuario.id_usuario,
            'nome_usuario': novo_usuario.nome_usuario,
            'email': novo_usuario.email
        }
    )

@app.route('/Receitas', methods=['GET'])
def get_receita():
    receitas = Receitas.query.all()
    receitas_dic = []
    for receita in receitas:
        receita_dic = {
            'id_receita': receita.id_receita,
            'descricao': receita.descricao,
            'valor': receita.valor,
            'data': receita.data,
            'id_usuario': receita.id_usuario
        }
        receitas_dic.append(receita_dic)
    return jsonify(
        mensagem='Lista de Receitas',
        receitas=receitas_dic
    )

@app.route('/Receitas', methods=['POST'])
def post_receita():
    receita = request.json
    nova_receita = Receitas(
        descricao=receita.get('descricao'),
        valor=receita.get('valor'),
        data=receita.get('data'),
        id_usuario=receita.get('id_usuario')
    )
    db.session.add(nova_receita)
    db.session.commit()

    return jsonify(
        mensagem='Receita Cadastrada com Sucesso',
        receita={
            'id_receita': nova_receita.id_receita,
            'descricao': nova_receita.descricao,
            'valor': nova_receita.valor,
            'data': nova_receita.data
        }
    )

@app.route('/Despesas', methods=['GET'])
def get_despesa():
    despesas = Despesas.query.all()
    despesas_dic = []
    for despesa in despesas:
        despesa_dic = {
            'id_despesa': despesa.id_despesa,
            'descricao': despesa.descricao,
            'valor': despesa.valor,
            'data': despesa.data,
            'id_usuario': despesa.id_usuario
        }
        despesas_dic.append(despesa_dic)
    return jsonify(
        mensagem='Lista de Despesas',
        despesas=despesas_dic
    )

@app.route('/Despesas', methods=['POST'])
def post_despesa():
    despesa = request.json
    nova_despesa = Despesas(
        descricao=despesa.get('descricao'),
        valor=despesa.get('valor'),
        data=despesa.get('data'),
        id_usuario=despesa.get('id_usuario')
    )
    db.session.add(nova_despesa)
    db.session.commit()

    return jsonify(
        mensagem='Despesa Cadastrada com Sucesso',
        despesa={
            'id_despesa': nova_despesa.id_despesa,
            'descricao': nova_despesa.descricao,
            'valor': nova_despesa.valor,
            'data': nova_despesa.data
        }
    )

@app.route('/Poupanca', methods=['GET'])
def get_poupanca():
    poupancas = Poupanca.query.all()
    poupancas_dic = []
    for poupanca in poupancas:
        poupanca_dic = {
            'id_poupanca': poupanca.id_poupanca,
            'descricao': poupanca.descricao,
            'valor': poupanca.valor,
            'data': poupanca.data,
            'id_usuario': poupanca.id_usuario
        }
        poupancas_dic.append(poupanca_dic)
    return jsonify(
        mensagem='Lista de Poupanças',
        poupancas=poupancas_dic
    )

@app.route('/Poupanca', methods=['POST'])
def post_poupanca():
    poupanca = request.json
    nova_poupanca = Poupanca(
        descricao=poupanca.get('descricao'),
        valor=poupanca.get('valor'),
        data=poupanca.get('data'),
        id_usuario=poupanca.get('id_usuario')
    )
    db.session.add(nova_poupanca)
    db.session.commit()

    return jsonify(
        mensagem='Poupança cadastrada com Sucesso',
        poupanca={
            'id_poupanca': nova_poupanca.id_poupanca,
            'descricao': nova_poupanca.descricao,
            'valor': nova_poupanca.valor,
            'data': nova_poupanca.data
        }
    )
