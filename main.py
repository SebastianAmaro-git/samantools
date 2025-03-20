from Sistema_ventas import SistemaVentas, Factura
from Herramienta import HerramientaPlomeria, HerramientaHerreria, HerramientaCarpinteria

def mostrar_menu():
    print("\n--- Sistema de Gestión de Ventas de Saman Tools ---")
    print("1. Agregar Cliente")
    print("2. Realizar Compra")
    print("3. Ver Estadísticas")
    print("4. Salir")

def main():
    sistema = SistemaVentas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            edad = int(input("Ingrese la edad del cliente: "))
            cedula = input("Ingrese el número de cédula del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = sistema.agregar_cliente(nombre, edad, cedula, telefono)
            print(f"Cliente agregado: {cliente}")

        elif opcion == "2":
            if not sistema.clientes:
                print("No hay clientes registrados. Agregue un cliente primero.")
                continue

            print("Seleccione un cliente:")
            for i, cliente in enumerate(sistema.clientes):
                print(f"{i + 1}. {cliente.nombre}")

            cliente_index = int(input("Seleccione el número del cliente: ")) - 1
            cliente = sistema.clientes[cliente_index]

            factura = Factura(cliente)

            while True:
                tipo_herramienta = input("Ingrese el tipo de herramienta (plomería, herrería, carpintería): ").lower()
                marca = input("Ingrese la marca de la herramienta: ")
                color = input("Ingrese el color de la herramienta: ")
                precio = 0

                if tipo_herramienta == "plomería":
                    precio = 50
                    pulgadas = input("Ingrese las pulgadas: ")
                    ajustable = input("¿Es ajustable? (sí/no): ").lower() == "sí"
                    requiere_mantenimiento = input("¿Requiere mantenimiento? (sí/no): ").lower() == "sí"
                    herramienta = HerramientaPlomeria(marca, color, precio, pulgadas, ajustable, requiere_mantenimiento)

                elif tipo_herramienta == "herrería":
                    precio = 40
                    calor_soportado = input("Ingrese el calor soportado (grados Celsius): ")
                    herramienta = HerramientaHerreria(marca, color, precio, calor_soportado)

                elif tipo_herramienta == "carpintería":
                    precio = 30
                    anos_garantia = input("Ingrese los años de garantía: ")
                    herramienta = HerramientaCarpinteria(marca, color, precio, anos_garantia)

                else:
                    print("Tipo de herramienta no válido.")
                    continue

                cantidad = int(input("Ingrese la cantidad: "))
                factura.agregar_herramienta(herramienta, cantidad)

                continuar = input("¿Desea agregar otra herramienta? (sí/no): ").lower()
                if continuar != "sí":
                    break

            print(factura.generar_factura())
            sistema.agregar_factura(factura)

        elif opcion == "3":
            sistema.mostrar_estadisticas()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
