from flask import render_template
from app import app
from models.order import *
from models.book_order import *



@app.route("/")
def index():
    return render_template("index.html", order=orders)


@app.route('/order/<index>')
def view_order(index):
    return render_template("order.html", order=orders[int(index)-1])


