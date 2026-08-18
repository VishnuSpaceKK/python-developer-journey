# Calculate each student's average mark.
# A student passes if their average is 60 or higher.
# Find all passing students.
# Find the student with the highest average.
# Calculate the overall average of all students.
# Handle an empty student list.

students = [
    {"name": "Arun", "marks": [85, 78, 92]},
    {"name": "Rahul", "marks": [42, 55, 48]},
    {"name": "Meera", "marks": [91, 88, 95]},
    {"name": "Vikas", "marks": [67, 72, 61]},
]

def cal_avg(marks):
    if not marks:
        return None
    return sum(marks)/len(marks)
     


def student_performance(students):
    passed_students = []
    top_scorer = None
    student_avgs = []
    highest_avg = None

    for student in students:
        avg = cal_avg(student['marks'])
        if avg is None:
            continue
        student_avgs.append(avg)
        if avg >= 60:
            passed_students.append(student['name'])
        if highest_avg is None or avg > highest_avg:
            highest_avg = avg
            top_scorer = student['name']
    if not student_avgs:
        return None
    overall_average = cal_avg(student_avgs)

    result = {
    "passed": passed_students,
    "top_student": top_scorer,
    "overall_average": round(overall_average, 2)}
    return result


result = student_performance(students)

if result is None:
    print("Please provide a valid data.")
else:
    print("passed students:")
    for name in result['passed']:
        print(name)
    print(f"Top Scorer : {result['top_student']}")
    print(f"overall Average : {result['overall_average']}")