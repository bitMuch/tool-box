## /* Preamble */
**prototype tools (R&D)**
- Offensive Security: **Fphil-0.01.py** :: **w3ndy.py** :: **z0e.py**
- Defensive Reconaissance: **kn0wn.py**
```
      Essentially for study, research and development. Unlikely to be of use to anyone at present.
```
--------------------------------------------------------------------------------------------------------------------------------
### /* tool-box */

(**ftp-cracker/Fphil.py**) :

Example Output:
```
-------------------------------------------------------------------------
### FTP Pen-Testing/Hacking Infiltration Utility ########################
--------------------------------------------------------- [Fphil-0.01] --
[*] TARGETING	 ->	   USER: alarm @ HOST: 192.168.1.72
-------------------------------------------------------------------------
[+] Trying anonymous credentials for ftp@192.168.1.72
[-] FTP anonymous login failed.
-------------------------------------------------------------------------
[!] Attempting Brute-Force method, in..
[3] Press CTRL-C to Abort
[2] Press CTRL-C to Abort
[1] Press CTRL-C to Abort
[0] Press CTRL-C to Abort
[#] ...
[#] Trying password list.. This may take a while
[#] ...
-------------------------------------------------------------------------
[!] FTP login successful with:
[>] USER: alarm
[>] PASS: alarm
[.]
--------------------------------------------------------- [Fphil-0.01] --
```
--

(**web-scraper/w3ndy**) :

Example output:

```
Oxlade-Chamberlain15
Holding16
Iwobi17
Monreal18
Cazorla19
Mustafi20
Sanogo22
Welbeck23
Bellerín24
```
A friend of mine, shared with me two of his passwords for popular online services. They were both surnames of well known footballers,  with the players jersey number added to the end. 
He is a regular user, and this made sense as each password contained a capital letter, a fair number of characters, included numbers and was easy to remember. 

Well, after finishing up the first few excercises from the book: Violent Python, by T.J. O'Conner, and wanting something a little beefier for a pwfile than the *"cp /usr/share/dict/words dictionary.txt"* I had initially run.

I got to thinking about the habits of human behaviour, and soon remembered my friend and his system. 
That inspired me to wip up a quick script that would (with the help of BeautifulSoup4) scrape the target data of each teams roster from: http://www.footballsquads.co.uk/eng/2016-2017/faprem.htm, concatonate the players Surname+Number, then write that list to a file.

w3ndy, grabbed 1068 player names and numbers in all.

- **To** do: it's sloppy as hell and hardcoded, so clean up, modularize.
- **Bugs**: A few names appeared with some kind of error in encoding. eg. "Granit\xa0Xhaka29"
- *What next?*: commonBabyName+commonDateOfBirth.. nine months after Valentines is supposedly popular, right.

--

(**zip-cracker/z0e**) :
Takes two arguments a 'password_protected.zip' file and a 'wordlist.txt'

For example:

```
$ ./zip_crack.py treasure_chest.zip dictionary.txt 
[+] Password = secret
$
```
--

(**defensive-scanner/kn0wn**) :
Prototype of a simple lightweight defensve scanner applet, focused on LAN monitoring.
Currently just loads in a whitelist of known host ip and checks them against an nmap scan.

Example output:

```
--- Summary Of Scan ---------------------------------------------
-----------------------------------------------------------------
[G]	KNOWN	192.168.1.254	>>>	BThomehub.home
-----------------------------------------------------------------
[G]	KNOWN	192.168.1.64	>>>	User-PC.home
-----------------------------------------------------------------
[R]	UNKNOWN	192.168.1.66	>>> hp-laptop.home
-----------------------------------------------------------------
[G]	KNOWN	192.168.1.75	>>>	kindle-97bm28000.home
-----------------------------------------------------------------
```

Much-bits to add.
:wq
