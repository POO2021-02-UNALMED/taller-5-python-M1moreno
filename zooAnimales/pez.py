from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self._colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def movimiento(self):
        return "nadar"

    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        return salmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        return bacalao