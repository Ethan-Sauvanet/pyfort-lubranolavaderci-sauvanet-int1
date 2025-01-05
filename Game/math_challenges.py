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

    #Prevent input errors
    guess = input("Your answer : ")
    for i in range(len(guess)):
        if not ord('0') <= ord(guess[i]) <= ord('9'):
            guess = input("Your answer is in an invalid format. Try again : ")
    guess = int(guess)
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
#The function is prime calculates the closest prime number to the generated number (numer that will be generated in the math challenge prime function
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
    guess = input('Find the closest prime number (greater or equal) to {} : '.format(n))

    #Prevent input errors
    while len(guess) != 2 or ord(guess[0]) < ord('0') or ord(guess[0]) > ord('9') or ord(guess[1]) < ord('0') or ord(guess[1]) > ord('9'):
        guess = input('Invalid format. Find the closest prime number (greater or equal) to {}: '.format(n))

    guess = int(guess)
    correct_answer = nearest_prime(n)
    #Checks whether the guess is correct or not
    if guess == correct_answer:
        print("Congratulations! You found the prime number,", guess,'.')
        print('\033[93mCongratulations, you win a key !\033[0m')
        return True
    else:
        print('Your answer is not correct, the closest prime number of', n, 'is', correct_answer, ".")
        return False



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
    guess = input('Your answer is : ')

    #Prevent input errors
    invalid_character = True
    while invalid_character:
        invalid_character = False  # Assume valid input initially

        #Special case for the "-" before negative numbers
        if random_operation == 'subtraction' and guess[0] == '-':
            for i in range(1, len(guess)):
                if not (ord('0') <= ord(guess[i]) <= ord('9')):
                    guess = input('Invalid format. Try again: ')
                    invalid_character = True
                    break
        else:
            for i in range(len(guess)):
                if not (ord('0') <= ord(guess[i]) <= ord('9')):
                    guess = input('Invalid format. Try again: ')
                    invalid_character = True
                    break


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