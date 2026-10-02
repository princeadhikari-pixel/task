
name = input("Enter student name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
highest_mark = max(subject1, subject2, subject3)
lowest_mark = min(subject1, subject2, subject3)

if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 40:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result Summary ---")
print(f"Student Name: {name}")
print(f"Total Marks: {total_marks:.2f}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Mark: {highest_mark:.2f}")
print(f"Lowest Mark: {lowest_mark:.2f}")
print(f"Final Grade: {grade}")