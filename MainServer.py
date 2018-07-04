# encoding: utf-8
"""
@contact: liuguiyang15@mails.ucas.edu.cn
@file: MainServer.py
@time: 2018/7/1 15:05
"""

from socket import *
from time import ctime

from video_process import utils

# ﻿/*
#  *客户端和服务器之间通信指令：
#  * 1. CMD::VIDEONAME:name
#  * 2. CMD::MODELNAME:name
#  * 3. POS::x1,y1,x2,y2,label;x1,y1,x2,y2,label
#  * 4. CMD::FINISHED
# */


def parse_client_communication(content):
    content = content.decode("utf8")
    if not content:
        return (False, "ERROR::content is void")
    print(ctime(), content)
    if "CMD" == content[:3]:
        prefix = content[5:].split(":")[0]
        if "VIDEONAME" == prefix:
            video_name = content[5:].split(":")[1]
            return (True, "CMD::VIDEONAME")
        elif "MODELNAME" == prefix:
            model_name = content[5:].split(":")[1]
            return (True, "CMD::MODELNAME")
        else:
            return (False, "ERROR::No Such Command")
    return (False, "ERROR::Client format Error")




def run_server():
    HOST = ""
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpServer = socket(AF_INET, SOCK_STREAM)
    tcpServer.bind(ADDR)
    tcpServer.listen(5)

    while True:
        print("waiting for connection ...")
        tcpClient, addr = tcpServer.accept()
        print("... connected from: ", addr)

        while True:
            content = '[{}]::connet to server'.format(ctime())
            tcpClient.send(bytes(content, encoding='utf8'))
            data = tcpClient.recv(BUFSIZE)
            status = parse_client_communication(data)
            print(status)
        tcpClient.close()


run_server()
