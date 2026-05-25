# Arquivo para testar diferentes módulos interagindo, no caso evento e area

from area.areaEsportiva import AreaEsportiva
from evento.evento import Evento
from datetime import datetime
from area.areaSocial import AreaSocial


# teste área esportiva

area_esportiva = AreaSocial("area esportiva", 12, 12, True)


evento1 = Evento('evento 1', datetime(year=2026, month=5, day=25, hour=12, minute=0), 11)
evento2 = Evento('evento 2', datetime(year=2026, month=5, day=25, hour=19, minute=0), 11)

area_esportiva.adicionar_evento(evento1)
area_esportiva.adicionar_evento(evento2)
print(area_esportiva.lista_eventos)