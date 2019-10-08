from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def departments():
    return render_template("departments.html")



if __name__ =="__main__":
    app.run()
