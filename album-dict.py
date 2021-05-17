#!/usr/bin/python
full = []

with open("names.txt") as fileOpen:
    for line in fileOpen:
        text = line.strip()
        names = text.split(" - ")
        full.append(names)

#print(full)
#print(dict(full))

file = open('name.txt', 'w')
file.write(str(dict(full)))
file.close()