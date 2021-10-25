list = []

def showMenu():
    print("1.- Add a number to the list")
    print("2.- Add a number in a position in the list")
    print("3.- Show the length of the list")
    print("4.- Delete the last number in the list")
    print("5.- Delete a number in the list")
    print("6.- Count numbers")
    print("7.- Positions of a numbers")
    print("8.- Show the list")
    print("9.- Exit")

    option = int(input("Choose an option: "))
    return option

def addNumber():
    num = int(input("Input a number: "))
    list.append(num)

def addNumberInPosition(num, pos):
    if pos <= len(list):
        list.insert(pos, num)
        return True
    else:
        return False

def printLengthList():
    print("The length of the list is ",len(list))

def getLastElement():
    if len(list) > 0:
        return list.pop()
    
    return False

def deletePos(pos):
    if pos <= len(list):
        return list.pop(pos)
    
    return False

def positionNumber(num):
    iList = []
    pos = 0
    for elem in range(0, list.count(num)):
        index = list.index(num, pos)
        """print(index, end=" ")"""
        iList.append(index)
        pos += 1
    return iList

while True:
    option = int(showMenu())
    if option == 1:
        addNumber()
    
    elif option == 2:
        num = int(input("Input a number: "))
        pos = int(input("Input the position: "))
        if addNumberInPosition(num, pos):
            print("Numer added")
        else:
            print("Index out")

    elif option == 3:
        printLengthList()

    elif option == 4:
        num = getLastElement()
        if num == False:
            print("The list is empty")
        else:
            print("The last element is ", num)
    
    elif option == 5:
        pos = int(input("Input the position: "))
        num = deletePos()
        if num == False:
            print("The posintion dos not exists")
        else:
            print("Deleting the element ", num)
    
    elif option == 6:
        num = int(input("Input a numer: "))
        print("The ocurrences of numer ", num, " is ", list.count(num))

    elif option == 7:
        num = int(input("Input a number: "))
        for i in positionNumber(num):
            print(i, )

        print()
        pos = 0

    elif option == 8:
        for elem in list:
            print(elem, end=" ")
            
        print()

    elif option == 9:
        break
