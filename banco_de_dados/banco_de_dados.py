import json

class BancoDeDados:
    def __init__(self):
        self.diretorio = 'banco_de_dados'
        self.nome_do_arquivo = 'banco_de_dados.json'

    def ler_dados(self):
        with open(f'{self.diretorio}/{self.nome_do_arquivo}', 'r', encoding='utf-8') as arq:
            try:
                json_puro = json.load(arq)
            except json.JSONDecodeError as e:
                json_puro = []

a = BancoDeDados()
a.ler_dados()