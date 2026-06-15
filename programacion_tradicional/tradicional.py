from optparse import Option

#funcion para registrar una mascota
def registrar_mascota():
    print("\n Registre su mascota")

    nombre=input("Ingrese el nombre de su mascota: ")
    edad=input("Ingrese la edad de su mascota: ")
    raza=input("Ingrese la raza de su mascota: ")
    dueño=input("Ingrese el nombre del dueño de la mascota: ")

    #almacenar datos de la mascota
    mascota={
        "nombre": nombre,
        "edad": edad,
        "raza": raza,
        "dueño": dueño
    }

    return mascota

#mostrar informacion de la mascota
def mostrar_mascota(mascota):
    print("\n Información de la mascota registrada:\n")
    print(f"Nombre: {mascota['nombre']}")
    print(f"Edad: {mascota['edad']}")
    print(f"Raza: {mascota['raza']}")
    print(f"Dueño: {mascota['dueño']}")
    print("\n Los datos se han registrado correctamente.\n")

#funcion del tipo menu para interactuar con el usuario
def main():
        
        print("\n Menú de opciones:")
        print("1. Registrar una mascota")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mascota = registrar_mascota()
            mostrar_mascota(mascota)
        elif opcion == "2":
            print("Saliendo del programa")

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

#ejecucion del programa
if __name__ == "__main__":   
    main()

