# Aim :- Write a program in python to display the execution of Sets. 
# Demo the use of sets to display employee records of a company.


employee1 = set(["A","B","C","D"])
employee2 = set(["P","Q","R","S"])
print("Employee Records :")
print(employee1)
print(employee2)
#To add new Employee data in existing set
employee1.add("Tom")
print(employee1)
# to Remove data from set
employee2.discard("Q")
print(employee2)
# To perform Intersection
Intersection = employee1 & employee2
print(Intersection)
# To perform Union
Union = employee1 | employee2
print(Union)
# To find Difference
Difference = employee1 - employee2
print(Difference)
# To check if a given set is subset  or superset of another set
compare1 = employee1 >= employee2
compare2 = employee1 <= employee2
print(compare1)
print(compare2)
