#!/usr/bin/python3
# Created by c@caine
# On: 14/02/2017
# --- Preamble --- #
from bs4 import BeautifulSoup
from urllib.request import urlopen

# --- Declarations --- #
target = 'http://www.footballsquads.co.uk/eng/2016-2017/faprem.htm'
root_addy = target[:46] #modularise this
teams = []
transfer  = []
roster = []
players = []

# --- Functions --- #
def chef(ingredient):
  soup = BeautifulSoup(urlopen(ingredient), 'html.parser')
  return soup

def scoop(players):
  # get name and number
  for sibling in players.find_all(width="180"): 			# grabs surname + num
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

  for player in roster:
    if "NameNumber" not in player:
      print(player)
      with open('players.txt', mode='wt', encoding='utf-8') as goal:  
        goal.write('\n'.join(player))

# --- Main --- #
if __name__ == "__main__":
  main()
