import re
line = 'Cats are marter than dogs'
matchObj = re.match(r'(.*) are (.?).*',line, re.M|re.I)

matchObj1 = re.match(r'dog',line, re.M|re.I)
searchObj = re.match(r'(.*) are (.*)', line, re.M|re.I)
if matchObj:
    print(matchObj1.groups())
    print(matchObj.group(1))
    print(matchObj.group(2))
    print(matchObj.groups())
    print(searchObj.group())
    # Raw string
print(R'\n')
print(r'\n')

