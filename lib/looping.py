#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        if i == 1:
            print("Happy New Year!")
        i -= 1

def square_integers(int_list):
    return [int ** 2 for int in int_list]

def fizzbuzz():
    for i in range(100):
        i += 1
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else: 
            print(i)
