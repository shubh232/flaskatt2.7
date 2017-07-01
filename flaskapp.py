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

@app.route('/about')
def calc_input():
    p = request.form['present']
    t = request.form['total']
    pw = request.form['week']
    return redirect(url_for('calc_atten',p=p,t=t,pw=pw))

@app.route('/about/<p>/<t>/<pw>')
def calc_atten(p,t,pw):
    cal = CalcAtten(str(p),str(t),str(pw))
    require = cal.req_lec()
    return render_template('atten_calculator.html', required_lecture = require)

if __name__ == '__main__':
    app.run()