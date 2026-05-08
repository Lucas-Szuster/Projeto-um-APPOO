from abc import ABC, abstractmethod
import datetime as dt

class Evento(ABC):
    def __init__(self,nome_evento: str, horario: dt.time, data: dt.date, qtd_participantes: int):
        self.horario = horario
        self.data = data
        self.qtd_participantes = qtd_participantes
        self.restricoes = [str]


    @abstractmethod
    def adicionar_restricao(self):
        pass
    
    @property
    def horario(self):
       return self.horario

    @horario.setter
    def horario(self, novo_horario: dt.time):
        if not isinstance(novo_horario, dt.time):
            raise TypeError('horario deve estar no formato de tempo')
            
        self.horario = novo_horario

    @property
    def data(self):
        return self.data
    
    @data.setter
    def data(self, nova_data: dt.date):
        if not isinstance(nova_data, dt.date):
            raise TypeError('data deve estar no formato de tempo')
        
        self.data = nova_data


    @property
    def qtd_participantes(self):
        return self.qtd_participantes
    
    @qtd_participantes.setter
    def qtd_participantes(self, qtd_atualizada: int):
        if qtd_atualizada <= 0:
            raise ValueError('quantidade de participantes nao pode ser negativa ou nula')
        
        self.qtd_participantes = qtd_atualizada



class EventoTeste(Evento):
    def __init__(self,horario: dt.time, data: dt.date, qtd_participantes: int):
        super().__init__(horario, data, qtd_participantes)

    def adicionar_restricao(self, restricao: str):
        if not restricao.strip:
            raise ValueError("Restricao invalida")
        
        self.restricoes.append(restricao)

evento1 = EventoTeste(20, 21, 4)
evento1.adicionar_restricao("Proibido fumar")
        
