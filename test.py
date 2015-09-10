# Paisan.py
# By Paisan Khonjumpa (c) September 2015

# import sys
import a as myLamda
import b as myFunc

# print("The operating system is ", sys.platform)

# def a(x):
#    return lambda x: x + 5

z = myLamda.a(4)
print(z(9))

y = myFunc.myStringPrint("test")
print("Funciton output is ", y)