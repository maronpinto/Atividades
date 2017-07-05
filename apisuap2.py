from urllib.request import Request, urlopen
import json, os, requests, getpass

os.system('clear')

def tela_menu(menu, msg):
	os.system('clear')
	print('\n')
	msg_menu = "                  API DE DADOS DO SUAP - " + menu + "              "
	print(msg_menu)
	print('-----------------------------------------------------------------')
	print(msg)
	print('-----------------------------------------------------------------')


def cons_login(login, senha):
	consulta = requests.post('https://suap.ifrn.edu.br/api/autenticacao/token/?format=json', json={'username':login, 'password':senha})
	cons_json = json.loads(consulta.content.decode('utf-8'))
	token = cons_json['token']
	return token

def cons_dados(mat, tok, aut):
	dados = Request('https://suap.ifrn.edu.br/api/v2/edu/aluno/{}/'.format(mat))
	dados.add_header('Accept', 'application/json')
	dados.add_header('X-CSRFToken', tok)
	dados.add_header('Autorization', aut)

	dados_byte = urlopen(dados).read()
	dados_txt = dados_byte.decode('utf-8')
	print(dados_txt)

	

	#dados = requests.get('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format('20132014050351'))
	#dados_json = json.loads(dados.content.decode('utf-8'))
	#print(dados_json)
	return dados_byte


tela_menu('MENU', 'teste')
opcao = ''

while opcao != '\x18':
	opcoes = ('|  1-Login  |  2-Dados   |   3-Notas   |   0-Sair             |')
	tela_menu('MENU', opcoes)

	
	if opcao == '1':
		tela_menu('LOGIN', 'Fazer Login  -  ESC para voltar')

		login = ''
		while login == '':
			login = 20132014050351#input(' Degite sua matricula => ')
			senha = 'Qwqw123'#getpass.getpass(' Digite sua senha =>')
			

			MATRICULA = 20132014050351
			TOKEN = 'Hq02aACXwizVEwQ8YlHdptbemmQ6tyFg5JivjRYQe5eJntpAr6vqP14uePOWNcRq'
			AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='

			token = cons_login(login, senha)
			print(' Seu token e ' + token)
			retorno = cons_dados(MATRICULA, TOKEN, AUTHORIZATION)
			print(retorno)
		opcao = ''

	elif opcao == '2':

		tela_menu('DADOS', 'Consultar dados do aluno  - ESC para voltar ')
		opcao = '' 

	elif opcao == '3':
		tela_menu('NOTAS', 'Consultar notas do aluno  - ESC para voltar ')
		opcao = '' 

	elif opcao == '0':
		print('Opcao 0 - Sair')
		opcao = '\x18'
		print(opcao)
	else:
		opcao = ''

	if opcao == "":
		opcao = input(' Digite Opcao = > ')
	