import sys

''' gives the version '''
print(sys.version)

'''  LIST OF ARGUMENT FROM THE LOOP '''
print(sys.argv)
# this print argument along with the py file name i.e. sysExample.py
argv = sys.argv
for i in argv[1:]:
    print(i, end = " ")


''' CHANGING THE OUTPUT BEHAVIOUR '''
x = 25
def display():
    x = 25
    print('OutPut ')
    print(x)
sys.displayhook = display
# print(x)