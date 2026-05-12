from abc import ABC, abstractmethod
from evento.evento import Evento

class Area(ABC):
    def __init__(self, nome: str, qtd_pessoas: int, lista_restricoes: list[str]):
        self.nome: str = nome
        self.qtd_pessoas: int = qtd_pessoas
        self.lista_restricoes: list[str] = lista_restricoes
        self.lista_eventos: list[Evento] = []
    
    #Metodos associados a area

    ##adiciona evento
    @abstractmethod
    def adicionar_evento(self, evento):
        pass

    ##remove evento
    @abstractmethod
    def remover_evento(self, evento):
        pass
    
    #Getters e Setters
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