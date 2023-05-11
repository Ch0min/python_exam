import argparse
import os

# Define the CLI menu options
parser = argparse.ArgumentParser(description="Select a QUESTION:")
parser.add_argument("script", type=int, nargs="?", choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], default=None,
                    help="Select a QUESTION between 1 and 9 or use the -m or --menu to show the QUESTIONS.")
parser.add_argument("-m", "--menu", action="store_true", help="display the CLI MENU options")

# Parse the command-line arguments
args = parser.parse_args()

if args.menu:
    print("1 - Which month had the most and least released games in 2022?")
    print("2 - Which Game Development Company had released the most games in 2022?")
    print("3 - Which gaming platform was the most popular in 2022?")
    print("4 - Which game had won the most awards in 2022?")
    print("5 - Which genre was the most popular among the released games in 2022?")
    print("6 - Show a graph for the most released gaming genre in 2022.")
    print("7 - Show a graph for the Critically Acclaimed Games with the best rating.")
    print("8 - Is there a connection between genre and platform?")
    print("9 - Which game will we recommend based on genre and platform (possibly rating too)?")


else:
    if args.script is None:
        print("##### #    # ###### #    # ###### #    #     ###### #     #      #      #     #")
        print("#   #  #  #    #    #    # #    # ##   #     #       #   #      # #     ##   ##")
        print("#   #   ##     #    #    # #    # # #  #     #        # #      #   #    # # # #")
        print("####    #      #    ###### #    # #  # #     ######    #      #######   #  #  #")
        print("#       #      #    #    # #    # #   ##     #       #   #   #       #  #     #")
        print("#       #      #    #    # ###### #    #     ###### #     # #         # #     #")
        print("                     PYTHON EXAM 2023 - GAMES IN 2022                          ")
        print("Please select a QUESTION or use the -m or --menu OPTION to display the MENU.   ")
    else:
        # Run the selected script
        if args.script == 1:
            os.system('python3 ../Which_Month_had_the_most_released_games_in_2022_and_vice_versa?/month_released_most.py')
            os.system('python3 ../Which_Month_had_the_most_released_games_in_2022_and_vice_versa?/month_released_less.py')
        elif args.script == 2:
            os.system('python3 helloworld.py')
        elif args.script == 3:
            os.system('python3 calculate.py')
        elif args.script == 4:
            os.system('python3 helloworld.py')
        elif args.script == 5:
            os.system('python3 calculate.py')
        elif args.script == 6:
            os.system('python3 helloworld.py')
        elif args.script == 7:
            os.system('python3 calculate.py')
        elif args.script == 8:
            os.system('python3 helloworld.py')
        elif args.script == 9:
            os.system('python3 calculate.py')
