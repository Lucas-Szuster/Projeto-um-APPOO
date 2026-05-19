from evento.evento import Evento

from copy import deepcopy

class Usuario:
    def __init__(self, nome: str, idade: int, id: int):
        self.nome = nome
        self.__idade = idade
        self.__id = id
        self.__lista_de_eventos: list[Evento] = []

    # ============
    # PROPRIEDADES
    # ============ 

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome deve ser uma string")
        if not novo_nome.strip():
            raise ValueError("O nome não pode ser vazio")
        
        self.__nome = novo_nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        raise AttributeError("A idade não pode ser alterada")
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        raise AttributeError("O id não pode ser alterado")
    
    @property
    def lista_de_eventos(self):
        return deepcopy(self.__lista_de_eventos)
    
    @lista_de_eventos.setter
    def lista_de_eventos(self, nova_lista_de_eventos):
        raise AttributeError("A lista de eventos não pode ser alterada")
    
    # =======
    # MÉTODOS
    # =======

    def adicionar_evento(self, evento: Evento):
        if not isinstance(evento, Evento):
            raise TypeError("O evento deve ser do tipo evento")

        self.__lista_de_eventos.append(evento)

    