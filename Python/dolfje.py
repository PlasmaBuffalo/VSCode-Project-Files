class Dolfje:
    #this is for Dolfje
    def __init__(self) -> None:
        self.isHungry = True
        self.isHateful = True

    def printCurrentState(self):
        #if hungry, return "eating"
        #else if hateful, return "hating"
        #else return "sleeping"

        if self.isHungry:
            return "eating"
        elif self.isHateful:
            return "hating"
        else:
            return "sleeping"