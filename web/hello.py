import os
import sqlite3
import requests
from flask import Flask, render_template, request

FOLDER = os.path.join('static', 'screenshots')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

conn = sqlite3.connect("alfa_bee.db", check_same_thread=False)
cursor = conn.cursor()

@app.route('/', methods=["GET", "POST"])
def index(img_src=None, key_word=None, done_site=None, all_site=None):
    cursor.execute("SELECT * FROM t WHERE checked = '0' and in_proccess = '0' LIMIT 1;")
    result = cursor.fetchone()

    if result is None:
        return render_template('success.html')

    kw = result[0]
    screenshot = result[2]

    cursor.execute("UPDATE t SET in_proccess = '1' WHERE screenshot = ?;", (screenshot,))
    conn.commit()

    cursor.execute("SELECT count(*) FROM t WHERE checked = '1' or checked = '2';")
    result = cursor.fetchone()

    done_site = result[0]

    cursor.execute("SELECT count(*) FROM t;")
    result = cursor.fetchone()

    all_site = result[0]

    if request.method == "POST":
        sql = ""
        action = request.form['action']
        file_name = request.form['file_name'][19:-4]
        
        if action.find("ok") != -1:
            sql = "UPDATE t SET in_proccess = '0', checked = '1' WHERE screenshot = ?;"
        elif action.find("drop") != -1:
            sql = "UPDATE t SET in_proccess = '0', checked = '2' WHERE screenshot = ?;"

        if len(sql) > 0:
            cursor.execute(sql, (file_name,))
            conn.commit()
        
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{screenshot}.png')

    return render_template('index.html', img_src=full_filename, key_word=kw, done_site=done_site, all_site=all_site)