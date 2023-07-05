# MP3 Trimming App
A web app for trimming MP3 files.

## Project Goal
This was a learning project for me to get familiar with Flask and FFmpeg.

Right now, it only runs locally. I intend to publish this app using Docker and AWS Elastic Beanstalk.

This was a fun project to create and I learned a lot. I hope you find it useful.

## Tech Stack
- Python
- Flask
- FFmpeg
- TailwindCSS

## About Me
I'm a full-stack software developer with a passion for designing clean, beautiful interfaces and writing efficient, maintainable code.

You can view my portfolio at [https://www.jamestrent.net](https://www.jamestrent.net).

---

## Installation
1. Install [Python 3.7](https://www.python.org/downloads/release/python-370/) or higher.
2. Install [FFmpeg](https://www.ffmpeg.org/download.html).
3. Install [Git](https://git-scm.com/downloads).
4. Clone this repository.
5. Create a .env file in the root directory of the repository with the following contents:
```
UPLOAD_PATH=<path to directory where uploaded files will be stored>
```
6. Install the required Python packages:
```
pip install -r requirements.txt
```
7. Run the app:
```
python app.py
```
8. Open http://localhost:5000 in your browser.

---

## Usage
1. Upload an MP3 file.
2. Enter the start and end times of the section you want to keep.
3. Click the "Trim" button.
4. Click the "Download" button to download the trimmed file.
