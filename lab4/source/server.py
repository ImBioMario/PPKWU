#!/usr/bin/env python3
from flask import Flask, request, jsonify

parameter_names = ["sum", "sub", "mul", "div", "mod"]

app = Flask(__name__)

def get_operation_stats(num1 :int, num2: int):
    return [num1+num2, num1-num2, num1*num2, num1//num2, num1%num2]


@app.get('/')
def generate_stats():
    num1 = request.args.get('num1',type = int)
    num2 = request.args.get('num2', type = int)
    my_json = jsonify(dict(zip(parameter_names, get_operation_stats(num1, num2))))
    return my_json

app.run(port=4080, host='0.0.0.0')
