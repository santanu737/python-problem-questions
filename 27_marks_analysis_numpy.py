import numpy as np

marks = np.array([
    [50, 85, 80],
    [60, 95, 35],
    [70, 65, 68],
    [85, 55, 65],
    [45, 95, 35]
])

print("Here's our marks data for 5 students across 3 subjects:")
print(marks)


# 1 - Find the maximum marks across the whole array
max_marks = np.max(marks)
print("\nThe highest score is (for a sub)", max_marks)

# 2 - Find the minimum marks across the whole array
min_marks = np.min(marks)
print("The lowest score ia(for a sub)", min_marks)


# 3 - Find the average marks across the whole array
avg_marks = np.mean(marks)
print("average marks ", avg_marks, "marks")

# 4 - Find the student id (row index) who scored maximum marks in Subject 1
student_id = np.argmax(marks[:, 1])
print("\nStudent", student_id, "topped Subject 1 with", marks[student_id, 1], "marks")


# 5 - Find the maximum marks subject-wise (best score in each column)
max_subject_wise = np.max(marks, axis=0)
print("\nBest score in each subject:", max_subject_wise)

# 6 - Find the average marks subject-wise (mean of each column)
avg_subject_wise = np.mean(marks, axis=0)
print("Average score in each subject:", avg_subject_wise)


# 7 - Add 40 marks for students whose score is less than 50, in Subject 2 only
marks_updated = marks.copy()
marks_updated[:, 2] = np.where(marks[:, 2] < 50, marks[:, 2] + 40, marks[:, 2])
print("\nUpdated marks (Subject 2 scores below 50 get +40):\n", marks_updated)

# 8 - Number of students scoring more than 50 in Subject 2
count_sub2 = np.sum(marks[:, 2] > 50)
print("\nNumber of students scoring more than 50 in Subject 2:", count_sub2)

# 9 - Minimum marks of Student 2
student2_min = np.min(marks[2])
print("Student 2's lowest score:", student2_min)

# 10 - Maximum marks of Student 4
student4_max = np.max(marks[4])
print("Student 4's highest score:", student4_max)

# 11 - Solve the two linear equations using numpy's linear algebra package
#      3x = 5y + 10   ->  3x - 5y = 10
#      4x - 2y = 7    ->  4x - 2y = 7
A = np.array([
    [3, -5],
    [4, -2]
])
b = np.array([10, 7])

x, y = np.linalg.solve(A, b)
print(f"\nSolving 3x = 5y + 10 and 4x - 2y = 7:")
print(f"x = {x:.4f}, y = {y:.4f}")