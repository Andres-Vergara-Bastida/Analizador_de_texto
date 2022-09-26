print ("Bienvenido al analizador de texto \n")

texto = input("escribe el texto que quieras: \n".lower())

letra1 = input("escribe una letra que quieras: \n".lower())
letra2 = input("escribe otra letra que quieras: \n".lower())
letra3 = input("escribe una letra mas que quieras: \n".lower())

letras = [letra1,letra2,letra3]

lista_texto = texto.split()
contador_texto = len(lista_texto)

primera_letra = texto[0]
ultima_letra = texto[-2]

contador1 = texto.count(letra1)
contador2 = texto.count(letra2)
contador3 = texto.count(letra3)

lista_texto.reverse()
texto_invertido = " ".join(lista_texto)

python = "python"
busqueda_python = python in lista_texto

print("\n")
print("La letra " + letra1 + " aparece " + str(contador1) + " veces\n")
print("\n")
print("La letra " + letra2 + " aparece " + str(contador2) + " veces\n")
print("\n")
print("La letra " + letra3 + " aparece " + str(contador3) + " veces\n")
print("\n")
print("Este texto tiene " + str(contador_texto) + " palabras\n")
print("\n")
print(primera_letra + " Es la primera letra del texto, y " + ultima_letra + " es la ultima letra del texto\n")
print("\n")
print("Así se ve tu texto del reves\n" + texto_invertido)
print("\n")

if busqueda_python is False:
    print("La palabra ""python"" no aparece en este texto")
else:
    print("la palabra ""python"" aparece en este texto")



