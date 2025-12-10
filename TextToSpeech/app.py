#https://github.com/Metehan-bas

from flask import Flask, request, send_file
import mysql.connector
import pyttsx3
import pythoncom


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ttsdb"
)
from flask import render_template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    text = request.json["text"]
    cur = db.cursor()
    cur.execute("INSERT INTO texts (content) VALUES (%s)", (text,))
    db.commit()
    return "ok"

@app.route("/speak", methods=["GET"])
def speak():
    pythoncom.CoInitialize()
    cur = db.cursor()
    cur.execute("SELECT content FROM texts ORDER BY id DESC LIMIT 1")
    text = cur.fetchone()[0]

    engine = pyttsx3.init()
    file = "ses.mp3"
    engine.save_to_file(text, file)
    engine.runAndWait()

    return send_file(file, as_attachment=True)

app.run(debug=True)
