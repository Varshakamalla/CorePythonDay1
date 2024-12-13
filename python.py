salary = int(input("Enter your total salary: "))
x = int(input("Enter the first day shopping bill: "))
y = int(input("Enter the second day shopping bill: "))
z = int(input("Enter the third day shopping bill: "))
sum_of_shopping = x + y + z
print(f'Total money spent on shopping: {sum_of_shopping}')

percent = (sum_of_shopping / salary) * 100
print(f'Percentage of salary spent on shopping: {percent:.2f}%') 
