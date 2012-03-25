#!/usr/bin/python

LOGDIR="/var/log/iptables"

print ':msg,contains,"iptables: [DROP IP SRC]" %s/drop-by-source-ip.log' % LOGDIR
print ':msg,contains,"iptables: [DROP]" %s/drop-by-dest-port.log' % LOGDIR

for subnet in range(1,256):
  print ':msg,contains,"iptables: [172.16.%d.0/24]" %s/%d-16-172-drop.log' % (subnet, LOGDIR, subnet)

print ':msg,contains,"iptables: " %s/all.log' % LOGDIR
print '& ~'
