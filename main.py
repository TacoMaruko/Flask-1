from flask import Flask, render_template
import xlrd

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"


@app.route("/bs")
def bs():
    book = xlrd.open_workbook("./static/others/student.xls")
    sh = book.sheet_by_index(0)
    print(sh)
    student = {
        "name": sh.cell_value(rowx=0, colx=1),
        "chi": sh.cell_value(rowx=1, colx=1),
        "eng": sh.cell_value(rowx=2, colx=1),
        "math": sh.cell_value(rowx=3, colx=1)
    }
    return render_template("index.html", **student)


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/home")
def home():
    return render_template("home.html", title="5G 新時代")


@app.route("/item1")
def item1():
    return render_template("item1.html", title="Features")


@app.route("/item2")
def item2():
    return render_template("item2.html", title="Pricing")


@app.route("/item3")
def item3():
    return render_template("item3.html", title="Dashboard")
