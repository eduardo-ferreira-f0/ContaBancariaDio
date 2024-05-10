


# data exemplo 


dia_hoje = 3
mes_hoje = 3
ano_hoje = 2024
hora = "00:00"

##

limite_diario_de_saques = 3
conta_corrente_saldo = 2000
conta_corrente_limite_valor_por_saque = 500
numero_de_depositos = 0







def _menu_conta ():
    # inicia o menu de opções

    menu = ('''\n
              ◤----------------| Banco PYDIO |----------------◥


                        Consultar sado                [1]
                        Consultar limite de saques    [2]
                        Consultar extrato             [3]
                        Sacar                         [4]
                        Depositar                     [5]
                        Sair                          [0]


               ◣---------------------------------------------◢

            \nDigite uma opção: ''')



    # checagem menu
    checagem = {}
    checagem['Menu'] = menu
    checagem['Menu_valores'] = [0,1,2,3,4,5]


    while True :
        # Mantem tudo funcionando ate o usuario discar o numero de saida.

        chave_loop_while = True

        while chave_loop_while :
            try:
                # checar o que o usuari quer fazer, apresentando a ele o menu.
                # e checa se o usuario esta digitando o valor correto.

                opcao = int(input(menu))
                if opcao not in checagem['Menu_valores']:
                    print("Essa opçao nao existe!")
                else:
                    #print("Valor valido :)")
                    chave_loop_while = False
                    
                    return opcao;

            except ValueError:
                print("O valor passado é invalido, insira um valor valido!")
    
        if opcao == 0 :
            break
    
    return opcao
def pode_depositar ():


### sacar func 
    while True:

        try:
            print("")
            qtde=int(input("Digite o valor que deseja depositar: R$"))

            if qtde > 0:
                return qtde
            else:
                print("O valor deve ser maior que 0!")
                

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
def pode_sacar (conta_id, valor):

    # Sinaliza se o saque pode ser feito
    if valor > 0 :
        return True
    else:
        return False
    
def tem_limite_no_dia (dia,mes,ano,limit):
    # checa para ver se tem limite no dia
    if ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] == 0:
        return 3
    if ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] == 1:
        return 2
    if ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] == 2:
        return 1
    if ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] == 3:
        return 0
    else:
        return -1
    

def extrato_conta ():
    return print(f"""\n
          ◤----------------| Banco PYDIO |----------------◥
          
             Saldo:
             R${conta_corrente_saldo :.2f}
             Limite de saque disponivel no dia:
             {(tem_limite_no_dia(dia_hoje,mes_hoje,ano2024_dp,limite_diario_de_saques))}
             Saques diarios limitados a R${(500 * limite_diario_de_saques) :.2f}

             Depositos hoje:
             
             {printsaques(numero_de_depositos)}

         ◣-----------------------------------------------◢
         ◤-----------------------------------------------◥
                 Data: dd/mm/yyyy | Horario: 00:00
         ◣-----------------------------------------------◢
""")
# def printsaques (limitis):

    
#     if limitis > 0:
#         for i in range(limitis +1):
#             a =''
#             a += str (ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][i])
             
#         return a
#     else:
#         return "# - sem saque"
    
def printsaques (limitis):

    
    if limitis > 0:
        lista_de_depositos=""
        for i in range(limitis + 1):
            lista_de_depositos_temp =''
            lista_de_depositos_temp +=  f"{str (ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][i])} \n"
            lista_de_depositos = lista_de_depositos + lista_de_depositos_temp
        return lista_de_depositos
    else:
        return "# - sem saque"
    
    
# def printsaques (limitis):

    
#     if limitis > 0:
#         for i in range(limitis +1):
#             a =''
#             a += f"{str (ano2024[(mes_hoje-1)][(f"dia-{dia_hoje}")][i])} \n"
             
#         return a
#     else:
#         return "# - sem saque"
    


################################################## datas e depositos 

janeiro_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
fevereiro_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
marco_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
abril_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
msio_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
junho_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
julho_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
agosto_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
setembro_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
outubro_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
novembro_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
dezembro_dp = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}

