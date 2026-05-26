from interfaceGrafica.interfaceGrafica import App
from gerenciadora.gerenciadora import Gerenciadora
from usuario.usuario import Usuario
from evento.evento import Evento
from datetime import datetime
from area.areaSocial import AreaSocial
from bancoDeDados.bancoDeDados import BancoDeDados


if __name__ == "__main__":
    # gerando as instâncias necessários
    gerenciadora = Gerenciadora()
    bancoDeDados = BancoDeDados()
    app = App("Aplicativo de eventos", "500x500", gerenciadora)

    # lendo o banco de dados e salvando na gerenciadora
    bancoDeDados.ler_dados(gerenciadora)
    
    # inicializando o aplicativo do sistema
    app.iniciar()

    # finalizando, salvando os dados no banco de dados
    bancoDeDados.salvar_dados(gerenciadora)