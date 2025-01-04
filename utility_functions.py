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
        player = {"name": name, "profession": profession, "leader": leader, "keys_wons": 0}
        team.append(player)

    # a corriger si cas ou il y a deux team leaders
    found = False
    for i in range(len(team)):
        if team[i]["leader"]:
            found = True

    if not found:
        team[0]["leader"] = True
        print(team[0]["name"], " is now the leader.")

    return team



def challenges_menu():
    print('1. Mathematics challenge')
    print('2. Logic challenge')
    print('3. Chance challenge')
    print('4. Père Fouras riddle')

    challenge=int(input('Enter the number to the corresponding challenge you would like to play : '))
    while challenge not in [1, 2, 3, 4]:
        challenge = int(input('Please answer by 1, 2, 3 or 4. Which challenge you would like to play :'))
    if challenge == 1:
        print('You have selected the mathematics challenge')
    if challenge == 2:
        print('You have selected the logic challenge')
    if challenge == 3:
        print('You have selected the chance challenge')
    else:
        print('You have selected the Père Fouras riddle')

    return challenge

def choose_player(team):
    print('Here is the list of players')

    for i in range(len(team)):
        if team[i]["leader"]:
            role = 'Leader'
        else :
            role = 'Member'
        print(i+1, '. ', team[i]["name"], ' (', team[i]["profession"], ') - ', role)

    number_selected = int(input('Please select the corresponding number to a player to take on the challenge : '))
    if number_selected > 3 or number_selected <= 0:
        number_selected = int(input('You must choose a valid number, who will do the challenge : '))

    player = team[number_selected - 1]
    print('You selected player', number_selected)

    return player
