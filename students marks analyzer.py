# Basic project of Student Marks Analysis #
# step 1: give input for 5 subjects

marks = list(map(int,input("Enter marks of 5 subjects sperated with space:").split()))

# Calculations
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

# Grade system

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

# Results
print("\n----- Student Marks Analysis -----")
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", grade)
                           
