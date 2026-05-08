from abc import ABC, abstractmethod
import datetime as dt

class Evento(ABC):
    def __init__(self,horario: dt.time, data: dt.date, qtd_participantes: int, restricoes_usuario: str, restricoes_evento: str):
        self.horario = horario
        self.data = data
        self.qtd_participantes = qtd_participantes
        self.restricoes_usuario = restricoes_usuario
        self.restricoes_evento = restricoes_evento

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


    @property
    def restricoes_usuario(self):
        return self.restricoes_usuario
    
    @restricoes_usuario.setter
    def restricoes_usuario(self, novas_restricoes_usuario: str):
        if not isinstance(novas_restricoes_usuario, str):
            raise TypeError('restricoes devem ser strings')
        
        self.restricoes_usuario = novas_restricoes_usuario

    @property
    def restricoes_eventos