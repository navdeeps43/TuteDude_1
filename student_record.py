student = {
            'harry' : 'A', 
            'garry' : 'B', 
            'larry' : 'C'
          }
a= (int(input(" Enter 1 to add new student \n Enter 2 to Update student's greade \n Enter 3 to print all Student \n")))

if a == 3:
    print (student)
elif a ==2:
    name=input("Enter student's name \n")
    grade=input("Enter the new grade \n")
    student[name]=grade
    print (student)
elif a==1:
    name=input("Enter new student name\n")
    grade=input("Enter the greade of new student\n")
    student[name]=grade
    print (student)
else:
    print ("Invalid option selected")

