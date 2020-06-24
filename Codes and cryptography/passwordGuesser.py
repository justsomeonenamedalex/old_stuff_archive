import time
import matplotlib.pyplot as plt 
startTime = time.time()
code = "2004"
digits = ["0","1","2","3","4","5","6","7","8","9"]

def search(guess):
    if len(guess)==len(code):
        if guess==code:
            print(guess)
            print(time.time()-startTime)
            return
        else:
            return

    for char in digits:
        search(guess+char)

def main():
    for i in digits:
        search(i)
main()
