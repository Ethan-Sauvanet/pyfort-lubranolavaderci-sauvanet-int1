
def introduction():
    print('Welcome to the Fort Boyard game!')
    print('Your goal is to collect three keys by completing challenges to then unlock the treasure room.')


def compose_teams():
    n = input('How many players will be playing: ')

    #Prevent input errors
    while not (len(n) > 0 and all(char in '0123456789' for char in n) and 0 < int(n) <= 3):
        print("Please enter a number between 1 and 3.")
        n = input('How many players will be playing: ')

    n = int(n)

    team = []

    for i in range(n):
        print("Enter details for Player", i + 1)
        name = input("Name: ")
        profession = input("Profession: ")

        is_leader = input("Is this player the team leader ? (yes/no): ")
        while is_leader not in ['yes', 'no', 'Yes', 'No']:
            is_leader = input("Please answer by yes or no, Is this player the team leader ? : ")

        if is_leader == 'yes' or is_leader == 'Yes' :
            leader = 'Leader'
        else:
            leader = 'Member'

        player = {"name": name, "profession": profession, "leader": leader, "keys_wons": 0}
        team.append(player)

    #Prevent multiple team leaders
    found = False
    for i in range(len(team)):
        if team[i]["leader"] == 'Leader':
            found = True
            break
    if i <= (len(team) - 1) :
        team[i+1]["leader"] = 'Member'
        team[len(team)-1]["leader"] = 'Member'

    if not found:
        team[0]["leader"] = 'Leader'
        print(team[0]["name"], " is now the leader.")

    return team

def challenges_menu():
    print('1. Mathematics challenge')
    print('2. Logic challenge')
    print('3. Chance challenge')
    print('4. Père Fouras riddle')

    #Prevent input errors
    challenge = input('Enter the number to the corresponding challenge you would like to play : '))
    while challenge not in [1, 2, 3, 4]:
        challenge = input('Please answer by 1, 2, 3 or 4. Which challenge you would like to play :'))

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