import csv
#from collections import defaultdict


with open('student.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    highest_marks = {}
    failed_students = {}
    subject_average = {}
    subject_row_mapping = {}
    first_line = True
    no_of_students = 0
    for row in reader:
        if first_line:
            first_line = False
            subject_average[row[3]] = 0
            subject_average[row[4]] = 0
            subject_average[row[5]] = 0
            subject_row_mapping['3']= row[3]
            subject_row_mapping['4']= row[4]
            subject_row_mapping['5']= row[5]
            continue
       
        if not highest_marks.get(row[2]):
            highest_marks[row[2]] = 0
            #print(" highest_marks[row[2]]",  highest_marks[row[2]])
            failed_students[row[2]] = 0
        total_marks = 0
        total_marks = int(row[3]) + int(row[4]) + int(row[5])
        print("total_marks", total_marks)
        
        if total_marks > highest_marks[row[2]]:
            highest_marks[row[2]] = total_marks

        if int(row[3]) < 35 or int(row[4]) < 35 or int(row[5]) < 35:
             failed_students[row[2]] = failed_students[row[2]] + 1
        subject_average[subject_row_mapping['3']] = subject_average[subject_row_mapping['3']] + int(row[3])
        subject_average[subject_row_mapping['4']] = subject_average[subject_row_mapping['4']] + int(row[4])
        subject_average[subject_row_mapping['5']] = subject_average[subject_row_mapping['5']] + int(row[5])
        no_of_students += 1
            
    for classno in highest_marks.keys():
        print("Highest marks of class " + classno + " is " + str(highest_marks.get(classno)))
        print("No. of failed students of class " + classno + " is " + str(failed_students.get(classno)))
        print("\n")

    for subject in subject_row_mapping.values():
        print("Average marks of " + subject + " is " + str(subject_average[subject]/no_of_students))

