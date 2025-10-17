class Chai:

    def __init__(self, sweetness, milk):
        self.sweetness= sweetness
        self.milk = milk

    def sip(self):
        print("Sipping Chai")

    def addSugar(self, amount):
        print("sugger added")


my_Chai =  Chai(2, 3)

my_Chai.addSugar(2)
my_Chai.sip()
