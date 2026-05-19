from gerenciadora.gerenciadora import gerenciadora
from area.areaSocial import AreaSocial
from evento.evento import Evento
from datetime import datetime
from usuario.usuario import Usuario


geral = gerenciadora()

geral.adicionar_area(AreaSocial('area social 1', 12, 14, True))
geral.adicionar_area(AreaSocial('area social 2', 12, 14, True))

print('parte 1\n=========')
for area in geral.lista_areas:
    print(area.nome)
    for evento in area.lista_eventos:
        print(f'{evento.nome_evento}')
    print('\n\n')


geral.adicionar_evento_em_area('area social 1', Evento('evento 1', datetime(1, 1, 1, 1, 1, 1), 13))
geral.adicionar_evento_em_area('area social 1', Evento('evento 2', datetime(2, 2, 2, 2, 2, 2), 13))

print('parte 2\n=========')
for area in geral.lista_areas:
    print(area.nome)
    for evento in area.lista_eventos:
        print(f'{evento.nome_evento}')
    print('\n\n\n')

geral.remover_evento_em_area('area social 1', geral.buscar_area_por_nome('area social 1').lista_eventos[0])

print('parte 3\n=========')
for area in geral.lista_areas:
    print(area.nome)
    for evento in area.lista_eventos:
        print(f'{evento.nome_evento}')
    print('\n\n\n')