ano2024_dp =[janeiro_dp,fevereiro_dp,marco_dp,abril_dp,msio_dp,junho_dp,julho_dp,agosto_dp,setembro_dp,outubro_dp,novembro_dp,dezembro_dp]


################################################## datas e saques 

janeiro = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
fevereiro = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
marco = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
abril = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
maio = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
junho = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
julho = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
agosto = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
setembro = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
outubro = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
novembro = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}
dezembro = {'dia-1': [0], 'dia-2': [0], 'dia-3': [0], 'dia-4': [0], 'dia-5': [0], 'dia-6': [0], 'dia-7': [0], 'dia-8': [0], 'dia-9': [0], 'dia-10': [0], 'dia-11': [0], 'dia-12': [0], 'dia-13': [0], 'dia-14': [0], 'dia-15': [0], 'dia-16': [0], 'dia-17': [0], 'dia-18': [0], 'dia-19': [0], 'dia-20': [0], 'dia-21': [0], 'dia-22': [0], 'dia-23': [0], 'dia-24': [0], 'dia-25': [0], 'dia-26': [0], 'dia-27': [0], 'dia-28': [0], 'dia-29': [0], 'dia-30': [0], 'dia-31': [0]}

ano2024 =[janeiro,fevereiro,marco,abril,maio,junho,julho,agosto,setembro,outubro,novembro,dezembro]


# estrutura principal 


while True:
    opcao_user = _menu_conta()

    if opcao_user == 0:
        break

    if opcao_user == 1:
        #Consultar saldo
        print(f'''\n
    ◤----------------| Banco PYDIO |----------------◥
    ◣-----------------------------------------------◢
                       Saldo atual :
              R${conta_corrente_saldo:.2f}
    ◤-----------------------------------------------◥
             Data: dd/mm/yyyy | Horario: 00:00
    ◣-----------------------------------------------◢

''')

    if opcao_user == 2:
        # Consultar limite de saques no dia 
        print(f'''\n
    ◤----------------| Banco PYDIO |----------------◥
    ◣-----------------------------------------------◢
                 Saques disponiveis hoje :
                          {tem_limite_no_dia(dia_hoje,mes_hoje,ano2024_dp,limite_diario_de_saques)}
    ◤-----------------------------------------------◥
             Data: dd/mm/yyyy | Horario: 00:00
    ◣-----------------------------------------------◢

''')
        
    if opcao_user == 3:
        # Consultar extrato
        extrato_conta()



   # if opcao_user == 4:
        # Sacar
        

    if opcao_user == 5:
        # Deposita
        depositar = pode_depositar()
        if depositar == "sair-0":
            break
        else:
            conta_corrente_saldo += depositar
            numero_de_depositos +=1
            ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[N°-{numero_de_depositos}] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
            ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = numero_de_depositos
         
     #f"[{ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][1]}] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}"
#     if tem_limite_no_dia(dia_hoje,mes_hoje,ano_hoje, limite_diario_de_saques) == 3:
#         ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[1] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
#       ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = 1
#          #print(ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")])

# # #     elif( tem_limite_no_dia(dia_hoje,mes_hoje,ano_hoje, limite_diario_de_saques) == 2):
# # #         ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = 2
# # #         ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[2] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
# # #         #print(ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")])
# # #     elif tem_limite_no_dia(dia_hoje,mes_hoje,ano_hoje, limite_diario_de_saques) == 1:
# # #         ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][0] = 3
# # #         ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")].append(f"[3] - Saque efetuado no dia {dia_hoje}/{mes_hoje}/{ano_hoje} as {hora} No valor de : {depositar}")
# # #         #print(ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")])
# # #     
# # #     else:
# # #         print ("Limite diario atingido!")
# # {ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][1] if len(ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")])  >1 else "# - sem saque"}
# #          {ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][2] if len(ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")])  >2 else "# - sem saque"}
# #         {ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")][3] if len(ano2024_dp[(mes_hoje-1)][(f"dia-{dia_hoje}")])  >3 else "# - sem saque"}




    
    


    
