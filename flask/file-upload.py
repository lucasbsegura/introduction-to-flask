from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/uploads/file.txt')

@app.route('upload2', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/uploads/' + secure_filename(f.filename))       

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)