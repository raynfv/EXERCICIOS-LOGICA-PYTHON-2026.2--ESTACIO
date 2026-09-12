print(""""
==================================== CONVERSÃO DE TEMPERATURA ====================================
""")
celsius = float(input("Digite a temperatura em Celsius:"))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print("""
==================================== RESULTADO ====================================
celsius: {: .2f}ºC
fahrenheit: {: .2f}ºF
kelvin: {: .2f}K
==================================== """.format(celsius, fahrenheit, kelvin))