# Problem solving Questions: 

# 1. Write a python program to remove the duplicate in given list.
#                 a = [2,3,4,2,3,4,5,7]
#                 output: [2,3,4,5,7]

# def fun(num):
#     li=set(num)
#     print(list(li))
# a = [2,3,4,2,3,4,5,7]
# fun(a)

# def fun(num):
#     uni=[]
#     for i in num:
#         if i not in uni:
#             uni.append(i)
#     print(uni)
# a = [2,3,4,2,3,4,5,7]
# fun(a)   






# 2. Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.

#               Testcase1	:  [ 7, 4, 7, 23, 10, 6]
#                Output     	:  4 10 6


# def fun(num):
#     for i in num:
#         num1=i+1
#         count=0
#         for j in range(1,num1+1):
#             if num1%j==0:
#                 count +=1
#         if count==2:
#             print(i,end=" ")
# fun([ 7, 4, 7, 23, 10, 6])




# 3. Write python program 
#               a   = " aaabbaaccdd"
#              output: "a5b2c2d2"


a   = "aaabbaaccdd"
res=""
aset=[]
for i in a:
    if i not in aset:
        aset.append(i)

for i in aset:
    res+=i + str(a.count(i))
print(res)





