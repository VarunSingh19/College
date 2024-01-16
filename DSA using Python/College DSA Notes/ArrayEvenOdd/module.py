def SplitEvenOdd(A):
    evenlist = []
    oddlist = []
    for i in A:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Even List:", evenlist)
    print("Odd List:", oddlist)

# A = []
# n = int(input("Enter the size of the list: "))
# print("Enter the elements of the list:")
# for i in range(n):
#     k = int(input())
#     A.append(k)

# SplitEvenOdd(A)
def SplitEvenOddNum(A):
    evenlist = []
    oddlist = []
    for i in A:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Even List :", evenlist)
    print("Odd List :", oddlist)
A = []
n = int(input("Enter the size of the list :"))
print("Enter the elements of the list:")
for i in range(n):
    k = int(input())
    A.append(k)

SplitEvenOddNum(A)