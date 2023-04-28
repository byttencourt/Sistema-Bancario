menu = ''''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 0
totsaques = 0

print(f'\33[30:44mBemvindo ao sistema\33[m')

while True:
    op = str(input('Qual operação deseja realizar? '))

    if op == 'd':
        deposito = int(input('Digite o valor do depósito: '))
        if deposito <= 0:
            print('\33[30:41mValor de Depósito inválido: Verifique a quantia digitada.\33[m')
        else:
            saldo += deposito
            print(f'\33[30:42mVocê Depositou R${deposito:.2f}.\33[m')

    if op == 's':
        if totsaques >= 3:
            print(f'\33[30:41mQuantidade de Saques Excedidos. Tente novamente no próximo dia útil\33[m')
        else:
            saque = int(input('Digite o valor do saque: '))
            if saque <= 0:
                print('\33[30:41mValor de Saque inválido: Verifique a quantia digitada.\33[m')
            elif saque >= 501:
                print('\33[30:41mValor de Saque excede o Limite da Operação. Verifique o valor limite de cada Saque.\33[m')
            elif saque > saldo:
                print('\33[30:41mSaldo indisponível. Verifique o valor do seu limite.\33[m')
            else:
                saldo -= saque
                totsaques += 1
                print(f'\33[30:42mVocê Sacou R${saque:.2f} novo saldo disponível R${saldo:.2f}.\33[m')

    if op == 'e':
        print(f'\33[30:44mSaldo disponível R${saldo:.2f}.\33[m')

    if op == 'q':
        break
print(f'\33[30:43mEncerrando o sistema, Obrigado pela preferencia\33[m')