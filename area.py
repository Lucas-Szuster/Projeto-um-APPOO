from abc import ABC, abstractmethod

class Area(ABC):
    def __init__(self, nome_area: str, qtd_maxima: int, lista_restricoes: list[str]):
        self.nome = nome_area
        self.qtd = qtd_maxima
        self.restricoes = lista_restricoes
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
        return self.nome_area
    
    def nome(self, novo_nome:str):
        if novo_nome.strip():
            self.nome_area = novo_nome()
        else:
            raise SyntaxError("Entrada Invalida!")
        
    @property
    def qtd_pessoas(self):
        return self.qtd_maxima
    
    def qtd_pessoas(self, nova_qtd: int):
        if nova_qtd > 0:
            self.qtd_maxima = nova_qtd
        else:
            raise ValueError("Valor invalido!")
        
    @property
    def restricoes(self):
        return self.lista_restricoes
    
    def restricoes(self, nova_lista_restricoes: list[str]):
        for restricao in nova_lista_restricoes:
            if not restricao.strip():
                raise SyntaxError("Restricao Invalida!")
            else:
                self.lista_restricoes = nova_lista_restricoes

    @property
    def eventos(self):
        return self.lista_eventos


    
        
    
