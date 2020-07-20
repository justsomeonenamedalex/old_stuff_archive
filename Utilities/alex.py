# This is a .py for every useful bit of code I write or find online

# imports
import functools


# classes

class Text:

    @staticmethod
    def is_palindrome(string):
        """Takes an input and returns a boolean of if the string was a palindrome"""
        return string.lower() == string.lower()[::-1]

    @staticmethod
    def split_to_length(string, chuncklength):
        """Takes a string and returns a list of segments if the list of the length specified"""
        return [string[i:i + chuncklength] for i in range(0, len(string), chuncklength)]

class Files:

    @staticmethod
    def get_lines(filename):
        """Returns a list of every line in the given file"""
        return [line.strip() for line in open(filename)]


class Maths:
    @staticmethod
    def factorial(num):
        """Returns the factorial of the given number, uses functools"""
        return functools.reduce(lambda x, y: x * y, range(1, num+1))

    @staticmethod
    def fibonacci(n):
        """Returns the Fibonacci sequence to the given number of places"""
        fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
        sequence = []
        for i in range(n):
            sequence.append(fib(i))
        return sequence

    @staticmethod
    def LCM(x ,y):
        """Returns the LCM of the given numbers using Euclids Algorithim"""
        while(y):
            x, y = y, x%y
        return x

    @staticmethod
    def HCF(x, y):
        """Returns the highest common factor of x and y"""
        return (x * y) // Maths.LCM(x, y)

    @staticmethod
    def prime_factors(n: int):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors



def fizzbuzz():
    """A single line solution to the Fizbuzz problem"""
    return ['Fizzbuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)]