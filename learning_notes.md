# Codomax Level 2: Introduction to AI & Python

## 1. Introduction to Artificial Intelligence

Artificial Intelligence (AI) is a branch of computer science that focuses on developing computer systems capable of performing tasks that normally require human intelligence.

These tasks include understanding language, recognising images, solving problems, making recommendations, and assisting in decision-making.

### Examples of AI
- Voice assistants such as Siri and Alexa.
- Chatbots that answer questions.
- Recommendation systems used by YouTube and Netflix.
- Facial recognition systems.
- AI-powered translation tools.

### Importance of AI
- Automates repetitive tasks.
- Helps analyse large amounts of data.
- Supports faster decision-making.
- Improves efficiency and productivity.
- Enables personalised user experiences.

## 2. Difference Between AI, Machine Learning and Deep Learning

### Artificial Intelligence (AI)

AI is the broad field of developing computer systems that perform tasks associated with human intelligence.

### Machine Learning (ML)

Machine Learning is a subset of AI that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every situation.

### Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns from large amounts of data.

### Comparison

| Feature | Artificial Intelligence | Machine Learning | Deep Learning |
|---|---|---|---|
| Meaning | Broad field of intelligent systems | Systems learn from data | Systems learn using multilayer neural networks |
| Scope | Broadest | Subset of AI | Subset of ML |
| Data requirement | Depends on the technique | Often requires training data | Often benefits from large datasets |
| Techniques | Rules, search, ML and others | Decision trees, regression and others | Deep neural networks |
| Applications | Planning and intelligent assistants | Spam detection and predictions | Image recognition and speech processing |

### Relationship

**Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence**

This means Deep Learning is part of Machine Learning, and Machine Learning is part of Artificial Intelligence.

## 3. Real-World Applications of AI

AI is used across many industries to automate tasks, identify patterns, and support decisions.

### 3.1 Healthcare
- Assists in analysing medical images.
- Helps identify potential signs of diseases.
- Supports medical research and patient monitoring.

### 3.2 Banking and Finance
- Detects suspicious transactions.
- Helps identify possible fraudulent activities.
- Supports customer service through chatbots.

### 3.3 Agriculture
- Helps monitor crop health.
- Supports plant disease detection.
- Assists with weather analysis and irrigation planning.

### 3.4 Education
- Provides personalised learning recommendations.
- Supports students through intelligent tutoring tools.
- Helps teachers organise and analyse learning progress.

### 3.5 Transportation
- Predicts traffic patterns.
- Supports driver-assistance systems.
- Helps optimise routes and travel times.

### 3.6 Environmental Protection
- Analyses environmental data.
- Helps forecast air pollution.
- Supports wildlife monitoring and climate research.

## 4. Python Installation and Setup

Python is a high-level, general-purpose programming language known for its readable syntax and wide range of applications.

Python is commonly used in:
- Web development.
- Automation.
- Data analysis.
- Artificial Intelligence.
- Machine Learning.
- Scientific computing.

### Google Colab

For this task, I used **Google Colab**, an online notebook environment that allows users to write and execute Python programs directly in a web browser.

Website: https://colab.research.google.com/

### Steps to Use Google Colab

1. Open the Google Colab website.
2. Sign in with a Google account if prompted.
3. Create a new notebook.
4. Enter Python code into a code cell.
5. Click the Run button or press `Shift + Enter`.
6. Observe the output displayed below the cell.

### Advantages of Google Colab
- No local Python installation is required.
- Programs can be executed in a browser.
- Notebooks can be saved and shared.
- It supports data analysis and machine learning libraries.

## 5. Python Fundamentals

### 5.1 Variables

Variables are names used to store values in a program. Python determines a variable's type from the value assigned to it.

Example:

```python
student_name = "Pradnya"
age = 19

print(student_name)
print(age)
```

Output:

```text
Srinithi
19
```

### 5.2 Data Types

Data types describe the kind of value stored in a variable.

| Data Type | Description | Example |
|---|---|---|
| `str` | Text | `"Hello"` |
| `int` | Whole number | `19` |
| `float` | Decimal number | `85.5` |
| `bool` | True or False | `True` |
| `list` | Ordered collection | `[10, 20, 30]` |

