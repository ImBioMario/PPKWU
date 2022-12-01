#!/usr/bin/env python3
from flask import Flask, request, jsonify

parameter_names_nums = ["sum", "sub", "mul", "div", "mod"]
parameter_names_str = ["lowercase", "uppercase", "digits", "special"]

app = Flask(__name__)

def get_operation_stats(num1 :int, num2: int):
    return [num1+num2, num1-num2, num1*num2, num1//num2, num1%num2]


def str_statistics(strng :str):
    lowercases = len([x for x in strng if x.islower()])
    uppers = len([x for x in strng if x.isupper()])
    digits = len([x for x in strng if x.isnumeric()])
    specials = len(strng) - lowercases - uppers - digits
    return [lowercases, uppers, digits, specials]


@app.post('/')
def generate_stats():
    response_str = {}
    response_nums = {}
    data = request.json
    if 'str' in data:
        response_str = dict(zip(parameter_names_str, str_statistics(data['str'])))

    if 'num1' in data and 'num2' in data:
        response_nums = dict(zip(parameter_names_nums, get_operation_stats(data['num1'], data['num2'])))

    return {**response_str, **response_nums}

app.run(port=4080, host='0.0.0.0')
