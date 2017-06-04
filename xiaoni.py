#coding=utf8
import itchat, time, tuling
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    msgContent = msg['Text']
    msg.user.send(tuling.getTulingResponse(msgContent))
    #return itchat.send(getTulingRes(msg))

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('很高兴认识你！')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        msgContent = msg['Text']
        itchat.send(tuling.getTulingResponse(msgContent))

itchat.auto_login()
itchat.run()

