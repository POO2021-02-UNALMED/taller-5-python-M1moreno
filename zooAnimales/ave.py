from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self._colorPlumas

    def movimiento(self):
        return "volar"

    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        return aguila