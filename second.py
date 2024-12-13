basic_salary=float(input("enter the basic salary"))
if basic_salary<10000:
    hra=(67/100)*basic_salary
    da=(73/100)*basic_salary
elif 10000<=basic_salary<=20000:
    hra = (69/100) * basic_salary
    da = (76/100) * basic_salary
else:
    hra = (73/100) * basic_salary
    da= (89/100) * basic_salary
gs= hra + da+ basic_salary
print(f'Gross salary is : {gs:.2f}')