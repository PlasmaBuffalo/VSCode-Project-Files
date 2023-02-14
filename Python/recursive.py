# write a method that recursively calculates the number of 8's in a number provided as a parameter
def count8s(num):
    if num == 0:
        return 0
    elif num % 10 == 8:
        return 1 + count8s(num // 10)
    else:
        return count8s(num // 10)

#same as count8s, but this time, the 8's adjacent to each other are counted as an extra 8
def count8s2(num):
    if num == 0:
        return 0
    elif num % 10 == 8:
        if num % 100 == 88:
            return 2 + count8s2(num // 10)
        else:
            return 1 + count8s2(num // 10)
    else:
        return count8s2(num // 10)

# given a string, recursively separate each pair of identical characters by inserting a * between them
def pairStar(string):
    if len(string) == 1:
        return string
    elif string[0] == string[1]:
        return string[0] + "*" + pairStar(string[1:])
    else:
        return string[0] + pairStar(string[1:])

# given an array of ints, compute recursively if the array contains somewhere a value followed later by that value times 10
def TimesTen(array, index) -> bool:
    if index == len(array) - 1:
        return False
    elif array[index] * 10 == array[index + 1]:
        return True
    else:
        return TimesTen(array, index + 1)

#recursively calculate the number of times a pair of characters appear in a string
def countPairs(string):
    if len(string) < 3:
        return 0
    elif string[0] == string[2]:
        return 1 + countPairs(string[1:])
    else:
        return countPairs(string[1:])

# given a string, recursively count the number of times "11" appears in the string, but only when they are not overlapped
def count11s(string):
    if len(string) < 2:
        return 0
    elif string[0:2] == "11":
        return 1 + count11s(string[2:])
    else:
        return count11s(string[1:])

#given a string, recursively count the number of times "hi" appears in the string, but only when not after an "x"
def countHi2(string):
    if len(string) < 2:
        return 0
    elif string[0:2] == "hi":
        return 1 + countHi2(string[2:])
    elif string[0:3] == "xhi":
        return countHi2(string[3:])
    else:
        return countHi2(string[1:])

#given a string and some substring, compute recursively the number of times that the substring appears in the string without overlapping
def strCount(string, substring):
    if len(string) < len(substring):
        return 0
    elif string[0:len(substring)] == substring:
        return 1 + strCount(string[len(substring):], substring)
    else:
        return strCount(string[1:], substring)

#given a string and a non-empty substring, compute recursively the largest substring which starts and ends with sub and return its length
def strDist(string, substring):
    if len(string) < len(substring):
        return 0
    elif string[0:len(substring)] == substring and string[len(string) - len(substring):] == substring:
        return len(string)
    elif string[0:len(substring)] == substring:
        return strDist(string[0:len(string) - 1], substring)
    else:
        return strDist(string[1:], substring)

#given an array of ints, compute recursively if the array contains a 2.
def has2(array, index) -> bool:
    if index == len(array):
        return False
    elif array[index] == 2:
        return True
    else:
        return has2(array, index + 1)

#main method to test the methods above and print the results
def main():
    print("count8s(8818):", count8s(8818))
    print("count8s2(8818):", count8s2(8818))
    print("pairStar(\"hello\"):", pairStar("hello"))
    print("TimesTen([1, 2, 10, 10, 10], 0):", TimesTen([1, 2, 10, 10, 10], 0))
    print("countPairs(\"axa\"):", countPairs("axa"))
    print("count11s(\"111\"):", count11s("111"))
    print("countHi2(\"ahixhi\"):", countHi2("ahixhi"))
    print("strCount(\"catcowcat\", \"cat\"):", strCount("catcowcat", "cat"))
    print("strDist(\"catcowcat\", \"cat\"):", strDist("catcowcat", "cat"))
    print("has2([1, 2, 3], 0):", has2([1, 2, 3], 0))
    
main()