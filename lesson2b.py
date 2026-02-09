# Tuple
# A tuple is an immutable type of alist (cannoot change)
# To introduce a tuple you intro a parenthesis

counties =("Nairobi" ,"Mombasa" , "Nakuru", "Garissa", "Embu", "Kirinyaga")
print(counties)
print(type(counties))


#Slicing of tuples
print(counties[3:])

# accessing items of a tuple byy use of the indexes
print(counties[5])

#NOTE-beloow will generate  an error
#Attribute Error
counties.append("nyeri")
print(counties)
