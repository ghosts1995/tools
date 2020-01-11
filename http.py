# !/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, Response
import json
import demjson


def ok(msg, idata={}):
    data = {}
    data["code"] = 200
    data["msg"] = msg
    data["data"] = idata
    jsonData = json.dumps(data)
    return Response(jsonData, mimetype='application/json')


def error(msg, code=204):
    data = {}
    data["code"] = code
    data["msg"] = msg
    data["data"] = {}
    jsonData = json.dumps(data)
    return Response(jsonData, mimetype='application/json')


def req():
    data = demjson.decode(request.data.decode(encoding='utf-8'))
    return data
