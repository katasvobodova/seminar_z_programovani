pocet_barev = int(input("napiš s kolika bavama chceš hrát"))
pocet_mist = int(input("napiš pocet mist na ktere budes dosazovat barvy"))
prvni_barva = "cervena"
druha_barva = "zluta"
treti_barva = "zelena"
ctvrta_barva = "modra"
pata_barva = "ruzova"
sesta_barva = "cerna"
sedma_barva = "bila"
osma_barva = "seda"
barvy = [prvni_barva, druha_barva, treti_barva, ctvrta_barva, pata_barva, sesta_barva, sedma_barva, osma_barva]
nahodny_vyber_n_barev = rnd(barvy, size=pocet_barev)
print(nahodny_vyber_n_barev)
