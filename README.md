# iftttMaker
Easy IFTTT Maker Channel requests

Docs:

'''python

import requests

def iftttMaker(event, key, value1="", value2="", value3=""):
    """
    Input your event and key as specified on the IFTTT Maker Channel.
    
    If your applet allows, three custom values can be included.
    
    More info here:
    """
    payload = r"{ 'value1 = '" + value1 + "', value2 = '" + value2 + "', value3 = '"+ value3 +"'}"
    requests.post(r"https://maker.ifttt.com/trigger/" + event +"/with/key/" + key, data=payload)

'''
