import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from parsesite import ParseSite
from mat import pieplot
app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/')
def hello_world():
    return render_template('input_data.html')
@app.route('/',methods=['POST'])
def form_data():
    text = request.form['text']
    password = request.form['password']
    return redirect(url_for('shubh',text = text , password =password))


@app.route('/details/<text>/<password>')
def shubh(text,password):
    s = ParseSite(str(text),str(password))
    head = s.extract_headings()
    lis = pieplot(head,str(text))
    return render_template('graph.html',names = lis)    

if __name__ == '__main__':
    app.run()
