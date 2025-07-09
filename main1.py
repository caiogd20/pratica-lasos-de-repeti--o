print("programa que caucula P=ax¹+ax²+ax³+...+axⁿ")
a = float(input("Digite o valor de a: "))
x = float(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))
seq = []
for i in range(1,(n + 1)):
    seq.append(a * (x ** i))
    print("O valor de P para n = {} é: {} = {} * {} ^ {}".format(i, seq[i - 1], a, x, i))
print("A soma dos valores de P é: ", sum(seq))