#!/usr/bin/env python3

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
    print("2 - Which Game Dev Publisher had released the most games in 2022?")
    print("3 - Which gaming platform has had the most games released in 2022?")
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
        print("Please select a QUESTION (./cli_program.py (1-9)) or use the -m or --menu OPTION to display the MENU.   ")
    else:
        # Run the selected script
        if args.script == 1:
            os.system("python3 ../Questions/Which_month_had_the_most_and_least_released_games_in_2022/month_released_most.py")
            print("\t")
            os.system("python3 ../Questions/Which_month_had_the_most_and_least_released_games_in_2022/month_released_less.py")
        elif args.script == 2:
            os.system("python3 ../Questions/Which_Game_Dev_Publisher_had_released_the_most_games_in_2022/most_game_releases_2022_by_company.py")
        elif args.script == 3:
            os.system("python3 ../Questions/Which_platform_has_had_the_most_games_released_in_2022/most_releases_by_platform.py")
        elif args.script == 4:
            os.system("python3 ../Questions/Which_game_had_won_the_most_awards_in_2022/MostAwardsByCategory.py")
            print("\t")
            os.system("python3 ../Questions/Which_game_had_won_the_most_awards_in_2022/MostAwardsInTotal.py")
        elif args.script == 5:
            os.system("python3 missing")
        elif args.script == 6:
            os.system("python3 ../Questions/Show_a_graph_for_the_most_released_gaming_genre_in_2022/PopularGenreGraph.py")
        elif args.script == 7:
            os.system("python3 ../Questions/Show_a_graph_for_the_Critically_Acclaimed_Games_with_the_best_rating/critically_acclaimed.py")
        elif args.script == 8:
            os.system("python3 helloworld.py")
        elif args.script == 9:
            os.system("python3 calculate.py")
