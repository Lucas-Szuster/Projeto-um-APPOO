from area.area import Area

class AreaEsportiva(Area):
    def __init__(self, nome: str, qtd_pessoas: int, lista_restricoes: list[str]):
        super().__init__(nome, qtd_pessoas, lista_restricoes)

    def adicionar_evento(self, eventoesportivo: Evento):
        

    def adicionar_restricao(self, evento)