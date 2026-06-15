class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("\nInformación de la mascota registrada:\n")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Especie: {self.especie}")
        print("\nLos datos se han registrado correctamente.\n")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

        especie = self.especie.lower()
        if especie == "perro":
            print("Guau guau!")
        elif especie == "gato":
            print("Miau miau!")
        elif especie == "pájaro" or especie == "ave":
            print("Pío pío!")
        else:
            print("Sonido desconocido para esta especie.")

