import re
def bodyguards(file):
    data=''
    with open(file, "r") as myfile:
        data+=myfile.read()
    result=''
    list= re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',data)
    for str in list:
        result=result+str
    return result
    #return re.match('[A-Z]{3}[a-z][A-Z]{3}',data)