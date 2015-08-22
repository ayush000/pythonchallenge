import pickle


def pick1():
    with open('banner.pickle', 'rb') as f:
        a = pickle.load(f)
    for l in a:
        # print(l)
        sum1=0
        for asc in l:
            print(asc[0]*asc[1],end='')


            # if asc[0]==' ':
            #     l=int(asc[1])
            #     for i in range(l):
            #         print(' ',end='')
            # else:
            #     for i in range(l):
            #         print('#',end='')
        # print(sum1)
        print()