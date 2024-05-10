


#                                      |Declaração de Variaveis|

# dia
hoje = date.today()

# opçoes do menu
menu = ["sair", 1, 2, 3, 4, 5]

# inicio do banco de dados dos usuarios e das contas
db_contas = {}
usuario = db_contas


#                                      |Definições de Funções|


def cria_user(db: dict, user: str, senha: str, limite=500):
    '''
    Cria uma nova conta no banco de dados.
    -
    \t\t\t|\tcria_user (db,user, senha,limite=500 )\t|
    |
    dict db = o Banco de dados das contas.\n
    |
    str user = Novo usuario.\n
    |
    str senha = Nova senha.\n
    |
    Retorna um dicionario com o novo usuario.
    '''

    try:

        id = len(db)

        usuarios = {
                        user: {
                                    "senha": senha,
                                    "conta_corrente": {
                                                            "id": id,
                                                            "limite": limite,
                                                            "saldo": 0,
                                                            "extrato_saque": '''
◤----------------| Banco PYDIO |----------------◥
                |Saques atuais|\n
''',
                                                            "extrato_deposito": '''
◤----------------| Banco PYDIO |----------------◥
                |Depositos atuais|\n
''',
                                                            "limite_diario_saque": 3
                }
            }
        }

        return usuarios
    except ValueError:
        print("Valor inserido na fubção não é valido, revise os argumentos.")


def entrada_definitiva(tipo: int, texto: str, verificacao: any):
    '''
    verifica se a entrada é valida.
    -
    int tipo :\n
    1 para seleção de menu\n
    2 para verificação de usuario\n
    3 para verificação de senha\n

    str texto: Sera passado para o input().\n

    any verificacao: recebe um dado ou uma lista para comparar com a entrada do usuario.\n
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

                    for opcoes_menu in verificacao:

                        if entrada_user == str(opcoes_menu):
                            print(f"OK , OPCÃO {opcoes_menu}, SELECIONADA")
                            return opcoes_menu
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


def login(usuario):
    '''
    Inicia a verificação se o usuario esta correto\n
    -
    - recebe o banco de dados de ususrio
    retorna:\n
    usuario se o os dados estiverem corretos.
    False se o banco de dados estiver vazio.

    '''
    if usuario == {}:
        return False
    while True:
        # try:
        user_correto = entrada_definitiva(2, "Digite seu usuario: ", usuario.keys())
        if user_correto[0] == -1:
            senha_correta = entrada_definitiva(3, "Digite sua senha: ", [usuario[user_correto[1]]["senha"]])
            if senha_correta == -1:
                return str(user_correto[1])
            elif senha_correta == "sair":
                print("programa interrompido.")
                return "sair"
        elif user_correto == "sair":
            print("programa interrompido.")
            return "sair"
  
  


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
                        return None
                    
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
                    return None
            except ValueError:
                print("valor não suportado pelo siatema!")
            except KeyboardInterrupt:
               print("terminal interrompido pelo usuario!")
               return "sair"


        # Inicia o processo de deposito
        if tipo == 2:

            try:
                # recebe valor e verifica se é posivel realizar a transação
                while True:
                    deposito = int(input("Qual valor voce deseja depositar? R$"))

                    if deposito > 0:
                        conta[user]["conta_corrente"]["saldo"] += deposito
                        conta[user]["conta_corrente"]["extrato_deposito"] += f"Deposito efetuado no valor de : {deposito}\n"
                        return None
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


    


#                                      --------------------------


#                                         |Corpo do Codigo|
while True:
    sair = 0  # 0 : normal / 1 : volta ao inicio do loop / 2 : interrompe o programa
    
    login_atual = 0 # serve so para salvar temporariamente o usuario do login para acessar a conta no segundo while
    
    # inicia o login
    while True:

        # Exibe menu de login
        user_entrada = entrada_definitiva(1, '''\n
                  ◤----------------| Banco PYDIO |----------------◥


                            Login                [1]
                            Criar conta          [2]

                   ◣---------------------------------------------◢
    ''', [1, 2])

        if user_entrada == 1:

            checa_login = login(usuario)
            if checa_login == False:
                print("Não existe contas registradas nesse servidor.")
            elif checa_login == "sair":
                sair = 1
                break
            else:
                login_atual = checa_login
                break

        if user_entrada == 2:
            try:
                user = input("qual usuario vc quer usar nessa conta? - ")
                senha = input("Crie uma senha - ")
            except KeyboardInterrupt:
                print("\nPrograma interrompido!")
                sair = 1
                break
            db_contas.update(cria_user(db_contas, user, senha))

            continue
        else:
            sair = 1
            break

    # Checa se o usuario quer sair
    if sair == 1:
        print("Saindo.. .")
        continue
    elif sair == 2:
        break
    else:
        print("Login autorizado.")
        print(login_atual)

    # inicia o terminal da conta
    while True:

        try:

            ############# define um menu e solicita a entrada do usuario ################

            # layout do menu
            texto_menu_conta = ('''\n
                      ◤----------------| Banco PYDIO |----------------◥


                                Consultar sado                [1]
                                Consultar limite de saques    [2]
                                Consultar extrato             [3]
                                Sacar                         [4]
                                Depositar                     [5]
                                Sair                         [Sair]


                       ◣---------------------------------------------◢

                    \nDigite uma opção: ''')

            # Exibe o menu da conta
            user_entrada = entrada_definitiva(1, texto_menu_conta, menu)

            ############## verifica se o usuario deseja sair do programa #############

            if str(user_entrada).isnumeric() == False and str(user_entrada).upper() == "SAIR":
                break

           ############ inicia a checagem e executa a opçao selecionada ############
           
            if user_entrada == 1:
                print(f'''
                     ◤----------------| Banco PYDIO |----------------◥
                                  R$ - {usuario[login_atual]["conta_corrente"]["saldo"]}
                     ◣-----------------------------------------------◢
                     ''')
                   
            if user_entrada == 2:
                print(f'''
                     ◤----------------| Banco PYDIO |----------------◥
                                  QUANTIDADE DE SAQUES DISPONIVEIS
                                  - {usuario[login_atual]["conta_corrente"]["limite_diario_saque"]}
                     ◣-----------------------------------------------◢
                     ''')
            if user_entrada == 3:
               print(usuario[login_atual]["conta_corrente"]["extrato_saque"])
               print("===================================================")
               print(usuario[login_atual]["conta_corrente"]["extrato_deposito"])
               
            try:
                if user_entrada == 4:
                    saca_deposita(1, login_atual, usuario )
                    if saca_deposita == "sair":
                        break
                if user_entrada == 5:
                    saca_deposita(2, login_atual, usuario )
                    if saca_deposita == "sair":
                        break
            except KeyError:
                print("valor invalido para os argumentos da função sacar / depositar ")
            except ValueError:
                print("revise os valores de entrada!")
               
           
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuario!")
            break

    #                                     ---------------------------
'''
◤----------------| Banco PYDIO |----------------◥
◣-----------------------------------------------◢
'''