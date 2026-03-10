numbet_one = int(input("enter number:"))
number_two = int(input("enter numbet: "))
if numbet_one == 0 or number_two == 0:
   print("NSD does not exist and nsn is 0")
else:
    if numbet_one < 0 and number_two < 0:
        numbet_one = numbet_one*(-1)
        number_two = number_two*(-1)
    else:
        numbet_one = numbet_one
        number_two = number_two
    if numbet_one > 0 and number_two < 0:
        number_two = (-1) * number_two
    elif number_two > 0 and numbet_one < 0:
        numbet_one = (-1) * numbet_one
    else:
        numbet_one = numbet_one
        number_two = number_two
    if numbet_one > number_two:
        bigger_number = numbet_one
        smaller_number = number_two
    elif numbet_one < number_two:
        bigger_number = number_two
        smaller_number = numbet_one
    else:
         print("there are simalar numbers")
    residue = 1
    while residue != 0:
        n = bigger_number // smaller_number
        residue = bigger_number - (smaller_number * n)
        bigger_number = smaller_number
        smaller_number = residue
    if x != 0:
        print("D:", bigger_number)
        o = ((numbet_one * number_two) / bigger_number )
        print("n:", o)
    else :
        print("D does not exist")
        s = numbet_one * number_two
        print("n:", s)