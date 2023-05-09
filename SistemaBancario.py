from datetime import datetime
saldo = 0
numero_saques = 0
limite_saques = 3
limite = 500


def menu():
    print('''
\33[31m======== MENU =========\33[m
\33[32m
    [d] Depositar 
    [s] Sacar 
    [e] Extrato 
    [q] Sair
    \33[m''')
    return input('Qual opção deseja? ')


def deposito(valor, saldo):
    if valor > 0:
        saldo += valor
        print(f'\33[30:42mVocê Depositou R${valor:.2f}.\33[m')
    else:
        print('\33[30:41mValor de Depósito inválido: Verifique a quantia digitada.\33[m')
    return saldo
        


def saque(saque, saldo):
    global numero_saques, limite, limite_saques
    if numero_saques >= limite_saques:
        print(f'\33[30:41mQuantidade de Saques Excedidos. Tente novamente no próximo dia útil\33[m')
    else:
        if saque <= 0:
            print('\33[30:41mValor de Saque inválido: Verifique a quantia digitada.\33[m')
        elif saque > limite:
            print('\33[30:41mValor de Saque excede o Limite da Operação. Verifique o valor limite de cada Saque.\33[m')
        elif saque > saldo:
            print('\33[30:41mSaldo indisponível. Verifique o valor do seu limite.\33[m')
        else:
            saldo -= saque
            numero_saques += 1
            print(f'\33[30:42mVocê Sacou R${saque:.2f} novo saldo disponível R${saldo:.2f}.\33[m')
    return saldo

def extrato(saldo):
    hora = datetime.now()
    horaatual = hora.strftime(('%d/%m/%Y %H:%M'))
    print('\33[31m======== EXTRATO =========\33[m')
    print(f'\33[33m     {horaatual}\nSaldo disponível R${saldo:.2f}.\33[m')
    print('\33[31m======== EXTRATO =========\33[m')

def quit():
    print(f'\33[30:43mEncerrando o sistema, Obrigado pela preferencia\33[m')


while True:
    op = menu()

    if op == 'd':
        valor = float(input('Digite o valor do depósito: '))
        saldo = deposito(valor, saldo)

    if op == 's':
        valor = float(input('Digite o valor do saque: '))
        saldo = saque(valor, saldo)

    if op == 'e':
        extrato(saldo)

    if op == 'q':
        quit()
        break
