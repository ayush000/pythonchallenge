import httplib2
import re


def followLinks():
    htobj = httplib2.Http('.cache')
    link1=12345
    # url1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'


    # link1 = re.search(r'\d+', content).group(0)

    for i in range(400):
        url1='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(link1)
        response, content = htobj.request(url1)
        content = content.decode('utf-8')
        if content=='Yes. Divide by two and keep going.':
            link1=int(link1)/2
        else:
            link1 = re.search(r'\d+$', content).group(0)
        print(link1)


if __name__ == '__main__':
    followLinks()
