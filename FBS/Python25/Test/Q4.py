area_wall = int(input("enter Area of Wall :"))
Int_cost = int(input("enter Interior Cost :"))
Ext_cost = int(input("enter Exterior Cost :"))

Total_wall = area_wall* 7

Amt_int = Total_wall * Int_cost

Amt_ext = Total_wall * Ext_cost

print(f'Cost of painting For Interior walls is {Amt_int} and Cost of painting for Exterior is {Amt_ext}')


