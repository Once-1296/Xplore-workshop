# fastapi_app.py
from html import escape

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# In-memory "database"
notes_db = []

# Reusing the same HTML/CSS from above for consistency
FAST_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background: #eef2f3; padding: 50px; }
        .container { background: white; padding: 20px; border-radius: 8px; border-left: 5px solid #007bff; }
        button { background: #007bff; color: white; border: none; padding: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>FastAPI Notes App</h2>
        <form action="/add" method="post">
            <input type="text" name="note" required>
            <button type="submit">Post Note</button>
        </form>
        <ul>
            __NOTES_ITEMS__
        </ul>
    </div>
</body>
</html>
"""


def render_notes_page() -> HTMLResponse:
    # Escape user input so note text is rendered safely as content.
    items = "".join(f"<li>{escape(n)}</li>" for n in notes_db)
    return HTMLResponse(content=FAST_HTML.replace("__NOTES_ITEMS__", items))


@app.get("/", response_class=HTMLResponse)
async def read_notes():
    return render_notes_page()

@app.post("/add")
async def create_note(note: str = Form(...)):
    notes_db.append(note)
    return render_notes_page()


# run in same directory as file
# Run with: uvicorn notes_app_fastapi:app --reload
