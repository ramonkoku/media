from Media import Media
from calculadora_de_temperatura import ConversorTemperaturas

while True:
    print("1. Calcular média")
    print("2. Celsius para Fahrenheit")
    print("3. Fahrenheit para Celsius")
    print("4. Sair") 

    escolha = input("Escolha uma opção: ")

    if escolha == '4':
        print("Encerrando o programa...")
        break

    if escolha == '1':           
        nota1 = float(input("nota1: "))
        nota2 = float(input("nota2: "))
        nota3 = float(input("nota3: "))
        
        media = Media(nota1, nota2, nota3)
        print("Média:", media.calcular_media())

        break

    valor = float(input('Digite um valor: '))


    if escolha == '2':
        result = ConversorTemperaturas.celsius_para_fahrenheit(valor)
        print("Resultado em Fahrenheit:", result)

    elif escolha == '3':
        result = ConversorTemperaturas.fahrenheit_para_celsius(valor)
        print("Resultado em Celsius:", result)

    else:
        print("Opção inválida. Tente novamente.")
    break
        