Example:

```python
name = "Pradnya"
age = 19
height = 5.6
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

The `type()` function returns the data type of a value.

### 5.3 Conditional Statements

Conditional statements allow a program to make decisions based on whether a condition is true or false.

Python provides:
- `if` — executes a block when a condition is true.
- `elif` — checks another condition when earlier conditions are false.
- `else` — executes a block when none of the preceding conditions is true.

Example:

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```text
Grade B
```

### 5.4 For Loop

A `for` loop repeats a block of code for each item in a sequence or iterable.

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

The `range(1, 6)` function generates numbers from 1 to 5.

### 5.5 While Loop

A `while` loop repeatedly executes a block of code as long as its condition remains true.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

The statement `count += 1` increases the counter after each iteration. Updating the counter prevents this example from running indefinitely.

### 5.6 Lists

A list stores multiple items in a single variable. Lists are ordered and can be modified after creation.

Example:

```python
subjects = ["Python", "AI", "Machine Learning"]

print(subjects)
print(subjects[0])

subjects.append("Data Science")
print(subjects)
```

Output:

```text
['Python', 'AI', 'Machine Learning']
Python
['Python', 'AI', 'Machine Learning', 'Data Science']
```

Important list operations:
- `append()` — adds an item to the end.
- `remove()` — removes a matching item.
- `len()` — returns the number of items.
- Indexing — accesses an item using its position, starting at index `0`.

### 5.7 Functions

A function is a reusable block of code that performs a specific task. Functions are defined using the `def` keyword.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```text
30
```

Benefits of functions:
- Reduce code repetition.
- Improve readability.
- Make programs easier to test.
- Allow code to be reused with different inputs.

## 6. Python Practice Programs

The file `python_basics.py` contains beginner exercises covering the following concepts.

1. **Variables:** Store and display values.
2. **Data Types:** Identify strings, integers, floats, and Boolean values.
3. **Conditional Statements:** Make decisions using `if`, `elif`, and `else`.
4. **For Loops:** Repeat statements over a sequence or range.
5. **While Loops:** Repeat statements while a condition is true.
6. **Lists:** Store and manipulate collections of values.
7. **Functions:** Create reusable blocks of code.
8. **Simple Calculator:** Perform arithmetic operations such as addition, subtraction, multiplication, and division.
9. **Even-or-Odd Checking:** Determine whether an integer is divisible by two.
10. **Basic Grade Calculator:** Assign a grade based on marks and specified conditions.

### Example: Even-or-Odd Checking

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

The modulo operator `%` returns the remainder after division. If the remainder after division by 2 is zero, the number is even.

### Example: Simple Calculator

```python
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division by zero is not allowed.")
```

This program accepts two numbers and performs basic arithmetic operations. It checks the second number before division to avoid division by zero.

## 7. What I Learned

Through this learning activity, I developed a basic understanding of Artificial Intelligence, Machine Learning, and Deep Learning.

I also learned about real-world applications of AI in healthcare, banking, agriculture, education, transportation, and environmental protection.

In Python programming, I practised:
- Creating variables and identifying data types.
- Using conditional statements for decision-making.
- Applying `for` and `while` loops.
- Creating and modifying lists.
- Defining functions and returning results.
- Writing simple calculator, even-or-odd, and grade-calculation programs.
- Using Google Colab to write and execute Python code online.

These concepts have helped me develop a foundation for further learning in Python programming, Artificial Intelligence, and Machine Learning.

## 8. Learning Resources

1. **Google Colab:** https://colab.research.google.com/
2. **Official Python Website:** https://www.python.org/
3. **Python Tutorial:** https://docs.python.org/3/tutorial/
4. **Python Built-in Functions:** https://docs.python.org/3/library/functions.html

## 9. Conclusion

This activity provided an introduction to Artificial Intelligence and fundamental Python programming concepts. By combining theoretical notes with practical coding exercises, I gained a clearer understanding of AI applications and basic programming techniques.

The knowledge gained through this task serves as a starting point for exploring more advanced topics, including data analysis, Machine Learning algorithms, and AI application development.

---

