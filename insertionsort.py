oglist = [1,6,34,87,25,51,38]
print("Original list: ", oglist)
def insertion(a):
    for i in range (1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp <a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp

insertion(oglist)
print("Sorted list: ", oglist)
