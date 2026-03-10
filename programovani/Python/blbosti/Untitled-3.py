pocet_barev = int(input("napiš s kolika bavama chceš hrát"))
pocet_mist = int(input("napiš pocet mist na ktere budes dosazovat barvy"))
colors = [
    "Red", "Green", "Blue", "Yellow",
    "White", "Orange", "Black", "Purple",
    "Red_", "Green_", "Blue_", "Yellow_",
    "White_", "Orange_", "Black_", "Purple_"]

# Přiřazení čísla ke každé barvě
colors_with_numbers = {color: index + 1 for index, color in enumerate(colors)}

for color, number in colors_with_numbers.items():
    print(f"{color}: {number}")

