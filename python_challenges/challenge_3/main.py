name = str(input("Enter your name :"))

salary_per_hour = float(input("enter your salary per hour :"))

hours_number = int(input("Enter your Working Hour :"))
legal_hour = 40


total_salary = 0.0
try:
    if hours_number >= 40:
        suplemetary_hour = hours_number - legal_hour
        
        regular_salary = legal_hour * salary_per_hour
        
        sup_salary = suplemetary_hour * (salary_per_hour * 1.5)
        
        total_salary = regular_salary + sup_salary
        
        print(f"your name is {name} and your sup salary: {sup_salary} and regular salary {regular_salary} and total salary {total_salary}")

    else:
        working_salary = hours_number * salary_per_hour
except:
        print("thre is an error !")
