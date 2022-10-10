from datetime import date
 
def CalculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year = today.year)
    except ValueError:
        birthday = born.replace(year = today.year,
                  month = born.month + 1, day = 1)
 
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
         
# Enter the year of birth then the month then day
print(CalculateAge(date(2020,7,23)), "years")  