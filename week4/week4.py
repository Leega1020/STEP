from flask import Flask,render_template,session,request,redirect,url_for

app=Flask(__name__,
        static_folder="static"
        )

app.secret_key="akksso"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signin",methods=["GET","POST"])
def signin():
    id = request.form.get("id")
    password = request.form.get("password")
    if id == "test" and password == "test":
        session["pass"]=True
        return redirect("/member")
        
    else:
        error_message = "帳號或密碼錯誤"
        return redirect("/error?message=" + error_message)
       
@app.route("/member")
def mem():
    if session["pass"]==False:
        return redirect("/")
    else:
        return render_template("member.html")

@app.route("/error") 
def er():
    return render_template("fail.html")
   
@app.route("/signout")
def singout():
    session["pass"]=False
    return redirect("/")

@app.route("/square", methods=["POST"])
def square():
    integer = request.form.get("intenger")
    return redirect(url_for("coculate", integer=integer))
  
@app.route("/square/<int:integer>", methods=["GET"])
def coculate(integer):
    result = integer ** 2
    return render_template("square.html", result=result)

app.run(port=3000)