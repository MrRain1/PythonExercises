#pokemon Table
from prettytable import PrettyTable

tableDrawer = PrettyTable()

tableDrawer.add_column("Pokemon Name",
                       ["Pikachu",
                        "Squirtle",
                        "Bulbasaur"]
                       )

tableDrawer.add_column("Type",
                       ["Electric",
                        "Water",
                        "Grass"]
                       )

tableDrawer.align ="l"

print(tableDrawer)