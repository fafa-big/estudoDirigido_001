def saudacao(nome):
    return f"Olá, {nome}!"

def idade_para_100(idade):
    return 100 - idade

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(saudacao(nome))
faltam = idade_para_100(idade)
print(f"Faltam {faltam} anos para você completar 100.")