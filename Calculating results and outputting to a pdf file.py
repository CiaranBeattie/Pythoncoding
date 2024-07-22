def display_menu():
    print("1. Input Student Names, Modules, and Results")
    print("2. Calculate Results")
    print("3. Output to PDF File")
    print("4. Exit")

def input_student_info():
    students = []
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        modules = {}
        for _ in range(7):
            module_code = input("Enter module code: ")
            module_name = input("Enter module name: ")
            credits = int(input("Enter credits: "))
            grade = float(input("Enter grade: "))
            modules[module_code] = {"Module Name": module_name, "Credits": credits, "Grade": grade}
        students.append({"Name": name, "Modules": modules})
    return students

def calculate_results(students):
    for student in students:
        total_credits = total_weighted_grade = 0
        for module in student["Modules"].values():
            total_credits += module["Credits"]
            total_weighted_grade += module["Credits"] * module["Grade"]
        student["GPA"] = total_weighted_grade / total_credits if total_credits > 0 else 0

def output_to_pdf(students):
    for student in students:
        filename = f"{student['Name']}_transcript.pdf"
        with open(filename, "w") as f:
            f.write(f"Student Name: {student['Name']}\n")
            for module_code, module_info in student['Modules'].items():
                f.write(f"{module_code}: {module_info['Module Name']} - Grade: {module_info['Grade']}\n")
            f.write(f"Overall GPA: {student['GPA']:.2f}\n")
        print(f"Transcript for {student['Name']} has been saved to {filename}")

def main():
    students = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            students = input_student_info()
        elif choice == "2":
            if students:
                calculate_results(students)
                print("Results calculated successfully.")
            else:
                print("Please input student information first.")
        elif choice == "3":
            if students:
                output_to_pdf(students)
                print("Transcripts generated successfully.")
            else:
                print("Please input student information first.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()