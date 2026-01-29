from grade import show_result

print("===== Input Score Page =====")
score = float(input("Enter score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
else:
    show_result(score)
