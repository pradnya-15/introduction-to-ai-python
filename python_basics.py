name = "Student"
age = 19
course = "Artificial Intelligence"

print("Name:", name)
print("Age:", age)
print("Course:", course)

ai_applications = [
    "ChatGPT",
    "Spam Detection",
    "Image Recognition"
]

for application in ai_applications:
    print(application)

for number in range(1, 6):
    print(number)

def greet(name):
    return "Hello, " + name + "!"

message = greet("AI Learner")
print(message)

temperature = 38

if temperature > 35:
    print("High temperature detected")
else:
    print("Temperature is normal")