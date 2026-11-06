
salario = float(input('informe seu salário: '))
venda = float(input('quanto vendeu: '))

if venda >= 1000:
    bonus1 = salario + 150
    print(f'você ganha bônos mais seu salário mais primeiro Bônos {bonus1} ')
elif venda >= 500:
    bonus2 = salario + 75
    print(f'você ganha bônos mais seu salário mais segundo Bônos {bonus2}')
else:
    print('você não ganha bônos')
