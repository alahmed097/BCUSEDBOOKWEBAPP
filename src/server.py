import time
import cmd
import sqlite3
import src
import os
from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)



@app.route("/")
def departments():
    return render_template("main.html")


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




    def database(name, data):
        conn = sqlite3.connect("BOOKS.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS my_table (name TEXT,data BLOP) """)
        cursor.execute("""INSERT INTO my_table (name, data) VALUES (?,?) """, (name, data))

        conn.commit()
        cursor.close()
        conn.close()

        def query():
            conn = sqlite3.connect("BOOKS.db")
            cursor = conn.cursor()
            print("IN DATABASE FUNCTION ")
            c = cursor.execute(""" SELECT * FROM  my_table """)

            for x in c.fetchall():
                name_v = x[0]
                data_v = x[1]
                break

            conn.commit()
            cursor.close()
            conn.close()



if __name__ =="__main__":
    app.run()
