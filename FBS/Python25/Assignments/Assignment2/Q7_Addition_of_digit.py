reve_num=int(input("Enter the number"))
num2= reve_num

digit1=num2%10
num2=num2//10

digit2 = num2%10
digit3=num2//10

addition= digit1 + digit2+digit3
print(f'Digit addition Of {reve_num} is {addition}')