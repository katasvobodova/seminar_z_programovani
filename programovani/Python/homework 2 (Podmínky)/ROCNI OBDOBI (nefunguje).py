number_month = int(input("enter the number of month"))
number_day = int(input("enter the number of day"))
if number_day>21:
    numer_of_month_to_season=number_month+1
else:
    numer_of_month_to_season=number_month

if 3< numer_of_month_to_season <7:
    print("it's spring!!!!!!")
elif 6< numer_of_month_to_season <10:
    print("it's summer!!!!!!") 
elif 9< numer_of_month_to_season <13:
    print("it's autumn!!!!!!!!!")
elif 0<numer_of_month_to_season <4 or 13:
    print("it's winter!!!!!!!!")
else:
    print("There is something wrong, try it again!")
