#!/usr/bin/env python

import socket
import base64


TCP_IP = '127.0.0.1'

TCP_PORT = 5013
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
file = "123331.png" #������ͧ�����
bytes1 = open(file,'rb').read() #��ҹ���亵�
bytes1 = base64.b64encode(bytes1) #������� base64
s.send(bytes1)
s.close()

print "send image success"
