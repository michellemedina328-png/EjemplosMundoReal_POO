"""
EJEMPLO DEL MUNDO REAL: TIENDA VIRTUAL
Autor: [Tu Nombre]
Descripción:
Este programa representa una tienda virtual utilizando POO.
Permite crear productos y calcular el total de una compra.
Se aplican:
- Encapsulamiento
- Métodos de clase
- Interacción entre objetos
"""

# -------------------------------
# CLASE PRODUCTO
# -------------------------------
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio  # Encapsulamiento

    def get_precio(self):
        return self.__precio

    def mostrar_producto(self):
        return f"{self.nombre} - ${self.__precio}"


# -------------------------------
# CLASE CARRITO
# -------------------------------
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.get_precio()
        return total

    def mostrar_compra(self):
        print("Productos en el carrito:")
        for p in self.productos:
            print(p.mostrar_producto())
        print(f"Total a pagar: ${self.calcular_total()}")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
def main():
    prod1 = Producto("Laptop", 800)
    prod2 = Producto("Mouse", 20)

    carrito = Carrito()
    carrito.agregar_producto(prod1)
    carrito.agregar_producto(prod2)

    carrito.mostrar_compra()


if __name__ == "__main__":
    main()
