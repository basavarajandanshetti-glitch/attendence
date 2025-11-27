# Student Attendance Tracker Program

import sys

# If arguments are provided (classes held, attended)
if len(sys.argv) == 3:
    classes_held = int(sys.argv[1])
    classes_attended = int(sys.argv[2])
    print("User provided attendance data")
else:
    # Default values
    classes_held = 50
    classes_attended = 40
    print("Default attendance data used")

# Calculate attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance Percentage:", attendance_percentage)
