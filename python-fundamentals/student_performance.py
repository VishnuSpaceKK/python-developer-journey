# Finds students who scored 60 or higher.
# Stores those students somewhere.
# Calculates the average marks of the passing students.
# Prints the names of the passing students.
# Prints the average.
# Handles the case where nobody passes.

students = [
    {"name": "Arun", "marks": 85},
    {"name": "Rahul", "marks": 42},
    {"name": "Meera", "marks": 91},
    {"name": "Vikas", "marks": 67},
]

def process_student(students):
    passed = []
    total = 0
    for i in students:
        if i['marks'] >= 60:
            passed.append(i['name'])
            total += i['marks']
    if not passed:
        return {"avg": None, "passed": passed}
    
    avg = total/len(passed)
    return {"avg" : avg, "passed": passed}

result = process_student(students)
if not result['passed']:
    print('No students have passed')
else:
    print(f"Average score = {result['avg']}")
    for i in result['passed']:
        print(i)

