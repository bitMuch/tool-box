#!/usr/bin/python3
# Created by c@caine
# On: 14/02/2017
# --- Preamble --- #
from bs4 import BeautifulSoup			# funtions for parsing html
from urllib.request import urlopen		# functions for d/l web page

# --- Declarations --- #
target = 'http://www.footballsquads.co.uk/eng/2016-2017/faprem.htm'
root_addy = target[:46]				# strip url for use later 
# ---- lists
teams = []
transfer  = []
roster = []
players = []
# --- Functions --- #

def chef(ingredient): 				# fetch page
  soup = BeautifulSoup(urlopen(ingredient), 'html.parser')
  return soup

def scoop(players):				# grabs surname + num
  for sibling in players.find_all(width="180"): 
    try:
      # works, but my gosh what a mess, (better way?)
      roster.append(repr(sibling.string.split(' ')[-1]).strip("'") + \
      str(repr(sibling.string.previous_element.previous_element.previous_element.previous_element.string.strip('\r\n')).strip("'")))
    except:
      pass
    
def main ():
  soup = chef(target)

  for link in soup.find_all('a')[10:]:
    teams.append(root_addy + link.get('href'))
  for team in teams:
    transfer.append(chef(team))
    print (team)    
  for players in transfer:
    scoop(players)

  with open('players.txt','w') as goal:
    for player in roster:
      if "NameNumber" not in player:
        print(player)      
        goal.writelines(player + '\n')
# --- Main --- #
if __name__ == "__main__":
  main()
