from flask import Flask, render_template
import time
import cmd

app = Flask(__name__)

@app.route("/")
def departments():
    return render_template("departments.html")


@app.route('/<cmd>')
def execute(cmd=None):
    page = ''

    if cmd == 'ANTH':
        page = 'ANTH.html'
    if cmd == 'BIO':
      page = 'BIO.html'
    if cmd == 'CISC':
      page = 'CISC.html'
    if cmd == 'ENG':
      page = 'ENG.html'
    if cmd == 'MATH':
      page = 'MATH.html'

    if page != '':
      return render_template(page)


if __name__ =="__main__":
    app.run()
