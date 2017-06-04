#coding=utf8
import itchat, time, tuling
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    msg.user.send(getTulingRes(msg))
    #return itchat.send(getTulingRes(msg))

def getTulingRes(msg):
    msgContent = msg['Text']
    return tuling.getTulingResponse(msgContent)

itchat.auto_login()
itchat.run()

