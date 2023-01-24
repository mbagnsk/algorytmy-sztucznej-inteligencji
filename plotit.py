import matplotlib.pyplot as plt


path = "hist.txt"
points = []
file = open(path, "r")
rows = file.read().splitlines()

perms = []
for row in rows:
    rowElements = row.split()
    perm = []
    for element in rowElements:
        perm.append(int(element))
    perms.append(perm)

print(perms)





