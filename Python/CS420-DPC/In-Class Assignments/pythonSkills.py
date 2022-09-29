# Write a function that accepts 2 string parameters with one being a file name and one being a text string.  Open the specified file, write the text string to the file, and then close the file.
# ex. myPythonFucntion( filename, userTxtString)
def firstFunction(fileName, textString):
    file = open(fileName, 'w')
    file.write(textString)
    file.close()

firstFunction("C:/Users/liamz/OneDrive/Documents/VSC HolderFolder/VSCode-Project-Files/Python/CS420-DPC/In-Class Assignments/textFile1.txt","chum'd.")

# Write a function that accepts a list of numbers and sorts the values in the list. Any sort algorithm will work (ex. bubble sort).
def secondFunction(numList):
    currentIndex = 0
    isSorted = False
    while not isSorted:
        for number in numList:
            print()
    
# Write a function that accepts 2 numbers. Add, subtract, multiply, and divide the numbers and return all calculated values

# Write a Class titled Animal
class Animal():
    def __init__(self, legCt, sound, isHerbivore, weight):
        self.weight = weight
# This class should contain the following properties 
# number of legs
# sound it makes
# is a vegetarian or not
# weight
# All properties should be protected
# Create Getter/Setter for each property
# create a method "type()" for the Animal class that returns the string "Animal"
# Write a class named Dog and a class named Cat that inherit Animal.
# Set a value for all properties in the constructor
# Override the method "type()" for child class and return the classes type as a string ("Dog" or "Cat")
# Write a function that accepts an Animal object and prints out the type and sound of the Animal
# Use this dictionary to answer the following questions - sampleDict = { "class": { "student": { "name": "Mike", "marks": { "cosc420": 90, "history": 80, "biology":85 } } } } 
# print out the value for the student's name
# loop through all "marks" and print out the class and score
# change the student's name to your own
# add an additional course titled "math" with a score of 100
# update the mark for "cosc420" to 95
# delete the mark for "biology" so it no longer exists


