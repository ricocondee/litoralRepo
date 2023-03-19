#Emanuel Rico
num = int(input("Numero: "))
def fibo(x):
    a=0
    b=1
    for i in range(x):
        c = a+b
        a = b
        b = c
    return b**3
for j in range(num):
    print(fibo(j))
