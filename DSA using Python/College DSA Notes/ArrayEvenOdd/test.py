def splitEvNOd(A):
    evL = []
    OdL = []
    for i in A:
        if i % 2 == 0:
            evL.append(i)
        else:
            OdL.append(i)
    print("Even List :",evL)
    print("Odd List :",OdL)

a = []
n = int(input("enter the size of the list :"))
print("enter the elements :")
for i in range(n):
    k = int(input())
    a.append(k)
splitEvNOd(a)