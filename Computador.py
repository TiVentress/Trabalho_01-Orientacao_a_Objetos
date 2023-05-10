from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo = None, cor = None, preco = None):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def get_modelo(self):
        return self.modelo
    
    def get_cor(self):
        return self.cor
    
    def get_preco(self):
        return self.preco
        
    def imprimir(self):
        print("Modelo: " + self.modelo)
        print("Cor: " + self.cor)
        print("Preco: " + str(self.preco))
    
    @abstractmethod
    def cadastrar(self):
        pass