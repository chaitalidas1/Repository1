from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML for upload screen
UPLOAD_FORM = """
<!doctype html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>
    <h2>Select a file to upload</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(UPLOAD_FORM)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    # You can save the file or process it here
    # Example: file.save(f"./uploads/{file.filename}")
    
    return f"File '{file.filename}' uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)