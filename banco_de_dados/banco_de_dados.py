import json

from gerenciadora.gerenciadora import Gerenciadora

class BancoDeDados:
    def __init__(self):
        self.enconding = "utf-8"
        self.diretorio = "banco_de_dados"
        self.nome_do_arquivo = "banco_de_dados.json"

    def ler_dados(self):
        with open(f'{self.diretorio}/{self.nome_do_arquivo}', 'r', encoding=self.enconding) as arq:
            try:
                json_puro = json.load(arq)
            except json.JSONDecodeError as e:
                json_puro = []

    def salvar_dados_usuarios(self, gerenciadora: Gerenciadora):
        lista_de_dicts_usuarios: list[dict] = [usuario.to_dict() for usuario in gerenciadora.lista_usuarios]

        print(lista_de_dicts_usuarios)

        with open(f'{self.diretorio}/{self.nome_do_arquivo}', 'w', encoding=self.enconding) as arq:
            json.dump(lista_de_dicts_usuarios, arq, indent=4)

    def salvar_dados(self, gerenciadora: Gerenciadora):
        self.salvar_dados_usuarios(gerenciadora)

a = BancoDeDados()
a.ler_dados()