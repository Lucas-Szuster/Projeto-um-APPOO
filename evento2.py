from abc import ABC, abstractmethod
import datetime as dt

class Evento(ABC):
    def __init__(self, nome_evento: str, horario: dt.time, data: dt.date, qtd_participantes: int):
        self.nome_evento = nome_evento
        self.horario = horario
        self.data = data
        self.qtd_participantes = qtd_participantes
        self.restricoes = []


    @abstractmethod
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



class EventoTeste(Evento):
    def __init__(self,nome_evento: str, horario: dt.time, data: dt.date, qtd_participantes: int):
        super().__init__(nome_evento, horario, data, qtd_participantes)

    def adicionar_restricao(self, restricao: str):
        if not restricao.strip():
            raise ValueError("Restricao invalida")
        
        self.restricoes.append(restricao)

class EventoTeste2(Evento):
    def __init__(self,nome_evento: str, horario: dt.time, data: dt.date, qtd_participantes: int):
        super().__init__(nome_evento, horario, data, qtd_participantes)

    def adicionar_restricao(self, restricao: str):
        if not restricao.strip:
            raise ValueError("Restricao invalida")
        
        self.restricoes.append(restricao)


print("Antes de EventoTeste 2")
evento1 = EventoTeste("aniversario", dt.time(16,0,0),dt.date(2026, 3, 21), 4)
evento1.adicionar_restricao("Proibido fumar")

print(f"Print somente evento 1: {evento1.nome_evento}, {evento1.qtd_participantes}, {evento1.restricoes}")

evento2 = EventoTeste("Parabens",  dt.time(17,0,0),dt.date(2028, 5, 23), 10)

evento2.adicionar_restricao("Proibido Pular")

print(f"Print evento 2: {evento2.nome_evento}, {evento2.qtd_participantes}, {evento2.restricoes}")
print(f"Print evento 1 novamente: {evento1.nome_evento}, {evento1.qtd_participantes}, {evento1.restricoes}")

print("Depois de Evento Teste 2")

evento3 = EventoTeste2("sinuca", dt.time(18,0,0),dt.date(2023, 3, 20), 4)

evento3.adicionar_restricao("Proibido nadar")

print(f"Print evento 3: {evento3.nome_evento}, {evento3.qtd_participantes}, {evento3.restricoes}")
print(f"Print evento 1 novamente: {evento1.nome_evento}, {evento1.qtd_participantes}, {evento1.restricoes}")


