import os

# Create the directory structure for the school app
base_dir = 'school_app'
templates_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

os.makedirs(templates_dir, exist_ok=True)
os.makedirs(static_dir, exist_ok=True)

# Define the content for each file
app_content = """from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for demonstration
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        students.append({'name': name, 'grade': grade})
        return redirect(url_for('index'))
    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)
"""

index_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>School App</title>
</head>
<body>
    <h1>Student List</h1>
    <a href="{{ url_for('add_student') }}">Add Student</a>
    <ul>
        {% for student in students %}
            <li>{{ student.name }} - Grade: {{ student.grade }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

add_student_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Student</title>
</head>
<body>
    <h1>Add Student</h1>
    <form action="{{ url_for('add_student') }}" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="grade">Grade:</label>
        <input type="text" id="grade" name="grade" required>
        <button type="submit">Add Student</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Student List</a>
</body>
</html>
"""

styles_css_content = """body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

a {
    display: inline-block;
    margin-bottom: 20px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    background: #fff;
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ccc;
}
"""

# Create the files
with open(os.path.join(base_dir, 'app.py'), 'w') as f:
    f.write(app_content)

with open(os.path.join(templates_dir, 'index.html'), 'w') as f:
    f.write(index_html_content)

with open(os.path.join(templates_dir, 'add_student.html'), 'w') as f:
    f.write(add_student_html_content)

with open(os.path.join(static_dir, 'styles.css'), 'w') as f:
    f.write(styles_css_content)

# If you want to create a zip of the project
import shutil
shutil.make_archive(base_dir, 'zip', base_dir)
