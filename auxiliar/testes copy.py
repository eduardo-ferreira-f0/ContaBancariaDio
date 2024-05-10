





# ENTRDA VALIDA É SÓ 0/1 SENDO 0 PARA NÃO E 1 PARA SIM  #

a = 0

#

def entrada (texto_entrada, lista_menu):

    '''Recebe um Texto para adicionar ao input(), e uma lista de valores para as opções validas.
       Checa se a entrada do usuari esta na lista de valores validos, e retorna o valor se estiver.
    '''

    while True:

        try:
            entrada_user = input(texto_entrada)

            for menu in lista_menu:
                
                if entrada_user == str(menu) :
                    print(f"OK , OPCÃO {menu}, SELECIONADA")
                    return menu
            else:
                print('tente novamente!')

        except ValueError:
            print("valor não suportado pelo sistema!")
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuario!")
            return "sair"
         
    
             
menu = ["sair",1,2,3]



while True :

    abc = ('''\n
              ◤----------------| Banco PYDIO |----------------◥


                        Consultar sado                [1]
                        Consultar limite de saques    [2]
                        Consultar extrato             [3]
                        Sacar                         [4]
                        Depositar                     [5]
                        Sair                         [Sair]


               ◣---------------------------------------------◢

            \nDigite uma opção: ''')
    
    user_entrada = entrada(abc, menu)
    if str(user_entrada).isnumeric() == False and str(user_entrada).upper() == "SAIR":
        break
    if user_entrada in menu:
        break
   






