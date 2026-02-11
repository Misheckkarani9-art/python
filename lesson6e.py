# On the try and except block: You run some codes / and if it is successful the try block will get executed other the  except block will 


try:
    number = 100

    answer = number / 0

    print("the answer is:" , answer)
except Exception as e :
   print("There is an error: " , e)