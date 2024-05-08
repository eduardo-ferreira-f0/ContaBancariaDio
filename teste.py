# a = {}
# b='''\n
#           ◤----------------| Banco PYDIO |----------------◥
          
          
#                     Consultar sado                [1]
#                     Consultar limite de saques    [2]
#                     Consultar extrato             [3]
#                     Sacar                         [4]
#                     Depositar                     [5]
#                     Sair                          [0]
          
          
#            ◣---------------------------------------------◢
        
#         \nDigite uma opção: '''
# a['Menu'] = b
# a['Chaves_de_acesso'] = [0,1,2,3,4,5]

# print(type(a["Chaves_de_acesso"]))
# print(1 in a["Chaves_de_acesso"] )

# print(9 not in a["Chaves_de_acesso"])


# def deposit ():
#     while True:

#         try:
#             print("")
#             qtde=int(input("Digite o valor que deseja depositar: R$"))

#             if qtde > 0:
#                 return qtde

#         except ValueError:
#             print("Valor digitado é invalido!")

def pode_sacar ():


### sacar func 
    while True:

        try:
            print("")
            qtde=int(input("Digite o valor que deseja sacar: R$"))

            if qtde > conta_corrente_saldo:
                print("O valor digitato é maior que o saldo em sua conta, entre com um valor valido!")
                print(f"Saldo atual: {conta_corrente_saldo}")
            elif qtde > 0 and qtde < conta_corrente_saldo:
                return qtde

        except ValueError:
            print("Valor digitado é invalido!")
    else:
        while True:
            try:
                ax =int(input("Sair e fechar? [1]- SIM | [0]- NÂO"))
                if ax in [1,0]:
                    if ax == 1:
                        return "sair-0"
            except ValueError:
                print("Valor digitado é invalido!")





# if tem_limite_no_dia(dia_hoje,mes_hoje,ano_hoje, limite_diario_de_saques) == 3:
#         ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[1] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
#       ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = 1
#          print(ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")])

#      elif( tem_limite_no_dia(dia_hoje,mes_hoje,ano_hoje, limite_diario_de_saques) == 2):
#          ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = 2
#          ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[2] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
#          #print(ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")])
#      elif tem_limite_no_dia(dia_hoje,mes_hoje,ano_hoje, limite_diario_de_saques) == 1:
#          ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = 3
#          ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[3] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
#          #print(ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")])
     
#      else:
#          print ("Limite diario atingido!")










