def cadastrar(lista, item):
    # Impedir itens duplicados
    if item in lista:
        print("✖ Este item já existe na lista!")
        return

    lista.append(item)
    print("✔ Item cadastrado!")


def listar(lista):
    if not lista:
        print("Lista vazia.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")


def remover(lista, numero):
    # Verificar se o número é válido
    if numero < 1 or numero > len(lista):
        print("✖ Número inválido!")
        return

    removido = lista.pop(numero - 1)
    print(f"✔ Item removido: {removido}")