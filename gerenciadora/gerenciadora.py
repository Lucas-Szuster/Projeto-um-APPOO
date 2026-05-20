from area.area import Area
from evento.evento import Evento
from usuario.usuario import Usuario

class Gerenciadora:
    def __init__(self):
        self.__lista_areas: list[Area] = []
        self.__lista_usuarios: list[Usuario] = []

    # ============
    # PROPRIEDADES
    # ============

    @property
    def lista_areas(self):
        return (self.__lista_areas)
    
    @property
    def lista_usuarios(self):
        return (self.__lista_usuarios)

    # =======
    # MÉTODOS
    # =======

    def validar_usuario(self, nome_usuario: str, senha_usuario: str) -> bool:
        for usuario in self.lista_usuarios:
            if (usuario.nome == nome_usuario) and (usuario.senha == senha_usuario):
                return True
            
        return False
    
    def get_usuario_por_nome(self, nome_usuario: str) -> Usuario:
        lista_de_nomes_de_usuarios: list[str] = [usuario.nome for usuario in self.__lista_usuarios]
        if nome_usuario not in lista_de_nomes_de_usuarios:
            raise ValueError("Este usuário não existe")
        
        return (self.__lista_usuarios[lista_de_nomes_de_usuarios.index(nome_usuario)])
    
    def adicionar_usuario(self, novo_usuario: Usuario):
        if not isinstance(novo_usuario, Usuario):
            raise TypeError("O usuário deve ser do tipo Usuario")

        self.__lista_usuarios.append(novo_usuario)

    def buscar_usuario_por_nome(self, nome_usuario: str):
        lista_de_nomes_de_usuarios: list[str] = [usuario.nome for usuario in self.__lista_usuarios]
        if nome_usuario not in lista_de_nomes_de_usuarios:
            raise ValueError("Este usuário não existe")

        return self.__lista_usuarios[lista_de_nomes_de_usuarios.index(nome_usuario)]

    def adicionar_evento_em_usuario(self, nome_usuario: str, novo_evento: Evento):
        self.buscar_usuario_por_nome(nome_usuario).adicionar_evento(novo_evento)

    def remover_evento_em_usuario(self, nome_usuario: str, evento_a_ser_removido: Evento):
        self.buscar_usuario_por_nome(nome_usuario).remover_evento(evento_a_ser_removido)

    def adicionar_area(self, nova_area: Area):
        if not isinstance(nova_area, Area):
            raise TypeError("A área deve ser do tipo Area")

        self.__lista_areas.append(nova_area)

    def buscar_area_por_nome(self, nome_area) -> Area:
        lista_de_nomes_de_areas: list[str] = [area.nome for area in self.__lista_areas]
        if nome_area not in lista_de_nomes_de_areas:
            raise ValueError("Esta área não existe")
        
        return self.__lista_areas[lista_de_nomes_de_areas.index(nome_area)]

    def adicionar_evento_em_area(self, nome_area: str, novo_evento: Evento):
        self.buscar_area_por_nome(nome_area).adicionar_evento(novo_evento)

    def remover_evento_em_area(self, nome_area: str, evento_a_ser_removido: Evento):
        self.buscar_area_por_nome(nome_area).remover_evento(evento_a_ser_removido)

    def gerar_relatorio(self):
        pass