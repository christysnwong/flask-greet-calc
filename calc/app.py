# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

oper = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def math_op(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(oper[operation](a, b))



@app.route('/add')
def adding():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def subtracting():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def multiplying():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def dividing():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

