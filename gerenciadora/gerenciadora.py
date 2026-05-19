from area.area import Area
from evento.evento import Evento
from usuario.usuario import Usuario

from copy import deepcopy

class gerenciadora:
    def __init__(self):
        self.lista_areas: list[Area] = []

    def adicionar_area(self, nova_area: Area):
        self.lista_areas.append(nova_area)

    def buscar_area_por_nome(self, nome_area):
        lista_de_nomes_de_areas: list[str] = [area.nome for area in self.lista_areas]
        if nome_area not in lista_de_nomes_de_areas:
            raise ValueError("Esta área não existe")
        
        return self.lista_areas[lista_de_nomes_de_areas.index(nome_area)]

    def adicionar_evento_em_area(self, nome_area: str, novo_evento: Evento):
        self.buscar_area_por_nome(nome_area).adicionar_evento(novo_evento)

    def remover_evento_em_area(self, nome_area: str, evento_a_ser_removido: Evento):
        self.buscar_area_por_nome(nome_area).remover_evento(evento_a_ser_removido)

    def gerar_relatorio(self):
        pass