from abc import ABC, abstractmethod
import datetime as dt

class Evento:
    def __init__(self, nome_evento: str, horario: dt.time, data: dt.date, qtd_participantes: int):
        self.nome_evento = nome_evento
        self.horario = horario
        self.data = data
        self.qtd_participantes = qtd_participantes
        self.restricoes = []


    def adicionar_restricao(self, restricao: str):
        pass

    @property
    def nome_evento(self):
        return self.__nome_evento
    
    @nome_evento.setter
    def nome_evento(self, novo_nome: str):
        if not isinstance(novo_nome, str):
            raise TypeError("Tipo de nome Inálido!")

        if not novo_nome.strip():
            raise ValueError("Nome inválido")

        self.__nome_evento = novo_nome        
    
    @property
    def horario(self):
       return self.__horario

    @horario.setter
    def horario(self, novo_horario: dt.time):
        if not isinstance(novo_horario, dt.time):
            raise TypeError('horario deve estar no formato de tempo')
            
        self.__horario = novo_horario

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data: dt.date):
        if not isinstance(nova_data, dt.date):
            raise TypeError('data deve estar no formato de tempo')
        
        self.__data = nova_data


    @property
    def qtd_participantes(self):
        return self.__qtd_participantes
    
    @qtd_participantes.setter
    def qtd_participantes(self, qtd_atualizada: int):
        if qtd_atualizada <= 0:
            raise ValueError('quantidade de participantes nao pode ser negativa ou nula')
        
        self.__qtd_participantes = qtd_atualizada