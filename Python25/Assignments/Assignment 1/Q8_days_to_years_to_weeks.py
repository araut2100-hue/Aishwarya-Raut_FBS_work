Days = int(input("enter number of days : "))

years = Days // 365
Days_1= Days % 365
weeks= Days_1 // 7
Total_days = Days_1 % 7

print(f'In {Days} there are {years} years , {weeks} weeks, {Total_days} days')