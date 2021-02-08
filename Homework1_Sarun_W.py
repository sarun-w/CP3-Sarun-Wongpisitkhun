def additionNumber(firstNumber, secondNumber):
    totalNumber = firstNumber + secondNumber
    return totalNumber

def subtractionNumber(firstNumber, secondNumber):
    totalNumber = firstNumber - secondNumber
    return totalNumber

def multiplicationNumber(firstNumber, secondNumber):
    totalNumber = firstNumber * secondNumber
    return totalNumber

def divisionNumber(firstNumber, secondNumber):
    totalNumber = firstNumber / secondNumber
    return totalNumber

def printNumber(numberInput):
    print("Total number: ",numberInput)

print("Enter the numbers you want to addition.")
printNumber(additionNumber(int(input("First number: ")), int(input("Second number: "))))

print("Enter the numbers you want to subtraction.")
printNumber(subtractionNumber(int(input("First number: ")), int(input("Second number: "))))

print("Enter the numbers you want to multiplication.")
printNumber(multiplicationNumber(int(input("First number: ")), int(input("Second number: "))))

print("Enter the numbers you want to division.")
printNumber(divisionNumber(int(input("First number: ")), int(input("Second number: "))))