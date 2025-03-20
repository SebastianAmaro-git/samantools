class Cliente:
    def __init__(self, nombre, edad, cedula, telefono):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Cédula: {self.cedula}, Teléfono: {self.telefono}"