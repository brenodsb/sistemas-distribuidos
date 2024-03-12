import requests

url = 'https://viacep.com.br/abc/'

r = requests.get(url)

if (r.status_code == 200):
    print()
    print('XML : ', r.text)
    print()
else:
    print(r.headers)
    print('Nao houve sucesso na requisicao. Codigo:', r.status_code)