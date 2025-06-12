#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:username>')
def print_string(username):
    print(f'{username}')
    return f'{username}'

@app.route('/count/<int:number>')
def count(number):
    result = ""
    for i in range(1, number+1):
        result += str(i) + '<br>'
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>') 
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
