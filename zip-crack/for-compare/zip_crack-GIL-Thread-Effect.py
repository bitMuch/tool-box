#!/usr/bin/python
# Created by c@caine
# On: 13/02/2017
# --- Preamble --- #
import sys
import zipfile
from threading import Thread

# --- Declarations --- #
zip_file = sys.argv[1]
unzip_me = zipfile.ZipFile(zip_file)
word_list = sys.argv[2]

# --- Functions --- #
def extract_file (unzip_me, password):
  try:
    unzip_me.extractall(pwd = password)
    print('[+] Password = ' + password + '\n')

  except:
    pass

def main ():
  with open (word_list) as pass_file:
    for line in pass_file.readlines():
      password = line.strip('\n')
      t = Thread (target=extract_file, args=(unzip_me, password))
      t.start()
      
# --- Main --- #
if __name__ == "__main__":
  main()

