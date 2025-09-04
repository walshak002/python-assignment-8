"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""

class AttendanceRegister:
    def __init__(self):
        # Store attendance in a dictionary where student name is the key
        self.records = {}

    def mark_present(self, student_name):
        self.records[student_name] = "Present"

    def mark_absent(self, student_name):
        self.records[student_name] = "Absent"

    def get_status(self, student_name):
        return self.records.get(student_name, "No record found")

    def show_register(self):
        """Return the full attendance register"""
        return self.records
    
register = AttendanceRegister()
register.mark_present("John")
register.mark_absent("Mary")

print(register.get_status("John"))     
print(register.show_register())      
