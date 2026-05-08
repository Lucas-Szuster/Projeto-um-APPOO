from abc import ABC, abstractmethod

class Area(ABC):
    def __init__(self, nome_area: str, qtd_maxima: int, lista_restricoes: list[str]):
        self.nome: str = nome_area
        self.qtd_pessoas: int = qtd_maxima
        self.restricoes: list[str] = lista_restricoes
        self.lista_eventos = []
    
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
    

a = Area('a', 12, ['restrição 1', 'restrição 2', 'restrição 3'])
try:
    a.restricoes = ['fds', 'fdsafds', '', 'hdfjsafjds']
except Exception as e:
    pass
print(a.restricoes)
    
        
    
