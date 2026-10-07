import csv

def read_dictionary(filename, key_column_index):
    student_dictionary = {}
    
    with open(filename, "rt") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        for row in csv_reader:
            key_value = row[key_column_index]
            student_dictionary[key_value] = row
    return student_dictionary

def main():
    KEY_COLUMN_INDEX = 0
    NAME_COLUMN_INDEX = 1

    students = read_dictionary("students.csv", KEY_COLUMN_INDEX)
    i_number = input("Enter the student's I-Number: ")
    i_number = i_number.replace("-", "")

    if not i_number.isdigit():
        print("Invalid I-Number.")

    elif len(i_number) > 10:
        print("Invalid I-Number: too many digits.")

    elif len(i_number) < 5:
        print("Invalid I-Number: too few digits.")

    elif i_number not in students:
        print("No such students.")

    else:
        student = students[i_number]
        name = student[NAME_COLUMN_INDEX]
        print(f"Student: {name}")

if __name__ == "__main__":
    main()