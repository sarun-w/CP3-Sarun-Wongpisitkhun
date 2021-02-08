def vatCalculate(totalPrice):
    result = totalPrice + ((totalPrice * 7) / 100)
    return result

priceInput = int(input("Please enter your price: ")) 
print("Your price including vat: ", vatCalculate(priceInput))