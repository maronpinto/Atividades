import requests
import json
import os, getpass
os.system('clear')

print('                        API - SUAP                         ')
print('---------------------------------------------------------\n')
login = input(' Digite seu login => ')
senha = getpass.getpass(' Digite sua senha => ')

consulta = requests.post('https://suap.ifrn.edu.br/api/autenticacao/token/?format=json', json={'username':login, 'password':senha})
cons_json = json.loads(consulta.content.decode('utf-8'))
token = cons_json['token']
print(' Seu token => ' + token)