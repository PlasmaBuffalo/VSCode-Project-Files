# Write a function that accepts 2 string parameters with one being a file name and one being a text string.  Open the specified file, write the text string to the file, and then close the file.
# ex. myPythonFucntion( filename, userTxtString)
from fnmatch import fnmatchcase


def firstFunction(fileName, textString):
    file = open(fileName, 'w')
    file.write(textString)
    file.close()


#firstFunction("Python/CS420-DPC/In-Class Assignments/textFile1.txt", "chum'd.")


# Write a function that accepts a list of numbers and sorts the values in the list. Any sort algorithm will work (ex. bubble sort).
def secondFunction(numList):
    # numList.sort()
    # return numList
    #
    currentIndex = 0
    sorted = False
    while not sorted:
        if currentIndex == len(numList):
            return numList
        currentSmallest = (int)
        numList[currentIndex]
        for number in numList:
            if number < currentSmallest:
                temp = (int)
                numList[currentIndex]
                numList[currentIndex] = number
                number = temp
                currentIndex += 1


#secondFunction([3, 2, 3])
# Write a function that accepts 2 numbers. Add, subtract, multiply, and divide the numbers and return all calculated values


def mathFunction(a, b):
    print('a =', a)
    print('b =', b)
    calcs = [a+b, a-b, a*b, a/b]
    for num in calcs:
        print(num)
    return calcs

# mathFunction(3,5)

# Write a Class titled Animal
class Animal:
    # This class should contain the following properties
    # # All properties should be protected
    def __init__(self, legCt, sound, isHerbivore, weight):
        # number of legs
        self._legCt = legCt
        # sound it makes
        self._sound = sound
        # is a vegetarian or not
        self._isHerbivore = isHerbivore
        # weight
        self._weight = weight
    
    # Create Getter/Setter for each property
    # get/set for legCt
    def getLegCt(self):
        return self._legCt

    def setLegCt(self, newVal):
        self._legCt = newVal

    # get/set for sound
    def getSound(self):
        return self._sound

    def setSound(self, newVal):
        self._sound = newVal

    # get/set for isHerbivore
    def getIsHerbivore(self):
        return self._isHerbivore

    def setIsHerbivore(self, newVal):
        self._isHerbivore = newVal

    # get/set for weight
    def getWeight(self):
        return self._weight

    def setWeight(self, newVal):
        self._weight = newVal

    # create a method "type()" for the Animal class that returns the string "Animal"
    def type(self):
        #I think you meant this commented version, but 
        #return
        return self.__name__
        

# Write a class named Dog and a class named Cat that inherit Animal.
# Set a value for all properties in the constructor
class Dog(Animal):
    def __init__(self, legCt, sound, isHerbivore, weight):
        super().__init__(legCt, sound, isHerbivore, weight)
    
    def type(self):
        return self.__name__


class Cat(Animal):
    def __init__(self, legCt, sound, isHerbivore, weight):
        super().__init__(legCt, sound, isHerbivore, weight)
        
    def type(self):
        return self.__name__

# Write a function that accepts an Animal object and prints out the type and sound of the Animal
def animalSoundFind(thing):
    print(thing.getSound())

tux = Cat(4, "meow", False, 10)
animalSoundFind(tux)

# Use this dictionary to answer the following questions
sampleDict = {"class": {
    "student": {
        "name": "Mike",
        "marks": {
                "cosc420": 90,
                "history": 80,
                "biology": 85
        }
    }
}
}
# print out the value for the student's name
print ("Name", sampleDict["class"]["student"]["name"])
# loop through all "marks" and print out the class and score
for thing in sampleDict["class"]["student"]["marks"]:
    print(thing+" grade = "+str(sampleDict["class"]["student"]["marks"][thing]))
# change the student's name to your own
sampleDict["class"]["student"]["name"] = "Liam"
# add an additional course titled "math" with a score of 100
sampleDict["class"]["student"]["marks"]["math"]=100
# update the mark for "cosc420" to 95
sampleDict["class"]["student"]["marks"]["cosc420"]=95
# delete the mark for "biology" so it no longer exists
del sampleDict["class"]["student"]["marks"]["biology"]

print(sampleDict)