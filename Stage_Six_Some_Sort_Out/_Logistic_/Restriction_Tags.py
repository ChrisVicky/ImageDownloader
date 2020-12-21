import os
import re


def getRestriction_Tags():
    List = []
    path = os.getcwd() + '\_Logistic_' + '\Restriction_Tag.txt'
    with open(path, 'r') as FILE:
        for content in FILE.readlines():
            List.append(content[:content.find('\n')])
        return List


def Tag_legal(url):
    for tag in LIST:
        if tag in url:
            tag1 = tag + '%'
            tag2 = tag + '.'
            if tag1 in url or tag2 in url:
                print("\n[Forbidden tag]:%s\n[Right Here]:%s" % (tag, url[url.find(tag):]))
                return False
    return True


LIST = getRestriction_Tags()
