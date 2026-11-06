pontos = int(input('infome os pontos: '))

if pontos >= 100:
    pontos = pontos + 10
    print(f'exelente!\n Você tem {pontos} agora!')

elif pontos >= 50:
    pontos = pontos + 5
    print(f'bom desempenho! você tem {pontos} agora!')

else:
    print(f'Não desanime, vc está começando seus pontos {pontos} ')
