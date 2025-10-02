# ESEMPIO MACCHINE
class Car:
    # costruttore: costruisce l'oggetto
    # definendo i suoi attributi e inizializzandoli
    def __init__(self):
        self.licensePlate = 0
        self.bodyColor = ''
        self.turnedOn = False


c = Car()

# posso accedere agli attributi dell'oggetto

c.licensePlate = 'AB123CD'
print(c.licensePlate)
