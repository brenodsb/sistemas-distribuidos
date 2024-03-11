import requests

url = 'https://viacep.com.br/ws/'
formato = '/xml/'

# Lista de CEPs sequenciais
ceps = ['30140071', '30140072', '30140073', '30140074', '30140075']

for cep in ceps:
    r = requests.get(url + cep + formato)
    if (r.status_code == 200):
        print(f'CEP: {cep}')
        print('XML : ', r.text)
        print()
    else:
        print(f'Nao houve sucesso na requisicao do CEP {cep}.')
