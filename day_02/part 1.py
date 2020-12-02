import re

validCounter = 0
notValidCounter = 0

f = open('input.txt', 'r')
for line in f:
    r = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    min = r.group(1)
    max = r.group(2) 
    letter = r.group(3)
    password = r.group(4)
    counter = password.count(letter)
    if int(min) <= counter <= int(max):
        validCounter = validCounter+1
    else:
        notValidCounter = notValidCounter+1 

print("Valid: ", validCounter)
print("Not Valid: ", notValidCounter)
