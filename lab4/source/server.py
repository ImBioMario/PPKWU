#!/usr/bin/env python3
from flask import Flask, request, jsonify

parameter_names = ["sum", "sub", "mul", "div", "mod"]

server = Flask()

def get_operation_


@app.get('/')
def generate_stats():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')


