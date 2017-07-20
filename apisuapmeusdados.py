#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
O token/ficha e a autorização devem ser obtidos, separadamente, em
    https://suap.ifrn.edu.br/api/docs/
    
No canto superior direito há os botões:
* Django login (necessário para o token);
* e Authorize (necessário para obter a autorização).
'''

from urllib.request import Request, urlopen
import json

MATRICULA = '20132014050351'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjIwMTMyMDE0MDUwMzUxIiwib3JpZ19pYXQiOjE1MDA0MDY5NTAsInVzZXJfaWQiOjUxOTU0LCJlbWFpbCI6Im1hcm9uLnRlcnR1bGlub0BhY2FkZW1pY28uaWZybi5lZHUuYnIiLCJleHAiOjE1MDA0OTMzNTB9.WSbs7iJ13lFsZFSC148iQqkFzJBYkNEy-35KMxwT7w8'
AUTHORIZATION = 'Basic MjAxMzIwMTQwNTAzNTE6UXdxdzEyMw=='

req = Request('https://suap.ifrn.edu.br/api/v2/ae/bolsas/?limit=100&offset=100')
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_txt = dados_byte.decode('utf-8')
dados_json = json.loads(dados_txt)

#for item in range(0,len(dados_json)):
	#print(dados_json['results'][item]['aluno'])
print(json.dumps(dados_json, indent=4))