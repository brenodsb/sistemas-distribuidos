import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

# GET: Pesquisar
@app.route('/api-loja/pesquisar/<int:idproduto>', methods=['GET'])

def pesquisar(idproduto=None):
    if idproduto == None:
        return jsonify({'mensagem': 'parametro invalido'})
    else:
        try:
            conn = sqlite3.connect('atividade_3/database/db-loja.db')

            if idproduto == 0:
                sql = '''SELECT * FROM produtos'''
            else:
                sql = '''SELECT * FROM produtos WHERE idproduto = ''' + str(idproduto)

            cur = conn.cursor()
            cur.execute(sql)
            registros = cur.fetchall()

            if registros:
                nomes_colunas = [x[0] for x in cur.description]

                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))
                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'})

        except Error as e:
            return jsonify({'mensagem': f'erro: {e}'})
        finally:
            conn.close()

# POST: Inserir
@app.route('/api-loja/inserir', methods=['POST']) # type: ignore

def inserir():
    if request.method == 'POST':
        dados = request.get_json()

        descricao = dados['descricao']
        ganhopercentual = dados['ganhopercentual']
        datacriacao = date.today()

        if descricao and ganhopercentual and datacriacao:
            registro = (descricao, ganhopercentual, datacriacao)

            try:
                conn = sqlite3.connect('atividade_3/database/db-loja.db')

                sql = '''INSERT INTO produtos (descricao, ganhopercentual, datacriacao) VALUES (?, ?, ?)'''

                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                print("PASSOU AQUI")
                return jsonify({'mensagem': 'registro inserido com sucesso'})

            except Error as e:
                return jsonify({'mensagem': f'erro: {e}'})
            finally:
                conn.close()
        else:
            return jsonify({'mensagem': 'campos <descicao> e <ganhopercentual> sao obrigatorios'})

# DELETE: Excluir
@app.route('/api-loja/excluir/<int:idproduto>', methods=['DELETE'])

def excluir(idproduto=None):
    if idproduto == None:
        return jsonify({'mensagem': 'parametro invalido'})
    else:
        try:
            conn = sqlite3.connect('atividade_3/database/db-loja.db')

            sql = '''DELETE FROM produtos WHERE idproduto = ''' + str(idproduto)

            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

            return jsonify({'mensagem': 'registro excluido'})
        except Error as e:
            return jsonify({'mensagem': f'erro: {e}'})
        finally:
            conn.close()

# PUT: Alterar
@app.route('/api-loja/alterar/', methods=['PUT']) # type: ignore

def alterar():
    if request.method == 'PUT':
        dados = request.get_json()

        idproduto = dados['idproduto']
        descricao = dados['descricao']
        ganhopercentual = dados['ganhopercentual']

        if idproduto and descricao and ganhopercentual:
            registro = (descricao, ganhopercentual, idproduto)

            try:
                conn = sqlite3.connect('atividade_3/database/db-loja.db')

                sql = '''UPDATE produtos SET descricao = ?, ganhopercentual = ? WHERE idproduto = ?'''

                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro alterado com sucesso'})

            except Error as e:
                return jsonify({'mensagem': f'erro: {e}'})
            finally:
                conn.close()
        else:
            return jsonify({'mensagem': 'campos <idproduto>, <descicao> e <ganhopercentual> sao obrigatorios'})

# UrlPoint nao localizado
@app.errorhandler(404)

def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

# Execução da Aplicação
if __name__ == '__main__':
    app.run()