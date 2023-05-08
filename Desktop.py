from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, potenciaDaFonte = None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
    
    def getInformacoes(self):
        super().getInformacoes()
        print("Potencia da Fonte: " + str(self._potenciaDaFonte))
