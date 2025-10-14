#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


def create_grid(n):
    """
    This function creates a grid of n rows and n columns which is 10, actually.

    :param n: the number of rows and columns
    :return: a DataFrame containing the grid of n rows and n columns.
    """
    return pd.DataFrame([['~'] * n for _ in range(n)],
                        index= [str(number +1) for number in range(n)],
                        columns= [chr(65 + i) for i in range(n)])


def naval_battle(grid, my_boats):
    """
    This function asks the user to enter x and y coordinates and check them
    before it calls the touched_or_not() function or quit to close the programme.
    It also keeps track of already played coordinates and break if the game is over.
    :param grid: the grid of n size
    :param my_boats: a list of boats (dict)
    :return:
    """

    # We create some variables for checking valid input
    # and keep tracks of previous shots with 'played_coords'
    valid_columns = list(grid.columns)
    valid_rows = list(grid.index)
    played_coords = set()

    # Infinite loop
    while True:
        user_input = input("\nEnter coordinate (ex: A2, B3, etc) or 'quit': ").strip().upper()

        # Quitting case
        if user_input == 'QUIT':
            print('\nThank you for playing!')
            break

        # Checking if user_input have a 2 or 3 len, if not then it's not correct
        if 2 < len(user_input) > 3:
            print("Invalid format. Please use A1 to J10.")
            continue

        coord_x = user_input[0]
        coord_y = user_input[1:]

        # We check if both coord are valid otherwise we print out a message
        if coord_x not in valid_columns or coord_y not in valid_rows:
            print("Invalid coordinate! Column must be A–J and row 1–10.")
            continue

        # We put together coord_x and coord_y into a variable 'coord'
        coord = (coord_x, coord_y)

        # Then we check if those coord are in the 'played_coords' set,
        # if that's the case then we print out a message accordingly
        if coord in played_coords:
            print("You already played that coordinate! Try a new one.")
            continue

        # We add the coord into our set so we can check if they are new or not
        played_coords.add(coord)

        # We create a victory variable, so when there's no more boats, the game ends.
        victory = hit_or_not(grid, coord_x, coord_y, my_boats)
        if victory:
            break


def hit_or_not(grid, coord_x, coord_y, boats):
    """
    The function checks if the boat is touched or not and print
    out a message accordingly. Then it modify the grid and print it.

    :param grid: the grid which is a dataframe
    :param coord_x: x coordinate of player's input.
    :param coord_y: y coordinate of player's input.
    :param boats: the list of boats.
    :return: a grid modified accordingly to the inputs.
    """

    # We create a boolean for hit
    hit = False

    for boat in boats:
        # If the coord given are the coord of one of the boats
        if (coord_x, coord_y) in boat['pos']:
            boat['touché'] += 1
            grid.at[coord_y, coord_x] = 'X'
            hit = True
            if boat['touché'] == boat['part']:
                print(f"\n!!!!!!! Congratulations! you have sunk the {boat['name']} !!!!!!!!\n")
            else:
                print('Nice! You touched a boat!')
            break

    if not hit:
        print('You missed! Try again')
        grid.at[coord_y, coord_x] = 'O'

    # Remaining boats
    remaining_boats = sum(1 for boat in boats if boat['touché'] < boat['part'])

    # If remaining boat = 0 then the game end.
    if remaining_boats == 0:
        print('===================================')
        print('     Congratulations! You Won!  ')
        print('===================================')
        # Victory's signal
        return True
    else:
        print(f"--------> {remaining_boats} boats left !<----------\n")

    # Print the updated grid
    print(grid.to_string())
    return False


def main():
    """
    This is the main function.
    It contains our list of dicts 'my_boats' which contains all the boats.
    We create a grid of n rows and n columns and place boats in the grid.
    :return: the message for user to put a coord and the updated grid accordingly.
    """

    # A list of dict which contains all boats
    my_boats = [{'name': 'aircraft', 'part': 5, 'pos': [('B','2'), ('C','2'), ('D','2'), ('E','2'), ('F','2')],
                 'touché': 0},
                {'name': 'cruiser', 'part': 4, 'pos': [('A','4'), ('A','5'), ('A','6'), ('A','7')], 'touché': 0},
                {'name': 'destroyer', 'part': 3, 'pos': [('C','5'), ('C','6'), ('C','7')], 'touché': 0},
                {'name': 'submarine', 'part': 3, 'pos': [('H', '5'), ('I','5'), ('J','5')], 'touché': 0},
                {'name': 'torpedo', 'part': 2, 'pos': [('E','9'), ('F','9')], 'touché': 0}]

    grid = create_grid(10)
    naval_battle(grid, my_boats)


if __name__== '__main__':
    main()