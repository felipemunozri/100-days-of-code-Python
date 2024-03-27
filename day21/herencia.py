class Animal:
    
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):  # para heredar basta con agregar entre paréntesis el nombre de la clase de la cual queremos heredar
    
    def __init__(self):
        super().__init__()  # inicializa la clase hija con todos los atributos y métodos de la clase padre super()

    def swim(self):  # método unico de la clase Fish()
        print("moving in water.")

    def breath(self):  # redefinimos el método breath() para Fish(), tomamos el método de la clase super() + un print
        super().breath()
        print("doing this underwater.")


nemo = Fish()
print(nemo.num_of_eyes)
nemo.swim()
nemo.breath()
