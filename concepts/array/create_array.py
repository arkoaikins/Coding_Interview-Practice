# in python you need to import the array module
# to be able to use arrays

import array

balance = array.array('i', [300,200,100])
print(balance)
# Write comment on how this works
# arrayName = array.array(dataType,[array,items])

# You can a acess a specific value or element using its index
print(balance[0])

# Now let's look at operations that can be done on arrays

# We can add more values to the array
# using  arrayName.insert(index,value)
balance.insert(2, 150)
print(balance)

# You can also delete a value from the array
# Using arrayName.remove(value)
balance.remove(150)
print(balance)

# You can also search for an item in an array based on its value
# using arrayName.index(value)
print(balance.index(200)) # it will output the index of that value

# We also have the `.update` which will update a value at a specific index
balance[1] = 200
print(balance)

# You can also traverse a python array by usung loops 
for x in balance:
    print(x)