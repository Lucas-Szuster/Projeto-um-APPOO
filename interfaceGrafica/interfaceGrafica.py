import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from interfaceGrafica.enumInterfaceGrafica import enumTelas

from usuario.usuario import Usuario
from gerenciadora.gerenciadora import Gerenciadora
from evento.evento import Evento
from area.area import Area
from area.areaSocial import AreaSocial
from area.areaEsportiva import AreaEsportiva

class App:
    def __init__(self, titulo_app: str, geometria_app: str, gerenciadora: Gerenciadora):
        self.area_atual: Area | None = None
        self.janela_principal = tk.Tk()
        self.janela_principal.title(titulo_app)
        self.janela_principal.geometry(geometria_app)

        if not isinstance(gerenciadora, Gerenciadora):
            raise TypeError("A gerenciadora deve ser do tipo Gerenciadora")
        self.gerenciadora = gerenciadora

        self.trocar_tela(enumTelas.TELA_LOGIN)

    def limpar_widgets_filhos(self, widget: tk.Tk | tk.Widget ):
        """
        Função que chama o método destroy de todos os elementos filhos do widget passado.

        Raises:
            TypeError:
                caso o argumento widget passado não seja do tipo tk.Tk ou tk.Widget
        """
        if not (isinstance(widget, tk.Tk) or isinstance(widget, tk.Widget)):
            raise TypeError("O argumento não é do tipo tk.Tk ou tk.Widget")

        for elemento in widget.winfo_children():
            elemento.destroy()

    def trocar_tela(self, tela: enumTelas):
        """
        Função que troca a tela que está sendo mostrada no aplicativo para uma nova tela

        Raises:
            TypeError:
                caso o argumento tela passado não seja do tipo enumTelas
        """
        if not isinstance(tela, enumTelas):
            raise TypeError("A nova tela deve ser válida")

        self.limpar_widgets_filhos(self.janela_principal)

        match (tela):
            case enumTelas.TELA_LOGIN:
                self.gerar_tela_login()
            case enumTelas.TELA_MENU_USUARIO:
                self.gerar_tela_menu_usuario()
            case enumTelas.TELA_AREAS_DISPONIVEIS:
                self.gerar_tela_areas_disponiveis()
            case enumTelas.TELA_EVENTOS_AREA:
                self.gerar_tela_eventos_area()
            case _:
                pass

    # TELA LOGIN

    def gerar_tela_login(self):
        def criar_campo_de_dados(master: tk.Tk | tk.Widget, texto_rotulo: str, show: str = ''):
            """
            Função que cria um campo de dados com rótulo para o que deve ser inserido.

            Parâmetros:
                master: Onde deve ser anexado o campo de dados criado;
                texto_rotulo: O texto que deve ser utilizado no rótulo da entrada de dados;
                variavel_texto: A variável que deve ser utilizada para guardar o que é escrito na entrada de daos gerada;
                show: O que deve ser mostrando enquanto o usuário digita (por padrão mostra o texto que ele digitou, mas se for alterado mostra o caractere inserido).
            """
            frame_campo_de_dados = ttk.Frame(master)
            frame_campo_de_dados.pack(expand=True, pady=2)

            label_entrada_de_dados = ttk.Label(frame_campo_de_dados, text=texto_rotulo)
            label_entrada_de_dados.pack()

            variavel_de_texto = tk.StringVar()

            entrada_de_dados = ttk.Entry(frame_campo_de_dados, textvariable=variavel_de_texto, show=show)
            entrada_de_dados.pack()

            return variavel_de_texto

        frame_geral_login = ttk.Frame(self.janela_principal)
        frame_geral_login.pack(expand=True)

        titulo_login = ttk.Label(frame_geral_login, text='Insira seus dados', font=('', 14, 'bold'))
        titulo_login.pack()

        variavel_de_texto_nome_do_usuario = criar_campo_de_dados(frame_geral_login, "Insira o nome de usuário")
        variavel_de_texto_senha_do_usuario = criar_campo_de_dados(frame_geral_login, "Insira a senha", '*')

        botao_enviar_dados = ttk.Button(
            frame_geral_login, 
            text='Enviar dados',
            command= lambda: self.enviar_dados_login(
                var_nome_do_usuario=variavel_de_texto_nome_do_usuario,
                var_senha_do_usuario=variavel_de_texto_senha_do_usuario
            ))
        botao_enviar_dados.pack(pady=10)

    def enviar_dados_login(self, var_nome_do_usuario: tk.StringVar, var_senha_do_usuario: tk.StringVar):
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            var_nome_do_usuario.set('')
            var_senha_do_usuario.set('')
        
        nome_do_usuario = var_nome_do_usuario.get()
        senha_do_usuario = var_senha_do_usuario.get()

        if not nome_do_usuario.strip():
            erro_dados("Não há nome de usuário inserido")
            return
        if not senha_do_usuario.strip():
            erro_dados("Não há senha de usuário inserida")
            return

        if(self.gerenciadora.validar_usuario(nome_do_usuario, senha_do_usuario)):
            self.usuario_logado = self.gerenciadora.get_usuario_por_nome(nome_do_usuario)
            self.trocar_tela(enumTelas.TELA_MENU_USUARIO)
        else:
            erro_dados("Usuário não encontrado na base de dados: senha e/ou nome de usuário errados")
            return

    # TELA MENU USUARIO

    def gerar_tela_menu_usuario(self):
        area_botoes_tela_menu_usuario = ttk.Frame(self.janela_principal)
        area_botoes_tela_menu_usuario.pack(expand=True)

        botao_ver_areas = ttk.Button(
            area_botoes_tela_menu_usuario,
            text="Ver áreas disponíveis",
            command=lambda: self.trocar_tela(enumTelas.TELA_AREAS_DISPONIVEIS)
        )
        botao_ver_areas.grid(column=0, row=0, padx=10)

        botao_ver_eventos_proprios = ttk.Button(
            area_botoes_tela_menu_usuario,
            text="Ver eventos próprios",
            command=lambda: self.trocar_tela(enumTelas.TELA_EVENTOS_PROPRIOS)
        )
        botao_ver_eventos_proprios.grid(column=1, row=0, padx=10)

    # TELA ÁREAS DISPONÍVEIS

    def gerar_tela_areas_disponiveis(self):
        def gerar_componente_label_simples(master, texto: str):
            return ttk.Label(
                master,
                text=texto
            )

        def comando_botao_ver_eventos(area: Area):
            self.area_atual = area
            self.trocar_tela(enumTelas.TELA_EVENTOS_AREA)

        def formatar_area(area: Area, master):
            widget_area = ttk.Frame(master)
            widget_area.pack(padx=5, pady=5)

            gerar_componente_label_simples(widget_area, f"Nome da área: {area.nome}").pack()
            gerar_componente_label_simples(widget_area, f"Quantidade máxima de pessoas: {area.qtd_pessoas}").pack()

            if (isinstance(area, AreaSocial)):
                gerar_componente_label_simples(widget_area, f"Espaco da área: {area.area_espaco} metros quadrados").pack()
                gerar_componente_label_simples(widget_area, f"A área possui sistema de som? {"Sim" if area.sistema_de_som else "Não"}").pack()

            if (isinstance(area, AreaEsportiva)):
                gerar_componente_label_simples(widget_area, f"Esporte da área: {area.esporte_praticado}").pack()
                gerar_componente_label_simples(widget_area, f"A área possui sistema de iluminação? {"Sim" if area.sistema_de_iluminacao else "Não"}").pack()

            botao_ver_eventos = ttk.Button(
                widget_area, 
                text="Ver eventos da área",
                command= lambda: comando_botao_ver_eventos(area))
            botao_ver_eventos.pack()

        area_de_areas = ttk.Frame(self.janela_principal)
        area_de_areas.pack()

        for area in self.gerenciadora.lista_areas:
            formatar_area(area, area_de_areas)

    # TELA EVENTOS AREA

    def gerar_tela_eventos_area(self):
        def gerar_componente_label_simples(master, texto: str):
            return ttk.Label(
                master,
                text=texto
            )

        def formatar_evento(evento: Evento, master):
            frame_evento = ttk.Frame(master)
            frame_evento.pack(padx=5, pady=5)

            gerar_componente_label_simples(frame_evento, f"Nome do evento: {evento.nome_evento}").pack()
            gerar_componente_label_simples(frame_evento, f"Data do evento: {evento.data_e_horario.date()}, Hora do evento: {evento.data_e_horario.time()}").pack()

        if (self.area_atual == None):
            messagebox.showerror('Erro', 'Não há área selecionada')

        area_do_evento = ttk.Frame(self.janela_principal)
        area_do_evento.pack()

        for evento in self.area_atual.lista_eventos:
            formatar_evento(evento, area_do_evento)

    # INICIAR

    def iniciar(self):
        self.janela_principal.mainloop()

if __name__ == "__main__":
    a = App("Aplicativo gestor de espaços", "500x500")
    a.iniciar()