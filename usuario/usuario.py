from evento.evento import Evento

from copy import deepcopy

class Usuario:
    def __init__(self, nome: str, idade: int, id: int, senha: str):
        self.nome = nome
        self.senha = senha
        self.__lista_de_eventos: list[Evento] = []

        if not isinstance(idade, int):
            raise TypeError("A idade deve ser um int")
        if idade <= 0:
            raise ValueError("A idade deve ser válida (maior que 0)")
        self.__idade = idade

        if not isinstance(id, int):
            raise TypeError("O id deve ser um número")
        self.__id = id

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
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha: str):
        if not isinstance(nova_senha, str):
            raise TypeError("A senha deve ser uma string")
        if not nova_senha.strip():
            raise ValueError("A senha não pode ser vazia")

        self.__senha = nova_senha

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

    def remover_evento(self, evento: Evento):
        if not isinstance(evento, Evento):
            raise TypeError("O evento deve ser do tipo evento")
        
        try:
            self.__lista_de_eventos.remove(evento)
        except Exception as e:
            raise e