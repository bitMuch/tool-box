#!/usr/bin/python3
# Created by c@caine
# On: 16/02/2017
# kn0wn: A defensive scanner
# --- Preamble --- #
# Task: To monitor an internal network for devices not in white list
import nmap 		# easy port scan, great for prototyping 
			# but very slow and or bloated, for this task
# --- Definitions --- #
internal_network = '192.168.1.*'		# define inet ip
whitelist = []					# define list of known ip's
nm = nmap.PortScanner()				# define global nmap object
# --- Functions --- #
def scan_init ():
  nm.scan(internal_network, arguments='-F')	# just a fast scan

def load_known ():				# load known hosts
  global whitelist				# into 'whitelist[]'
  with open('whitelist.txt', 'r') as wl:	
    whitelist = [line.strip(' \n') for line in wl]	

def print_sum ():				# print a summery
  print('=================================================================')
  print('--- Summary Of Scan ---------------------------------------------')

  for host in nm.all_hosts():
    print('-----------------------------------------------------------------')
    if host in whitelist:
      print ('[G]\tKNOWN\t%s\t>>>\t%s' % (host, nm[host].hostname()))
    else:
      print ('[R]\tUNKNOWN\t%s\t>>>\t%s' % (host, nm[host].hostname()))
  print('-----------------------------------------------------------------')  
  print('=================================================================')
  print('\n')

def main ():
  scan_init()
  load_known()
  print_sum()

# --- Main --- #
if __name__ == "__main__":
  main()
