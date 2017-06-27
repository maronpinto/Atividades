import os, socket
host = '127.0.0.1'
port = 5000

conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (host, port)
conexao.bind(origem)
conexao.listen(1)

os.system('clear')
print("Servidor Pronto")

while True:
	conec, cliente = conexao.accept()
	print('Conectado por ', cliente)
	while True:
		msg = conec.recv(1024)

		if not msg: break
		
		print(cliente, msg)
		print('Recebido => ' + msg.decode())
		
		mensagem = "Retornado => " + msg.decode()
		print(mensagem)

		conec.sendto(mensagem.encode('utf-8'), cliente)

	print("finalizando conexao do cliente ", origem)


	conec.close()

