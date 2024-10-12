class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def agregarEstudiante(listaEstudiantes):
    nombreEstudiante = input("Ingresa el nombre del nuevo estudiante \n")
    edad = input("Ingresa la edad del nuevo estudiante \n")
    estudiante = Estudiante(nombreEstudiante, edad)
    listaEstudiantes.append(estudiante)

def mostrarLista(listaEstudiantes):
    for i in listaEstudiantes:
        print("Nombre: " + i.nombre + " Edad:" + i.edad)

def buscarEstudiante(nombre, edad):
    for i in listaEstudiantes:
        if i.nombre == nombre and i.edad == edad:
            return True
    return False

def eliminarEstudiante(estudianteAEliminar, edadAEliminar, listaEstudiantes):
    nuevaLista = []
    if (buscarEstudiante(estudianteAEliminar, edadAEliminar)):
        for i in listaEstudiantes:
            if i.nombre != estudianteAEliminar and i.edad != edadAEliminar:
                nuevaLista.append(i)
    return nuevaLista
        
    

quiereSalir = False
listaEstudiantes = []

while not quiereSalir:
    opcion = int(input("1- Agregar estudiante \n" +
                       "2- Ver lista de estudiantes \n" +
                       "3- Buscar estudiante \n" +
                       "4- Eliminar estudiante \n" +
                       "5- Salir \n"))
    
    if opcion == 5:
        quiereSalir = True
    elif opcion == 1:
        agregarEstudiante(listaEstudiantes)
    elif opcion == 2:
        mostrarLista(listaEstudiantes)
    elif opcion == 3:
        nombreABuscar = input("Nombre del estudiante a buscar \n")
        edadABuscar = input("Ingresa la edad del nuevo estudiante \n")

        if buscarEstudiante(nombreABuscar, edadABuscar):
            print("Existe")
        else:
            print("No existe ese estudiante")
    elif opcion == 4:
        estudianteAEliminar = input("Estudiante a eliminar")
        edadAEliminar = input("Ingresa la edad del estudiante a eliminar \n")

        listaEstudiantes = eliminarEstudiante(estudianteAEliminar, edadAEliminar, listaEstudiantes)
        for i in listaEstudiantes:
            print("Nombre: " + i.nombre + " Edad:" + i.edad)