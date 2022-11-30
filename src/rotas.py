from __main__ import app
from flask import Flask, render_template, request
import bd

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        form = request.form
        bd.insereUsers(form)
        return render_template('contato.html')
    else:
        return render_template('contato.html')

@app.route('/quem')
def quem():
    return render_template('quem.html')

@app.route('/users')
def users():
    users = bd.selecionaUsers()
    return render_template('users.html', usuarios = users)