from silla import Silla

class TipoGamer(Silla):
    def __init__(self, color, precio, edicion):
        super().__init__(color, precio)
        self.edicion = edicion
    def infoExtendida(self):
        print("Metodo del hijo")
        print(f"color: {self.color}, precio: {self.precio}, edicion: {self.edicion}")