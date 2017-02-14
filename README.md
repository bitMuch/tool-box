# tool-box
prototype tools (R&D)

# --- Preamble --- #
web_scraper.py :
A friend of mine shared with me, two of his passwords for popular online services. They were both surnames of well known footballers,  with the players jersey number added to the end it of them. 
He is a regular user, and this made sense as eash password contained a capital letter, a fair number of characters, at least one number and was easy to remember. 

Finishing up the first few excercises in: Violent Python, by T.J. O'Conner, wanting something a little beefier for a passwords.txt file, than the "cp /usr/share/dict/words dictionary.txt" I had initially run to get going with the examples.

Thinking about the habits of human behaviour, I remembered my friend. His generosity inspired me to wip up a quick script that would (with the help of BeautifulSoup4) scrape the target data of each teams roster from: http://www.footballsquads.co.uk/eng/2016-2017/faprem.htm, concatonate as Surname+Number, and then wrting that list to a file.

To do:
it's sloppy as hell and hardcoded, so clean up, modularize and send back out to generate more passwords..

What next? commonBabyName+commonDateOfBirth.. nine months after Valentines is supposedly popular, right. Now you're thinking.
