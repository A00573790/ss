temperatura = float(input("inserta la temperatura de ruby: "))
riego = input("que dia es hoy?: ")
humedad = input("inserte el porcentaje de humedad: ")

if temperatura <= 20:
  print("llevala adentro rapido")
elif temperatura == 23:
  print("buenas condiciones")
else:
  print("ponla frente al ventilador")

if riego == "martes" or riego == "jueves" or riego == "sabados":
  print("regar a rubi")
else:
  print("todo bien :)")

if humedad == 20:
  print("humedad adecuada")
elif temperatura < 20:
  print("redebes regar a rubi")
else:
  print("no es necesario regar a rubi")
