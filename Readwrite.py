# Write Data

file = open("student.txt", "w")

file.write("Name: Rahul\n")
file.write("Course: Python")

file.close()

# Read Data

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()