# Arquivo para testar diferentes módulos interagindo, no caso evento e area

from area.areaEsportiva import AreaEsportiva
from evento.evento import Evento
from datetime import datetime

a = AreaEsportiva("nome", 12, "futebol", True)

a.adicionar_item_na_lista('bola de futebol')

print(a.lista_de_itens)