# progerama para somar 10 mumeros inteiros
# e mostrar o resultado
# Autor: caio Gonçalves Dias
soma = 0
for i in range(10):
    numero = int(input("Digite um número {}°: ".format(i + 1)))
    if i == 0:
        soma = numero
    else:
        soma += numero
print(f"A soma dos números é: {soma}")