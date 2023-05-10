from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

obj1 = Desktop("Desktop", "Preto", "5.000", "220w")
print('-' * 25)
obj1.imprimir()
print('-' * 25)
obj1.cadastrar()
print('-' * 25)

obj2 = Notebook("Notebook", "Branco", "6.000", "3 horas")
obj2.imprimir()
print('-' * 25)
obj2.cadastrar()
print('-' * 25)

obj3 = Desktop("Desktop", "Rosa", "4.000", "110w")
obj3.imprimir()
print('-' * 25)
obj3.cadastrar()
print('-' * 25)

obj4 = Notebook("Notebook", "Cinza", "7.000", "5 horas")
obj4.imprimir()
print('-' * 25)
obj4.cadastrar()
print('-' * 25)