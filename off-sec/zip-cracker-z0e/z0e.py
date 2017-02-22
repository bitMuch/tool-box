#!/usr/bin/python
# Created by c@caine
# On: 13/02/2017
# --- Preamble --- #

import sys
import zipfile
# --- Declarations --- #

zip_file = sys.argv[1]
unzip_me = zipfile.ZipFile(zip_file)
word_list = sys.argv[2]
# --- Functions --- #

def extract_file (unzip_me, password):
  try:
    unzip_me.extractall(pwd = password)
    return password
  except:
    return

def main ():
  with open (word_list) as pass_file:
    for line in pass_file.readlines():
    
      password = line.strip('\n')
      guess = extract_file(unzip_me, password)

      if guess:
        print('[+] Password = ' + password + '\n')
        exit(0)
# --- Main --- #

if __name__ == "__main__":
  main()

