import os


def getRestriction_Tags():
    LIST = []
    path = os.getcwd() + '\_Logistic_' + '\Restriction_Tag.txt'
    with open(path, 'r') as FILE:
        for content in FILE.readlines():
            LIST.append(content[:content.find('\n')])
        return LIST


def Tag_legal(url):
    LIST = getRestriction_Tags()
    for tag in LIST:
        if tag in url:
            return False
    return True
