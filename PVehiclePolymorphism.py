from abc import ABC, abstractclassmethod

class Ferrari(ABC):
    def creator(self):
        print("Enzo Ferrari")
    def Popularity(self):
        print("In 2022 4,992 were sold in the US")
    def top_selling(self):
        print("The most bought ferrari was the: Ferrari F40")

class BMW(ABC):
    def creator(self):
        print("Karl Rapp, Gustavo Otto, Camillo Castiglioni, Franz Josef Popp")
    def Popularity(self):
        print("In 2022 101,738 were sold in the US")
    def top_selling(self):
        print("The most bought BMW was the: BMW X5")

B = BMW()
F = Ferrari()
print("--------")
for i in (F,B):
    i.creator()
    i.Popularity()
    i.top_selling()
    print("--------")