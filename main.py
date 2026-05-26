from gerenciadora.gerenciadora import Gerenciadora
from usuario.usuario import Usuario
from banco_de_dados.banco_de_dados import BancoDeDados
from evento.evento import Evento

from datetime import datetime

gen = Gerenciadora()

bancoDeDados = BancoDeDados()
bancoDeDados.ler_dados(gen)

for usuario in gen.lista_usuarios:
    print(f'{usuario.nome}, {usuario.lista_de_eventos}')

#bancoDeDados.ler_dados_usuarios()