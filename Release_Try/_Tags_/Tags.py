import os


def getRestriction_Tags():
    List = []
    path = os.path.join(os.getcwd(), "_Tags_")
    path = os.path.join(path, "ForbiddenTags.txt")
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
                print("\n[被禁止的标签]:%s\n[标签位置]:%s" % (tag, url[url.find(tag):url.rfind('.')]))
                return False
    return True


LIST = getRestriction_Tags()
