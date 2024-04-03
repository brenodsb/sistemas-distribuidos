import json
import requests

dado = {'idproduto': 1,
        'descricao':'agua mineral com gas',
        'ganhopercentual': 0.20}

dado_json = json.dumps(dado)

url = 'http://127.0.0.1:5000/api-loja/alterar'

r = requests.put(url, data=dado_json, headers={'Content-Type': 'application/json'})

print(r.text)