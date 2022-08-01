student_names = []
course_names = []
student_data = {}

#=====student details=====
while True:
    try:
        student_number = int(input("How many students ? "))
        break
    except ValueError:
        print("Invalid Input")

print(" ")
for number in range(1, student_number + 1):
    while True:
        name = input(str(number) + ". Enter Student Name: ")
        if name.isalpha():
            student_names.append(name)
            break

        print("Invalid Name")
        
print(" ")
#=====course details=====
while True:
    try:
        course_number = int(input("How many courses ? "))
        break
    except ValueError:
        print("Invalid Input")

print(" ")
for number in range(1, course_number + 1):
    while True:
        name = input(str(number) + ". Enter the course Name: ")
        if name.isalpha():
            if name not in course_names:
                course_names.append(name)
                break
            else:
                print("This name is already exist")
        else:
            print("Invalid Name")

print(" ")
#=====marks=====
for student_name in student_names:
    all_marks = {}
    print(" ")
    for course_name in course_names:
        while True:
            try:
                mark = int(input(f"Enter marks of {student_name} for {course_name} :"))
                if 0 <= mark <= 100:
                    all_marks[course_name] = mark
                    break
            except ValueError:
                pass
            print("Invalid Mark")

    student_data[student_name] = all_marks

averages = []
best_performer_data = {}

#=====marks sheet=====
for student_name in student_names:
    with open(student_name + ".txt", "w") as file:
        text = "--Marks Sheet--\nCourse\tMarks\n"
        total = 0
        for course_name in course_names:
            mark = student_data[student_name][course_name]
            text += f"{course_name}\t{mark}\n"
            total += mark
        average = total/course_number
        averages.append(average)
        best_performer_data[average] = student_name
        text += f"\nTotal:  {total}\nAverage: {average}"
        file.write(text)

best = averages[0]
for average in averages:
    if average > best:
        best = average

#=====summary sheet=====
with open("summary.txt", "w") as file:
    text = f"--Summary of the Batch--\nOverall Average:\t\t{sum(averages)/student_number}\n" \
           f"Best Performer:\t\t{best_performer_data[best]}"
    file.write(text)
