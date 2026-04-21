#Loop principal: mantém o programa rodando continuamente
while True:
#Entrada de dados pelo usuario
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input ('Digite o segundo numero: ')
    operador = input ('Digite o operador (+-/*): ')
# Inicialização de variáveis de controle
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

# Validação e conversão dos números e operadores
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numero digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operador) > 1:
        print ('Digite apenas um operador.')
        continue
#Estrutura condicional para escolher a operação
    print('Realizando a sua conta, confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float} =',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float} =',num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float} =',num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float} =',num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')
#Condição de parada do programa
    sair = input('Quer sair? [s] im: ').lower().startswith('s')

    if sair is True:
        break
