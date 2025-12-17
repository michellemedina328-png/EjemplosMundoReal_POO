"""
EJEMPLO DEL MUNDO REAL: SISTEMA DE RESERVAS
Autor: [Tu Nombre]
Descripción:
Este programa modela un sistema básico de reservas utilizando
Programación Orientada a Objetos (POO).
Se aplican los principios de:
- Abstracción
- Encapsulamiento
- Interacción entre objetos
"""

# -------------------------------
# CLASE CLIENTE
# -------------------------------
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"


# -------------------------------
# CLASE RESERVA
# -------------------------------
class Reserva:
    def __init__(self, cliente, fecha, lugar):
        self.__cliente = cliente        # Encapsulamiento
        self.__fecha = fecha
        self.__lugar = lugar

    def confirmar_reserva(self):
        print("Reserva confirmada")
        print(self.__cliente.mostrar_datos())
        print(f"Fecha: {self.__fecha}")
        print(f"Lugar: {self.__lugar}")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
def main():
    cliente1 = Cliente("María López", "maria@email.com")
    reserva1 = Reserva(cliente1, "20/06/2025", "Hotel Bolívar")

    reserva1.confirmar_reserva()


if __name__ == "__main__":
    main()
