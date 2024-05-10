

'''

# ENTRDA VALIDA É SÓ 0/1 SENDO 0 PARA NÃO E 1 PARA SIM  #

a = 0

#

def entrada (texto_entrada, lista_menu):

    Recebe um Texto para adicionar ao input(), e uma lista de valores para as opções validas.
       Checa se a entrada do usuari esta na lista de valores validos, e retorna o valor se estiver.
    

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

    abc = (\n
              ◤----------------| Banco PYDIO |----------------◥


                        Consultar sado                [1]
                        Consultar limite de saques    [2]
                        Consultar extrato             [3]
                        Sacar                         [4]
                        Depositar                     [5]
                        Sair                         [Sair]


               ◣---------------------------------------------◢

            \nDigite uma opção: )
    
    user_entrada = entrada(abc, menu)
    if str(user_entrada).isnumeric() == False and str(user_entrada).upper() == "SAIR":
        break
    if user_entrada in menu:
        break
   

'''


menu = ["sair", 1, 2, 3]


db_contas = {}

usuario = db_contas



def cria_user(db, user, senha, limite=500):
    '''
    Cria uma nova conta no banco de dados.
    -
    \t\t\t|\tcria_user (db,user, senha,limite=500 )\t|
    |
    db = o Banco de dados das contas.\n
    |
    user = Novo usuario.\n
    |
    senha = Nova senha.\n
    |
    Retorna um dicionario com o novo usuario.
    '''

    id = len(db)
    usuarios = {
                user: {
                        "senha": senha,
                        "conta_corrente": {
                                            "id": id,
                                            "limite": limite,
                                            "saldo": 0,
                                            "extrato": '',
            }
        }
    }

    return usuarios


def entrada_definitiva(tipo: int, texto: str, verificacao: any):
    '''
    verifica se a entrada é valida.
    -
    tipo :\n
    1 para seleção de menu\n
    2 para verificação de usuario\n
    3 para verificação de senha\n

    texto: Sera passado para o input().\n

    verificacao: recebe um dado ou uma lista para comparar com a entrada do usuario.\n
    return:\n
    tipo 1 : opção do menu em str, caso o usuario queira sair retorna "sair"\n
    tipo 2 : retorna uma lista [ -1, str(usuario)] , caso o usuario queira sair retorna "sair"\n
    tipo 3 : retorna -1 para senha correta, caso o usuario queira sair retorna "sair"\n

    '''

    # abre um bloco try pare caso a entrada for de valor diferente a de cada tipo de argumentos
    try:

        # veririfica e aciona o tipo selecionado

        if tipo == 1:
            # Lógica para validar a seleção de menu
            # Se a entrada for válida, retorne a opção selecionada ou "sair" se o usuário quiser sair

            while True:

                try:
                    entrada_user = input(texto)

                    for menu in verificacao:

                        if entrada_user == str(menu):
                            print(f"OK , OPCÃO {menu}, SELECIONADA")
                            return menu
                    else:
                        print('tente novamente!')

                except ValueError:
                    print("valor não suportado pelo sistema!")
                except KeyboardInterrupt:
                    print("Programa interrompido pelo usuario!")
                    return "sair"

        elif tipo == 2:
            # Lógica para verificar usuário
            # Se a entrada for válida, retorne uma lista [-1, str(usuario)] ou "sair" se o usuário quiser sair

            while True:

                try:
                    entrada_user = input(texto)

                    for user in verificacao:

                        if entrada_user == str(user):

                            return [-1, str(entrada_user)]
                    else:
                        print('Usuario nao existe!, tente novamente.')

                except ValueError:
                    print("valor não suportado pelo sistema!")
                except KeyboardInterrupt:
                    print("Programa interrompido pelo usuario!")
                    return "sair"

        elif tipo == 3:
            # Lógica para verificar senha
            # Se a entrada for válida, retorne -1 ou "sair" se o usuário quiser sair

            while True:

                try:
                    entrada_user = input(texto)

                    for senha in verificacao:

                        if entrada_user == str(senha):

                            return -1
                    else:
                        print('Snha errada!, tente novamente.')

                except ValueError:
                    print("valor não suportado pelo sistema!")
                except KeyboardInterrupt:
                    print("Programa interrompido pelo usuario!")
                    return "sair"

        else:
            # valor tipo não existe na função
            print("O valor atribuido ao 'tipo' não é suportado por essa função!")

    except ValueError:
        # Se ocorrer um erro de valor, informe o usuário e continue solicitando entrada
        print("Entrada inválida! Por favor, insira um valor válido.")






def entrada(texto_entrada, menus):
    ''' Recebe um Texto para adicionar ao input(), e uma lista de valores para as opções validas.
       Checa se a entrada do usuari esta na lista de valores validos, e retorna o valor se estiver.'''
    while True:

        try:
            entrada_user = input(texto_entrada)

            for menu in menus:

                if entrada_user == str(menu):
                    print(f"OK , OPCÃO {menu}, SELECIONADA")
                    return menu
            else:
                print('tente novamente!')

        except ValueError:
            print("valor não suportado pelo sistema!")
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuario!")
            return "sair"


def entrada_senha(texto_entrada, senhas):
    ''' Recebe um Texto para adicionar ao input(), e uma lista de valores para as opções validas.
       Checa se a entrada do usuari esta na lista de valores validos, e retorna o valor se estiver.'''
    while True:

        try:
            entrada_user = input(texto_entrada)

            for senha in senhas:

                if entrada_user == str(senha):

                    return -1
            else:
                print('Snha errada!, tente novamente.')

        except ValueError:
            print("valor não suportado pelo sistema!")
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuario!")
            return "sair"


def entrada_user(texto_entrada, users):
    ''' Recebe um Texto para adicionar ao input(), e uma lista de valores para as opções validas.
       Checa se a entrada do usuari esta na lista de valores validos, e retorna o valor se estiver.'''
    while True:

        try:
            entrada_user = input(texto_entrada)

            for user in users:

                if entrada_user == str(user):

                    return [-1, str(entrada_user)]
            else:
                print('Usuario nao existe!, tente novamente.')

        except ValueError:
            print("valor não suportado pelo sistema!")
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuario!")
            return "sair"


def login():
    if db_contas == {}:
        return False
    while True:
        user_correto = entrada_definitiva(2,"Digite seu usuario: ", usuario.keys())
        if user_correto[0] == -1:
            senha_correta = entrada_definitiva(3,"Digite sua senha: ", [usuario[user_correto[1]]["senha"]])
            if senha_correta == -1:
                return True
            else:
                print("programa interrompido.")
        else:
            print("programa interrompido.")


while True:

    user_entrada = entrada_definitiva(1,'''\n
              ◤----------------| Banco PYDIO |----------------◥


                        Login                [1]
                        Criar conta          [2]
                           
               ◣---------------------------------------------◢
''', [1, 2])

    if user_entrada == 1:
        lg = login()
        if lg == False:
            print("Não existe contas registradas nesse servidor.")
        else:
            break

    if user_entrada == 2:
        user = input("qual usuario vc quer usar nessa conta? - ")
        senha = input("Crie uma senha - ")
        db_contas.update(cria_user(db_contas, user, senha))

        continue
    else:
        continue

