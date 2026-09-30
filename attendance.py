# STUDENT ATTENDANCE MANAGEMENT SYSTEM

students = {}
attendance = {}

while True:
    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Attendance Report")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        students[roll] = name
        attendance[roll] = []

        print("Student added successfully!")

    # 2. Mark Attendance
    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P":
                attendance[roll].append("Present")
                print("Attendance marked Present.")
            elif status == "A":
                attendance[roll].append("Absent")
                print("Attendance marked Absent.")
            else:
                print("Please enter only P or A.")
        else:
            print("Student not found.")

    # 3. Attendance Report
    elif choice == "3":
        print("\n===== ATTENDANCE REPORT =====")

        for roll, name in students.items():
            records = attendance[roll]
            present = records.count("Present")
            absent = records.count("Absent")
            total = present + absent

            print("\nRoll Number:", roll)
            print("Name:", name)
            print("Present:", present)
            print("Absent:", absent)
            print("Total Classes:", total)

    # 4. Search Student
    elif choice == "4":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student Found!")
            print("Roll Number:", roll)
            print("Name:", students[roll])
        else:
            print("Student not found.")

    # 5. Exit
    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
