import random 

def letraNoEncontrada(numError):
    if numError == 1:
        print("()")
    elif numError == 2:
        print("() \n" +
              " |")
    elif numError == 3:
        print(" () \n" +
              "`|´")
    elif numError == 4:
        print(" () \n" +
              "`|´ \n" +
              "/ \\")
        print("PERDISTE")

def comprobarPalabra(letra, palabraSecreta, cadenaAMostrar):
    nuevaCadena = ""
    
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] == letra:
            nuevaCadena += letra + " "
        else:
            nuevaCadena += cadenaAMostrar[i * 2] + " "   

    return nuevaCadena.strip()  



listaPalabras = ["flama", "cerca", "jugar", "tigre", "playa", "volar", "cielo", "fruta"]
palabraSecreta = random.choice(listaPalabras)
palabraAdivinada = False
numErrores = 0
cadenaMostrar = "_ " * len(palabraSecreta)
print("Palabra secreta:", palabraSecreta)

while not palabraAdivinada and numErrores < 4:
    intentoLetra = input("Di una letra: ")

    if intentoLetra in palabraSecreta:
        cadenaMostrar = comprobarPalabra(intentoLetra, palabraSecreta, cadenaMostrar)
        print("Estado actual: " + cadenaMostrar)  
    else:
        numErrores += 1
        letraNoEncontrada(numErrores)
    
    if "_" not in cadenaMostrar or intentoLetra == palabraSecreta:
        print("¡Felicidades! Has adivinado la palabra: " + palabraSecreta)
        palabraAdivinada = True

if numErrores >= 4:
    print("La palabra era " + palabraSecreta)
