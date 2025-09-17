# 7. Login simples
# Peça um nome de usuário e uma senha. Se o usuário for "admin" e a senha "1234", exiba “Acesso permitido”; caso contrário, “Acesso negado”.

nome_de_usuario = input("Digite o nome de usuario: \n")
senha = input("Digite a senha: \n")

if nome_de_usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")