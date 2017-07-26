from urllib.request import Request, urlopen
import json, os, requests, getpass
import time

os.system('clear')
MATRICULA = ''
token = ''
AUTHORIZATION = ''
ativ_log = ''

def reg_log(ativ):
	hoje = '%s' % (time.strftime('%Y_%m_%d'))
	arq_log = open('log_atividades.json', 'a')

	hora = time.strftime('%H:%M:%S %Z')
	

	list_grava_log = [dict(hora=hora, atividade=ativ)]
	dict_grava_log = {'log':list_grava_log}

	arq_log.write(json.dumps(dict_grava_log, indent=4))


def tela_menu(menu, msg):
	os.system('clear')
	print('\n')
	print('                    API DE DADOS DO SUAP                         ')
	print('-----------------------------------------------------------------')
	print('|   1-Placa   |  2-Dados    |   3-Bolsa    |   0-Sair           |')
	print('-----------------------------------------------------------------')
	print(msg)
	print('-----------------------------------------------------------------')

def gravar(reg):
		
		#print(arq_dict['placa'][0]['numplaca'])

		arq = open('arq_placa.json', 'a')
		arq.write(json.dumps(reg, indent=4))
		arq.close()
		print('')
		print('Gravado')



def placa(mat):
	print()


def cons_dados(mat, tok, aut):
	
	dados = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(mat))
	dados.add_header('Accept', 'application/json')
	dados.add_header('X-CSRFToken', tok)
	dados.add_header('Authorization', aut)

	dados_byte = urlopen(dados).read()
	dados_json = json.loads(dados_byte.decode('utf-8'))

	return dados_json



def bolsa(mat, tok, aut):
	
	dados_bolsa = Request('https://suap.ifrn.edu.br/api/v2/ae/bolsas/?limit=200&offset=100')
	dados_bolsa.add_header('Accept', 'application/json')
	dados_bolsa.add_header('X-CSRFToken', tok)
	dados_bolsa.add_header('Authorization', aut)

	dados_byte = urlopen(dados_bolsa).read()
	dados_txt = dados_byte.decode('utf-8')
	dados_json = json.loads(dados_txt)
	
	return dados_json


def bolsa_id(num_id, tok, aut):
	
	dados_bolsa_id = Request('https://suap.ifrn.edu.br/api/v2/ae/bolsas/{}/'.format(num_id))
	dados_bolsa_id.add_header('Accept', 'application/json')
	dados_bolsa_id.add_header('X-CSRFToken', tok)
	dados_bolsa_id.add_header('Authorization', aut)

	dados_byte_id = urlopen(dados_bolsa_id).read()
	dados_txt_id = dados_byte_id.decode('utf-8')
	
	return dados_txt_id


tela_menu('MENU', 'teste')
opcao = ''

ativ_log = 'Sistema iniciado'
reg_log(ativ_log)

while opcao != '\x18':
	
	tela_menu('MENU', '')



	if opcao == '1':

		ativ_log = 'Cadastra placa'
		reg_log(ativ_log)	

		tela_menu(' PLACA', 'Cadastrar placa')

		TOKEN = 'XRlPjOId7WLsW8HoGeQ60witnjd7dIw5bBZT7dmna0NTr4kuR1IbhAwLu97rfqUo'
		AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='
		matricula = input(' Matricula=> ')
		num_placa = input(' Placa=> ')
		dados = cons_dados(matricula, token, AUTHORIZATION)
		print()
		print('Matricula=> %s' % (dados['matricula']))
		print('Nome=>      %s' % (dados['nome']))
		print('Situacao=>  %s' % (dados['situacao']))
		print('Campos=>    %s' % (dados['campus']))
		print()

		
		lista_gravar = [dict(matricula=dados['matricula'], nome=dados['nome'], situacao=dados['situacao'], campus=dados['campus'], numplaca=num_placa)]
		dict_gravar = {'placa':lista_gravar}


		#print(json.dumps(dict_gravar))
		gravar(dict_gravar)
		opcao = ''




	elif opcao == '2':

		ativ_log = 'Consultar dados do aluno'
		reg_log(ativ_log)

		#MATRICULA = '20132014050351'
		TOKEN = 'XRlPjOId7WLsW8HoGeQ60witnjd7dIw5bBZT7dmna0NTr4kuR1IbhAwLu97rfqUo'
		AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='
		
		tela_menu('DADOS', 'Consultar dados do aluno  - ESC para voltar ')
		MATRIC_PESQUISA = input('Matricula => ')
		retorno = cons_dados(MATRIC_PESQUISA, token, AUTHORIZATION)
		print(json.dumps(retorno, indent=4))

		opcao = '' 




	elif opcao == '3':

		ativ_log = 'Consultar aluno bolsista'
		reg_log(ativ_log)

		num_id = input(' Digite o ID=> ')

		AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='
		tela_menu('BOLSAS', 'Consultar aluno com bolsa')
		retorno = bolsa_id(num_id, token, AUTHORIZATION)
		bolsista = json.loads(retorno)

		
		print(json.dumps(bolsista, indent=4))
		#print(json.dumps(retorno, indent=4))

		opcao = '' 

	elif opcao == '0':
		ativ_log = 'Sair do programa'
		reg_log(ativ_log)

		print('Opcao 0 - Sair')
		opcao = '\x18'
		print(opcao)
	else:
		opcao = ''

	if opcao == "":
		opcao = input(' Digite Opcao = > ')
	