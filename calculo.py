def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

def apresentar_resultado(tempo, velocidade, distancia, litros_usados):
    print("Velocidade média: {} km/h".format(velocidade))
    print("Tempo gasto na viagem: {} horas".format(tempo))
    print("Distância percorrida: {} km".format(distancia))
    print("Quantidade de litros utilizada: {} litros".format(litros_usados))

tempo = float(input("Quantas horas demorou a viagem: "))
velocidade = float(input("Qual a media de velocidade dessa viagem em km/h: "))

distancia = calcular_distancia(tempo, velocidade)
litros_usados = calcular_litros(distancia)

apresentar_resultado(tempo, velocidade, distancia, litros_usados)