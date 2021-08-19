
def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return (number)
    elif (number % 2) == 1:
        print(3 * number + 1)
        return (number)

print('Please enter your number to collatz')
number = int(input())
while number != None:
    collatz(number)

