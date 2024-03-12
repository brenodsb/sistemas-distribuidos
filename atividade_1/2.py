import requests

url = 'https://viacep.com.br/ws/'
cep = 30140071
formato = '/xml/'

for i in range(cep, cep+5, 1):
    r = requests.get(url + str(i) + formato)

    if (r.status_code == 200):
        print()
        print('XML : ', r.text)
        print()
    else:
        print('Nao houve sucesso na requisicao.')