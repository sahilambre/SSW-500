from random import choice

def get_human_move() -> str:
    """ Asking the user for R, P, or S  loop gives a valid input """
    while True:
        user_input: str = input("Please choose 'r', 'p', 's' or 'q' to quit: ")

        # match user_input.lower():
        #     case 'r':
        #         return 'rock'
        #     case 'p':
        #         return 'paper'
        #     case 's':
        #         return 'scissors'
        #     case 'q':
        #         return 'quit'
        #     case other:
        #         print('Please enter valid option!')

        if user_input.lower() == 'r':
            return 'rock'
        elif user_input.lower() == 'p':
            return 'paper'
        elif user_input.lower() == 's':
            return 'scissors'
        elif user_input.lower() == 'q':
            return 'quit'
        else: 
            return 'Please enter valid option!'


def get_computer_move() -> str:
    """ 
    returns the computer's random choice using choice
    """
    move: str = choice(['rock', 'paper', 'scissors'])
    return move


def play_game() -> bool:
    """ 
        The human may enter 'q' any time to stop the game.
        prints message of the winner
    """
    human: str = get_human_move()
    if human == 'quit':  # human wants to quit
        return False
    computer: str = get_computer_move()

    if human == computer:
        print(f'Tie: we both chose {human}')
    elif human == 'rock' and computer == 'scissors':
        print(f'{human} beats {computer} - You win!')
    elif human == 'scissors' and computer == 'paper':
        print(f'{human} beats {computer} - You win!')
    elif human == 'paper' and computer == 'rock':
        print(f'{human} beats {computer} - You win')
    # elif human != 'r' or 'p' or 's' or 'q':
    else:
        print(f'{computer} beats {human} - You lose!')
    return True  


def main() -> None:
    """ 
    game continues till human press 'q' to stop
    """
    again: bool = True
    while again:
        again = play_game()

    print("Thanks for playing!")


if __name__== "__main__":
    main()

# main()