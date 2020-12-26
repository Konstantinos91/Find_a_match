import nltk
from nltk import re

with open('Find_a_match.txt', 'r') as file:
    index = file.read().replace('\n', '')
Regexp = re.compile(r'([£ $ €])?([1-9][\d]{0,5}(?:\,[\d]{1,3})?(?:\.[\d]{1,3})?(?:bn|m|p)?)( Euros| Euro| Pounds| Dollars| euros| euro| pounds| dollars)?')

print("The results are:")

for c in re.finditer(Regexp, index):
    if c != 0:
         if c.group(1) == '$':
            print("\nFound a match!")
            print("Currency : Dollar")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' Dollars':
            print("Found a match!")
            print("Currency : Dollar")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' Dollars':
            print("Found a match!")
            print("Currency : Dollar")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' dollars':
            print("Found a match!")
            print("Currency : Dollar")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(1) == '£':
            print("Found a match!")
            print("Currency : Pounds")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' Pounds':
            print("Found a match!")
            print("Currency : Pounds")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' pounds':
            print("Found a match!")
            print("Currency : Pounds")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(1) == '€':
            print("Found a match!")
            print("Currency : Euros")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' Euros':
            print("Found a match!")
            print("Currency : Euros")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' euros':
            print("Found a match!")
            print("Currency : Euros")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' euro':
            print("Found a match!")
            print("Currency : Euros")
            print("Amount :", c.group(2))
            print("----------------------")
         elif c.group(3) == ' Euro':
            print("Found a match!")
            print("Currency : Euros")
            print("Amount :", c.group(2))
            print("----------------------")
       
    else:
        print("No match found.")
