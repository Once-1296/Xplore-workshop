# flask_app.py
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory "database"
notes = []

# Simple HTML template with CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background: #f4f4f4; padding: 50px; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        input[type="text"] { padding: 10px; width: 70%; border: 1px solid #ddd; }
        button { padding: 10px 20px; background: #28a745; color: white; border: none; cursor: pointer; }
        ul { list-style: none; padding: 0; }
        li { background: #eee; margin: 5px 0; padding: 10px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Flask Notes App</h2>
        <form method="POST" action="/add">
            <input type="text" name="note_content" placeholder="Enter a note..." required>
            <button type="submit">Add Note</button>
        </form>
        <ul>
            {% for note in notes %}
                <li>{{ note }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note_content')
    if note:
        notes.append(note)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # print("Flask running at http://127.0.0.1:5000")
    app.run(debug=True)