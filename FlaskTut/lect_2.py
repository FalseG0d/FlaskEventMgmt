from flask import Flask,render_template

app=Flask(__name__)

@app.route("/<name>")
def name(name):
    return render_template("name.html",content=name,r=2)

if __name__=="__main__":
    app.run()