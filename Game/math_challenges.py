import random

#Factorial challenge (weak)
def factorial(n) :
    value = 1
    if n > 0 :
        for i in range(1, n+1) :
            value = value*i
    else :
        value = 1
    return value



def math_challenge_factorial():

    print("Welcome to the factorial challenge !")
    print("In this game, you need to calculate the factorial of a random number between 1 and 10 to obtain a key !\n")

    n = random.randint(1, 10)
    print("Calculate the factorial of", n)
    guess = int(input("Your answer : "))

    correct_answer = factorial(n)

    if guess == correct_answer:
        print("Correct, the factorial of", n, 'is', guess, '.')
        print('\033[93mCongratulations, you win a key !\033[0m')
        found = True
    else:
        print('Your answer is not correct, the factorial of', n, 'is', correct_answer, '.')
        found = False
    return found



#Prime Numbers challenge (average)
def is_prime(n):
    found = True
    if n <= 1:
        found = False  # Numbers <= 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to sqrt(n)
        if n % i == 0:
            found = False  # If a divisor is found, n is not prime
    return found

def nearest_prime(n):
    while not is_prime(n):
        n += 1
    return n

def math_challenge_prime():

    print("Welcome to the prime number challenge !")
    print("")
    n = random.randint(10, 20)
    guess = int(input('Find the closest prime number to {}: '.format(n)))

    correct_answer = nearest_prime(n)

    if guess == correct_answer:
        print("Congratulations! You found the prime number,", guess,'.')
        print('\033[93mCongratulations, you win a key !\033[0m')
    else:
        print('Your answer is not correct, the closest prime number of', n, 'is', correct_answer, ".")



#Roulette challenge (average)
def math_roulette_challenge():
    numbers = [random.randint(1, 20) for _ in range(5)]

    operation = ['addition', 'subtraction', 'multiplication']
    random_operation = random.choice(operation)

    result = 0

    if random_operation == 'addition':
        result = 0
        for num in numbers :
            result += num
    elif random_operation == 'subtraction':
        result = 0
        for num in numbers :
            result -= num
    elif random_operation == 'multiplication':
        result = 1
        for num in numbers :
            result *= num


    print('The obtained numbers on the roulette are :',numbers)
    print('Calculate the', random_operation, 'of these numbers')
    guess = int(input('Your answer is :'))

    if guess == result:
        print('\033[93mCongratulations, you win a key !\033[0m')
        return True
    else:
        print('Your answer is not correct, the result is', result)
        return False


def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge]
    challenge = random.choice(challenges)