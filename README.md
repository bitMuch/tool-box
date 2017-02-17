# --- tool-box --- #
prototype tools (R&D)
offensive: web_scraper.py, zip_crack.py
defensive: kn0wn.py

Essentially for study, research and devlopment. Unlikely to be of use to anyone at present.

# --- Preamble --- #
web_scraper.py :
A friend of mine shared with me, two of his passwords for popular online services. They were both surnames of well known footballers,  with the players jersey number added to the end it of them. 
He is a regular user, and this made sense as eash password contained a capital letter, a fair number of characters, at least one number and was easy to remember. 

Finishing up the first few excercises in: Violent Python, by T.J. O'Conner, wanting something a little beefier for a passwords.txt file, than the "cp /usr/share/dict/words dictionary.txt" I had initially run to get going with the examples.

Thinking about the habits of human behaviour, I remembered my friend. His generosity inspired me to wip up a quick script that would (with the help of BeautifulSoup4) scrape the target data of each teams roster from: http://www.footballsquads.co.uk/eng/2016-2017/faprem.htm, concatonate as Surname+Number, and then wrting that list to a file.
- -
To do: it's sloppy as hell and hardcoded, so clean up, modularize and send back out to generate more passwords..
--
Bugs: A few names appear with some kind of error in encoding. eg. "Granit\xa0Xhaka29"
- -
What next?: commonBabyName+commonDateOfBirth.. nine months after Valentines is supposedly popular, right. Now you're thinking.

zip_crack.py :
Takes two arguments a 'password_protected.zip' file and a 'wordlist.txt'
For example:
'''$ ./zip_crack.py treasure_chest.zip dictionary.txt 
[+] Password = secret
$'''

kn0wn.py :
Prototype of a simple lightweight defensve scanner applet,f ocused on internal network monitoring.
Pretty limited currently, simply loads in a whitelist of known host ip and checks them against an nmap scan.

Example output:
'''--- Summary Of Scan ---------------------------------------------
-----------------------------------------------------------------
[G]	KNOWN	192.168.1.254	>>>	BThomehub.home
-----------------------------------------------------------------
[G]	KNOWN	192.168.1.64	>>>	User-PC.home
-----------------------------------------------------------------
[R]	UNKNOWN	192.168.1.66	>>> hp-laptop.home
-----------------------------------------------------------------
[G]	KNOWN	192.168.1.75	>>>	kindle-97cf28561.home
-----------------------------------------------------------------
'''

Much-bits to add.
