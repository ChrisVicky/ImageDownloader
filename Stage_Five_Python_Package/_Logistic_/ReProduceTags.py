import os


def getRestriction_Tags():
    path = os.getcwd() + '\\Restriction_Tag.txt'
    List = []
    with open(path, 'r') as FILE:
        for content in FILE.readlines():
            List.append(content[:content.find('\n')])
        return List


List = getRestriction_Tags()
path = os.getcwd() + '\\Restriction_Tag.txt'
with open(path, 'w') as file:
    for tag in List:
        tag = '%20' + tag
        print(tag, file=file)
