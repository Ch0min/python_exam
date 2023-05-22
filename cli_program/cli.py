#!/usr/bin/env python3

import argparse
import subprocess
# Subprocess kort sagt er et library i Python, som hjælper med, at oprette subprocesser.
# Vi har brugt det, da det er up-to-date og er stærkere end os.system.

# Dictionary for CLI menu spørgsmål.
menu_options = {
    1: {
        "name": "Which month had the most and least released games in 2022?",
        "scripts": [
            "../Questions/Which_month_had_the_most_and_least_released_games_in_2022/month_released_most.py",
            "../Questions/Which_month_had_the_most_and_least_released_games_in_2022/month_released_less.py"
        ]
    },
    2: {
        "name": "Which Game Dev Publisher had released the most games in 2022?",
        "scripts": [
            "../Questions/Which_Game_Dev_Publisher_had_released_the_most_games_in_2022/most_game_releases_2022_by_company.py",
            "../Questions/Which_Game_Dev_Publisher_had_released_the_most_games_in_2022/predict_games_released_next_month.py"
        ]
    },
    3: {
        "name": "Which gaming platform has had the most games released in 2022?",
        "scripts": [
            "../Questions/Which_platform_has_had_the_most_games_released_in_2022/most_releases_by_platform.py"
        ]
    },
    4: {
        "name": "Which game had won the most awards in 2022?",
        "scripts": [
            "../Questions/Which_game_had_won_the_most_awards_in_2022/MostAwardsByCategory.py",
            "../Questions/Which_game_had_won_the_most_awards_in_2022/MostAwardsInTotal.py"
        ]
    },
    5: {
        "name": "Show a graph for the most released gaming genre in 2022.",
        "scripts": [
            "../Questions/Show_a_graph_for_the_most_released_gaming_genre_in_2022/PopularGenreGraph.py"
        ]
    },
    6: {
        "name": "Show a graph for the Critically Acclaimed Games with the best rating.",
        "scripts": [
            "../Questions/Show_a_graph_for_the_Critically_Acclaimed_Games_with_the_best_rating/critically_acclaimed.py"
        ]
    },
    7: {
        "name": "Is there a connection between genre and platform?",
        "scripts": [
            "../Questions/Connection_Between_Genre_And_Platform/Connection.py"
        ]
    }
}

# Definer CLI argumenter.
parser = argparse.ArgumentParser(description="Select a QUESTION:")
parser.add_argument("script", type=int, nargs="?", choices=list(menu_options.keys()), default=None,
                    help=f"Select a QUESTION between {menu_options.keys()} or use the -m or --menu to show the QUESTIONS.")
parser.add_argument("-m", "--menu", action="store_true", help="display the CLI MENU options")

# Parse CLI argumenter.
args = parser.parse_args()

if args.menu:
    for key, option in menu_options.items():
        print(f"{key} - {option['name']}")
else:
    if args.script is None:
        print("##### #    # ###### #    # ###### #    #     ###### #     #      #      #     #")
        print("#   #  #  #    #    #    # #    # ##   #     #       #   #      # #     ##   ##")
        print("#   #   ##     #    #    # #    # # #  #     #        # #      #   #    # # # #")
        print("####    #      #    ###### #    # #  # #     ######    #      #######   #  #  #")
        print("#       #      #    #    # #    # #   ##     #       #   #   #       #  #     #")
        print("#       #      #    #    # ###### #    #     ###### #     # #         # #     #")
        print("                     PYTHON EXAM 2023 - GAMES IN 2022                          ")
        print(
            "Please select a QUESTION (./cli_program.py (1-9)) or use the -m or --menu OPTION to display the MENU.   ")
    else:
        # Kør det valgte script/scripts.
        if args.script in menu_options:
            scripts = menu_options[args.script]["scripts"]
            for script in scripts:
                subprocess.run(["python3", script])
                print("\t")
        else:
            print("Invalid script number. Please select a valid QUESTION.")
