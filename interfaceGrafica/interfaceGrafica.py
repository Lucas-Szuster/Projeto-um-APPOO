import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from enumInterfaceGrafica import enumTelas

from gerenciadora.gerenciadora import Gerenciadora


class App:
    def __init__(self, titulo_app: str, geometria_app: str, gerenciadora: Gerenciadora):
        self.janela_principal = tk.Tk()
        self.janela_principal.title(titulo_app)
        self.janela_principal.geometry(geometria_app)

        # =============================================
        # A FAZER: ADICIONAR UMA INSTâNCIA DE GESTORA QUE SERÁ RECEBIDA E UTILIZADA PARA VALIDAR DADOS/GERAR INTERFACES
        # =============================================

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

        print(f'{nome_do_usuario =}, {senha_do_usuario =}')

        # =============================================
        # A FAZER: VALIDAR USUÁRIO, E, CASO EXISTA, PASSAR PARA A PRÓXIMA FASE
        #
        # ideia básica:
        #   usuario = Usuario(nome_do_usuario, senha_do_usuario)
        #
        #   if (self.instancia_gestora.validar_usuario(usuario)):
        #       self.trocar_tela(enumTelas.TELA_MENU_USUARIO)
        #   else:
        #       erro_dados("Usuário não encontrado na base de dados: senha e/ou nome de usuário errados")
        #       return
        # =============================================

    # TELA MENU USUARIO

    # =============================================
    # A FAZER: TELA QUE MOSTRE AS OPÇÕES PARA O USUÁRIO
    #
    # ideia básica:
    #   for area in self.instancia_gestora.areas:
    #       gerar_opcao_de_marcar_evento_em_area(area)
    # =============================================    

    # INICIAR

    def iniciar(self):
        self.janela_principal.mainloop()

if __name__ == "__main__":
    a = App("Aplicativo gestor de espaços", "500x500")
    a.iniciar()