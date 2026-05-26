import json
from datetime import datetime

from gerenciadora.gerenciadora import Gerenciadora
from usuario.usuario import Usuario
from evento.evento import Evento
from area.area import Area
from area.areaEsportiva import AreaEsportiva
from area.areaSocial import AreaSocial

class BancoDeDados:
    def __init__(self):
        self.enconding = "utf-8"
        self.diretorio = "bancoDeDados"
        self.arquivo_usuarios = "banco_de_usuarios.json"
        self.arquivo_areas = "banco_de_areas.json"

    # LER DADOS

    def ler_arquivo_json(self, diretorio: str, nome_do_arquivo: str):
        with open(f'{diretorio}/{nome_do_arquivo}', 'r', encoding=self.enconding) as arq:
            try:
                json_puro = json.load(arq)
            except json.JSONDecodeError as e:
                json_puro = []

        return json_puro 

    def formatar_data_e_horario(self, dict_data_e_horario):
        return datetime(
            year=dict_data_e_horario["year"],
            month=dict_data_e_horario["month"],
            day=dict_data_e_horario["day"],
            hour=dict_data_e_horario["hour"],
            minute=dict_data_e_horario["minute"],
            second=dict_data_e_horario["second"]
        )

    def criar_evento(self, dict_evento: dict):
        return Evento(
            nome_evento=dict_evento["nome_evento"],
            qtd_participantes=dict_evento["qtd_participantes"],
            data_e_horario=self.formatar_data_e_horario(dict_evento["data_e_horario"])
        )

    def ler_dados_usuarios(self, gerenciadora: Gerenciadora):
        for dict_usuario in self.ler_arquivo_json(self.diretorio, self.arquivo_usuarios):
            novo_usuario = Usuario(
                nome=dict_usuario["nome"],
                idade=dict_usuario["idade"],
                id=dict_usuario["id"],
                senha=dict_usuario["senha"],
                is_adm=dict_usuario["is_adm"]
            )

            for dict_evento in dict_usuario["lista_de_eventos"]:
                novo_evento = self.criar_evento(dict_evento)
                novo_usuario.adicionar_evento(novo_evento)

            gerenciadora.adicionar_usuario(novo_usuario)

    def criar_area(self, dict_area: dict):
        match (dict_area["tipo"]):
            case "AreaEsportiva":
                return AreaEsportiva(
                    nome=dict_area["nome"],
                    qtd_pessoas=dict_area["qtd_pessoas"],
                    esporte_praticado=dict_area["esporte_praticado"],
                    sistema_de_iluminacao=dict_area["sistema_de_iluminacao"]
                )
            case "AreaSocial":
                return AreaSocial(
                    nome=dict_area["nome"],
                    qtd_pessoas=dict_area["qtd_pessoas"],
                    area_espaco=dict_area["area_espaco"],
                    sistema_de_som=dict_area["sistema_de_som"]
                )
            case _:
                return None

    def ler_dados_areas(self, gerenciadora: Gerenciadora):
        for dict_area in self.ler_arquivo_json(self.diretorio, self.arquivo_areas):
            nova_area = self.criar_area(dict_area)

            for dict_evento in dict_area["lista_eventos"]:
                novo_evento = self.criar_evento(dict_evento)
                nova_area.adicionar_evento(novo_evento)

            for item in dict_area["lista_de_itens"]:
                nova_area.adicionar_item_na_lista(item)

            for restricao in dict_area["lista_restricoes"]:
                nova_area.adicionar_restricao_area(restricao)

            gerenciadora.adicionar_area(nova_area)

    def ler_dados(self, gerenciadora: Gerenciadora):
        self.ler_dados_usuarios(gerenciadora)
        self.ler_dados_areas(gerenciadora)

    # SALVAR DADOS

    def salvar_dados_usuarios(self, gerenciadora: Gerenciadora):
        lista_de_dicts_usuarios: list[dict] = [usuario.to_dict() for usuario in gerenciadora.lista_usuarios]
        with open(f'{self.diretorio}/{self.arquivo_usuarios}', 'w', encoding=self.enconding) as arq:
            json.dump(lista_de_dicts_usuarios, arq, indent=4)

    def salvar_dados_areas(self, gerenciadora: Gerenciadora):
        lista_de_dicts_areas: list[dict] = [area.to_dict() for area in gerenciadora.lista_areas]
        with open(f'{self.diretorio}/{self.arquivo_areas}', 'w', encoding=self.enconding) as arq:
            json.dump(lista_de_dicts_areas, arq, indent=4)

    def salvar_dados(self, gerenciadora: Gerenciadora):
        self.salvar_dados_usuarios(gerenciadora)
        self.salvar_dados_areas(gerenciadora)