# https://goheels.com/sports/mens-basketball/roster

import pandas as pd


roster = ['Davis', 'Bacot', 'Ingram']
player = {'Last Name': roster}

# Creates a dataframe of the players dictionary using pandas, assigns it to a variable named data
data = pd.DataFrame(player)
print(data)

# Prints a divider for the output
print('----------------')

# Prints roster list
print(roster)

# Prints a divider for the output
print('----------------')

# Loops through each player in the roster list and prints their name
for player in roster:
    print(player)