"""
Things To Do:
●	Get the word format from the user so they can customise it. Convert it to lowercase using a str method.
●	Try and make the program more interesting, For example:
a.	Use wildcards for the vowels (#) and consonants (%) or either (*) and make alphabetical characters use that actual character - e.g. the format “%re#*l*” might produce a word like “greatly” or “breuzla”
b.	Automatically (randomly) generate the word_format variable.

"""
import random

def is_valid_format(word_format):
  word = ""
  for kind in word_format:
     if kind == "c":
        word += random.choice(CONSONANTS)
     elif kind == "v":
        word += random.choice(VOWELS)
     else:
         pass#invalid

  if kind != "c" and kind != "v":
      return False#invalic
  else:
      return True


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word_format = input("Enter word format with c for consonant and v for vowel")
return_value = is_valid_format(word_format)
print(return_value)
