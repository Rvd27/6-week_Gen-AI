from flask import Flask, request, jsonify

# Create Flask App
app = Flask(__name__)

# Temporary database
students = []

# -----------------------------------
# HOME API
# -----------------------------------

@app.route('/')
def home():

    return jsonify({
        "message": "Welcome to Student API"
    })

# -----------------------------------
# ADD STUDENT API
# -----------------------------------

@app.route('/add-student', methods=['POST'])
def add_student():

    data = request.json

    name = data.get('name')
    age = data.get('age')

    # Validation
    if not name:
        return jsonify({
            "status": "error",
            "message": "Name is required"
        }), 400

    # Create student object
    student = {
        "name": name,
        "age": age
    }

    # Save student
    students.append(student)

    return jsonify({
        "status": "success",
        "message": "Student added successfully",
        "student": student
    })

# -----------------------------------
# GET ALL STUDENTS API
# -----------------------------------

@app.route('/students', methods=['GET'])
def get_students():

    return jsonify({
        "total_students": len(students),
        "students": students
    })

# -----------------------------------
# RUN APPLICATION
# -----------------------------------

if __name__ == '__main__':

    app.run(debug=True)