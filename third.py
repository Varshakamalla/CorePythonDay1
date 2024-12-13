project = float(input("Enter the project score: "))
internal = float(input("Enter the internal score: "))
external = float(input("Enter the external score: "))
if project < 50:
    print(f'Failed in project, marks are: {project}')
if internal < 50:
    print(f'Failed in internal, marks are: {internal}')
if external < 50:
    print(f'Failed in external, marks are: {external}')
else:
    total_marks = (70 / 100) * project + (10 / 100) * internal + (20 / 100) * external
    print(f'Total score is {total_marks:.2f}')
    if total_marks > 90:
        print("A grade")
    elif total_marks > 80:
        print("B grade")
    elif total_marks > 70:
        print("C grade")
    else:
        print("Below C grade")
