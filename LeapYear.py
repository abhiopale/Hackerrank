#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
#1900<=year<=10**5
def is_leap(year):
    if (year>=1900 and year<=10**5):
        if year%100==0:
            if year%400==0: return True
            else : return False
        elif year%4==0: return True
        else: return False
year = int(input())