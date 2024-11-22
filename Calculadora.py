# Solicita o primeiro número
numero1 = float(input("Digite o primeiro número:"))
# Solicita a operação desejada
operador = input("Digite o operador:")
# Solicita o segundo número
numero2 = float(input("Digite o segundo número:"))

# Soma os dois números e retorna o resultado
if operador == "+":
    def soma():
        resultado = numero1 + numero2
        return resultado
    print(soma())

# Subtrai os dois números e retorna o resultado
if operador == "-":
    def subtracao():
        resultado = numero1 - numero2
        return resultado
    print(subtracao())

# Multiplica os dois números e retorna o resultado
if operador == "*":
    def multiplicacao():
        resultado = numero1 * numero2
        return resultado
    print(multiplicacao())

# Divide os dois números e retorna o resultado
if operador == "/":
    def divisao():
        resultado = numero1 / numero2
        return resultado
    print(divisao())



