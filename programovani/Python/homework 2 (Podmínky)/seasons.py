number_month = int(input("enter the number of month"))
number_day = int(input("enter the number of day"))
if number_day>21:
    numer_of_month_to_season=number_month+1
else:
    numer_of_month_to_season=number_month

if numer_of_month_to_season == 4 or 5 or 6:
    print("it's spring!!!!!!")
elif numer_of_month_to_season == 7 or 8 or 9:
    print("it's summer!!!!!!") 
elif numer_of_month_to_season == 10 or 11 or 12:
    print("it's autumn!!!!!!!!!")
elif numer_of_month_to_season == 1 or 2 or 3 or 13:
    print("it's winter!!!!!!!!")
else:
    print("There is something wrong, try it again!")
