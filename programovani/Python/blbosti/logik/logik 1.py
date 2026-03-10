pocet_barev = int(input("napiš s kolika bavama chceš hrát"))
pocet_mist = int(input("napiš pocet mist na ktere budes dosazovat barvy"))
colors = [
    "Red", "Green", "Blue", "Yellow",
    "White", "Orange", "Black", "Purple",
    "Red_", "Green_", "Blue_", "Yellow_",
    "White_", "Orange_", "Black_", "Purple_"
]

# Přiřadíme čísla ke každé barvě
colors_with_indices = {color: index for index, color in enumerate(colors)}

print(colors_with_indices)

