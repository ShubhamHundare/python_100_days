student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# total = sum(student_scores)
# print(total)
#
# max_val = max(student_scores)
# print(max_val)

min_val = 1000
for score in student_scores:
    if score < min_val:
        min_val = score

print(min_val)
