def fibonacci(num):
    if not isinstance(num, int):
        return "Isto é um texto, retorne um número inteiro positivo"
    if num < 0:
        return "Digite um número acima de 0"
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

while 0 == 0:
    num = int(input("Digite um número inteiro positivo para calcular o n-ésimo número de Fibonacci: "))
    print(fibonacci(num))