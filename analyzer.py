import statistics
import matplotlib.pyplot as plt

grades = [85, 92, 78, 96, 88, 74, 91, 82]

average = statistics.mean(grades)
highest = max(grades)
lowest = min(grades)
count = len(grades)

print("=== Smart Data Analyzer ===")
print(f"Average Grade: {average}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
print(f"Number of Grades: {count}")

plt.bar(range(len(grades)), grades)
plt.title("Student Grades")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.show()
