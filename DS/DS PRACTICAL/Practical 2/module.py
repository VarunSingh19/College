# Aim :- Write a program to display the execution of Tuples. 
# Create a student attendance table to demo the use of  tuples.
from typing import Tuple
import numpy as np
roll_no = (1,2,3)
name =  ("Shweta","Annu" ,"Parth")
Att = ()
DataS = ()
ReTry = True
print("\nStudent attendance :\n") 
DataS = ((roll_no)) , ((name)) 
N = np.matrix(DataS)
print(N)
#print(Att) 
print("\n")
reEntry = input("Do you want add any new entries (Y/N):") 
if reEntry.upper() == "N":
        pass 
else :
    while(ReTry):
     print("\n\t\tInsert new data:") 
     Name = input("Name :") 
     Roll_no = input("Roll NO :")
     N =(str(Name),)
     R = (str(Roll_no),)
     roll_no += tuple(R) 
     name += tuple(N)
     DataS = ((roll_no) , (name)) 
     N = np.matrix(DataS)
     print(N)
     z = input("Continue.. (Y/N)")
     if z.upper() == "Y":
           ReTry = True 
     else:
           ReTry = False
for i in range(0,len(roll_no)):
          log = input(f"(A/P)roll no {roll_no[i]} : ")
          Att+=((roll_no[i],name[i],log.upper()),)
N = np.matrix(Att) 
print("\n") 
print(N)
