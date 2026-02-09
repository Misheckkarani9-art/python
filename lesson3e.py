#Below is a grading statement based on what a student would have gotten
marks = int(input("enter students marks: "))
# print("entered marks is " ,marks)
if marks >0 and marks < 30:
    print("below average")
elif marks >= 30 and marks < 40 :
    print("Average")
elif marks >= 40 and marks < 70 :
    print("above Average")
elif marks >= 70 and marks <= 100 :
    print("excellent") 
else:
    print("invalid input")