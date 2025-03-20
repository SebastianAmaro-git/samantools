class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.herramientas = []
        self.total = 0

    def agregar_herramienta(self, herramienta, cantidad):
        self.herramientas.append((herramienta, cantidad))
        self.total += herramienta.precio * cantidad

    def aplicar_descuentos(self):
        descuento = 0
        if self.es_numero_abundante(self.cliente.edad):
            descuento += 0.10 * self.total
        if self.es_numero_primo(int(self.total)):
            descuento += 0.10 * self.total
        return descuento

    def es_numero_abundante(self, numero):
        def suma_divisores(n, divisor=1, suma=0):
            if divisor >= n:
                return suma
            if n % divisor == 0:
                suma += divisor
            return suma_divisores(n, divisor + 1, suma)

        return suma_divisores(numero) > numero

    def es_numero_primo(self, numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def generar_factura(self):
        descuento = self.aplicar_descuentos()
        total_final = self.total - descuento
        factura_str = f"Factura para: {self.cliente}\n"
        factura_str += "Herramientas compradas:\n"
        for herramienta, cantidad in self.herramientas:
            factura_str += f"{herramienta} - Cantidad: {cantidad}\n"
        factura_str += f"Total: {self.total}\n"
        factura_str += f"Descuento: {descuento}\n"
        factura_str += f"Total a pagar: {total_final}\n"
        return factura_str