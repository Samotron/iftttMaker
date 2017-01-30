# -*- coding: utf-8 -*-

import requests

def iftttMaker(event, key, value1="", value2="", value3=""):
    payload = r"{ 'value1 = '" + value1 + "', value2 = '" + value2 + "', value3 = '"+ value3 +"'}"
    requests.post(r"https://maker.ifttt.com/trigger/" + event +"/with/key/" + key, data=payload)

