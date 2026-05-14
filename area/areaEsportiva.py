from area.area import Area
from evento.evento import Evento
from datetime import time

# ======================
# IMPORTANTE: Como lista_eventos é um atributo interno que NÃO queremos chamar o getter (pois ele retorna uma cópia),
# deve-se utilizar o nome real do atributo, _lista_eventos.
# ======================

class AreaEsportiva(Area):
    def __init__(self, nome: str, qtd_pessoas: int, lista_restricoes: list[str]):
        super().__init__(nome, qtd_pessoas, lista_restricoes)

    def adicionar_evento(self, eventoesportivo: Evento):
        if not isinstance(eventoesportivo, Evento):
            raise TypeError('O evento deve ser do tipo evento')
        
        for evento in self._lista_eventos:
            if (evento.data_e_horario == eventoesportivo.data_e_horario):
                raise AttributeError('eventos não podem ter o mesmo dia e hora')

        self._lista_eventos.append(eventoesportivo) 
        self._lista_eventos.sort(key=lambda o: o.data_e_horario)

    def remover_evento(self, evento):
        # =================
        # IDEIA BÁSICA: PODE-SE ALTERAR MUITO
        # ================

        self._lista_eventos.remove(evento)