"""
This is the utility functions file.
In this file, there is all the functions used in main program to initialize every game
"""

#This function firstly displays a welcome message and then introduces the player the game and the rules
def introduction():
    print('Welcome to the Fort Boyard game!')
    print('Your goal is to collect three keys by completing challenges to then unlock the treasure room.')

#The function compose teams, creates teams in forms of lists
def compose_teams():
    n = input('How many players will be playing: ')

    # This block ensures the number of players selected is valid, going from 1 to 3
    while not (len(n) > 0 and all(char in '0123456789' for char in n) and 0 < int(n) <= 3):
        print("Please enter a number between 1 and 3.")
        n = input('How many players will be playing: ')

    n = int(n)
    team = []

    # This block saves informations about each players
    for i in range(n):
        print("\nEnter details for Player", i + 1)
        name = input("Name: ")
        profession = input("Profession: ")

        is_leader = input("Is this player the team leader ? (yes/no): ")
        while is_leader not in ['yes', 'no', 'Yes', 'No']:
            is_leader = input("Please answer by yes or no, Is this player the team leader ? : ")

        if is_leader == 'yes' or is_leader == 'Yes' :
            leader = 'Leader'
        else:
            leader = 'Member'

        #Players are here represented as dictionaries containing information about them
        player = {"name": name, "profession": profession, "leader": leader, "keys_wons": 0}
        team.append(player)

    #Prevent multiple team leaders
    found = False
    for i in range(len(team)):
        if team[i]["leader"] == 'Leader':
            found = True
            break
    if i < (len(team) - 1) :
        if len(team) > 1 :
            team[i+1]["leader"] = 'Member'
        team[len(team)-1]["leader"] = 'Member'

    if not found:
        team[0]["leader"] = 'Leader'
        print("As there was no leader in your team,", team[0]["name"], "is now the leader.")
        return team

    for player in team:
        if player["leader"] == 'Leader' :
            print(player["name"], "is the leader of the team.")
    return team

#The challenges menu function displays all of the different challenges to choose from
def challenges_menu():
    print("\nThis is the list of the challenges. You have to choose a challenge by entering its corresponding number.")

    print('1. Mathematics challenge')
    print('2. Logic challenge')
    print('3. Chance challenge')
    print('4. Père Fouras riddle')

    #Prevent input errors
    challenge = input('Enter the number to the corresponding challenge you would like to play : ')
    while len(challenge) != 1 or ord('4') < ord(challenge) or ord('1') > ord(challenge) :
        challenge = input('Please answer by 1, 2, 3 or 4. Which challenge you would like to play :')

    challenge = int(challenge)

    if challenge == 1:
        print('You have selected the mathematics challenge.\n')
    if challenge == 2:
        print('You have selected the logic challenge.\n')
    if challenge == 3:
        print('You have selected the chance challenge.\n')
    if challenge == 4:
        print('You have selected the Père Fouras riddle.\n')

    return challenge

#The function choose player allows the players to select who will compete in the challenge
def choose_player(team):
    print('Here is the list of players :')

    # The block displays all the players and their informations
    for i in range(len(team)):
        if team[i]["leader"]:
            role = 'Leader'
        else :
            role = 'Member'
        print(i+1, '. ', team[i]["name"], ' (', team[i]["profession"], ') - ', role)

    #Prevent input errors
    number_selected = input('\nPlease select the corresponding number to a player to take on the challenge : ')
    while len(number_selected) != 1 or ord('0') > ord(number_selected) or ord(number_selected) > ord('3') or len(team) < int(number_selected) :
        number_selected = input('Invalid answer. Please select the corresponding number to a player to take on the challenge : ')

    number_selected = int(number_selected)
    player = team[number_selected - 1]
    print('You selected player', number_selected, ".\n")

    return player