from __main__ import app
from flask_mysqldb import MySQL

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234' #Insira aqui a senha do seu servidor local do MYSQL
app.config['MYSQL_DB'] = 'usuario'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

def insereUsers(form):
    cur = mysql.connection.cursor()
    cur.execute(f"INSERT INTO usuario(email_users, assunto_users, descricao_users) VALUES(%s, %s, %s)", (form['email'], form['assunto'], form['descricao']))
    mysql.connection.commit()
    cur.close()
    return None

def selecionaUsers():
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM usuario")
    tabela = cur.fetchall()
    cur.close()
    return tabela