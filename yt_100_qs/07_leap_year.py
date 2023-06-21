def leap_year(years):
    for year in years:
        if year % 10 != 0:
            if year % 4 == 0:
                print("Leap year")
            else:
                print("not Leap year")

        else:
            if year % 100 == 0 and year % 400 ==0:
                print("Leap year again")
            else:
                print("Not a leap year again")







years = [2004, 2008, 1900, 2023, 1600]
leap_year(years)