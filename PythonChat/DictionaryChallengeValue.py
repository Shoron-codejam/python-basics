fruit_price = {
    "Apple"   : 3,
    "Banana"  : 2,
    "Orange"  : 4
}

print (fruit_price.values())

for value in fruit_price.values():
    print (value)

total = sum(fruit_price.values())
print(total)  

print(f"Total Price : {total}")