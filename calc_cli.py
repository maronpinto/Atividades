import socket
import os

serverName = 'localhost'
serverPort = 2000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system('clear')
#print('                   CALCULADORA                        ')
#print('------------------------------------------------------')
#operacao = input(' Operacao - 1 Soma, 2 Raiz ou 0 Sair => ')
operacao = ""

out_oper = 0
while operacao != '0':
	
	if out_oper == '1':
		os.system('clear') 

	print('                   CALCULADORA                        ')
	print('------------------------------------------------------')
	operacao = input(' Operacao - 1 Soma, 2 Raiz ou 0 Sair => ')
	print('------------------------------------------------------\n')


	if operacao == '1':
		a = input(" Digite o parcela 1 => ")
		print('')
		b = input(" Digite o parcela 2 => ")
		message = "soma " + a + " " +  b + "\n"
		retorno = " A soma entre " + a + " e " + b + " e => "  


	elif operacao == "2":
		a = input(" Digite o Radicando ")
		message = "raiz " + a + "\n"
		retorno = " A raiz de " + a + " e => " 

	elif (operacao) == '0':
		message = "fim"
		break

	else:
		print(' Operacao invalida')


	if message != " ":
		byte_msg = message.encode('utf-8')
		clientSocket.sendto(byte_msg, (serverName, serverPort))

	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print('\n')
	print(retorno + modifiedMessage.decode('utf-8') + "\n")
	print('------------------------------------------------------')
	
	out_oper = input(" Fazer outro calculo ? 1 Sim ou 0 Nao => ")
	if out_oper == '0':
		os.system('clear')
		operacao = '0'
	else:
		os.system('clear')
	
clientSocket.close()
