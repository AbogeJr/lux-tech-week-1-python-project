import math


def isPerfectSquare(num):
    s = int(math.sqrt(num))
    return s*s == num               #Returns True if num is a perfect Square


def isFibonacci(num):
    return isPerfectSquare(5*num*num+4) or isPerfectSquare(5*num*num-4)


def checkFibonacci(i):
    if(isFibonacci(i)):
        print(i," - Fibbonacci")
    else:
        print(i," - NOT Fibbonacci")


num_ = int(input("Enter a Number: "))
checkFibonacci(num_)