from game.director import Director
from game.army import Army
from game.battle import Battle

game = Director()
army1 = Army()
army2 = Army()
battle = Battle()

def main():
    # Starting a new game loop if the player did not type "quit" previously
    while game.answer != "quit":
        print("Welcome to the Lord of the Rings game")
        print()

        # Asking the player to choose army size for both armies
        print("Choose army size for Army 1: ")
        army1.setArmySize()
        print("Choose army size for Army 2: ")
        army2.setArmySize()
        # Asking the user to set soldiers for Army 1
        army1.setSoldiers()
        print("Army 1 completed!")
        print()
        # Asking the user to set soldiers for Army 2
        army2.setSoldiers()
        print("Army 2 completed!")
        print()

        print("To start the battle press any key and hit Enter")
        input()
        print()

        # Calling the battle methods
        battle.selectArmies(army1.soldiers, army2.soldiers)
        battle.startBattle()

        # Letting user to start a new game or quit
        print("To quit the game type 'quit' and hit Enter. If you want to start new game press any key and hit Enter: ")
        print()
        game.answer = input("")

if __name__ == "__main__":
    main()

