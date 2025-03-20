class Herramienta:
    def __init__(self, marca, color, precio, tipo):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"Herramienta: {self.marca}, Color: {self.color}, Precio: {self.precio}, Tipo: {self.tipo}"


class HerramientaPlomeria(Herramienta):
    def __init__(self, marca, color, precio, pulgadas, ajustable, requiere_mantenimiento):
        super().__init__(marca, color, precio, "Plomería")
        self.pulgadas = pulgadas
        self.ajustable = ajustable
        self.requiere_mantenimiento = requiere_mantenimiento


class HerramientaHerreria(Herramienta):
    def __init__(self, marca, color, precio, calor_soportado):
        super().__init__(marca, color, precio, "Herrería")
        self.calor_soportado = calor_soportado


class HerramientaCarpinteria(Herramienta):
    def __init__(self, marca, color, precio, anos_garantia):
        super().__init__(marca, color, precio, "Carpintería")
        self.anos_garantia = anos_garantia