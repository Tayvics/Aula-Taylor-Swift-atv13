'''
Aluna: Tayná Vitória Queiroz Moraes 
2° info mat
INSTRUÇÕES:
●	Crie dois módulos, um chamado ‘main.py’ e um chamado ‘conversor.py’.
●	Envie a pasta compactada  no AVA ou o link direcionando para o código no Repl.it

1.	No módulo conversor, escreva uma função que, ao receber um valor em centímetros, o converta para polegadas. Após a conversão, a função deverá escrever em um arquivo a seguinte mensagem “o valor [valor_cm] em centímetros corresponde a [valor_pol] valor em polegadas”.
'''

from conversor import * 
print("CONVERSOR DE CENTÍMETROS PARA POLEGADAS")
des=input("Você deseja iniciar a conversão (s/n)?")
if des == 's':
  nemcm = int(input("Digite o valor, em cm, que você deseja converter:"))
  conversao(nemcm)
else:
  print("Tchau")


