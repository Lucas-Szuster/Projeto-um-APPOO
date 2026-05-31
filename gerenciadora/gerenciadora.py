from area.area import Area
from evento.evento import Evento
from usuario.usuario import Usuario
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from area.areaEsportiva import AreaEsportiva
from area.areaSocial import AreaSocial


class Gerenciadora:

    NOVO_ID = 1

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

    def adicionar_restricao_area(self, area: Area, restricao: str):
        self.buscar_area_por_nome(area.nome).adicionar_restricao(restricao)  

    def remover_restricao_area(self, area: Area, restricao: str):
        self.buscar_area_por_nome(area.nome).remover_restricao(restricao)   
    
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
        Gerenciadora.NOVO_ID += 1

    def buscar_usuario_por_id(self, id_usuario: int):
        lista_ids_de_usuario: list[int] = [usuario.id for usuario in self.__lista_usuarios]
        if id_usuario not in lista_ids_de_usuario:
            raise ValueError("Este usuário não existe")
    
        return self.__lista_usuarios[lista_ids_de_usuario.index(id_usuario)]

    def adicionar_evento(self, id_usuario: int, novo_evento: Evento, nome_area: str):
        self.buscar_area_por_nome(nome_area).adicionar_evento(novo_evento)
        self.buscar_usuario_por_id(id_usuario).adicionar_evento(novo_evento)

        self.gerar_relatorio(self.buscar_area_por_nome(nome_area), novo_evento)

    def remover_evento(self, evento_a_ser_removido: Evento):
        for usuario in self.__lista_usuarios:
            try:
                usuario.remover_evento(evento_a_ser_removido)
            except Exception as e:
                print(f'{usuario.nome}: {e}')

        for area in self.__lista_areas:
            try:
                area.remover_evento(evento_a_ser_removido)
            except Exception as e:
                print(f'{area.nome}: {e}')

    def checar_adm(self, id_usuario: int):
        return self.buscar_usuario_por_id(id_usuario).is_adm

    def adicionar_area(self, nova_area: Area):
        if not isinstance(nova_area, Area):
            raise TypeError("A área deve ser do tipo Area")

        self.__lista_areas.append(nova_area)

    def buscar_area_por_nome(self, nome_area) -> Area:
        lista_de_nomes_de_areas: list[str] = [area.nome for area in self.__lista_areas]
        if nome_area not in lista_de_nomes_de_areas:
            raise ValueError("Esta área não existe")
        
        return self.__lista_areas[lista_de_nomes_de_areas.index(nome_area)]

    def gerar_relatorio(self, area_maracda: Area, novo_evento: Evento):
        nome_arquivo = "relatorio_gerado.pdf"
        pdf = canvas.Canvas(nome_arquivo, A4)

        Titulo = str("Relatorio de agendamento de Evento")
        nome_area = area_maracda.nome
        area_qtd = str(area_maracda.qtd_pessoas)

        pdf.drawString(100, 750, Titulo)
        pdf.drawString(100, 700, nome_area)
        pdf.drawString(100, 680, area_qtd)
        
        if isinstance(area_maracda, AreaEsportiva):
            
            esporte_praticado = area_maracda.esporte_praticado
            pdf.drawString(100, 660, esporte_praticado)

            if area_maracda.sistema_de_iluminacao == True:
                pdf.drawString(100, 640, "Possui sistema de iluminacao!")
            else:
                pdf.drawString(100, 640, "Não Possui sistema de iluminacao!")

        if isinstance(area_maracda, AreaSocial):
            tamanho = str(area_maracda.area_espaco)
            pdf.drawString(100, 660, tamanho)

            if area_maracda.sistema_de_som == True:
                pdf.drawString(100, 640, "Possui sistema de som!")
            else:
                pdf.drawString(100, 640, "Não Possui sistema de som!")

        
        pdf.save()

    def adicionar_item_em_area(self, nome_area: str, item: str):
        self.buscar_area_por_nome(nome_area).adicionar_item_na_lista(item)

    ##Verificação de usuário já é feita em interface gráfica
    ##- Só apagar as dependenciias de id_usuario quando for fazer, igual ta em cima
    def remover_item_em_area(self, id_usuario: int, nome_area: str, item: str):
        if self.checar_adm(id_usuario) == False:
            raise TypeError("O usuário não é do tipo ADM! Logo, não pode remover item!")
        
        self.buscar_area_por_nome(nome_area).remover_item_da_lista(item)
        