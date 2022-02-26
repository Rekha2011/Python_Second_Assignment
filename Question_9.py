#Question 9:
#We have the marks of a student in each subject given below. Write a Python function that takes two parameters 'name' and 'subjects_marks.' Finally, print the student's name and all the subjects in which his/her marks are above 60. If the 'name' is not provided, print 'None.'
def student_details(name = "none", **students_details):
    subjects=[]
    for key , value in students_details.items():
        if value >60:
            subjects.append(key)
        print("name :{} - subjects:{}".format(name, set(subjects)))
    students_details("Brandom",Mathematics = 80, Physics = 58, Chemistry = 62, English = 72, Biology = 50)


