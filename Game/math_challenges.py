import random

#Factorial challenge
#This function calculates the factorial.
#This function takes as parameter the value we want to calculate.
def factorial(n) :
    value = 1
    for i in range(1, n+1) :
        value = value*i
    return value

#this is the function math challenge factorial
#This function verifies if the player answer correctly, if he does it returns True otherwise False.
def math_challenge_factorial():

    print("Welcome to the factorial challenge !")
    print("In this game, you need to calculate the factorial of a random number between 1 and 10 to obtain a key !\n")

    #random.randint allows n to take a random value between the two selected values
    n = random.randint(1, 10)
    print("Calculate the factorial of", n)
    guess = int(input("Your answer : "))

    correct_answer = factorial(n)

    #this block verifies if the guess answer is correct or not
    if guess == correct_answer:
        print("Correct, the factorial of", n, 'is', guess, '.')
        print('\033[93mCongratulations, you win a key !\033[0m')
        #The player guessed correctly here, the function will return as true and the team wins
        found = True
    else:
        print('Your answer is not correct, the factorial of', n, 'is', correct_answer, '.')
        #The player guessed incorrectly here, the function will return as false and the team looses
        found = False
    return found


#Prime Numbers challenge
#The function is prime calculates the closests prime number to the generated number (numer that will be generated in the math challenge prime function
def is_prime(n):
    found = True
    if n <= 1:
        found = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            found = False
    return found

#This function, nearest prime, checks for the closets prime number to the generated number if it is not prime
def nearest_prime(n):
    while not is_prime(n):
        n += 1
    return n

#The math challenge prime function
#This function generates the number and checks whether the guessed answer of the player is correct
def math_challenge_prime():

    print("Welcome to the prime number challenge !")
    #Here a random number is generated between 10 and 20
    n = random.randint(10, 20)
    guess = int(input('Find the closest prime number to {}: '.format(n)))

    correct_answer = nearest_prime(n)
    #Checks whether the guess is correct or not
    if guess == correct_answer:
        print("Congratulations! You found the prime number,", guess,'.')
        print('\033[93mCongratulations, you win a key !\033[0m')
    else:
        print('Your answer is not correct, the closest prime number of', n, 'is', correct_answer, ".")



#Roulette challenge
#The math roulette challenge is a calculation challenge that returns true or false depending on the answer of the player
def math_roulette_challenge():
    numbers = []
    #Here 5 numbers will be generated
    for i in range(5):
        n = random.randint(1, 20)
        numbers.append(n) #These numbers are then added to a list

    operation = ['addition', 'subtraction', 'multiplication']
    random_operation = random.choice(operation) #A random operator is then selected with the random.choice

    result = 0
    #Then the correct answer is calculated by the algorthim
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

    #The guess is then compared to the correct answer
    if guess == result:
        print('\033[93mCongratulations, you win a key !\033[0m')
        return True
    else:
        print('Your answer is not correct, the result is', result)
        return False

#This function chooses a random math challenge amongst the 3
def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge]
    challenge = random.choice(challenges)
    return challenge()