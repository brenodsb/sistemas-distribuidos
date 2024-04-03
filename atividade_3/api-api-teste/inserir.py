import json
import requests

dado = {'descricao':'teste',
        'ganhopercentual': 1.0}

dado_json = json.dumps(dado)

url = 'http://127.0.0.1:5000/api-loja/inserir'

r = requests.post(url, data=dado_json, headers={'Content-Type': 'application/json'})

print(r.text)