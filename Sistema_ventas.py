from Cliente import Cliente
from Factura import Factura
from Herramienta import HerramientaPlomeria, HerramientaHerreria, HerramientaCarpinteria

class SistemaVentas:
    def __init__(self):
        self.clientes = []
        self.ventas = []

    def agregar_cliente(self, nombre, edad, cedula, telefono):
        cliente = Cliente(nombre, edad, cedula, telefono)
        self.clientes.append(cliente)
        return cliente

    def agregar_factura(self, factura):
        self.ventas.append(factura)

    def mostrar_estadisticas(self):
        num_clientes = len(self.clientes)
        print(f"Número de clientes diferentes que compraron productos: {num_clientes}")

        if not self.ventas:
            print("No hay ventas registradas.")
            return

        total_por_tipo = {}
        cantidad_por_tipo = {}

        for factura in self.ventas:
            for herramienta, cantidad in factura.herramientas:
                tipo = herramienta.tipo
                if tipo not in total_por_tipo:
                    total_por_tipo[tipo] = 0
                    cantidad_por_tipo[tipo] = 0
                total_por_tipo[tipo] += herramienta.precio * cantidad
                cantidad_por_tipo[tipo] += cantidad

        print("\nPromedio de compra por tipo de herramienta:")
        for tipo, total in total_por_tipo.items():
            promedio = total / cantidad_por_tipo[tipo]
            print(f"{tipo}: {promedio:.2f} $")

        print("\nTotal facturado por tipo de herramienta:")
        for tipo, total in total_por_tipo.items():
            print(f"{tipo}: {total:.2f} $")