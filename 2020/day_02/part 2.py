import re

validCounter = 0
notValidCounter = 0

f = open('input.txt', 'r')
for line in f:
    r = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    min = int(r.group(1))
    max = int(r.group(2)) 
    letter = r.group(3)
    password = r.group(4)

    if (password[min-1] == letter and password[max-1] != letter) or (password[min-1] != letter and password[max-1] == letter):
        validCounter = validCounter+1
    else:
        notValidCounter = notValidCounter+1 
    
print("Valid: ", validCounter)
print("Not Valid: ", notValidCounter)
