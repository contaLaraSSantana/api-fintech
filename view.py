from flask import Flask, request, jsonify, session
from main import app, db
from models import Receitas, Despesas,Usuario,Poupanca

@app.route('/Receitas', methods=['GET'])
def get_receita():
    Receita = Receitas.query.all()
    receitas_dic = []
    for receitas in Receita:
        receita_dic = {
            'id_receita': receitas.id_receita,
            'descricao': receitas.descricao,
            'valor': receitas.valor,
            'datas': receitas.data,
            'id_usuario': receitas.id_usuario
        }
        receitas_dic.append(receita_dic)
    return jsonify(
        mensagem='Lista de Receitas',
        receitas= receitas_dic
    )
@app.route('/Despesas', methods=['GET'])
def get_despesa():
    Despesa = Despesas.query.all()
    despesas_dic = []
    for despesas in Despesa:
        despesa_dic = {
            'id_receita': despesas.id_receita,
            'descricao': despesas.descricao,
            'valor': despesas.valor,
            'datas': despesas.data,
            'id_usuario': despesas.id_usuario
        }
        despesas_dic.append(despesa_dic)
    return jsonify(
        mensagem='Lista de Despesas',
        receitas= despesas_dic
    )

@app.route('/Receitas', methods=['POST'])
def post_receita():
    Receita = request.json
    nova_receita = Receita(
        id_receita=Receita.get('id_receita'),
        descricao=Receita.get('descricao'),
        valor=Receita.get('valor'),
        datas=Receita.get('data')
    )
    db.session.add(nova_receita)
    db.session.commit()

    return jsonify(
        mensagem='Receita Cadastrada com Sucesso',
        livro={
            'id_receita': nova_receita.id_receita,
            'descricao': nova_receita.descricao,
            'valor': nova_receita.valor,
            'datas': nova_receita.data
        }
    )


@app.route('/Poupanca', methods=['POST'])
def post_poupanca():
    Poupanca = request.json
    nova_poupanca = Poupanca(
        id_poupanca=Poupanca.get('id_poupanca'),
        descricao=Poupanca.get('descricao'),
        data=Poupanca.get('data'),
        valor=Poupanca.get('valor'),

    )
    db.session.add(nova_poupanca)
    db.session.commit()

    return jsonify(
        mensagem='Poupança cadastrada com Sucesso',
        livro={
            'id_poupanca': nova_poupanca.id_despesa,
            'descricao': nova_poupanca.descricao,
            'data': nova_poupanca.data,
            'valor': nova_poupanca.valor,
        }
    )

