# Arquivo para testar diferentes módulos interagindo, no caso evento e area

from area.areaEsportiva import AreaEsportiva
from evento.evento import evento1
from datetime import datetime

a = AreaEsportiva('NOME DA ÁREA', 12, ['restrição 1', 'restrição 2'])

a.adicionar_evento(evento1('asda', datetime(2026, 12, 12, 12, 12, 1), 12))
a.adicionar_evento(evento1('asda', datetime(2021, 12, 12, 12, 12, 1), 12))


print(a.lista_eventos[0] == a.lista_eventos[1])

b = a.lista_eventos
c = b.pop()

print(b)
print(a.lista_eventos)

a.remover_evento(c)

print(a.lista_eventos)