print("---------------------------------------------")
print("Welcome User!")
print("Student Activity Grading System")
print("----------------------------------------------")

def ave(score1, score2, score3):
    avg = (score1 + score2 + score3) / 3
    return avg

def get_status(avg):
    if avg >= 90:
        return "Excellent!!"
    elif avg >= 80:
        return "Very Good!"
    elif avg >= 75:
        return "Passed"
    else:
        return "Failed!"

students = int(input("Enter how many students: "))
print("---------------------------------------------")
n = 3
stu = 0

if students < n:
    print("Students must be Greater than 3!! Try again")
else:
    while stu < students:
        stu = stu + 1
        print("Student", stu)
        name = input("Enter name: ")
        score1 = float(input("Activity_1 score: "))
        score2 = float(input("Activity_2 score: "))
        score3 = float(input("Activity_3 score: "))

        avg = ave(score1, score2, score3)
        status = get_status(avg)


        print("")
        print("Name: ", name)
        print("Average: ", avg)
        print("Status: ", status)
        print("-------------------------------------------")

print("All done")
print("Thank you for Using this Student Activity Grading System!")
