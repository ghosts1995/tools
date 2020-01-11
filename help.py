# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import uuid
import hashlib
from tools.pageing import Pageing
import subprocess
import json
import base64


def byJsonToBase64Encode(idict):
    jsonStr = json.dumps(idict)
    return base64.b64encode(jsonStr.encode('utf-8'))


def byBase64DecodeToJsonInDict(brStr):
    #
    jsonStrs = base64.b64decode(brStr)
    print(jsonStrs)
    # jsonStrs = bytes.decode(jsonStrs)
    print(jsonStrs)
    # jsonStrs = base64.b64decode(brStr.encode('utf-8'))
    idc = json.loads(jsonStrs)
    print(idc)


def popen(cmd):
    child = subprocess.Popen(cmd, close_fds=True, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    child.wait()
    return child.stdout.read()


def md5(str):
    hash_md5 = hashlib.md5(str.encode("utf-8"))
    return hash_md5.hexdigest()


def getTime():
    return int(time.time())


def toTime(otherStyleTime):
    timeArray = time.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def toDate(timeStamp):
    if type(timeStamp) != int:
        return False
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def getGuid():
    return uuid.uuid1()


def setPageing(obj):
    page = Pageing(page=obj.page, pages=obj.pages, total=obj.total, next_num=obj.next_num, per_page=obj.per_page,
                   items=obj.items)
    return page.results()


def dictToListJoinDict(items):
    listTmp = []
    if len(items) != 0:
        for value in items:
            dictData = value.__dict__
            lenDictData = len(dictData)
            if lenDictData >= 1:
                # print(dictData)
                tmp = {}
                for keys, val in dictData.items():
                    if keys != "_sa_instance_state":
                        if keys == "create_time" or keys == "update_time":
                            val = toDate(val)
                        tmp[keys] = val
                listTmp.append(tmp)
    if len(listTmp) != 0:
        return listTmp
    else:
        return None


def checkArrayVal(isCheck, checkData):
    if isCheck in checkData:
        return True
    return False
