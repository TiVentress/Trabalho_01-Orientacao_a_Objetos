from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, tempoDeBateria = None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def get_modelo(self):
        super().get_modelo
    
    def get_cor(self):
        super().get_cor
    
    def get_preco(self):
        super().get_preco
    
    def get_tempoDeBateria(self):
        return self.__tempoDeBateria

    def cadastrar(self):
        super().imprimir()
        print("Tempo de Bateria: " + str(self.__tempoDeBateria))