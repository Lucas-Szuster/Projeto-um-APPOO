from area.area import Area
from evento.evento import Evento

class gerenciadora:
    def __init__(self):
        self.lista_areas = []

    def adicionar_area(self, nova_area: Area):
        self.lista_areas.append(nova_area)
        print(f"Area adicionada!")

    def adicionar_evento_em_area(self, nome_area: str, novo_evento: Evento):
        achado: bool = False
        
        for area_unitaria in self.lista_areas:
            if area_unitaria.nome == nome_area:
                achado = True
                ##chamar adicionar evento em area
        
        if achado == False:
             print(f"Evento invalido!")
        else:
             print(f"Evento adicionado!")
            

    def remover_evento_em_area(self, nome_area: str, evento_a_ser_removido: Evento):
        achado: bool = False
        
        for area_unitaria in self.lista_areas:
            if area_unitaria.nome == nome_area:
                achado = True
                ##chamar remover evento em area
        
        if achado == False:
            print(f"Evento invalido!")
        else:
            print(f"Evento removido!")
        
    def alterar_evento_em_area(self, nome_area : str,  evento_a_ser_alterado: Evento):
        achado: bool = False
        
        for area_unitaria in self.lista_areas:
            if area_unitaria.nome == nome_area:
                achado = True
                ##chamar alterar evento em area
        
        if achado == False:
            print(f"Evento invalido!")
        else:
            print(f"Evento alterado!")

    def gerar_relatorio(self):
        pass
        #implementar geracao de relatorio