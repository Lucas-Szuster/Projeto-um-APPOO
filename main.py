from gerenciadora.gerenciadora import Gerenciadora
from usuario.usuario import Usuario
from bancoDeDados.bancoDeDados import BancoDeDados
from evento.evento import Evento

from datetime import datetime

from gerenciadora.gerenciadora import Gerenciadora
from usuario.usuario import Usuario
from evento.evento import Evento
from datetime import datetime
from area.areaSocial import AreaSocial

# ev1 = Evento('evento 1', datetime(year=2026, month=10, day=12, hour=10), 10)
# ev2 = Evento('evento 2', datetime(year=2026, month=10, day=12, hour=19), 10)

# usuario_um = Usuario('lucas', 12, 13, 'lelebel', True)
# usuario_um.adicionar_evento(ev1)
# usuario_um.adicionar_evento(ev2)

ger = Gerenciadora()

# ger.adicionar_area(AreaSocial('area 1', 12, 14, True))
# ger.adicionar_area(AreaSocial('area 2', 14, 15, False))
# ger.adicionar_area(AreaSocial('area 3', 16, 16, True))

# ger.adicionar_evento_em_area('area 1', ev1)
# ger.adicionar_evento_em_area('area 1', ev2)

# ger.adicionar_usuario(usuario_um)

b = BancoDeDados()
b.ler_dados(ger)

print(ger.lista_areas)
print(ger.lista_usuarios)


b.salvar_dados(ger)