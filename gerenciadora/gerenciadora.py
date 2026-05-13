from area.area import Area
from evento.evento import Evento

class gerenciadora:
    def __init__(self):
        self.lista_areas = []

    def adicionar_area(self, nova_area: Area):
        self.lista_areas.append(nova_area)
        print(f"Area adicionada!")

    def adicionar_evento_em_area(self, nome_area: str, novo_evento: Evento):
        
        for area_unitaria in self.lista_areas:
            if area_unitaria.nome == nome_area:
                print(f"Evento adicionado!")
                ##chamar adicionar evento em area
                return
        
        print(f"Evento invalido!")
        return           

    def remover_evento_em_area(self, nome_area: str, evento_a_ser_removido: Evento):
        
        for area_unitaria in self.lista_areas:
            if area_unitaria.nome == nome_area:
                print(f"Evento removido!")
                ##chamar remover evento em area
        
            print(f"Evento invalido!")
            return
        
    def alterar_evento_em_area(self, nome_area : str,  evento_a_ser_alterado: Evento):
        
        for area_unitaria in self.lista_areas:
            if area_unitaria.nome == nome_area:
                print(f"Evento alterado!")
                ##chamar alterar evento em area
        
        print(f"Evento invalido!")
        return

    def gerar_relatorio(self):
        pass
        #implementar geracao de relatorio