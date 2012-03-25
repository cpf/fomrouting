import commands
import re

def chain_exists(table, chain):
  status, output = commands.getstatusoutput("iptables -n -t %s -L %s" % (table, chain))
  return (status == 0)

def chain_jump_index(table, chainsource, chaintarget):
  status, output = commands.getstatusoutput("iptables -t %s -L %s -n --line-number" % (table, chainsource))
  matchingLines = re.findall('^(\d+).*%s' % chaintarget, output, flags=re.MULTILINE)
  if (len(matchingLines) == 0):
    return -1
  return int(matchingLines[0])
