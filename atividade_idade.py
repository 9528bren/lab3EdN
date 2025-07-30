def classificar_idade():
    print("Classificador de Idade\n")

    while True:
        entrada = input("Digite sua idade (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            idade = int(entrada)

            if idade < 0:
                print("Idade inválida. Digite um número positivo.\n")
            elif idade <= 12:
                print("Categoria: Criança \n")
            elif idade <= 17:
                print("Categoria: Adolencente \n")
            elif idade <= 59:
                print("Categoria: Adulto \n")
            else:
                print("Categoria: Idoso \n")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro. \n")

classificar_idade()