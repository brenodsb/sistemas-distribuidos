from flask import Flask
from flask import request, jsonify
from flask import render_template
from datetime import date
import sqlite3
from sqlite3 import Error
#######################################################
# Instancia da Aplicacao Flask
app = Flask(__name__)
#######################################################
# 1. Cadastrar produtos
@app.route('/produtos/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        datacriacao = date.today()
        print(descricao, precocompra, precovenda, datacriacao)
        mensagem = 'Erro - nao cadastrado'
        if descricao and precocompra and precovenda and datacriacao:
            registro = (descricao, precocompra, precovenda, datacriacao)
            try:
                conn = sqlite3.connect('./atividade_4/db/db-produtos.db')
                sql = ''' INSERT INTO produtos(descricao, precocompra, precovenda, datacriacao) VALUES(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
                mensagem = 'Sucesso - cadastrado'
            except Error as e:
                print(e)
            finally:
                conn.close()
    return jsonify({'mensagem': 'registro adicionado com sucesso'})
#######################################################
# 2. Listar produtos
@app.route('/produtos/listar', methods=['GET']) # type: ignore
def listar():
    try:
        conn = sqlite3.connect('./atividade_4/db/db-produtos.db')
        sql = '''SELECT * FROM produtos'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        if registros:
            nomes_colunas = [x[0] for x in cur.description]

            json_dados = []
            for reg in registros:
                json_dados.append(dict(zip(nomes_colunas, reg)))
            return jsonify(json_dados)
    except Error as e:
        print(e)
    finally:
        conn.close()
#######################################################
# Rota de Erro
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404
#######################################################
# Execucao da Aplicacao
if __name__ == '__main__':
    app.run()