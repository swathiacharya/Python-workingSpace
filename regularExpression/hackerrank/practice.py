import re
text = input()
pattern =r'ac'
match = re.findall(pattern, text)
print("no of matches: ", len(match))
print("Matches: ", match)
