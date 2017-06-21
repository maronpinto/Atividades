import socket
import os

serverHost = 'localhost'
serverPort = 2000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))
os.system('clear')
print("Servidor pronto para receber: ")


soma = 0
while True:

	message, clientAddress = serverSocket.recvfrom(2048)
	print('Conexão de: ', clientAddress)
    #Processa a stringe para lestras maiusculas

	mens = message.decode('utf-8')

	operacao = mens.split()
	print(operacao)
	print(operacao[1])
	if operacao[0] == 'soma':
		soma = int(operacao[1]) + int(operacao[2])
	print(soma)

	serverSocket.sendto(message, clientAddress)
