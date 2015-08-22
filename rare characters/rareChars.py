import collections
def rare_chars(file):
    data=''
    with open(file, "r") as myfile:
        data+=myfile.read()
    cset=collections.OrderedDict()
    for char in data:
        if char in cset.keys():
            cset[char]+=1
        else:
            cset[char]=1
    return cset
