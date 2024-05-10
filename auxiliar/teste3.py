









def saca_deposita(tipo: int, user: str, conta: dict):
    '''
    int tipo = 1 para saque ou 2 para deposito.\n
    str user = usuario do login atual.\n
    dict conta = a conta para as verificações.\n
    
    tipo 1 saca e tipo 2 deposita\n
    retorna str "sair" quando o usuario desejar ou em caso de crlt+c
    
    '''
    
    # Inicia o processo de saque.
    while True:

        if tipo == 1:
            try:
                if conta[user]["conta_corrente"]["limite_diario_saque"] > 0:
                    saque = int(input("Qual valor voce deseja sacar? R$"))
                    if saque <= conta[user]["conta_corrente"]["saldo"] and saque > 0 and saque <= conta[user]["conta_corrente"]["limite"] :
                        conta[user]["conta_corrente"]["limite_diario_saque"] -= 1
                        conta[user]["conta_corrente"]["saldo"] -= saque
                        conta[user]["conta_corrente"]["extrato_saque"] += f"Saque efetuado no valor de : {saque}\n"
                        break
                    
                    else:
                        print(f"valor invalido seu sauqe tem que ser menor que seu limite diario que é R${conta[user]["conta_corrente"]["limite"]}\ne seu saque deve ser entre R$0 e R${conta[user]["conta_corrente"]["saldo"]}")
                        while True:
                            sair = str(input ("deseja sair ? S para sim N para nao: "))
                            if sair.capitalize() == "N":
                                break
                            elif sair.capitalize() == "S":
                                return "sair"
                else:
                    print("voce nao possui limite de saques para hoje, volte amanha.")
            except ValueError:
                print("valor não suportado pelo siatema!")



        # Inicia o processo de deposito
        if tipo == 2:

            try:
                # recebe valor e verifica se é posivel realizar a transação
                while True:
                    deposito = int(input("Qual valor voce deseja depositar? R$"))

                    if deposito > 0:
                        conta[user]["conta_corrente"]["saldo"] += deposito
                        conta[user]["conta_corrente"]["extrato_deposito"] += f"Deposito efetuado no valor de : {deposito}\n"
                        break
                    else:
                        print("Impossivel depositar valores abixo de 0 ou 0!")
                        while True:
                            sair = str(input ("deseja sair ? S para sim N para nao: "))
                            if sair.capitalize() == "N":
                                break
                            elif sair.capitalize() == "S":
                                return "sair"

            except KeyboardInterrupt:
               print("terminal interrompido pelo usuario!")
               return "sair"

            except ValueError:
                print("valor não suportado pelo siatema!")


    























