#!/usr/bin/env python3
from flask import Flask, request, jsonify

parameter_names = ["sum", "sub", "mul", "div", "mod"]

app = Flask(__name__)

def get_operation_stats(num1 :int, num2: int):
    return [num1+num2, num1-num2, num1*num2, num1//num2, num1%num2]


@app.post('/')
def generate_stats():
    data = request.json
    print(data)


    return data

app.run(port=4080, host='0.0.0.0')
