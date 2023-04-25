open_tabs = int(input())
salary = int(input())

fine = 0
initial_salary = salary

for _ in range(1, open_tabs + 1):
    web_name = input()
    if web_name == "Facebook":
        fine = 150
        initial_salary -= fine
        if initial_salary <= 0:
            print("You have lost your salary.")
            break
    elif web_name == "Instagram":
        fine = 100
        initial_salary -= fine
        if initial_salary <= 0:
            print("You have lost your salary.")
            break
    elif web_name == "Reddit":
        fine = 50
        initial_salary -= fine
        if initial_salary <= 0:
            print("You have lost your salary.")
            break

if initial_salary <= 0:
    pass
else:
    print(initial_salary)