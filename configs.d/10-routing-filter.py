#!/usr/bin/python
import os

### CONFIG HERE ###

allowed = [
    1,      # servers
    5,      # gameservers
    34,     # keuken
    35,     # inkom
    36,     # gamesgear
    37,     # tones
    38,     # crew
    39,     # crew
    40,     # crew
    41,     # crew
    42,     # crew
    43,     # vip
    44,     # vip
    47,     # rent-a-lan
    51,     # zaal rechts
    52,     # zaal rechts
    53,     # zaal rechts
    54,     # zaal rechts
    55,     # zaal rechts
    56,     # zaal rechts
    57,     # zaal rechts
    58,     # zaal rechts
    59,     # zaal links
    60,     # zaal links
    61,     # zaal links
    62,     # zaal links
    63,     # zaal links
    64,     # zaal links
    65,     # zaal links
    66,     # zaal links
    67,     # zaal links
    254,    # rent-a-lan
    255,    # rent-a-lan
]

### END CONFIG ###

# Cleanup raw table
os.system("iptables -t raw -F") 
os.system("iptables -t raw -X")
os.system("iptables -t raw -P PREROUTING ACCEPT")

# Set up drop-chain
DROPCHAIN = "drop-by-source-ip"
os.system("iptables -t raw -N %s" % DROPCHAIN)
os.system("iptables -t raw -A %s -m limit --limit 60/minute --limit-burst 10 -j LOG --log-level 4 --log-prefix 'iptables: [DROP IP SRC] '" % DROPCHAIN)
os.system("iptables -t raw -A %s -j DROP" % DROPCHAIN)


for subnet in range(1,256):
  if subnet not in allowed:
    os.system("iptables -t raw -A PREROUTING --source 172.16.%d.0/24 -j %s" % (subnet,DROPCHAIN))
