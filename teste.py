#!/usr/bin/ pyhton3

import argparse, socket
from datetime import datetime

MAX_BYTE = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Ouvindo na {} '.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTE)
        texto = data.decode('ascii')
        print('O cliente em {} disse {!r}'.format(address, texto))
        texto = 'Voce enviou {}'.format(len(data))
        data = texto.encode('ascii')
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DEGRAM)
    testo = 'Tempo: {}'.format(datetime.now())
    data = texto.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('O sistema operacional designou o ip {}'.format(sock.getsockname()))
    data, address = sock.recvform(MAX_BYTE)
    texto = data.decode('ascii')
    print('O servidor {} respondeu {!r}'.format(address, texto))




if __name__ == '__main__':
    choices ={'client': client, 'server':server}
    parser = argparse.ArgumentParser(description='Envia e recebe UDP localmente')
    parser.add_argument('funcao', choices=choices)
    help = 'Escolha se o script e: client ou server'
    parser.add_argument('-p', metavar = 'PORT', type = int, default = 1060, help = 'Porta UDP (porta padrao 1060)')
    args = parser.parse_args()
    function = choices[args.funcao]
    function(args.p)
