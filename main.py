from usuario.usuario import Usuario

user1 = Usuario("Lucas", 20, 2026078, "Luquinhas", False)
user2 = Usuario("Arthur", 20, 2026077, "Arthurzinho", True)

listinha_usuarios = [user1, user2]

for usuario in listinha_usuarios:
    print(f"{usuario.nome}, {usuario.idade}, {usuario.id}, {usuario.senha}, {usuario.is_adm}")