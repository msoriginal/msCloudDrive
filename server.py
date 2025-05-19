from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "FilesUploaded"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn't exist

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    message = None
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file and uploaded_file.filename != "":
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)
            message = f"File '{uploaded_file.filename}' uploaded successfully!"
        else:
            message = "No file selected or file upload failed."
    return render_template("upload.html", message=message)
    
@app.route('/view-files')
def view_files():
    try:
        folder = app.config['UPLOAD_FOLDER']
        files = os.listdir(folder)
        previews = {}

        for file in files:
            ext = file.split('.')[-1].lower()
            if ext in ['txt', 'log', 'csv']:
                try:
                    with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                        content = f.read(2000)  # Read first 2000 characters
                        previews[file] = content
                except:
                    previews[file] = "[Error reading file]"
        
        return render_template('view_files.html', files=files, previews=previews)
    except Exception as e:
        print(f"Error getting files: {e}")
        return render_template('view_files.html', files=None, error="Error getting files")
        
@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        print(f"Download error: {e}")
        return "Error downloading file", 500
        
@app.route('/view-file/<filename>')
def view_single_file(filename):
    try:
        folder = app.config['UPLOAD_FOLDER']
        file_path = os.path.join(folder, filename)

        ext = filename.split('.')[-1].lower()
        preview = None

        if ext in ['txt', 'log', 'csv']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    preview = f.read(2000)
            except:
                preview = "[Error reading file]"

        return render_template('file_view.html', filename=filename, ext=ext, preview=preview)
    except Exception as e:
        print(f"Error rendering file view: {e}")
        return "Error displaying file", 500


if __name__ == "__main__":
    app.run(debug=True, port=8000)
