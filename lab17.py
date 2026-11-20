def box(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

box("STUDENT RECORDS MANAGEMENT SYSTEM")

students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]},
}


def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average


def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(
        f"Roll No: {roll} | Name: {student['Name']:<10} | "
        f"Marks: {student['Marks']} | Total: {total} | "
        f"Average: {average:.2f}%")


def add_student(records, roll, name, marks):
    if roll in records:
        print(f"[ERROR] Roll Number '{roll}' already exists.")
        return

    records[roll] = {"Name": name, "Marks": marks}
    print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


while True:
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        print("\n--- All Student Records ---")
        for roll, student in students.items():
            display_student(roll, student)
        print(f"Total Students: {len(students)}")

    elif choice == "2":
        print("\n--- Add New Student ---")
        roll = input("Enter Roll Number: ").strip()

        if roll in students:
            print(f"[ERROR] Roll Number '{roll}' already exists.")
            continue

        name = input("Enter Student Name: ").strip()
        if not name:
            print("[ERROR] Student name cannot be empty.")
            continue

        marks = []
        print("Enter marks for 3 subjects:")
        valid_marks = True

        for subject in range(1, 4):
            try:
                mark = int(input(f"  Subject {subject}: "))
                if not 0 <= mark <= 100:
                    print("[ERROR] Marks must be between 0 and 100.")
                    valid_marks = False
                    break
                marks.append(mark)
            except ValueError:
                print("[ERROR] Enter marks as whole numbers.")
                valid_marks = False
                break

        if valid_marks:
            add_student(students, roll, name, marks)

    elif choice == "3":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)

        if student is not None:
            print("[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    elif choice == "4":
        print("Thank you for using the Student Records System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 4.")