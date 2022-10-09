class Army: 

    # Initiating the Army class. The purpose of the Army class is to create a new army object that will store the size of the army and the solders that we add to it.
    def __init__(self):
        self.soldiers = []
        self.size = 0
    
    # Setting army size by asking user to submit the input which will then be converted to integer
    def setArmySize(self):
        self.size = int(input("Pick army size: "))
        print()
    
    # Letting user add more soldiers to his army array
    def setSoldiers(self):
        currentSize = 0
        while currentSize < self.size:
            currentSize += 1
            print("Choose the next soldier by typing either Hobbit, Elf or Orc: ")
            print()
            self.soldiers.append(input())
            print()