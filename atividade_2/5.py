import requests
import sqlite3

def request():
    url = 'https://api.hgbrasil.com/finance?format=json-cors&key=21ae8ecf'
    resposta = requests.get(url)
    return resposta

def insert(data, dolar, euro):
    conn = sqlite3.connect('atividade_2/bdcotacoes.db')
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO moedas (data, dolar, euro) VALUES (?, ?, ?)"
        cursor.execute(sql, (data, dolar, euro))
        conn.commit()
        print("Registro inserido com sucesso")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    resposta = request()
    if resposta.status_code == 200:
        json = resposta.json()
        data = json['results']['taxes'][0]['date']
        dolar = json['results']['currencies']['USD']['buy']
        euro = json['results']['currencies']['EUR']['buy']
        insert(data, dolar, euro)
    else:
        print('Falhou')