#!/usr/bin/env python
# -*- coding: utf-8 -*-
'AIOT request'

__author__ = 'Louis'

import sys, requests, json

SITE_AIOT = 'https://aiot-rpc.aqara.cn'
APPID = 'c243b87d1cc98d82ccdb7519'
APPKEY = 'uP7N4EZFtoe0ptZgWk3O1JHD8xFEQJag'

def requestAIOT(path):
    url = SITE_AIOT + path
    data = {'field': 'ICON_EIGENSTONE_IOS'}
    headers = {'Appid': APPID, 'Appkey': APPKEY}
    r = requests.post(url, data=data, headers=headers, verify=False)
    print(r.text)

    results = r.json()['result']
    for result in results:
        print(result['downloadURL'])


if __name__ == '__main__':
    requestAIOT('/lumi/service/icon/package/query/list')
