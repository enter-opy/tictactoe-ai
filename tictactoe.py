from os import system
from time import sleep
from math import inf
from colorama import Fore

board = [
    Fore.BLUE + '1' + Fore.RESET, 
    Fore.BLUE + '2' + Fore.RESET,
    Fore.BLUE + '3' + Fore.RESET,
    Fore.BLUE + '4' + Fore.RESET,
    Fore.BLUE + '5' + Fore.RESET,
    Fore.BLUE + '6' + Fore.RESET,
    Fore.BLUE + '7' + Fore.RESET,
    Fore.BLUE + '8' + Fore.RESET,
    Fore.BLUE + '9' + Fore.RESET
]

X, O = Fore.GREEN + 'X' + Fore.RESET, Fore.RED + 'O' + Fore.RESET

def draw():
    _ = system('cls')
    print(' _____ _____ _____ ')
    print('|     |     |     |')
    print('|  ' + board[0] + '  |  ' + board[1] + '  |  ' + board[2] + '  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5] + '  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8] + '  |')
    print('|_____|_____|_____|')

def player(state):
    # return the next player of the given state
    count = {
        X: 0,
        O: 0
    }

    for i in state:
        if i is X:
            count[X] += 1
        elif i is O:
            count[O] += 1
    
    return O if count[X] > count[O] else X

def actions(state):
    # return all possible actions on the given state
    actions = []

    for i in range(len(state)):
        if state[i] in [
            Fore.BLUE + '1' + Fore.RESET,
            Fore.BLUE + '2' + Fore.RESET,
            Fore.BLUE + '3' + Fore.RESET,
            Fore.BLUE + '4' + Fore.RESET,
            Fore.BLUE + '5' + Fore.RESET,
            Fore.BLUE + '6' + Fore.RESET,
            Fore.BLUE + '7' + Fore.RESET,
            Fore.BLUE + '8' + Fore.RESET,
            Fore.BLUE + '9' + Fore.RESET
        ]:
            actions.append(i)
    
    return actions

def result(state, action, player):
    # return the result of the given action on the given state
    result = [i for i in state]
    result[action] = player
    return result

def winner(state):
    # return the winner of the given state
    if state[0] == state[1] and state[1] == state[2]: return state[0]
    if state[3] == state[4] and state[4] == state[5]: return state[3]
    if state[6] == state[7] and state[7] == state[8]: return state[6]
    if state[0] == state[3] and state[3] == state[6]: return state[0]
    if state[1] == state[4] and state[4] == state[7]: return state[1]
    if state[2] == state[5] and state[5] == state[8]: return state[2]
    if state[0] == state[4] and state[4] == state[8]: return state[4]
    if state[2] == state[4] and state[4] == state[6]: return state[4]
    return None    

def terminal(state):
    # return a boolean value representing whether the given state is a terminal state
    return winner(state) is not None or not any(i in state for i in [
        Fore.BLUE + '1' + Fore.RESET,
        Fore.BLUE + '2' + Fore.RESET,
        Fore.BLUE + '3' + Fore.RESET,
        Fore.BLUE + '4' + Fore.RESET,
        Fore.BLUE + '5' + Fore.RESET,
        Fore.BLUE + '6' + Fore.RESET,
        Fore.BLUE + '7' + Fore.RESET,
        Fore.BLUE + '8' + Fore.RESET,
        Fore.BLUE + '9' + Fore.RESET
    ])

def utility(state):
    # return an integer representing the winner of the given terminal state
    return 1 if winner(state) is X else -1 if winner(state) is O else 0

def minimax(state):
    t, action = minvalue(state)
    
    if action is not None:
        board[action] = O

def maxvalue(state):
    if terminal(state):
        return utility(state), None
    
    v = -inf
    
    # for every possible action in the given state pass the result of each action on the state to the minvalue function
    for action in actions(state):
        min_value, t = minvalue(result(state, action, X))
        if min_value > v:
            ACTION = action
            v = min_value
    
    return v, ACTION

def minvalue(state):
    if terminal(state):
        return utility(state), None
    
    v = inf
    
    # for every possible action in the given state pass the result of each action on the state to thes maxvalue function
    for action in actions(state):
        max_value, t = maxvalue(result(state, action, O))
        if max_value < v:
            ACTION = action
            v = max_value
        
    return v, ACTION

while True:
    draw()

    if player(board) is X:
        print('\nPlayer X, Enter a number: ', end='')
        action = int(input()) - 1

        if action in [0, 1, 2, 3, 4, 5, 6, 7, 8] and board[action] in [
            Fore.BLUE + '1' + Fore.RESET, 
            Fore.BLUE + '2' + Fore.RESET,
            Fore.BLUE + '3' + Fore.RESET,
            Fore.BLUE + '4' + Fore.RESET,
            Fore.BLUE + '5' + Fore.RESET,
            Fore.BLUE + '6' + Fore.RESET,
            Fore.BLUE + '7' + Fore.RESET,
            Fore.BLUE + '8' + Fore.RESET,
            Fore.BLUE + '9' + Fore.RESET
        ]:
            board[action] = X
        else:
            print("invalid move")
            sleep(0.5)
    else:
        print('\nComputer thinking...')
        sleep(0.5)
        
        minimax(board)
    
    if (terminal(board)):
        message = Fore.GREEN + '\n' + 'You won' if winner(board) is X else Fore.RED + '\n' + 'You lose' if winner(board) is O else Fore.BLUE + '\n' + 'Draw'
        _ = system('cls')
        draw()
        print(message)
        break