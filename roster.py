# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": [
                        "Davis", 
                        "Bacot", 
                        "Ingram",
                        "Ryan",
                        "Trimble",
                        "Washington",
                        "Withers",
                        "Wojcik",
                        "Cadeau",
                        "High"
                        ],
          "First Name": [
                        "RJ", 
                        "Armando", 
                        "Harrison",
                        "Cormac",
                        "Seth",
                        "Jalen",
                        "Jae'Lyn",
                        "Paxson",
                        "Elliot",
                        "Zayden"
                        ],
                        
          "height": [72, 83, 79, 77, 75, 82, 81, 77, 73, 81],
          "weight": [180, 240, 225, 195, 195, 230, 215, 195, 180, 225]}

# Creates a dataframe of the players dictionary using pandas, assigns it to a variable named data
data = pd.DataFrame(player)

data["bmi"] = (round((data["weight"]/2.205)/((data["height"]/39.37)**2), 2))

print(data)

data.to_csv("bmi.csv")