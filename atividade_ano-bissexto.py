def verificar_ano_bissexto():
    print("Verificador de Ano Bissexto\n")

    while True:
        entrada = input("Digite um ano (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            ano = int(entrada)
            if ano < 0:
                print("Ano inválido. Digite um ano positivo.\n")
                continue

            if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
                print(f"O ano {ano} É bissexto.\n")
            else:
                print(f"O ano {ano} NÃO é bissexto.\n")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o ano.\n")


verificar_ano_bissexto()
