# Codomax Level 2 - Introduction to AI & Python
# Beginner practice programs

# 1. Variables
name = "Pradnya"
age = 19
course = "AI and Data Science"
print("Name:", name)
print("Age:", age)
print("Course:", course)

# 2. Data types
name = "Pradnya"
age = 19
marks = 90
is_student = True
print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))

# 3. Conditions
temperature = 38
if temperature > 35:
    print("High temperature")
else:
    print("Normal temperature")

# 4. For loop
for number in range(1, 6):
    print(number)

# 5. While loop
count = 1
while count <= 5:
    print(count)
    count += 1

# 6. Lists
subjects = ["Python", "AI", "Machine Learning", "Data Science"]
for subject in subjects:
    print(subject)

# 7. Functions
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print("Sum:", result)

# 8. Simple calculator
a = 20
b = 10
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 9. Even or odd
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 10. Student grade
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs improvement")