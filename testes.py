# Arquivo para testar diferentes módulos interagindo, no caso evento e area

from area.areaEsportiva import AreaEsportiva
from evento.evento import Evento
from datetime import datetime
from area.areaSocial import AreaSocial


# teste área esportiva

areaesportiva = AreaEsportiva("area de esportes", 12, "futebol", True)
print(areaesportiva.qtd_pessoas)

areasocial = AreaSocial("area de lazer", 12, 23, False)
print(areasocial.area_espaco)