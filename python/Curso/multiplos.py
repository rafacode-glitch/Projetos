# CALCULAR MULTIPLOS DE UM NÚMERO ESPECÍFICO ENTRE UM INTERVALO DE NÚMEROS

# Solicita que o usuário insira o número desejado
numero = int(input("Digite o número para encontrar os múltiplos: "))

# Solicita que o usuário insira o início do intervalo
inicio_intervalo = int(input("Digite o início do intervalo: "))

# Solicita que o usuário insira o final do intervalo
fim_intervalo = int(input("Digite o final do intervalo: "))

# Cria um range com base nos dados inseridos pelo usuário
numeros = range(inicio_intervalo, fim_intervalo+1, numero)

# Itera sobre os números e imprime os múltiplos
for numero in numeros:
    print(numero)
