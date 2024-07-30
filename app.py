from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
db = SQL("sqlite:///rectifier.db")

@app.route("/")
def index():
        return render_template("home.html",active_page="home")


@app.route("/news")
def buy():
    
    return render_template("news.html",active_page="news")


@app.route("/contact_us")
def history():
    
    return render_template("contact_us.html", active_page="contact_us")

@app.route('/update_table', methods=['POST'])
def update_table():
    avg = request.form.get('avgI')
    Vr = request.form.get('VRR')
    peak = request.form.get('PeakI')

    TABLE = db.execute("SELECT * FROM diode WHERE Average_Rectified_Current_Max>=? AND Reverse_Voltage_Max>=? AND Peak_Current_Max>=?",avg,Vr,peak)

    return render_template('table.html', data_list=TABLE)
