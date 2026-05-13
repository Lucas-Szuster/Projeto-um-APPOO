from gerenciadora.gerenciadora import gerenciadora
from area.area import Area
from evento.evento import Evento
from datetime import date, time

geral = gerenciadora()

restricoes = ["Proibido nadar", "Proibido fumar"]

area_1 = Area("Sala de estar", 4, restricoes)
geral.adicionar_area(area_1)
area_2 = Area("Piscina", 7, restricoes)
geral.adicionar_area(area_2)

evento_1 = Evento("Festinha", time(14, 00, 00), date(2027, 3, 21), 5)

geral.adicionar_evento_em_area("Sala de estar", evento_1)
geral.adicionar_evento_em_area("Churrasqueira", evento_1)