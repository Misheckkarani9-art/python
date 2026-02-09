# python lists
# Alist in python is a collection of items that ordereed in a certain way.
#A list is in introduced by the use of a square brackets []
# The ooioitems of a lists are stored einside of indexes. NNote :In programming we start counting from index zero(0)
# Alist is mutable i.e the contents of a list ca be changed

cars = ["BMW", "BENZE" ,"PRADO", "MClaren" , "Range" ,"Probox" , "Hiace"]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("the car on index is" , cars[3])

# list slicing - This is creating alist from agiven bigger list

print(cars[4:])
print(cars [0:4])
print(cars[2:5])


#list mutability
# we use the function append to add an item at the end of a list

cars.append("subaru")
cars.append("mercedes")
print(cars)


#we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# we can use azn index to add items to a list
cars[5] = "Pajero"

# we use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)


