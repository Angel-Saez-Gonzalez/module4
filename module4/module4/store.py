cash = 129.9

quantProducts = {1 : 10, 2 : 4, 3 : 0, 4 : 9}

priceProduct = {1 : 9.99, 2 : 19.9, 3 : 14.99, 4 : 4.99}

"""1"""
def getPriceProduct(code):
    if code in priceProduct.keys():
        return priceProduct[code]
    else:
        return False

"""2"""
def getQuanityProduct(code):
    if code in quantProducts.keys():
        return quantProducts[code]
    else:
        return False

"""3"""
def getDetailProduct(code):
    if code in quantProducts.keys() and priceProduct.keys():
        detailProduct = {quantProducts[code] : priceProduct[code]}
        return detailProduct
    else:
        return False

"""4"""
def getCash():
    return  float(cash)

"""5"""
def addQuantProduct(code, quantity):
    if code in quantProducts.keys():
        sum = quantProducts[code] + quantity
        quantProducts[code] = sum 
        return True
    else:
        return False

def setPriceProduct(code, price):
    
    return


"""getFullStock its made with a list of tuples expl: 
myList = [] 
myList.append(("code",units,price))"""

"""1.getPriceProduct"""
code = int(input("Input the code of the product: "))

if getPriceProduct(code) == False:
    print("The code it's not in the dictionary")
else:
    print("The product costs",getPriceProduct(code))

"""2.getQuanityProduct"""
code = int(input("Input the code of the product: "))

if getQuanityProduct(code) == False:
    print("The code it's not in the dictionary")
else:
    print(getQuanityProduct(code),"products left")

"""3.getDetailProduct"""
code = int(input("Input the code of the product: "))

if getDetailProduct(code) == False:
    print("The code it's not in the dictionary")
else:
    detailProduct = getDetailProduct(code)
    for key, value in detailProduct.items():
        print("For the product with code", code, "there's", key, "left and it costs", value)

"""4.getCash"""
print("Cash:",getCash())

"""5.addQuantProduct"""
code = int(input("Input the code of the product: "))
quantity = int(input("Input the quantity to add: "))

if addQuantProduct(code, quantity) == True:
    print("You have Succesfuly increment the quantity of products!!")
    print(quantProducts[code])
else:
    print("Chupa pija Alvaro")
    
