class Battle: 
    # Initiating the Battle class. The purpose of the Battle calss is to create the battle object that will store the participating armies' arrays and keep the score.
    def __init__(self):
        self.army1 = []
        self.army2 = []
        self.score1 = 0
        self.score2 = 0
    
    # Select armies for battle
    def selectArmies(self, x, y):
        self.army1 = x
        self.army2 = y

    # Start battle
    def startBattle(self):
        print("The battle starts between Army 1:")
        print()
        for soldier in self.army1:
            print(soldier)
        print()
        print("and Army 2:")
        print()
        for soldier in self.army2:
            print(soldier)
        print()
        # Looping through the first array and then the second army array to make sure each Army 1 soldier fights each of the Army 2 soldiers
        for soldier1 in self.army1:
            for soldier2 in self.army2:
                if soldier1 == "Hobbit" and soldier2 == "Hobbit":
                    print("- No damage was exchanged between the two hobbits")
                elif soldier1 == "Hobbit" and soldier2 == "Orc":
                    print("- Orc damaged Hobbit")
                    self.score2 += 1
                elif soldier1 == "Hobbit" and soldier2 == "Elf":
                    print("- Hobbit damaged Elf")
                    self.score1 += 1
                elif soldier1 == "Orc" and soldier2 == "Hobbit":
                    print("- Orc damaged Hobbit")
                    self.score1 += 1
                elif soldier1 == "Orc" and soldier2 == "Orc":
                    print("- No damage was done between the two orcs")
                elif soldier1 == "Orc" and soldier2 == "Elf":
                    print("- Elf damaged damaged Orc")
                    self.score2 += 1
                elif soldier1 == "Elf" and soldier2 == "Hobbit":
                    print("- Hobbit damaged Elf")
                    self.score2 += 1
                elif soldier1 == "Elf" and soldier2 == "Orc":
                    print("- Elf damaged damaged Orc")
                    self.score1 += 1
                elif soldier1 == "Elf" and soldier2 == "Elf":
                    print("- No damage was done between the two elves")
        print()
        print("Army 1 has score " + str(self.score1))
        print("Army 2 has score " + str(self.score2))
        print()
        # Comparing the scores and determining the winner
        if self.score1 > self.score2:
            print("Army 1 won")
        elif self.score1 < self.score2:
            print("Army 2 won")
        else:
            print("The battle ended in a tie")
            