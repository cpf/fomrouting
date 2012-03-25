#!/usr/bin/python

LOGCHAIN = "log-drop"
RATE="30/minute"

import os

os.system("iptables -t filter -X %s" % LOGCHAIN)
os.system("iptables -t filter -N %s" % LOGCHAIN)
os.system("iptables -t filter -A FORWARD -j %s" % LOGCHAIN)

for subnet in range(1,256):
  os.system("iptables -t filter -A %s --source 172.16.%d.0/24 -m limit --limit %s -j LOG --log-level 7 --log-prefix 'iptables: [172.16.%s.0/24] '" % (LOGCHAIN,subnet,RATE,subnet))
