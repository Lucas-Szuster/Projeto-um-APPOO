import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from interfaceGrafica.enumInterfaceGrafica import enumTelas
from datetime import datetime

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

    def trocar_tela(self, tela: enumTelas, **kwargs):
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
            case enumTelas.TELA_EVENTOS_PROPRIOS:
                self.gerar_tela_eventos_proprios()
            case enumTelas.TELA_CRIAR_EVENTO:
                self.gerar_tela_criar_evento(**kwargs)
            case enumTelas.TELA_CRIAR_USUARIO:
                self.gerar_tela_criar_usuario()
            case enumTelas.TELA_CRIAR_AREA:
                self.gerar_tela_criar_area()
            case enumTelas.TELA_ADICIONAR_RESTRICAO_A_AREA:
                self.gerar_tela_adicionar_restricao_a_area(**kwargs)
            case enumTelas.TELA_REMOVER_RESTRICAO_A_AREA:
                self.gerar_tela_remover_restricao_area(**kwargs)
            case enumTelas.TELA_ADICIONAR_ITEM:
                self.gerar_tela_adicionar_item(**kwargs)
            case _:
                pass

    #ADICIONAR AREA

    def adicionar_area(self, nova_area: Area, tela_para_recarregar: enumTelas):
        self.gerenciadora.adicionar_area(nova_area)

        self.trocar_tela(tela_para_recarregar)
    
    # REMOVER EVENTO
    
    def remover_evento(self, evento: Evento, tela_para_recarregar: enumTelas):
        self.gerenciadora.remover_evento(evento)

        self.trocar_tela(tela_para_recarregar)

    # ADICIONAR EVENTO

    def adicionar_evento(self, evento: Evento, nome_area: str, id_usuario: int, tela_para_recarregar: enumTelas):
        self.gerenciadora.adicionar_evento(id_usuario, evento, nome_area)

        self.trocar_tela(tela_para_recarregar)

    # ADICIONAR USUARIO

    def adicionar_usuario(self, novo_usuario: Usuario, tela: enumTelas):
        self.gerenciadora.adicionar_usuario(novo_usuario)

        messagebox.showinfo("Informação", "Usuário criado com sucesso")

        self.trocar_tela(tela)

    # BOTAO VOLTAR

    def gerar_botao_voltar(self, tela_anterior):
        frame_botao_voltar = ttk.Frame(self.janela_principal)
        frame_botao_voltar.pack()

        botao_voltar = ttk.Button(
            frame_botao_voltar,
            text="Voltar",
            command=lambda: self.trocar_tela(tela_anterior)
        )
        botao_voltar.pack(side='left')

    # FUNÇÃO CRIAR CAMPO DE DADOS

    def criar_campo_de_dados(self, master: tk.Tk | tk.Widget, texto_rotulo: str, show: str = ''):
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

    # CANVAS ROLÁVEL

    def criar_tela_rolavel(self, master_canvas: tk.Tk | tk.Widget, master_barra_de_rolagem: tk.Tk | tk.Widget):
        canvas = tk.Canvas(master_canvas)
        canvas.pack(side="left", fill="both", expand=True)

        barra_de_rolagem = tk.Scrollbar(master_barra_de_rolagem, orient="vertical", command=canvas.yview)
        barra_de_rolagem.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=barra_de_rolagem.set)

        area_final = ttk.Frame(canvas)

        janela_id = canvas.create_window((0, 0), window=area_final, anchor="nw")

        area_final.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(janela_id, width=e.width))

        return area_final

    # TELA LOGIN

    def gerar_tela_login(self):
        frame_geral_login = ttk.Frame(self.janela_principal)
        frame_geral_login.pack(expand=True)

        titulo_login = ttk.Label(frame_geral_login, text='Insira seus dados', font=('', 14, 'bold'))
        titulo_login.pack()

        variavel_de_texto_nome_do_usuario = self.criar_campo_de_dados(frame_geral_login, "Insira o nome de usuário")
        variavel_de_texto_senha_do_usuario = self.criar_campo_de_dados(frame_geral_login, "Insira a senha", '*')

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

        if (self.gerenciadora.validar_usuario(nome_do_usuario, senha_do_usuario)):
            self.usuario_logado = self.gerenciadora.get_usuario_por_nome(nome_do_usuario)
            self.trocar_tela(enumTelas.TELA_MENU_USUARIO)
        else:
            erro_dados("Usuário não encontrado na base de dados: senha e/ou nome de usuário errados")
            return

    # TELA MENU USUARIO

    def gerar_tela_menu_usuario(self):
        area_botoes_tela_menu_adm = ttk.Frame(self.janela_principal)
        area_botoes_tela_menu_adm.pack(expand=True)

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

        if (self.gerenciadora.checar_adm(self.usuario_logado.id)):
            botao_novo_usuario = ttk.Button(
                area_botoes_tela_menu_adm,
                text="Criar novo usuário",
                command=lambda: self.trocar_tela(enumTelas.TELA_CRIAR_USUARIO)
            )
            botao_novo_usuario.pack()

            botao_criar_area = ttk.Button(
                area_botoes_tela_menu_adm,
                text="Criar area",
                command=lambda: self.trocar_tela(enumTelas.TELA_CRIAR_AREA)
            )
            botao_criar_area.pack()

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

            frame_dados_basicos_area = ttk.Frame(widget_area)
            frame_dados_basicos_area.pack()

            frame_restricoes = ttk.Frame(widget_area)
            frame_restricoes.pack(padx=5, pady=5)

            gerar_componente_label_simples(frame_dados_basicos_area, f"Nome da área: {area.nome}").pack()
            gerar_componente_label_simples(frame_dados_basicos_area, f"Quantidade máxima de pessoas: {area.qtd_pessoas}").pack()

            if (isinstance(area, AreaSocial)):
                gerar_componente_label_simples(frame_dados_basicos_area, f"Espaco da área: {area.area_espaco} metros quadrados").pack()
                gerar_componente_label_simples(frame_dados_basicos_area, f"A área possui sistema de som? {"Sim" if area.sistema_de_som else "Não"}").pack()

            if (isinstance(area, AreaEsportiva)):
                gerar_componente_label_simples(frame_dados_basicos_area, f"Esporte da área: {area.esporte_praticado}").pack()
                gerar_componente_label_simples(frame_dados_basicos_area, f"A área possui sistema de iluminação? {"Sim" if area.sistema_de_iluminacao else "Não"}").pack()

            if (len(area.lista_restricoes) > 1):
                gerar_componente_label_simples(frame_restricoes, "Restrições da área").pack()

            for restricao in area.lista_restricoes:
                gerar_componente_label_simples(frame_restricoes, restricao).pack()

            botao_ver_eventos = ttk.Button(
                widget_area, 
                text="Ver eventos da área",
                command= lambda: comando_botao_ver_eventos(area))
            botao_ver_eventos.pack()

            if (self.gerenciadora.checar_adm(self.usuario_logado.id)):
                botao_adicionar_restricao_area = ttk.Button(
                    widget_area,
                    text="Adicionar restrição à área",
                    command=lambda: self.trocar_tela(enumTelas.TELA_ADICIONAR_RESTRICAO_A_AREA, area=area)
                )
                botao_adicionar_restricao_area.pack()

                botao_remover_restricao_area = ttk.Button(
                    widget_area,
                    text="Remover restrição de área",
                    command=lambda: self.trocar_tela(enumTelas.TELA_REMOVER_RESTRICAO_A_AREA, area=area)
                )
                botao_remover_restricao_area.pack()

                botao_adicionar_item = ttk.Button(
                    widget_area,
                    text="Adicione um item",
                    command=lambda: self.trocar_tela(enumTelas.TELA_ADICIONAR_ITEM, area=area)
                )
                botao_adicionar_item.pack()


        self.gerar_botao_voltar(enumTelas.TELA_MENU_USUARIO)

        area_de_areas = self.criar_tela_rolavel(self.janela_principal, self.janela_principal)

        for area in self.gerenciadora.lista_areas:
            formatar_area(area, area_de_areas)

    # ADICIONAR RESTRIÇÃO A AREA

    def adicionar_item(self, var_item_a_ser_adicionado: tk.StringVar, area: Area):
        var_lista = [var_item_a_ser_adicionado]

        def erro_dados(mensage_de_erro):
            messagebox.showerror(title="Erro", message=mensage_de_erro)
            return
        
        def checar_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True

        if not checar_string(var_item_a_ser_adicionado):
            erro_dados("Item invalido!")
            return
        
        item = var_item_a_ser_adicionado.get()

        try:
            self.gerenciadora.adicionar_item_em_area(area.nome, item)
            messagebox.showinfo("Informação", "Item adicionado com sucesso!")
            self.trocar_tela(enumTelas.TELA_AREAS_DISPONIVEIS)
        except Exception as e:
            erro_dados(e)
            return


    
    def adicionar_restricao_a_area(self, var_restricao_area: tk.StringVar, area: Area):
        lista_var = [var_restricao_area]
        
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            for var in lista_var:
                var.set("")
            return

        def checagem_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True
        
        if not checagem_string(var_restricao_area):
            erro_dados("Restrição inválida")
            return
        
        restricao = var_restricao_area.get()

        try:
            self.gerenciadora.adicionar_restricao_a_area(area, restricao)
            messagebox.showinfo("Informação", "Restrição adicionada com sucesso")
            self.trocar_tela(enumTelas.TELA_AREAS_DISPONIVEIS)
        except Exception as e:
            erro_dados(e)
            return
        
    # REMOVER RESTRICAO AREA

    def gerar_tela_remover_restricao_area(self, area: Area):
        self.gerar_botao_voltar(enumTelas.TELA_AREAS_DISPONIVEIS)

        frame_remover_restricao = ttk.Frame(self.janela_principal)
        frame_remover_restricao.pack()

        var_restricao_a_remover = tk.StringVar()
        opcoes_area_do_evento = ttk.OptionMenu(
            frame_remover_restricao, 
            var_restricao_a_remover, 
            "Escolha uma opção",  
            *area.lista_restricoes        
        )
        opcoes_area_do_evento.pack(pady=2)

        botao_enviar_dados = ttk.Button(
            frame_remover_restricao,
            text="Enviar dados",
            command=lambda: self.remover_restricao_area(area, var_restricao_a_remover)
        )
        botao_enviar_dados.pack()

    def remover_restricao_area(self, area: Area, var_restricao_a_remover: tk.StringVar):
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            for var in lista_var:
                var.set("")
            return

        def checagem_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True
        
        if not checagem_string(var_restricao_a_remover):
            erro_dados("Restrição inválida")
            return
        
        restricao = var_restricao_a_remover.get()

        try:
            self.gerenciadora.remover_restricao_area(area, restricao)
            #
            # CONTINUAR AQUI!!!!!!!
            #
        except Exception as e:
            erro_dados(e)
            return

    def gerar_tela_adicionar_item(self, area: Area):
        self.gerar_botao_voltar(enumTelas.TELA_AREAS_DISPONIVEIS)

        frame_adicionar_item = ttk.Frame(self.janela_principal)
        frame_adicionar_item.pack()

        var_item_a_ser_adicionado = self.criar_campo_de_dados(frame_adicionar_item, "Qual item deseja inserir?")

        botao_para_envio_de_dados = ttk.Button(
            frame_adicionar_item,
            text="Inserir Item",
            command = lambda: self.adicionar_item(var_item_a_ser_adicionado, area)
        )
        botao_para_envio_de_dados.pack()


    def gerar_tela_adicionar_restricao_a_area(self, area: Area):
        self.gerar_botao_voltar(enumTelas.TELA_AREAS_DISPONIVEIS)

        frame_adicionar_restricao_a_area = ttk.Frame(self.janela_principal)
        frame_adicionar_restricao_a_area.pack()

        var_restricao_da_area = self.criar_campo_de_dados(frame_adicionar_restricao_a_area, "Insira a restrição que deve ser adicionada")

        botao_enviar_dados = ttk.Button(
            frame_adicionar_restricao_a_area,
            text="Enviar dados",
            command=lambda: self.adicionar_restricao_a_area(var_restricao_da_area, area)
        )
        botao_enviar_dados.pack()

    # GERAR LISTA DE EVENTOS (USADO PARA MÚLTIPLAS TELAS)

    def gerar_lista_de_eventos(self, master, lista: list[Evento], permissao: bool, tela_para_recarregar: enumTelas):
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

            if permissao:
                botao_remover = ttk.Button(
                    frame_evento, 
                    text="Remover evento",
                    command=lambda: self.remover_evento(evento, tela_para_recarregar)
                )
                botao_remover.pack()

        for evento in lista:
            formatar_evento(evento, master)

    # TELA CRIAR AREA

    def gerar_tela_criar_area(self):
        self.gerar_botao_voltar(enumTelas.TELA_MENU_USUARIO)

        tela_de_gerar_area = ttk.Frame(self.janela_principal)
        tela_de_gerar_area.pack()
        
        var_tipo_de_area = tk.StringVar()
        opcoes_area_do_evento = ttk.OptionMenu(
            tela_de_gerar_area, 
            var_tipo_de_area, 
            "Escolha uma opção",  
            *["Area esportiva", "Area Social"]         
        )
        opcoes_area_do_evento.pack(pady=2)
        
        frame_informacoes_extras = ttk.Frame(self.janela_principal)
        frame_informacoes_extras.pack()

        var_nome_da_area = self.criar_campo_de_dados(tela_de_gerar_area, "Escreva o nome da area:")
        var_qtd_pessoas = self.criar_campo_de_dados(tela_de_gerar_area, "Insira a quantidade maxima permitida de pessoas")
        
        var_tipo_de_area.trace_add(
            "write", 
            lambda *args: self.checar_tipo_de_area(
                var_tipo_de_area=var_tipo_de_area,
                tela_de_gerar_area=frame_informacoes_extras,
                var_nome_area=var_nome_da_area,
                var_qtd_pessoas=var_qtd_pessoas
            )
        )
        

    def checar_tipo_de_area(self, var_tipo_de_area: tk.StringVar, tela_de_gerar_area: tk.Frame, var_nome_area: tk.StringVar, var_qtd_pessoas: tk.StringVar):
        valor = var_tipo_de_area.get() 

        self.limpar_widgets_filhos(tela_de_gerar_area)
        if valor != "Escolha uma opção":
            match valor:
                case "Area esportiva":
                    var_esporte_praticado = self.criar_campo_de_dados(tela_de_gerar_area, "Insira o esporte praticado")
                    
                    var_iluminacao = tk.BooleanVar(value=False)
                    label_tem_iluminacao = ttk.Label(tela_de_gerar_area, text="O espaço tem iluminação?")
                    label_tem_iluminacao.pack()
                    botao_possui_iluminacao = ttk.Checkbutton(tela_de_gerar_area, variable=var_iluminacao)
                    botao_possui_iluminacao.pack()

                    botao_enviar = ttk.Button(
                        tela_de_gerar_area,
                        text="Enviar Dados",
                        command=lambda: self.enviar_dados_area_esportiva(
                            var_nome_area=var_nome_area,
                            var_qtd_pessoas=var_qtd_pessoas,
                            var_esporte_praticado=var_esporte_praticado,
                            var_iluminacao=var_iluminacao
                        )
                    )
                    botao_enviar.pack()


                
                case "Area Social":
                    var_area_em_metros = self.criar_campo_de_dados(tela_de_gerar_area, "Insira o tamanho de sua area social")

                    var_sistema_de_som = tk.BooleanVar(value=False)
                    label_tem_sistema_de_som = ttk.Label(tela_de_gerar_area, text="O espaço tem sistema de som?")
                    label_tem_sistema_de_som.pack()
                    botao_possui_sistema_de_som = ttk.Checkbutton(tela_de_gerar_area, variable=var_sistema_de_som)
                    botao_possui_sistema_de_som.pack()

                    botao_enviar = ttk.Button(
                        tela_de_gerar_area,
                        text="Enviar Dados",
                        command=lambda: self.enviar_dados_em_area_social(
                            var_nome_area=var_nome_area,
                            var_qtd_pessoas=var_qtd_pessoas,
                            var_area_em_metros=var_area_em_metros,
                            var_sistema_de_som=var_sistema_de_som
                        )
                    )
                    botao_enviar.pack()

    def enviar_dados_em_area_social(self, var_nome_area: tk.StringVar, var_qtd_pessoas: tk.StringVar, var_area_em_metros: tk.StringVar, var_sistema_de_som: tk.BooleanVar):
        lista_var = [
            var_nome_area,
            var_qtd_pessoas,
            var_area_em_metros
        ]
        
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            for var in lista_var:
                var.set("")
            return

        def checagem_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True

        def checagem_numero(var_num: tk.StringVar):
            try:
                num = int(var_num.get())
                return True
            except Exception as e:
                return False
            
        if not all([
            checagem_string(var_nome_area),
            checagem_numero(var_qtd_pessoas),
            checagem_numero(var_area_em_metros)
        ]):
            erro_dados("Um dos campos esta preenchido incorretamente!")
            return
        
        nome_area = var_nome_area.get()
        qtd_pessoas = int(var_qtd_pessoas.get())
        area_em_metros = float(var_area_em_metros.get())
        sistema_de_som = var_sistema_de_som.get()

        try:
            nova_area = AreaSocial(nome_area, qtd_pessoas, area_em_metros, sistema_de_som)
            self.adicionar_area(nova_area, enumTelas.TELA_MENU_USUARIO)
            messagebox.showinfo("Informação", "Área criada com sucesso")
        except Exception as e:
            erro_dados(e)
            return


    def enviar_dados_area_esportiva(self,var_nome_area: tk.StringVar, var_qtd_pessoas: tk.StringVar, var_esporte_praticado: tk.StringVar, var_iluminacao: tk.BooleanVar):
        lista_var = [
            var_nome_area,
            var_qtd_pessoas,
            var_esporte_praticado
        ]
        
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            for var in lista_var:
                var.set("")
            return

        def checagem_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True

        def checagem_numero(var_num: tk.StringVar):
            try:
                num = int(var_num.get())
                return True
            except Exception as e:
                return False
            
        if not all([
            checagem_string(var_nome_area),
            checagem_numero(var_qtd_pessoas),
            checagem_string(var_esporte_praticado)
        ]):
            erro_dados("Um dos campos esta preenchido corretamente!")
            return
        
        nome_area = var_nome_area.get()
        qtd_pessoas = int(var_qtd_pessoas.get())
        esporte_praticado = var_esporte_praticado.get()
        iluminacao = var_iluminacao.get()

        try:
            nova_area = AreaEsportiva(nome_area, qtd_pessoas, esporte_praticado, iluminacao)
            self.adicionar_area(nova_area, enumTelas.TELA_MENU_USUARIO)
            messagebox.showinfo("Informação", "Área criada com sucesso")
        except Exception as e:
            erro_dados(e)
            return



    # TELA EVENTOS AREA

    def gerar_tela_eventos_area(self):
        if (self.area_atual == None):
            messagebox.showerror('Erro', 'Não há área selecionada')

        self.gerar_botao_voltar(enumTelas.TELA_AREAS_DISPONIVEIS)

        area_de_eventos = self.criar_tela_rolavel(self.janela_principal, self.janela_principal)

        if (self.gerenciadora.checar_adm(self.usuario_logado.id)):
            self.gerar_lista_de_eventos(area_de_eventos, self.area_atual.lista_eventos, True, enumTelas.TELA_EVENTOS_AREA)
        else:
            self.gerar_lista_de_eventos(area_de_eventos, self.area_atual.lista_eventos, False, enumTelas.TELA_EVENTOS_AREA)

    # TELA EVENTOS PRÓPRIOS

    def gerar_tela_eventos_proprios(self):        
        self.gerar_botao_voltar(enumTelas.TELA_MENU_USUARIO)

        area_de_eventos = self.criar_tela_rolavel(self.janela_principal, self.janela_principal)

        self.gerar_lista_de_eventos(area_de_eventos, self.usuario_logado.lista_de_eventos, True, enumTelas.TELA_EVENTOS_PROPRIOS)    
        
        botao_novo_evento = ttk.Button(
            area_de_eventos,
            text="Criar novo evento",
            command=lambda: self.trocar_tela(
                enumTelas.TELA_CRIAR_EVENTO, 
                tela_voltar=enumTelas.TELA_EVENTOS_PROPRIOS,
            )
        )
        botao_novo_evento.pack(pady=20)        

    # TELA CRIAR EVENTO

    def gerar_tela_criar_evento(self, tela_voltar: enumTelas):
        self.gerar_botao_voltar(tela_voltar)

        area_criar_evento = ttk.Frame(self.janela_principal)
        area_criar_evento.pack()

        var_area_do_evento = tk.StringVar(area_criar_evento)
        opcoes_area_do_evento = ttk.OptionMenu(
            area_criar_evento, 
            var_area_do_evento, 
            "Escolha uma opção",  
            *[area.nome for area in self.gerenciadora.lista_areas]          
        )
        opcoes_area_do_evento.pack(pady=2)

        var_texto_nome_evento = self.criar_campo_de_dados(area_criar_evento, "nome do evento")
        var_quantidade_participantes_evento = self.criar_campo_de_dados(area_criar_evento, "quantidade de participantes")
        
        frame_data = ttk.Frame(area_criar_evento)
        frame_data.pack(expand=True, pady=2)

        label_data = ttk.Label(frame_data, text="Insira a data do evento")
        label_data.pack()
        dia_evento =ttk.DateEntry(frame_data)
        dia_evento.pack()

        var_horario_evento = self.criar_campo_de_dados(area_criar_evento, "Insira a hora que ocorrerá o evento (somente números)")
        var_minuto_evento = self.criar_campo_de_dados(area_criar_evento, "Insira o minuto que ocorrerá o evento (somente números)")

        botao_eviar = ttk.Button(
            area_criar_evento,
            text="Enviar e criar evento",
            command=lambda: self.enviar_dados_evento(
                var_opcao_area_evento=var_area_do_evento,
                var_nome_evento=var_texto_nome_evento,
                var_quantidade_de_participantes_evento=var_quantidade_participantes_evento,
                var_horario_evento=var_horario_evento,
                var_minuto_evento=var_minuto_evento,
                entrada_dia=dia_evento,
                tela_evento_adicionado=tela_voltar,
                tela_evento_nao_adicionado=enumTelas.TELA_CRIAR_EVENTO
            )
        )
        botao_eviar.pack()
    
    def enviar_dados_evento(self, var_opcao_area_evento: tk.StringVar, var_nome_evento: tk.StringVar, var_quantidade_de_participantes_evento: tk.StringVar, var_horario_evento: tk.StringVar, var_minuto_evento: tk.StringVar, entrada_dia: ttk.DateEntry, tela_evento_adicionado: enumTelas, tela_evento_nao_adicionado: enumTelas):
        lista_var = [
            var_nome_evento,
            var_quantidade_de_participantes_evento,
            var_horario_evento,
            var_minuto_evento
        ]
        
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            for var in lista_var:
                var.set("")
            return

        def checagem_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True

        def checagem_numero(var_num: tk.StringVar):
            try:
                num = int(var_num.get())
                return True
            except Exception as e:
                return False
        
        if var_opcao_area_evento.get() == "Escolha uma opção":
            erro_dados("Escolha uma área válida")
            return

        if not all([
            checagem_string(var_nome_evento), 
            checagem_numero(var_quantidade_de_participantes_evento),
            checagem_numero(var_horario_evento),
            checagem_numero(var_minuto_evento)
        ]):
            erro_dados("Entrada inválida: quantidade de participantes, horário e minuto devem ser números e nenhuma entrada pode estar vazia")

        area_evento = var_opcao_area_evento.get()
        nome_evento = var_nome_evento.get()
        quantidade_de_participantes = int(var_quantidade_de_participantes_evento.get())
        horario_evento = int(var_horario_evento.get())
        minuto_evento = int(var_minuto_evento.get())
        
        data_e_horario_evento: datetime = datetime.strptime(entrada_dia.entry.get(), "%d/%m/%Y").replace(
            hour=horario_evento,
            minute=minuto_evento
        )

        try:
            novo_evento = Evento(nome_evento, data_e_horario_evento, quantidade_de_participantes)
            self.adicionar_evento(novo_evento, area_evento, self.usuario_logado.id, tela_evento_adicionado)
        except Exception as e:
            erro_dados(e)
            return
        
    # TELA CRIAR USUARIO

    def gerar_tela_criar_usuario(self):
        self.gerar_botao_voltar(enumTelas.TELA_MENU_USUARIO)

        area_criar_usuario = ttk.Frame(self.janela_principal)
        area_criar_usuario.pack(expand=True)

        var_nome_usuario = self.criar_campo_de_dados(area_criar_usuario, "Insira o nome do usuário")
        id_usuario = Gerenciadora.NOVO_ID
        var_idade_usuario = self.criar_campo_de_dados(area_criar_usuario, "Insira a idade do usuário")
        var_senha_usuario = self.criar_campo_de_dados(area_criar_usuario, "Insira a senha do usuario", '*')
        
        var_is_adm_usuario = tk.BooleanVar(value=False)
        label_is_adm_usuario = ttk.Label(area_criar_usuario, text="O usuário é adm?")
        label_is_adm_usuario.pack()
        botao_is_adm_usuario = ttk.Checkbutton(area_criar_usuario, variable=var_is_adm_usuario)
        botao_is_adm_usuario.pack()

        botao_enviar_dados = ttk.Button(
            area_criar_usuario,
            text="Enviar dados",
            command=lambda: self.criar_novo_usuario(
                var_nome_usuario=var_nome_usuario,
                id_usuario=id_usuario,
                var_idade_usuario=var_idade_usuario,
                var_senha_usuario=var_senha_usuario,
                var_is_adm_usuario=var_is_adm_usuario
            )
        )
        botao_enviar_dados.pack(pady=2)

    def criar_novo_usuario(self, var_nome_usuario: tk.StringVar, id_usuario: int, var_idade_usuario: tk.StringVar, var_senha_usuario: tk.StringVar, var_is_adm_usuario: tk.BooleanVar):
        lista_var = [
            var_nome_usuario,
            var_idade_usuario,
            var_senha_usuario
        ]
        
        def erro_dados(mensagem_de_erro):
            messagebox.showerror(title="Erro", message=mensagem_de_erro)
            for var in lista_var:
                var.set("")
            return

        def checagem_string(var_string: tk.StringVar):
            string: str = var_string.get()
            if not string.strip():
                return False
            
            return True

        def checagem_numero(var_num: tk.StringVar):
            try:
                num = int(var_num.get())
                return True
            except Exception as e:
                return False
            
        if not all([
            checagem_string(var_nome_usuario),
            checagem_numero(var_idade_usuario),
            checagem_string(var_senha_usuario)
        ]):
            erro_dados("Algum campo está inválido")

        nome_usuario = var_nome_usuario.get()
        senha_usuario = var_senha_usuario.get()
        idade_usuario = int(var_idade_usuario.get())
        id_adm_usuario = var_is_adm_usuario.get()

        try:
            novo_usuario = Usuario(nome_usuario, idade_usuario, id_usuario, senha_usuario, id_adm_usuario)
            self.adicionar_usuario(novo_usuario, enumTelas.TELA_MENU_USUARIO)
        except Exception as e:
            erro_dados(e)
            return

    # INICIAR

    def iniciar(self):
        self.janela_principal.mainloop()