import time
startTime = time.time()
code = "9999"
digits = ["0","1","2","3","4","5","6","7","8","9"]


def main():
    for a in digits:
        for b in digits:
            for c in digits:
                for d in digits:
                    guess = a+b+c+d
                    if guess==code:
                        print(guess)
                        print(time.time()-startTime)
                        break

main()
