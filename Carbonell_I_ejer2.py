#Escriba un programa contenga una función llamada curvi(letra_mayuscula). Curvi recibe
#una letra mayúscula y devuelve 0 si la letra no contiene curvas y 1 si las contiene. Por
#ejemplo A no contiene curvas pero B si las contiene. Incluya la letra Ñ. Si la letra es
#minúscula devuelve siempre 0.


def curvi(letra_mayuscula=input("Introduce una palabra: ")):
  list = ["A", "E", "I", "O", "U"]
  if letra_mayuscula in ["O", "U",]:
    return 1
  else:
    return 0

curvi()
