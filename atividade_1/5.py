import requests
import io

r = requests.get('http://www.google.com/search', params={'q': 'Jesus Cristo'})

if (r.status_code == 200):
    with io.open('atividade_1/pagina.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
else:
    print('Nao houve sucesso na requisicao.')