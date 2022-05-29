class Silla():
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio
    def infoBasica(self):
        print("Metodo del padre")
        print(f"color: {self.color}, precio: {self.precio}")