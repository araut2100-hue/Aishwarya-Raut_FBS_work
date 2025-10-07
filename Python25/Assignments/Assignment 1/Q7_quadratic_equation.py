A = int(input("Enter Value Of A:" ))
B = int (input("Enter Value of B:"))
C = int (input("Enter Value Of C:"))

equi = ((4**2)- 4*A*C) ** 0.5
equi_1 = (-B + equi) / 2*A

equi_2 = (-B - equi) / 2*A
print(f'value of x1 is {equi_1} and value of x2 is {equi_2} ')
