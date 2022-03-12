import sqlite3
from flask import Flask,request,render_template,flash

app=Flask(__name__)
status=0

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login' ,methods=['POST','GET'])
def login():
    if request.method=='POST':
        conn=sqlite3.connect('login.db')
        c=conn.cursor()
        name=request.form.get('c_name')
        email=request.form.get('eid')
        password=request.form.get('pswd')
        q='select count(*) from login where email="{}"'.format(email)
        if c.execute(q).fetchall()[0][0]==1:
            return render_template('signup.html',result='already email id is registered')
        q="insert into login values('{}','{}','{}')".format(name,email,password)
        print(q)
        c.execute(q)
        conn.commit()
        conn.close()
    return render_template('login.html')
@app.route('/validate',methods=['POST','GET'] )
def validate():
    if request.method=='POST':
        email=request.form.get('eid')
        password=request.form.get('pswd')
        conn=sqlite3.connect('login.db')
        c=conn.cursor()
        q='select count(*) from login where email="{}"'.format(email)
        if c.execute(q).fetchall()[0][0]==0:
            return render_template('login.html',result='invalid user name')
        q="select password from login where email='{}'".format(email)
        c.execute(q)
        print(q)
        given=c.fetchall()
        if password==given[0][0]:
            global status
            status=1
            return render_template('login_home.html')
        else:
            return render_template('login.html',result='invalid user name or password')
@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')
@app.route('/cart')
def cart():
    global status
    if status==0:
        return render_template('login.html')
    return "status="+str(status)
@app.route('/logout')
def logout():
    global status
    status=0
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)
    