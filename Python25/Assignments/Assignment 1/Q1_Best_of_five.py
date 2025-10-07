m1 = int(input("enter marks of subject 1 :"))
m2 = int(input("enter marks of subject 2 :"))
m3 = int(input("enter marks of subject 3 :"))
m4 = int(input("enter marks of subject 4 :"))
m5 = int(input("enter marks of subject 5 :"))

sum = m1 + m2 + m3 + m4 + m5
perce = (sum / 500) *100

print(f'The percentage is {perce}')