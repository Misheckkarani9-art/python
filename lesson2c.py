# A dictionary iis data type that stores data in terms of  key -value pair
# It is introduceed by by the use of curly baces{}
# The value stored inside of a dictionary can be of any data type
#  To acces the values in  adictionary we use the keys


phonebook ={
    "Joyce" : "0718249788",
    "Mary" : "0741588020",
    "joseph" : "07565757575"
}
print( phonebook)
print(type( phonebook))

#print joyce number
print(phonebook["Joyce"])



players ={
    "Name": "Messi" ,
    "Age" : 40 ,
    "teams" :["Argentina","PSG" ,"Beceloona"],
    "more": {
        "children" : 3,
        "residence" : "us",
        "phone" : ( 2423567353, 252525252, 44255252525)
    }
    

}
print(players["more"] ["phone"] [2])
print(players ["teams"] [1])
