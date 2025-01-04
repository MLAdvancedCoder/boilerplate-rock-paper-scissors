# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "P"

    if len(opponent_history) >3:

        if opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
            if opponent_history[-1] == 'R':
                guess = 'P'
            if opponent_history[-1] == 'P':
                guess = 'S'
            if opponent_history[-1] == 'S':
                guess = 'R'

        if opponent_history[-1] != opponent_history[-2] != opponent_history[-3]:
            if opponent_history[-1] == 'R':
                guess = 'S'
            if opponent_history[-1] == 'P':
                guess = 'R'
            if opponent_history[-1] == 'S':
                guess = 'P'

        if opponent_history[-1] == opponent_history[-2] != opponent_history[-3]:
            if opponent_history[-1] == 'R':
               guess = 'S'
            if opponent_history[-1] == 'P':
               guess = 'R'
            if opponent_history[-1] == 'S':
               guess = 'P'
    return guess


from collections import Counter

def probability_tester(opponent_history):
    moves = Counter(opponent_history)
    most_common_move, most_common_count = moves.most_common(1)[0]
    return most_common_move
      
