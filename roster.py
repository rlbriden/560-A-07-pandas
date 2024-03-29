# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {'Last Name': ['Davis', 'Bacot', 'Ingram'],
          'First Name': ['RJ', 'Armando', 'Harrison'],
          'height': [72, 83, 79],
          'weight': [180, 240, 225]}

# Creates a dataframe of the players dictionary using pandas, assigns it to a variable named data
data = pd.DataFrame(player)
print(data)