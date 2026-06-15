from mascota import Mascota


def main():
	mascota1 = Mascota("Luna", 3, "Perro")
	mascota2 = Mascota("Mia", 2, "Gato")
	mascota3 = Mascota("Paco", 1, "Pájaro")

	mascota1.mostrar_informacion()
	mascota1.hacer_sonido()

	mascota2.mostrar_informacion()
	mascota2.hacer_sonido()

	mascota3.mostrar_informacion()
	mascota3.hacer_sonido()


if __name__ == "__main__":
	main()
