from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def isPelaje(self):
        return self._pelaje

    def setPatas(self, patas):
        self._patas = patas

    def getPatas(self):
        return self._patas

    @classmethod
    def cantidadMamiferos(self):
        return len(Mamifero._listado)

    @classmethod
    def crearCaballo(self, nombre, edad, genero):
        Mamifero.caballos += 1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return caballo

    @classmethod
    def crearLeon(self, nombre, edad, genero):
        Mamifero.leones += 1
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        return leon
