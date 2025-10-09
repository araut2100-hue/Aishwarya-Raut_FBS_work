Feet = int(input("enter Feet :"))
inch = int(input("enter Inch :"))

# Feet= 9
# inch= 8
meter = (Feet* 0.3048) +  (inch* 0.0254)
# print(meter)

cms_1=meter - (meter//1)

final_cm= cms_1*100
# print(final_cm)

print(f'in {Feet}feet and {inch} there is {meter} meters and {final_cm} cms')