# implement a function that takes a list of numbers as input and returns the average of these numbers.
# def avg(li):
#     avg=0
#     for i in li:
#         avg +=i
#     avg= avg/len(li)
#     print(avg)
# l1= list(map (int,input("enter a list of numbers:").split()))
# avg(l1)

# Create a function that accepts a string and returns the string with all vowels removed.

# def fun(string):
#     res=""
#     for i in string:
#         if i not in ["a","e","i","o","u","A","E","I","O","U"]:
#             res=res+i
#     print(res)
# fun("apple")
            
   
# Develop a function to find and return the maximum value in a given list of integers.

# def max(list):
#     max=list[0]
#     for i in list:
#         if i>max:
#             max=i
#     print(max)
# li=list(map(int, input("enter list of numbers:").split()))
# max(li)



# Design a function that simulates a basic calculator, allowing for addition, subtraction, multiplication, and division based on user input.

# def calculate(n1,n2):
#     print("1.addition")
#     print("2.substraction")
#     print("3.multiplication")
#     print("4.division")
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         print("sum",n1+n2)
#     elif choice==2:
#         print("substraction",n1-n2)
#     elif choice==3:
#         print("multiply",n1*n2)
#     elif choice==4:
#         print("divide",n1/n2)
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# calculate(num1, num2)




# Write a function that takes a list of strings as input and returns the longest string in the list.

# def maxstr(li):
#     mc=0
#     ms=""
#     for i in li:
#         count=0
#         for j in i:
#             count+=1 
#         if mc<count:
#             ms=i
#             mc=count
#     print(ms)
# l1=list(map(str,input("enter list of strings:").split()))
# maxstr(l1)




# Utilize functions to solve a problem of your choice (e.g., calculating the area and perimeter of different shapes, converting units, etc.),
#  demonstrating your understanding of how functions can be applied in various contexts.
# area of square 
def sqarea(side):
    print("area of square:",side*side)
s=int(input("enter lenght od side of square:"))
sqarea(s)

