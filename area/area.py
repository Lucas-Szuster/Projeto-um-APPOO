from abc import ABC, abstractmethod
from evento.evento import Evento
from datetime import datetime, timedelta

class Area(ABC):
    def __init__(self, nome: str, qtd_pessoas: int, intervalo: timedelta):
        self.nome: str = nome
        self.qtd_pessoas: int = qtd_pessoas
        self.intervalo = intervalo
        self.lista_restricoes: list[str] = []
        self._lista_eventos: list[Evento] = []
        self._lista_de_itens: list[str] = []
    
    # ============
    # PROPRIEDADES
    # ============

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome:str):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome deve ser uma string")
        if not novo_nome.strip():
            raise ValueError("Entrada Invalida!")
        
        self.__nome = novo_nome
        
    @property
    def qtd_pessoas(self):
        return self.__qtd_pessoas
    
    @qtd_pessoas.setter
    def qtd_pessoas(self, nova_qtd: int):
        if not isinstance(nova_qtd, int):
            raise TypeError("O novo valor deve ser um int")
        if nova_qtd <= 0:
            raise ValueError("Valor invalido!")

        self.__qtd_pessoas = nova_qtd

    @property
    def lista_eventos(self):
        return self._lista_eventos
    
    @lista_eventos.setter
    def lista_eventos(self, nova_lista: list[Evento]):
        raise AttributeError('Não se pode alterar a lista de eventos')
    
    @property 
    def lista_de_itens(self):
        return self._lista_de_itens
    
    @lista_de_itens.setter
    def lista_de_itens(self, nova_lista: list[str]):
        raise AttributeError('Não se pode alterar a lista de itens da área')
    
    # =======
    # MÉTODOS
    # =======

    def adicionar_evento(self, novo_evento: Evento):
        if not isinstance(novo_evento, Evento):
            raise TypeError('O evento deve ser do tipo evento')
        
        for evento in self._lista_eventos:
            if (evento.data_e_horario == novo_evento.data_e_horario):
                raise AttributeError('eventos não podem ter o mesmo dia e hora')
            
            if (evento.data_e_horario.date() == novo_evento.data_e_horario.date()) and (novo_evento.data_e_horario <= (evento.data_e_horario + self.intervalo)):
                print(f'{novo_evento.data_e_horario} | {(evento.data_e_horario + self.intervalo)} | {novo_evento.data_e_horario >= (evento.data_e_horario + self.intervalo)}')
                raise AttributeError(f"Um evento só pode ser agendado quando outro acabar, o intervalo é {self.intervalo}")

        self._lista_eventos.append(novo_evento) 
        self._lista_eventos.sort(key=lambda o: o.data_e_horario)

    def remover_evento(self, evento):
        self._lista_eventos.remove(evento)

    # =================
    # MÉTODOS ABSTRATOS
    # =================

    @abstractmethod
    def adicionar_item_na_lista(self, item: str):
        pass

    @abstractmethod
    def remover_item_da_lista(self, item: str):
        pass

    @abstractmethod
    def to_dict(self):
        pass