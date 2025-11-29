senha_correta = "123"
tentativas = 0

while tentativas < 3:
    tentativa = input("Digite a senha: ")

    if tentativa == senha_correta:
        print("Acesso liberado!")
        break

    print("Senha incorreta.")
    tentativas += 1

if tentativas == 3:
    print("Acesso bloqueado.")