# main() será executado quando você chamar essa ação
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
# @return A saída dessa ação, que deve ser um objeto JSON.
#
import requests
import json

def main(params):
    #cep = dict['cep']
    cep = '06852530'
    url= f'https://viacep.com.br/ws/{cep}/json/'
    conteudo=requests.get(url)
    return {'body': {'result': json.loads(conteudo.text)}}
