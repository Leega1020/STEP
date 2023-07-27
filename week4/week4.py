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
    elif id == ""or password == "":
        message = "帳號或密碼輸入不完整"
        return redirect(url_for("error",message=message))
    else:
        message = "帳號或密碼錯誤"
        return redirect(url_for("error",message=message))
       
@app.route("/member")
def mem():
    if session["pass"]==False:
        return redirect("/")
    else:
        return render_template("member.html")

@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("fail.html", error=message)
   
@app.route("/signout")
def singout():
    session["pass"]=False
    return redirect("/")

@app.route("/square/<int:number>")
def square(number):
    result = number * number
    return render_template("square.html", result=result)


app.run(port=3000)