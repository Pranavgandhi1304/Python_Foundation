marks = int(input("Enter marks (0-100): "))
#comparing marks to give the grade to student in the range
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")