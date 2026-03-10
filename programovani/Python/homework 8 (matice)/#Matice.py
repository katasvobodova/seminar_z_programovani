#Matice
#TESTOVACÍ matice DATA
M0 = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

M1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

M2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

M3 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

M4 = [
    [0, -1, -2],
    [-3, -4, -5],
    [-6, -7, -8]
]

M5 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

M6 = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

M7 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

M8 = [
    [2, 4, 6, 8],
    [10, 12, 14, 16],
    [18, 20, 22, 24],
    [26, 28, 30, 32]
]

M9 = [
    [5, 3, 1, 7],
    [9, 8, 6, 4],
    [3, 2, 1, 0],
    [7, 5, 4, 2]
]

M10 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

M11 = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5],
    [3, 5, 8]
]

M12 = [
    [0, -1, -2],
    [-3, -4, -5],
    [-6, -7, -8],
    [-9, -10, -11]
]

M13 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

M14 = [
    [4, 3, 2, 1],
    [8, 7, 6, 5],
    [12, 11, 10, 9]
]

M15 = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]
#endregion

MATICE_3X3 = [M0, M1, M2, M3, M4]
MATICE_4X4 = [M5, M6, M7, M8, M9]
MATICE_4X3 = [M10, M11, M12]
MATICE_3X4 = [M13, M14, M15]

# Fce pro sčítání nebo odčítání matic
def soucet_nebo_odecet_matic(first_matice, second_matice, scitani_nebo_odcitani_jedna_nebo_minus_jedna):
    #Podmínka stejných velikostí
    pocet_radku_prvni_matice = len(first_matice)
    pocet_sloupcu_prvni_matice = len(first_matice[0])
    pocet_radku_druhe_matice = len(second_matice)
    pocet_sloupcu_druhe_matice = len(second_matice[0])
    if pocet_radku_prvni_matice == pocet_radku_druhe_matice and pocet_sloupcu_prvni_matice == pocet_sloupcu_druhe_matice:
            #
        result = []
        for i in range(len(first_matice)):
            result.append([])
            for j in range(len(first_matice[0])):
                result[i].append(first_matice[i][j]+(second_matice[i][j])*scitani_nebo_odcitani_jedna_nebo_minus_jedna)
        return result
    else:
        raise ValueError("Matice musí mít stejnou velikost.")

#Fce prá násobení matic
def nasobeni_matic(first_matice, second_matice, hodnota_krerou_nasobim_prvni_matici, hodnota_krerou_nasobim_druhou_matici):
    pocet_sloupcu_prvni_matice = len(first_matice[0])
    pocet_radku_druhe_matice = len(second_matice)
    if pocet_radku_druhe_matice == pocet_sloupcu_prvni_matice and pocet_sloupcu_prvni_matice == pocet_radku_druhe_matice:
            #
        result = []
        for i in range(len(first_matice)):
            result_now = []
            for j in range(len(second_matice[0])):
                soucet = sum(first_matice[i][k] * second_matice[k][j] for k in range(len(second_matice)))
                result_now.append(soucet)
            result.append(result_now)
            return result
    else:
        raise ValueError("První matice musí stejný počet sloupců jako má druhá matice řádků. (Jsi tupec!!)")

# TODO: M1 + M2                         -> [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
#Součet matic M1 a M2
#print(soucet_nebo_odecet_matic(M1, M2, 1))

# TODO: M1 - M5                         -> ValueError: Matice musí mít stejnou velikost.
#print(soucet_nebo_odecet_matic(M1, M5, -1))

# TODO: M1 - 3 * M4                     -> [[1, 5, 9], [13, 17, 21], [25, 29, 33]]
#print(soucet_nebo_odecet_matic(M1, M4, -3))

# TODO: M5 * M7                         -> [[5, 5, 5, 5], [13, 13, 13, 13], [21, 21, 21, 21], [29, 29, 29, 29]]
print(nasobeni_matic(M5, M7, 1, 1))

# TODO: M10 * M14                       -> [[56, 50, 44, 38], [128, 113, 98, 83], [200, 176, 152, 128], [272, 239, 206, 173]]


# TODO: M13 * M0                        -> ValueError: První matice musí stejný počet sloupců jako má druhá matice řádků.


# TODO: M12 * M15 + M8 - 2 * M6         -> [[-50, -49, -48, -47], [-70, -78, -86, -94], [-90, -107, -124, -141], [-110, -136, -162, -188]]


# TODO: M10 − M5 * M9 + 2 * M1          -> ValueError: Matice musí mít stejnou velikost.


# TODO: M8 + 4 * M6 − M11 * M13         -> [[22, 12, 2, -8], [-49, -66, -83, -100], [-27, -42, -57, -72], [-58, -76, -94, -112]]