# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ['Davis', 'Bacot', 'Ingram']

print(roster)

for player in roster:
    print(player)

data = pd.DataFrame(roster)
print(data)