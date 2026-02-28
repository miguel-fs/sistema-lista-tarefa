import os

# Função que vai limpar a tela do terminal


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Mostrar o menu principal


def mostrar_menu():
    print("\n=== SISTEMA DE LISTA DE TAREFAS ===")
    print("[i] Inserir tarefa")
    print("[a] Apagar tarefa")
    print("[c] Concluir tarefa")
    print("[l] Listar tarefas")
    print("[f] Finalizar")

# Inserir uma nova tarefa


def inserir_tarefa(lista):
    limpar_tela()
    nome = input("Digite o nome da tarefa: ")
    lista.append({"nome": nome, "status": "pendente"})
    print("Tarefa adicionada com sucesso!")

# Vai listar todas as tarefas com índices e status


def listar_tarefas(lista):
    limpar_tela()
    if not lista:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n=== TAREFAS ===")
        for indice, tarefa in enumerate(lista):
            print(f"{indice} - {tarefa['nome']} - [{tarefa['status']}]")

# Apaga uma tarefa pelo índice


def apagar_tarefa(lista):
    limpar_tela()
    if not lista:
        print("Nenhuma tarefa para remover.")
        return

    listar_tarefas(lista)

    try:
        indice = int(input("Digite o número da tarefa que deseja apagar: "))
        del lista[indice]
        print("Tarefa removida com sucesso!")
    except (ValueError, IndexError):
        print("Índice inválido.")

# Conclui uma tarefa pelo índice


def concluir_tarefa(lista):
    limpar_tela()
    if not lista:
        print("Nenhuma tarefa para concluir. ")
        return
    listar_tarefas(lista)

    try:
        indice = int(input("Digite o número da tarefa que deseja concluir: "))
        lista[indice]["status"] = "concluída"
        print("Tarefa marcada como concluída")
    except (ValueError, IndexError):
        print("Índice inválido.")

# Vai rodar o loop do programa


def main():
    tarefas = []  # Lista que armazena todas as tarefas

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "i":
            inserir_tarefa(tarefas)

        elif opcao == "l":
            listar_tarefas(tarefas)

        elif opcao == "a":
            apagar_tarefa(tarefas)

        elif opcao == "f":
            print("Encerrando o sistema...")
            break

        elif opcao == "c":
            concluir_tarefa(tarefas)

        else:
            print("Opção inválida.")


# Vai garantir que o código rode somente se o arquivo for executado diretamente
if __name__ == "__main__":
    main()
