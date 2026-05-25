from gerenciadora.gerenciadora import Gerenciadora
from area.areaSocial import AreaSocial
from evento.evento import Evento
from datetime import datetime
from usuario.usuario import Usuario


geral = Gerenciadora()

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

print('parte 4\n========')

geral.adicionar_usuario(Usuario("Pedro", 19, 2021015, "Batata09", False))
geral.adicionar_usuario(Usuario("Olavo", 63, 2121212,"Sindicancia", True))

for usuario in geral.lista_usuarios:
    print(f"{usuario.nome}, {usuario.idade}, {usuario.id}, {usuario.senha}, {usuario.is_adm}")


print('parte 5\n========')

geral.adicionar_item_em_area(2121212, "area social 1", "Televisão")

for area in geral.lista_areas:
    print(f"{area.nome}, \n{area.lista_de_itens}")

print('parte 6\n========')

geral.remover_item_em_area(2121212, "area social 1", "Televisão")

for area in geral.lista_areas:
    print(f"{area.nome}, \n{area.lista_de_itens}")

print('parte 7\n========')

## Deve dar erro mesmo!
#geral.adicionar_item_em_area(2021015, "area social 1", "Televisão")

for area in geral.lista_areas:
    print(f"{area.nome}\n{area.lista_de_itens}")

for usuario in geral.lista_usuarios:
    print(f"{usuario.nome}: {geral.checar_adm(usuario.id)}")