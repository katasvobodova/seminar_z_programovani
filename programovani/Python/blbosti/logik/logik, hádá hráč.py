import random
print("Hraješ logik, hraje se na 4 místa s osmi barvami (Red, Green, Blue, Yellow, White, Orange, Black, Purple")
pocet_hranych_barev = 4
colors = [
    "Red", "Green", "Blue", "Yellow",
    "White", "Orange", "Black", "Purple"]

# Přiřazení čísla ke každé barvě
colors_with_numbers = {color: index + 1 for index, color in enumerate(colors)}

nahodny_vyber_n_barev = random.sample(colors, pocet_hranych_barev)
barva_na_prvni_pozici = 0
barva_na_druhe_pozici = 0
barva_na_treti_pozici = 0
barva_na_ctvrte_pozici = 0
cervene_indikatory = 0
barvy_ktere_si_hrac_mysli = [barva_na_prvni_pozici, barva_na_druhe_pozici, barva_na_treti_pozici, barva_na_ctvrte_pozici]

rozdily_v_polozkach_seznamu = sum(1 for a, b in zip(nahodny_vyber_n_barev, barvy_ktere_si_hrac_mysli) if a != b)

while cervene_indikatory != 4:
        barva_na_prvni_pozici = input("Napiš barvu která si mislíš že je na první pozici: ")
        barva_na_druhe_pozici = input("Napiš barvu která si mislíš že je na druhé pozici: ")
        barva_na_treti_pozici = input("Napiš barvu která si mislíš že je na třetí pozici: ")
        barva_na_ctvrte_pozici = input("Napiš barvu která si mislíš že je na čtvrté pozici: ")
        barvy_ktere_si_hrac_mysli = [barva_na_prvni_pozici, barva_na_druhe_pozici, barva_na_treti_pozici, barva_na_ctvrte_pozici]

        rozdily_v_polozkach_seznamu = sum(1 for a, b in zip(nahodny_vyber_n_barev, barvy_ktere_si_hrac_mysli) if a != b)
        #Cervena meaning is maz tam barvu spravne ale na spatnem miste
        def spocitej_zlute_indikatory(barvy_ktere_si_hrac_mysli, nahodny_vyber_n_barev):
            zbyvajici_nahodny_vyber_n_barev = nahodny_vyber_n_barev.copy()
            zbyvajici_hracuv_pokus = []

            # Odstraneni shod s cervenimi identifikatory
            for i in range(len(barvy_ktere_si_hrac_mysli)):
                if barvy_ktere_si_hrac_mysli[i] == nahodny_vyber_n_barev[i]:
                    zbyvajici_nahodny_vyber_n_barev[i] = None
                else:
                    zbyvajici_hracuv_pokus.append(barvy_ktere_si_hrac_mysli[i])

            # Pocet zlutych identifiatoru
            zluty_indikatory = 0
            for barva in zbyvajici_hracuv_pokus:
                if barva in zbyvajici_nahodny_vyber_n_barev:
                    zluty_indikatory += 1
                    zbyvajici_nahodny_vyber_n_barev[zbyvajici_nahodny_vyber_n_barev.index(barva)] = None

            return zluty_indikatory

        #Cervena meaning is maz tam barvu spravne a na spravnem miste
        def spocitej_cervene_indikatory(nahodny_vyber_n_barev, barvy_ktere_si_hrac_mysli, rozdily_v_polozkach_seznamu):
            cervene_indikatory = 0
            if nahodny_vyber_n_barev == barvy_ktere_si_hrac_mysli:
                cervene_indikatory = 4
            elif rozdily_v_polozkach_seznamu == 1:
                cervene_indikatory = 3
            elif rozdily_v_polozkach_seznamu == 2:
                cervene_indikatory = 2
            elif rozdily_v_polozkach_seznamu == 3:
                cervene_indikatory = 1
            elif rozdily_v_polozkach_seznamu == 4:
                cervene_indikatory = 0
            else:
                print("There is something wrong!")

            return cervene_indikatory

        # Výpočet žlutých indikátorů
        vysledek = spocitej_zlute_indikatory(barvy_ktere_si_hrac_mysli, nahodny_vyber_n_barev)
        print(f"Počet žlutých indikátorů: {vysledek}")

        # Výpočet červených indikátorů
        vysledek = spocitej_cervene_indikatory(nahodny_vyber_n_barev, barvy_ktere_si_hrac_mysli, rozdily_v_polozkach_seznamu)
        print(f"Počet červených indikátorů: {vysledek}")

        cervene_indikatory = spocitej_cervene_indikatory(nahodny_vyber_n_barev, barvy_ktere_si_hrac_mysli, rozdily_v_polozkach_seznamu)