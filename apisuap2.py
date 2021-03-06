from urllib.request import Request, urlopen
import json, os, requests, getpass

os.system('clear')

token = ''

def tela_menu(menu, msg):
	os.system('clear')
	print('\n')
	print('                    API DE DADOS DO SUAP                         ')
	print('-----------------------------------------------------------------')
	print('|   1-Login   |  2-Dados    |   3-Notas    |   0-Sair           |')
	print('-----------------------------------------------------------------')
	print(msg)
	print('-----------------------------------------------------------------')


def cons_login(login, senha):
	consulta = requests.post('https://suap.ifrn.edu.br/api/autenticacao/token/?format=json', json={'username':login, 'password':senha})
	cons_json = json.loads(consulta.content.decode('utf-8'))
	token = cons_json['token']
	return token

def cons_dados(mat, tok, aut):
	
	dados = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(mat))
	dados.add_header('Accept', 'application/json')
	dados.add_header('X-CSRFToken', tok)
	dados.add_header('Authorization', aut)

	dados_byte = urlopen(dados).read()
	#dados_txt = dados_byte.decode('utf-8')
	dados_json = json.loads(dados_byte.decode('utf-8'))
	return dados_json



def bolsa(mat, tok, aut):
	
	dados_bolsa = Request('https://suap.ifrn.edu.br/api/v2/{}/'.format('bolsa'))
	dados_bolsa.add_header('Accept', 'application/json')
	dados_bolsa.add_header('X-CSRFToken', tok)
	dados_bolsa.add_header('Authorization', aut)

	dados_byte = urlopen(dados_bolsa).read()
	#dados_txt = dados_byte.decode('utf-8')
	dados_json = json.loads(dados_byte.decode('utf-8'))
	return dados_json


tela_menu('MENU', 'teste')
opcao = ''

while opcao != '\x18':
	
	tela_menu('MENU', '')

	
	if opcao == '1':
		tela_menu('LOGIN', 'Fazer Login  -  ESC para voltar')

		login = ''
		while login == '':
			login = 20132014050351#input(' Degite sua matricula => ')
			senha = 'Qwqw123'#getpass.getpass(' Digite sua senha =>')

			MATRICULA = 20132014050351
			#token = 'XRlPjOId7WLsW8HoGeQ60witnjd7dIw5bBZT7dmna0NTr4kuR1IbhAwLu97rfqUo'
			AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='

			token = cons_login(login, senha)
			print(' Seu token e: ' + token)
		opcao = ''

	elif opcao == '2':
		MATRICULA = '20132014050351'
		#TOKEN = 'XRlPjOId7WLsW8HoGeQ60witnjd7dIw5bBZT7dmna0NTr4kuR1IbhAwLu97rfqUo'
		AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='
		
		tela_menu('DADOS', 'Consultar dados do aluno  - ESC para voltar ')
		retorno = cons_dados(MATRICULA, token, AUTHORIZATION)
		print(json.dumps(retorno, indent=4))

		opcao = '' 




	elif opcao == '3':
		MATRICULA = '20132014050351'
		#TOKEN = 'XRlPjOId7WLsW8HoGeQ60witnjd7dIw5bBZT7dmna0NTr4kuR1IbhAwLu97rfqUo'
		AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='
		tela_menu('BOLSAS', 'Consultar aluno com bolsa')
		retorno = bolsa(MATRICULA, token, AUTHORIZATION)
		#print(json.dumps(retorno, indent=4))

		opcao = '' 

	elif opcao == '0':
		
		print('Opcao 0 - Sair')
		opcao = '\x18'
		print(opcao)
	else:
		opcao = ''

	if opcao == "":
		opcao = input(' Digite Opcao = > ')
	