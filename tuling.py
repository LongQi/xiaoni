#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Tuling Module'

__author__ = 'Louis'

import sys, requests, json

URL_TULING_API = "http://openapi.tuling123.com/openapi/api/v2"
APIKEY_XIAONI = "35d1dda65e0c4610a5eee8dfd063e45a"

def getTulingResponse(content):
    response = requests.post(URL_TULING_API, buildTulingResponseData(content))
    print(response.json())

    responseText = getResponseResultText(response)
    print(responseText)
    return responseText

def getResponseResultText(response):
    results = response.json()['results']
    for result in results:
        if result['resultType']=='text':
            resultValues = result['values']
            return  resultValues['text']

def buildTulingResponseData(content):
    inputText = json.dumps({'text': content})
    perception = json.dumps({'inputText': inputText})
    userInfo = json.dumps({'apiKey': APIKEY_XIAONI, 'userId': '123'})
    data = json.dumps({'perception': perception, 'userInfo': userInfo})
    return data

if __name__=='__main__':
    getTulingResponse('hello')