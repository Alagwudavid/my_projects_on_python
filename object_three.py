import random


class Warrior:
    def __init__(self, name="", health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax
    def attack(self):
        attackAmt = self.blockMax * (random.random() + .5)

        return attackAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
