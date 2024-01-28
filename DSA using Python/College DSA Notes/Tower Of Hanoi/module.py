# Program to find factorial of number using Recursion.
def FirstProblem1():
    def factorial(n):
        if n == 1:
            return n
        else:
            return n * factorial (n-1)
    num = int(input("Enter Any Number :"))
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        print("The factorial of ", num, " is ", factorial(num))

# Program to find factorial of number using Iterative Method.
def FirstProblem2():
    num = int(input("Enter any number: "))
    factorial = 1

    if num < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i

        print("The factorial of", num, "is", factorial)

# Program to find Fibonacci Series of a number.
def SecondProblem1():
    def Recursive_Fibonacci(n):
        if n <= 1:
            return n
        else:
            return (Recursive_Fibonacci(n-1)+Recursive_Fibonacci(n-2))
        
    nterms = int(input("Enter range :"))
    if nterms <=0:
        print("enter the positive integer..")
    else:
        print("Fibonacci sequence :")
        for i in range(nterms):
            print(Recursive_Fibonacci(i))

# Program for Tower Of Hanoi.
def ThirdProblem1():
    def Tower_of_honai(n,from_rod,to_rod,aux_rod):
        if n == 1:
            print("Move disk 1 from rod ", from_rod, " to rod ", to_rod)
            return
        Tower_of_honai(n-1,from_rod,to_rod,aux_rod)
        print("Move disk ", n ," from rod ", from_rod, " to rod ", to_rod)
        Tower_of_honai(n-1,aux_rod,to_rod,from_rod)

    n = int(input("Enter the number of disks :"))
    Tower_of_honai(n,'A','B','C')

FirstProblem1()
FirstProblem2()
SecondProblem1()
ThirdProblem1()