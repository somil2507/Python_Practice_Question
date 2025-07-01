data = [{'item' : 'apple', 'quantity' : 10, 'price' : 0.5}, {'item' : 'banana', 'quantity' : 5, 'price' : 0.3}, 
        {'item' : 'orange', 'quantity' : 7, 'price' : 0.8}]

revenues = {}

for fruits in data:
    fruit = fruits['item']
    total_revnue = round(fruits['quantity'] * fruits['price'])

    if fruit in revenues:
        revenues[fruit] = revenues[fruit] + total_revnue

    else:
        revenues[fruit] = total_revnue

print(revenues)            
 