
#or = é uma condição de uma ou outra

compra = float(input('Valor da compra: '))
cliente_frequnte = input('Programa de didelidade? [s/n] ').lower()[0]
print('recebe brinde')

if compra > 100 or cliente_frequnte == 's':
    print('você recebe o brinde')
else:
    print('sem brinde')
