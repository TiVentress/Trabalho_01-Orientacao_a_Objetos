from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, tempoDeBateria = None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        super().getInformacoes()
        print("Tempo de Bateria: " + str(self.__tempoDeBateria))