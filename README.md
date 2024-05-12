# Banco PYDIO

Este é um sistema básico de banco chamado "Banco PYDIO". O código oferece funcionalidades de criação de contas de usuário, login, consulta de saldo, limite de saques, extrato de transações, saques e depósitos.

## Declaração de Variáveis

- **opções do menu**: Lista de opções do menu, contendo as opções de sair, 1, 2, 3, 4 e 5.
- **db_contas**: Dicionário vazio que irá armazenar os dados das contas dos usuários.
- **usuario**: Referência ao dicionário de contas, inicialmente vazio.

## Definições de Funções

### cria_user

- **Descrição**: Cria uma nova conta no banco de dados.
- **Argumentos**:
  - `db`: Dicionário representando o banco de dados das contas.
  - `user`: Nome do novo usuário.
  - `senha`: Senha do novo usuário.
  - `limite`: Limite de saldo para a conta (padrão é 500).
- **Retorno**: Retorna um dicionário com o novo usuário.

### entrada_definitiva

- **Descrição**: Verifica se a entrada é válida.
- **Argumentos**:
  - `tipo`: Tipo de verificação a ser realizada (1 para seleção de menu, 2 para verificação de usuário, 3 para verificação de senha).
  - `texto`: Texto a ser exibido para solicitar a entrada.
  - `verificacao`: Dado ou lista para comparar com a entrada do usuário.
- **Retorno**:
  - Para tipo 1: Opção do menu em string; "sair" se o usuário desejar sair.
  - Para tipo 2: Lista `[-1, str(usuario)]`; "sair" se o usuário desejar sair.
  - Para tipo 3: -1 para senha correta; "sair" se o usuário desejar sair.

### login

- **Descrição**: Inicia a verificação se o usuário está correto.
- **Argumentos**:
  - `usuario`: Dicionário contendo o banco de dados de usuários.
- **Retorno**: Retorna o usuário se os dados estiverem corretos, False se o banco de dados estiver vazio.

### saca_deposita

- **Descrição**: Realiza saque ou depósito na conta do usuário.
- **Argumentos**:
  - `tipo`: Tipo de operação a ser realizada (1 para saque, 2 para depósito).
  - `user`: Nome do usuário.
  - `conta`: Dicionário representando a conta do usuário.
- **Retorno**: "sair" quando o usuário desejar ou em caso de interrupção.

## Corpo do Código

O código inicia solicitando ao usuário que faça login ou crie uma nova conta. Após o login, o usuário tem acesso a um menu onde pode consultar saldo, limite de saques, extrato de transações, sacar, depositar ou sair do programa.
