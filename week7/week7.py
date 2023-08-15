from flask import Flask,render_template,session,request,redirect,url_for,jsonify
import mysql.connector.pooling
app=Flask(__name__,
        static_folder="static"
        )
app.secret_key="akksso"
dbconfig = {
    "database":"website",
    "user":"root",
    "host":"localhost",
    "password":"123",
}
connection_pool=mysql.connector.pooling.MySQLConnectionPool(**dbconfig)

con=connection_pool.get_connection()

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    name=request.form.get("name")
    username=request.form.get("username")
    password=request.form.get("password")
    cur=con.cursor()
    cur.execute("SELECT * FROM member WHERE username=%s",(username,))
    result=cur.fetchone()
    
   
    if result:
        message="帳號已被註冊"
        return redirect(url_for("error",message=message))

    else:  
        cur.execute("INSERT INTO member(name,username,password) VALUES(%s,%s,%s)",(name,username,password))
        con.commit()
        return redirect("/")
    
 
@app.route("/signin",methods=["GET","POST"])
def signin():
    username=request.form.get("username2")
    password=request.form.get("password2")
    cur=con.cursor()
    cur.execute("SELECT * FROM member WHERE username=%s AND password=%s", (username, password))
    result=cur.fetchone()
    
    if result:
        session["pass"]=True
        session["name"]=result[1]
        session["username"]=result[2]
        session["member_id"]=result[0] 
        return redirect("/member")
    
    else:
        message="帳號或密碼錯誤"
        return redirect(url_for("error",message=message))
  
  
@app.route("/member")
def mem():
    if "pass" in session :
        name=session["name"]
        cur=con.cursor()
        cur.execute("SELECT member.name, message.content, message.id, message.member_id FROM member INNER JOIN message ON member.id = message.member_id order by message.time DESC")
        messages=cur.fetchall()
        return render_template("member.html", name=name, messages=messages)
    
    else:
        return redirect('/')

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("fail.html", error=message)
   
@app.route("/signout")
def singout():
    session.clear()
    return redirect("/")


@app.route("/creatMessage", methods=["POST"])
def create_message():
    content=request.form.get("content")
    member_id=session["member_id"]
    
    if "pass" in session:
        cur=con.cursor()
        cur.execute("INSERT INTO message (content, member_id) VALUES (%s, %s)", (content, member_id))
        con.commit()
        
    return redirect("/member")

@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    message_id=request.form.get("message_id")
    member_id=session["member_id"]

    if "pass" in session :
        cur=con.cursor()
        cur.execute("DELETE FROM message WHERE id = %s AND member_id = %s", (message_id, member_id))
        con.commit()

    return redirect("/member")
@app.route("/api/member")
def member_api():
    username=request.args.get("username")
    cur=con.cursor()
    cur.execute("SELECT id,name,username FROM member WHERE username=%s",(username,))
    result=cur.fetchone()
    if "pass" in session and result is not None:
        data={
            "id": result[0],
            "name": result[1],
            "username": result[2]
        }
        return jsonify({"data": data})
    else:
        return jsonify({"data": None})
    
@app.route("/api/member",methods=["PATCH"])
def update_name():
    try:
        new_name=request.json.get("name")
        id=session["member_id"]
        if "pass" in session:
            cur=con.cursor()
            cur.execute("UPDATE member SET name=%s WHERE id=%s",(new_name,id))
            con.commit() 
            session["name"]=new_name
            return jsonify({"ok":True})
        else:
            return jsonify({"error":True})
    except Exception as e:
        return jsonify({"error":True})
    
app.run(port=3000)
