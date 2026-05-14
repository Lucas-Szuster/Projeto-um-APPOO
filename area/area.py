from abc import ABC, abstractmethod
from evento.evento import Evento
from copy import deepcopy

class Area(ABC):
    def __init__(self, nome: str, qtd_pessoas: int):
        self.nome: str = nome
        self.qtd_pessoas: int = qtd_pessoas
        self.lista_restricoes: list[str] = []
        self._lista_eventos: list[Evento] = []
    
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
        return deepcopy(self._lista_eventos)
    
    @lista_eventos.setter
    def lista_eventos(self, nova_lista: list[Evento]):
        raise AttributeError('Não se pode alterar a lista de eventos')
    
    # =======
    # MÉTODOS
    # =======

    @abstractmethod
    def adicionar_evento(self, evento):
        pass

    @abstractmethod
    def remover_evento(self, evento):
        pass