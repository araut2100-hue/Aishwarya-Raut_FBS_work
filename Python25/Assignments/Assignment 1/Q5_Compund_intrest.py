p = int(input("Enter Value Of principle:"))
T = int (input("Enter Value of Time:"))
R = int (input("Enter Value Of ROI:"))

Compund_Intrest1 = (1 + R/100 ) **T
Compund_Intrest = p * Compund_Intrest1 - p

print (f'Compound Intrest For amount {p}/- with {R}% ROI for {T} years is {Compund_Intrest}/-')