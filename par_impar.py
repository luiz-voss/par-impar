#projeto par ou impar
# 0,2,4,6,8,10....(pares)
# 1,3,5,7,9,11....(impar)

while True:
    try:
        valor = int(input("Digite um valor: "))
        if valor % 2 == 0:
            print("Número digitado PAR")
        else:
            print("Número digitado IMPAR")
    except:
        print("Digite apenas números por favor")



