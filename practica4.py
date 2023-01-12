inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
bono = 2400

while True:
    puntuacion = float(input("Introduce tu puntuacion:"))

    if puntuacion == inaceptable:
        nivel = "inaceptable"
        resultado = inaceptable * bono 
        print (f"Tu nivel es: {nivel} tu bono es de {resultado}:") 
        break
    elif puntuacion == aceptable:
        nivel = "Aceptable"
        resultado = aceptable * bono
        print (f"Tu nivel es: {nivel} tu bono es de {resultado}:") 
        break
    elif puntuacion == meritorio:
        nivel = "Meritorio"
        resultado = meritorio * bono
        print (f"Tu nivel es: {nivel} tu bono es de {resultado}:") 
        break
    else:
        print("La puntuación es incorrecta")