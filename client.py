#!/usr/bin/env python

import socket
import base64


TCP_IP = '127.0.0.1'

TCP_PORT = 5013
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
file = "123331.png" #ไฟล์ที่ต้องการส่ง
bytes1 = open(file,'rb').read() #อ่านไฟล์ไบต์
bytes1 = base64.b64encode(bytes1) #เข้ารหัส base64
s.send(bytes1)
s.close()

print "send image success"
