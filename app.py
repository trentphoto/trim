from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
import subprocess

# load environment variables from .env file
load_dotenv()

# load upload path from .env file
UPLOAD_PATH = os.getenv('UPLOAD_PATH')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():

    # first delete any existing files in the uploads folder
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))

    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part', 400
    
    # check if the file is empty
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    # check if the file is valid
    if file:

        # save the file
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully', 200

@app.route('/trim', methods=['POST'])
def trim_file():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    filename = request.form['filename']

    input_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'trimmed_' + filename)

    command = f"ffmpeg -i {input_file} -ss {start_time} -to {end_time} -c copy {output_file}"

    subprocess.call(command, shell=True)

    return 'File trimmed successfully', 200

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    
    # print the file download path
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # print(file_path)

    # Check if the file exists and can be read
    try:
        with open(file_path, 'rb') as f:
            print("File can be opened: ", f.readable())
    except Exception as e:
        print("Error opening file: ", e)

    
    return send_from_directory(UPLOAD_PATH, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
