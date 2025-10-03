# ESEMPIO MACCHINE
class Car:
    # costruttore: costruisce l'oggetto
    # definendo i suoi attributi e inizializzandoli
    def __init__(self):
        self.licensePlate = 0
        self.bodyColor = ''
        self.turnedOn = False

    def paint(self, color):
        self.bodyColor = color     # cambio colore

    def turnOn(self):
        self.turnedOn = True

c = Car()

# posso accedere agli attributi dell'oggetto c con la notazione puntata, scrittura e lettura

c.licensePlate = 'AB123CD'
c.paint('red')
c.turnOn()


