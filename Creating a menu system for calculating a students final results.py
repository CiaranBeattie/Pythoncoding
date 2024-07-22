from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.para import Paragraph


class Student:
    def __init__(self, name):
        """Initialize a Student object with a name attribute and an empty list to store module details."""
        self.name = name
        self.modules = []

    def add_module_result(self, module_code, credits, module_name, result):
        """Add module details and result for the student."""
        self.modules.append({
            "module_code": module_code,
            "credits": credits,
            "module_name": module_name,
            "result": result
        })


def input_student_data():
    """Input student details and module results."""
    name = input("Enter student name: ")
    student = Student(name)
    while True:
        module_code = input("Enter module code (or type 'done' to finish): ")
        if module_code.lower() == 'done':
            break
        try:
            credits = int(input("Enter credits for the module: "))
            module_name = input("Enter module name: ")
            result = float(input("Enter result for the module: "))
        except ValueError:
            print("Invalid input. Please enter valid numeric values for credits and result.")
            continue
        # Add module details to the student object
        student.add_module_result(module_code, credits, module_name, result)
    return student


def calculate_results(student):
    """Calculate overall result for the student."""
    total_credits = sum(module["credits"] for module in student.modules)
    total_marks = sum(module["credits"] * module["result"] for module in student.modules)
    try:
        overall_result = total_marks / total_credits
    except ZeroDivisionError:
        print("Error: Total credits cannot be zero.")
        return None
    return overall_result


def calculate_grade(percentage):
    """Calculate grade based on percentage."""
    if percentage >= 80:
        return 'A'
    elif 70 <= percentage < 80:
        return 'B'
    elif 60 <= percentage < 70:
        return 'C'
    elif 50 <= percentage < 60:
        return 'D'
    else:
        return 'F'


def generate_pdf_transcript(student, overall_result, filename):
    """Generate PDF transcript."""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []
    data = [["Module Code", "Credits", "Module Name", "Result", "Grade"]]

    for module in student.modules:
        percentage = (module["result"] / 120) * 100
        grade = calculate_grade(percentage)
        data.append([module["module_code"], module["credits"], module["module_name"], f"{percentage:.2f}%", grade])

    # Create a table
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Add the table to the elements list
    elements.append(table)

    # Add overall result and grade
    overall_percentage = (overall_result / 100) * 100
    overall_grade = calculate_grade(overall_percentage)
    overall_text = f"Overall Result: {overall_result:.2f} ({overall_percentage:.2f}%)\nOverall Grade: {overall_grade}"
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(overall_text, styles["Normal"]))

    # Build the PDF
    doc.build(elements)
    print(f"PDF Transcript saved to {filename}")


def save_student_data(student, filename):
    """Save student data to a text file."""
    try:
        with open(filename, 'w') as file:
            file.write(f"Student Name: {student.name}\n")
            file.write("Module Code\tCredits\tModule Name\tResult\n")
            for module in student.modules:
                file.write(f"{module['module_code']}\t\t{module['credits']}\t{module['module_name']}\t{module['result']}\n")
        print(f"Student data saved to {filename}")
    except Exception as e:
        print(f"Error saving student data: {e}")


def main():
    """Main function to run the program."""
    print("Welcome to Student Transcript Generator")
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Input Student Data")
        print("2. Calculate Results")
        print("3. Generate Transcript (PDF)")
        print("4. Save Student Data to a text file")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Input student data
            student = input_student_data()
        elif choice == '2':
            # Calculate overall result for the student
            overall_result = calculate_results(student)
            if overall_result is not None:
                print(f"Overall Result: {overall_result:.2f}")
        elif choice == '3':
            # Generate PDF transcript
            filename = input("Enter the filename to save the PDF transcript (e.g., transcript.pdf): ")
            if student and overall_result is not None:
                generate_pdf_transcript(student, overall_result, filename)
        elif choice == '4':
            # Save student data to a file
            filename = input("Enter the filename to save the student data (e.g., student_data.txt): ")
            if student:
                save_student_data(student, filename)
        elif choice == '5':
            # Exit the program
            print("Exiting program. Goodbye!")
            break
        else:
            # Error handling message
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()