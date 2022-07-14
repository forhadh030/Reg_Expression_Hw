from importlib.metadata import files
from os import link
import re

pattern = re.compile("abcd")
print(pattern)

# match will only find and match 1 set
match = pattern.match("abcd123")
print(match, "\n")

# finders will find multiple sets
finders = pattern.findall("123abcd abcd123 abcd abcabc acb")
print(finders, '\n')

#search will only find 1 set
random_string = "123 123 234 abcd abc"
search = pattern.search(random_string)
print(search, '\n')

# pattern_int will only print each number per bracket
pattern_int = re.compile('[0-7][7-9][0-3][7-9]')
random_number = pattern_int.search("67383")
print(random_number, '\n')

# char_pattern will only print each letter per bracket from multiple words
char_pattern = re.compile('[A-Z][a-z]')
found = char_pattern.findall("Hello there Mr. Anderson")
print(found, '\n')

# something that occurs {number of time} within the range
char_pattern_count = re.compile('[A-Z][a-z][0-3]{2}')
found_count = char_pattern_count.findall("Hello there Mr. An23dderson")
print(found_count, '\n')

# this will print all the m range(1-5) (make sure there's no space in between 1,5)
random_pattern = re.compile('m{1,5}')
random_statement = random_pattern.findall('This is an ummm example of a regular m mmm m')
print(random_statement, '\n')

# The question mark makes the 's' next to it optional. So it can either be 1s or 2s
patterns = re.compile('Mrss?')
found_pat = patterns.findall("Hello M there Mr. Anderson, Mid how is Mrs. Anderson and Mrss. Anderson?")
print(found_pat, '\n')

# the M prior to * is optional. Will print out MS or s, s, s, etc
# using {3} right of 's' will make it so that only the sx3 are printed
pattern_m = re.compile("M*s")
found_m = pattern_m.findall("MMMs name is Ms. Smith. This is Msssss.")
print(found_m, '\n')

# Will print as long as there is at LEAST 1M and 1s
pattern_again = re.compile('M+s')
found_patt = pattern_again.findall("MMMs name is Ms. Smith. This is Msssss.")
print(found_patt, '\n')

# \w returns unicode while \W returns everything else
pattern_1 = re.compile("\w+")
pattern_2 = re.compile("\W+")
found_1 = pattern_1.findall("This is a sentence with an exaclamation mark")
found_2 = pattern_2.findall("This is a sentence with an exaclamation mark")
print(found_1)
print(found_2, "\n")

# \d looks for any digit 0-9 while \D looks for anything that isn't a digit
pattern_nums = re.compile("\d{1,2}[a-z]{2}")
found_date = pattern_nums.findall("Today is the 7th, in 20days it will be the 27th. 3rd, 1st,30th")
print(found_date, '\n')

# \s look for any white space while \S looks for anything that isn't whitespace
pattern_no_space = re.compile('\S[a-z]+[\W]')
pattern_space = re.compile('\s+')
found_no_space = pattern_no_space.findall("Are you afraid of the dark? ")
found_space = pattern_space.findall("Are you afraid of the dark? ")
print(found_space)
print(found_no_space, "\n")

# \b looks for boundaries or edges of a word while \B look for anything that isn't a boundary
pattern_bound = re.compile(r"\bTheCodingTemple")
pattern_no_bound = re.compile(r"\BTheCodingTemple")
found_bound = pattern_bound.findall("TheCodingTemple")
no_found_bound = pattern_no_bound.findall("TheCodingTemple")
print(found_bound)
print(no_found_bound, '\n')

#Group using compiler; space bar between 2 bracket matters!!
string_again = "John Smith, michael mayer, Sam Smith, Marshall Mathers, Michael Jackson"
pattern_name = re.compile("([A-Z][a-zA-Za-z]+) ([A-Z][A-Za-z]+)")
found_names = pattern_name.findall(string_again)
print(found_names)

for name in string_again.split(', '):
    match = pattern_name.search(name)

    if match:
        print(match.groups(2))
    else:
        print("Not a name", "\n")

with open('name.txt.rtf') as f:
    data = f.read()
    print(re.match(r"Hawkins, Derek", data))
    print(re.search(r"ryanb@codingtemple.com", data))

f.close()
