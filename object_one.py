class Boy:
    def __init__(self, name="", height=0.0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} runs".format(self.name))
    def feats(self):
        print("{} is {}ft tall".format(self.name, self.height))
    def features(self):
        print(f'{self.name} is {self.height}ft tall and has a weight of {self.weight}kg')

def main():
    david = Boy("David", 6.1, 72)
    david.run()
    david.feats()
    david.features()
main()