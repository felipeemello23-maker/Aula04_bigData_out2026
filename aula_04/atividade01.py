compra = float(input('digite o valor '))
desconto = compra * 0.16
valor_de_desconto = compra - desconto
if compra > 250:
    print(f'valor final com desconto {valor_de_desconto:.2f}')
else:
    print(f'valor da compra sem desconto {compra} ')
    
