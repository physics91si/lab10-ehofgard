#!/usr/bin/python
import sys
import math

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        x1, x2 = find_roots(a, b, c)
        print ("This is x1: %f" %x1)
        print ("This is x2: %f" %x2)
    except ValueError:
        print("Please enter numerical input")
    except ZeroDivisionError:
        print ("a cannot be zero")
def find_roots(a,b,c):
    mid = b**2 - 4*a*c
    try:
        sqrt_mid = mid**(0.5)
        x1 = (-b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
        return x1, x2
    except ValueError:
        print ("These inputs will yield an imaginary answer")
        sys.exit(1)

if __name__=="__main__":
        main()
