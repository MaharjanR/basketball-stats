import constants
import copy
from random import randint


teams = constants.TEAMS
players = constants.PLAYERS

player_copy = copy.deepcopy(players)

def clean_data(players):
    experienced = []
    not_experienced = []
    for player in player_copy:
        for key, value in player.items():
            if key == 'guardians':
                exp = value.split('and')
                player[key] = exp
            elif key == 'height':
                height_int = [i for i in player[key].split() if i.isdigit()] 
                player[key] = int(height_int[0])
            elif key == 'experience':
                if value == 'YES':
                    player[key] = True
                    experienced.append(player)
                else:
                    player[key] = False
                    not_experienced.append(player)
                    
    return experienced, not_experienced


def balance_player(experienced, not_experienced, teams):
    total_experienced_player = len(experienced)
    total_not_experienced = len(not_experienced)
    team1 = []
    team2 = []
    team3 = []
    
    for i in range(total_experienced_player):
        random_number = randint(0,len(experienced) - 1)
        random_player = experienced[random_number]
        
        if len(team1) < 3:
            team1.append(random_player)
            experienced.remove(random_player)
        elif len(team2) < 3:
            team2.append(random_player)
            experienced.remove(random_player)
        else:
            team3.append(random_player)
            experienced.remove(random_player)

    for i in range(total_not_experienced):
        random_number = randint(0,len(not_experienced) - 1)
        random_player = not_experienced[random_number]

        if len(team1) < 6:
            team1.append(random_player)
            not_experienced.remove(random_player)
        elif len(team2) < 6:
            team2.append(random_player)
            not_experienced.remove(random_player)
        else:
            team3.append(random_player)
            not_experienced.remove(random_player)
    

    return team1, team2, team3
                 
               
def display_team(teams, name):
    print('----------------------------------------')
    print(f'Team: {name} stats')
    print('----------------------------------------\n')
    print(f'Total player: {len(teams)}\n')
    print('Player on Team:')
    experienced_player = 0
    height = 0
    guardians_list = []
    
    for i, team in enumerate(teams):
        for key, value in team.items():
            if key == 'name' and i == 0:
                print(f'\t{value}, ', end = '')
            elif key == 'name' and i < (len(teams) - 1):
                print(f'{value}, ', end = '')
            elif key == 'name' and i == (len(teams) - 1):
                print(f'{value}')
            elif key == 'experience' and value == True:
                experienced_player += 1
            elif key == 'height':
                height += value
            elif key == 'guardians':
                for guardian in value:
                    guardians_list.append(guardian)
    
    print(f'\nTotal experienced player: {experienced_player}')
    print(f'\nTotal inexperienced player: { len(teams) - experienced_player}')
    print(f'\nAverage height of the team: { height / len(teams) }')
    print(f'\nGuardians on Team:')
    
    for i, guardian in enumerate(guardians_list):
        if i == 0:
            print(f'\t{guardian}, ', end = '')            
        elif i < (len(guardians_list) - 1):
            print(f'{guardian},', end = '')
        else:
            print(f'{guardian}')
    
    
def display_menu():
    experienced, not_experienced = clean_data(players)
    team1, team2, team3 = balance_player(experienced, not_experienced, teams) 
    exit = 'false'
    
    while exit == 'false':
        
        print('---------------MENU---------------')
        print('Here are your choices:')
        print('\t1) Display Team Stats')
        print('\t2) Quit')
        print('\n')
        user_input = input('Enter your option > ')
        
        while user_input != '1' and user_input != '2':
            print('Invalid option, please enter 1 or 2')
            user_input = input('Enter your option > ')
            
        if user_input == '1':
            for i in range(len(teams)):
                print(f'\t{i+1}) {teams[i]}')
                
            print('\n')
            user_input = input('Enter your option > ')
            print('\n')
            
            while user_input != '1' and user_input != '2' and user_input != '3': 
                print('Invalid option, please enter 1 or 2 or 3')
                user_input = input('Enter your option > ')
                print(user_input)
                
            if user_input == '1':
                display_team(team1, teams[0])
            elif user_input == '2':
                display_team(team2, teams[1])
            else:
                display_team(team3, teams[2])
                
            input('\nPress enter to continue')
        
        else:
            exit = 'true'

if __name__ == "__main__":
    display_menu()
    