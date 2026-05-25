from gerenciadora.gerenciadora import Gerenciadora
from usuario.usuario import Usuario
from banco_de_dados.banco_de_dados import BancoDeDados


usu1 = Usuario('leila', 12, 1, 'hei', True)

gen = Gerenciadora()
gen.adicionar_usuario(usu1)

bancoDeDados = BancoDeDados()
bancoDeDados.salvar_dados(gen)