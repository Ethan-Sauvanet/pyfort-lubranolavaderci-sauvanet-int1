def introduction():
    print('Welcome to the Fort Boyard game!')
    print('Your goal is to collect three keys by completing challenges to then unlock the treasure room.')


def compose_teams():
    n = int(input('How many players will be playing : '))
    while n > 3 or n <= 0:
        print('You must choose a valid number of players, do not exceed 3')
        n = int(input('How many players will be playing : '))

    team = []

    for i in range(n):
        print("Enter details for Player", i + 1)
        name = input("Name: ")
        profession = input("Profession: ")
        is_leader = input("Is this player the team leader? (yes/no): ")
        while is_leader not in ['yes', 'no']:
            is_leader = input("Please answer by yes or no, Is this player the team leader? (yes/no): ")
        if is_leader == 'yes':
            leader = True
        else:
            leader = False

    player = {"name": name, "profession": profession, "leader": leader, "keys_wons": 0, }
    team.append(player)

#changer cette partie ne marche pas
    found = False
    for i in range(len(team)):
        if team[i]["leader"] == True:
            found = True

    if found == False:
            team[0]["leader"] = True
            print(team[0]["name"], " is now the leader.")

    return team




def challenges_menu():
    print('1. Mathematics challenge')
    print('2. Logic challenge')
    print('3. Chance challenge')
    print('4. Père Fouras riddle')

    challenge=int(input('Enter the number to the corresponding challenge you would like to play : '))
    while choice not in [1, 2, 3, 4]:
        challenge = int(input('Please answer by 1, 2, 3 or 4. Which challenge you would like to play :'))

    return challenge