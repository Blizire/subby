#!/usr/bin/env python
import os
from flask import Flask, render_template, url_for, request, jsonify
app = Flask(__name__)

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":
        if request.form["command"]:
            command = request.form["command"]
            if command == "sleep":
                sleep()
        return render_template("home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
