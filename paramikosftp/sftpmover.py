#!/usr/bin/env python3

import paramiko

t = paramiko.Transport("10.10.2.3", 22) ## IP and port
t.connect(username=input("username"), password=input("password"))
#t.connect(username="bender", password="alta3")
sftp = paramiko.SFTPClient.from_transport(t)

for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

sftp.close()


