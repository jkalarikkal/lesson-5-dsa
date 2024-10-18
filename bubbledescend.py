oglist = [12,5,89,43,7,22]
print("Original list: ", oglist)

for i in range (0,len(oglist)):
    for j in range (i, len(oglist)):
        if oglist[i] <oglist[j]:
            oglist[i], oglist[j] = oglist[j], oglist[i]

print("sorted list: ", oglist)
