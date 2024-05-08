
#
#
#def _menu_conta ():
#    
#    menu = ('''\n
#              ◤----------------| Banco PYDIO |----------------◥
#
#
#                        Consultar sado                [1]
#                        Consultar limite de saques    [2]
#                        Consultar extrato             [3]
#                        Sacar                         [4]
#                        Depositar                     [5]
#                        Sair                          [0]
#
#
#               ◣---------------------------------------------◢
#
#            \nDigite uma opção: ''')
#
#
#    # checagem menu
#    checagem = {}
#    checagem['Menu'] = menu
#    checagem['Menu_valores'] = [0,1,2,3,4,5]
#
#
#    while True :
#        # Mantem tudo funcionando ate o usuario discar o numero de saida.
#
#        chave_loop_while = True
#
#        while chave_loop_while :
#            try:
#                # checar o que o usuari quer fazer, apresentando a ele o menu.
#                # e checa se o usuario esta digitando o valor correto.
#
#                opcao = int(input(menu))
#                if opcao not in checagem['Menu_valores']:
#                    print("Essa opçao nao existe!")
#                else:
#                    print("Valor valido :)")
#                    chave_loop_while = False
#                    return opcao
#
#            except ValueError:
#                print("O valor passado é invalido, insira um valor valido!")
#    
#        if opcao == 0 :
#            break
#
# #    return opcao
# #
# #
janeiro = {"dia-1" : "saques1","dia-2" : "saques","dia-3" : "saques","dia-4":"saques","dia-5" : "saques","dia-6" : "saques","dia-7" : "saques","dia-8" : "saques","dia-9" : "saques","dia-10" : "saques","dia-11" : "saques","dia-12" : "saques","dia-13" : "saques","dia-14" : "saques","dia-15" : "saques","dia-16" : "saques","dia-17" : "saques","dia-18" : "saques","dia-19" : "saques","dia-20" : "saques","dia-21" : "saques","dia-22" : "saques","dia-23" : "saques","dia-24" : "saques","dia-25" : "saques","dia-26" : "saques","dia-27" : "saques","dia-28" : "saques","dia-29" : "saques","dia-30" : "saques","dia-31" : "saques"}

# #
# #
# #
# #for
# #
# #
# #    
j2={}
a=""
for k,v in janeiro.items():
    j2[k]=[0]
    


print(j2)

ano2024 =[j2]
k = "dia-1"

ano2024[0]['dia-1']

print(ano2024[0])
for y,z in ano2024[0].items():
       if y == k :
        
        print(type(z))

print(ano2024[0]["dia-1"])