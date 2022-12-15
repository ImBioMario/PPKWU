#!/usr/bin/env python3
from flask import Flask, request, jsonify, Response
import xmltodict
import dicttoxml
from xml.dom.minidom import parseString

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
    data_xml = request.get_data()
    data = xmltodict.parse(data_xml)
    if 'root' in data:
        data_to_parse = data['root']
        if 'str' in data_to_parse:
            response_str = dict(zip(parameter_names_str, str_statistics(data_to_parse['str'])))

        if 'num1' in data_to_parse and 'num2' in data_to_parse:
            response_nums = dict(zip(parameter_names_nums, get_operation_stats(int(data_to_parse['num1']), int(data_to_parse['num2']))))
    if 'str' in data:
        response_str = dict(zip(parameter_names_str, str_statistics(data['str'])))

    return_xml = dicttoxml.dicttoxml({**response_str, **response_nums}, attr_type = False)
    # return {**response_str, **response_nums}
    return Response(parseString(return_xml).toprettyxml(), mimetype='application/xml')

app.run(port=4080, host='0.0.0.0')
