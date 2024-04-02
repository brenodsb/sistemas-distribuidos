import requests
import sqlite3

conn = sqlite3.connect('bdcotacoes.db')
cursor = conn.cursor()

url = 'https://api.hgbrasil.com/finance?format=json-cors&key=21ae8ecf'

resposta = requests.get(url)

if resposta.status_code == 200:
    json = resposta.json()
    data = json['results']['taxes'][0]['date']
    dolar = json['results']['currencies']['USD']['buy']
    euro = json['results']['currencies']['EUR']['buy']

    try:
        sql = "INSERT INTO moedas (data, dolar, euro) VALUES (?, ?, ?)"
        cursor.execute(sql, (data, dolar, euro))
        conn.commit()
        print("Registro inserido com sucesso")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()
else:
    print('Falhou')