print(""" 
==================================== 
     ANÁLISE DE TEMPERATURAS 
==================================== 
""")

temperaturas = []

for i in range(7):
    temperatura = float(input("Digite a temperatura:"))
    temperaturas.append(temperatura)

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / 7

acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media = acima_media + 1 

print(""" 
  ==================================== 
  RELATÓRIO 
  ==================================== 
  Temperaturas registradas: {} 
  Maior temperatura: {:.2f} 
  Menor temperatura: {:.2f} 
  Temperatura média: {:.2f} 
  Dias acima da média: {} 
  ==================================== 
  """.format(temperaturas, maior, menor, media, acima_media))      

