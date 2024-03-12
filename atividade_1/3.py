import requests

url = 'https://viacep.com.br/ws'
estado = 'MG'
cidade = 'Belo Horizonte'
rua = 'Braulio Gomes Nogueira'
formato = '/json/'

r = requests.get(url + '/' + estado + '/' + cidade + '/' + rua + formato)

if (r.status_code == 200):
    print()
    print('Json : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')
