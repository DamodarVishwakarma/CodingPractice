# def sum(list):
#     return list[0] + list[1] + list[2] + list[3]
# list = [5, 6, 78, 8]
# print(sum(list))
#
# reverse any string
# str=input("Enter your string")
# print(str[::-1])
#
# function to check number is in given range or not
# N=int(input("Enter your number"))
# def range(n):
#     if N<=n:
#        print ("N is in given range")
#     else:
#        print("N is not in range")
# range(10)
#
# check even number is in given list
# def app(l):
#     for i in l:
#         if i % 2 == 0:
#             return app(l)
#         else:
#             pass
#
#
# l = [2, 3, 5, 66, 777, 4, 6]
# print(app(l))
#
# swapping of two numbers
# a=4
# b=3
# a,b=b,a
# print(a)
# print(b)
# 0R
#
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# x=x+y
# y=x-y
# x=x-y  OR
#
# temp=x
# x=y
# y=temp   OR
# print("value of x after swapping:",x)
# print("value of y after swapping:",y)
#
#
# def fib(n):
#     if n == 1 or n==0:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(3))
#
# BUBBLE SORT
#
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [4, 7, 35, 6, 77, 8, 9, 4]
# bubbleSort(arr)
# for i in range(len(arr)):
#     print(arr[i], end=" ")
#
# STAR PRINTING
# n=5
# for i in range(5):
#     print("*" * (i+1))
#
# n=8
# for i in range(9,0,-1):
#  for j in range(0,i-1):
#     print("*",end="")
#  print(" ")
#
# rows=int(input("Enter number of rows"))
# k=rows*2-2
# for i in range(0,rows):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-2
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("")
#
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#         print(" ")
#     i=i+1
#
# MINIMUM AND MAXIMUM ELEMENT IN ARRAY
# def getMin(arr, n):
#     res = arr[0]
#     for i in range(1, n):
#         res = min(res, arr[i])
#     # return res
# def getMax(arr, n):
#     res = arr[0]
#     for i in range(1, n):
#         res = max(res, arr[i])
#     return res
#
#
# arr = [45, 7, 88, 899, 4, 5, 67]
# n = len(arr)
# print("minimum element of array is: ",getMin(arr, n))
# print("maximum element of array is: ",getMax(arr, n))
#
# REMOVE DUPLICATE ELEMENT FROM AN ARRAY
#
# def remDup(arr, n):
#     if n == 0 or n == 1:
#         return n
#     temp = list(range(n))
#     j = 0
#     for i in range(0, n - 1):
#         if arr[i] != arr[i + 1]:
#             temp[j] = arr[i]
#             j += 1
#     temp[j] = arr[n - 1]
#     j += 1
#     for i in range(0, j):
#         arr[i] = temp[i]
#     return j
#
#
# arr = [1, 2, 2, 4, 5, 6, 7, 8, 8, 8, 9]
# n = len(arr)
# n=remDup(arr, n)
# for i in range(n):
#     print("%d" % (arr[i]), end=" ")

#
#
# def areaOfRhombus(diagonal1, diagonal2):
#     ans = (diagonal1 * diagonal2) // 2
#     return ans
#
#
# #main
# # string = input().strip().split(' ')
# # diagonal1 = int(string[0])
# # diagonal2 = int(string[1])
#
# ans = areaOfRhombus(11, 9)
#
# print(ans)
#
#
# from array import *
# arayr=array('i', [2, 45, 56, 6, 66, 7, 88, 8, 9])
# n=len(array)
#
# for ele in range(n):
#     min_value = min(array[ele:])
#     min_ind = array.index(min_value)
#     array[ele], array[ele + 1] = array[ele + 1], array[ele]
# for in range(n):
#       print(array[ele])

# def fact(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))

# num=int(input("Enter your number to find factorial: "))
# factorial=1
# for i in range (1,num+1):
#     factorial=factorial*i
# print(f"factorial of the {num} is {factorial}")

# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# n=int(input("Enter total number of term "))
# print(a,b,end=" ")
# while n-2:
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1

# def fibbo(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibbo(n-1)+fibbo(n-2)
# print(fibbo(4))

# list=[4,5,6,8,9,9,9,6,65,54,4,4,3,3]
# result=[i for i in list if i>45]
# print(result)
# import time
# print("Please insert your card")
# time.sleep(5)
# password = 2356
# pin = int(input("Please enter your pin:"))
# if pin == password:
#     print("Balance enquiry")
#     print("fast withdrawal")
#     print("widthdraw your ammount")
#     print("mini statement")
#     print("Change your pin")
#     print("Deposit your cash")
# else:
#     print("Incorrect pin,please enter again")
#
#
# def withdraw(balance):
#     amount = int(input("Please enter your amount to withdraw: "))
#     balance -= amount
#     print("Please collect your cash")
#     print("Your remaining balance is: ")
#     return balance
#
#
# print(withdraw(100000))

