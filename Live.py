def check_input(input,options):
    if input.isdigit():
        if(int(input) in options):
            return True
    return False

def welcome(name):
    print(f"""Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play.
""")
def load_game():
    game = input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    difficulty = input("Please choose game difficulty from 1 to 5:")
    if(check_input(game,range(1,4)) and check_input(difficulty,range(1,6))):
        print("good job")
    else:
        print("***** You have entered an incorrect input! Please try again ****")
        load_game()
