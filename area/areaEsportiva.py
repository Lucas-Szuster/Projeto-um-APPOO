from area.area import Area
from evento.evento import Evento
from datetime import time

class AreaEsportiva(Area):
    def __init__(self, nome: str, qtd_pessoas: int, lista_restricoes: list[str]):
        super().__init__(nome, qtd_pessoas, lista_restricoes)

    def adicionar_evento(self, eventoesportivo: Evento):
        if not isinstance(eventoesportivo, Evento):
            raise TypeError('O evento deve ser do tipo evento')
        
        for evento in self.lista_eventos:
            if (evento.horario == eventoesportivo.horario) and (evento.data == eventoesportivo.data):
                raise AttributeError('eventos não podem ter o mesmo dia e hora')

        self.lista_eventos.append(eventoesportivo) 
        