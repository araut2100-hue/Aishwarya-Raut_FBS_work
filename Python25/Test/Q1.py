length =int(input("ennter length :"))
breadth =int(input("ennter breadth :"))
radius = int(input("ennter radius :"))

area_rect = length * breadth
area_circle = ( 22/7 * radius **2) / 2
area = area_circle + area_rect

print(f'Area of given diagram is {area}')

perimeter_rect = 2*(length + breadth)
perimeter_circle = (22/7 * radius) + (radius *2)
perimeter = perimeter_rect + perimeter_circle

print(f'Parameter of given diagram is {perimeter}')

