import time, os
def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        time.sleep(0.1)
        return (number // 2)
    elif (number % 2) == 1:
        time.sleep(0.1)
        print(3 * number + 1)
        return (3 * number + 1)

while True:

    try:
        n = int(input('Please enter your number to collatz.'))

        while n != 1:
            n = collatz(n)
        while n == 1:
            n = int(input('Please enter your number to collatz.'))
            n = collatz(n)
    except ValueError:
        print('Please enter an integer.')
    except KeyboardInterrupt:
        os._exit(1)