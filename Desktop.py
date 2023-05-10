from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, potenciaDaFonte = None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
    
    def get_modelo(self):
        super().get_modelo
    
    def get_cor(self):
        super().get_cor
    
    def get_preco(self):
        super().get_preco
    
    def get_potenciaDaFonte(self):
        return self._potenciaDaFonte

    def cadastrar(self):
        super().imprimir()
        print("Potencia da Fonte: " + str(self._potenciaDaFonte))
