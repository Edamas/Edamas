menu = '''------------
d = depósito
s = saque
e = extrato
q = sair
------------
Digite a opção desejada: '''
opcao = ''
operacoes = {'Depósito': [], 'Saque': []}
while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Digite o valor para depósito: '))
        if valor:
            operacoes['Depósito'].append(valor)
        else:
            print('O valor deve ser superior a R$ 0.00')
    
    elif opcao == 's':
        valor = float(input('Digite o valor para saque: '))
        if 0 < valor <= 500:
            if valor <= sum(operacoes['Depósito']) - sum(operacoes['Saque']):
                if len(operacoes['Saque']) <= 3:
                    operacoes['Saque'].append(valor)
                else:
                    print('O limite de saques diários é 3')
            else:
                print('O valor solicitado é maior do que o seu saldo')
        else:
            print('O valor deve estar entre R$ 0.00 até R$ 500.00')
    
    elif opcao == 'e':
        saldo = 0
        print('=' * 100)
        for deposito in operacoes['Depósito']:
            saldo += deposito
            print(f'Depósito:\tR$ {deposito:.2f}')
        for saque in operacoes['Saque']:
            saldo -= saque
            print(f'Saque:\tR$ {saque:.2f}')
        print(f'Saldo:\tR$ {saldo:.2f}')
        print('=' * 100)
    
    elif opcao == 'q':
        break
    
    else:
        print('Opção inválida!')
    
        