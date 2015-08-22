def rot2(string):
    eng='abcdefghijklmnopqrstuvwxyz'*2
    rot_dict={}
    result=''
    for index in range(26):
        rot_dict[eng[index]]=eng[index+2]
    for char in string:
        if char in eng:
            result+=rot_dict[char]
        else:
            result+=char
    print(result+"fq")
    return result