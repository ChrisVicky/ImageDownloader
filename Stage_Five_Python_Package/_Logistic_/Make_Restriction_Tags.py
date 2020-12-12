import os
Dictionary_Tags = {}
TagDic = {}
FileName_txt = '\Restriction_Tag.txt'


def PushTag(name):
    if name in TagDic.keys():
        TagDic[name] += 1
        return
    TagDic[name] = 1
    return


def distinguishTags(url):
    url = url[url.rfind('Konachan.com%20-%20')+19:]
    while url:
        Indicator_l = url.find('%20') + 3
        url = url[Indicator_l:]
        Indicator_r = url.find('%20')
        if Indicator_r == -1:
            Indicator_r = url.find('.jpg')
            tag = url[:Indicator_r]
            PushTag(tag)
            return
        tag = url[:Indicator_r]
        PushTag(tag)


def collectTags(File):
    Picture_Name = os.listdir(File)
    for name in Picture_Name:
        if 'jpg' in name:
            name = name[:name.rfind('.jpg')]
            distinguishTags(Dictionary_Tags[name])


def getTags(File):
    with open(File, 'r') as file:
        DataList = file.readlines()
        i = 0
        while i < len(DataList):
            data = DataList[i]
            if data == '\n':
                i += 1
                continue
            name = data[data.find('[')+1:data.find(']')]
            i += 1
            data = DataList[i]
            url = data[data.find('[')+1:data.find(']')]
            Dictionary_Tags[name] = url
            i += 1


def Sort_Dic(dic):
    lis = list(dic.items())
    lis = sorted(lis, key=lambda x: x[1], reverse=True)
    lis_return = []
    for i in lis:
        lis_return.append(i)
    return dict(lis)


def Tag_Save(dic):
    SaveKey = ['long_hair', 'original', 'hat', 'white_hair', 'sky', 'purple_hair', 'blue_eyes', 'dress', 'school_uniform', 'short_hair', 'brown_eyes', 'brown_hair']
    for key in SaveKey:
        dic[key] = 0


def Test_TagOK(List):
    namelist = os.listdir(os.getcwd())
    for name in namelist:
        if 'jpg' in name:
            if Test_TagOK_Check(List, Dictionary_Tags[name]):
                print("Not Ok")
                print(name + "'s Tags are not totally included. Please edit it in SaveKey")
                return
    print("OK Yeah!")


def make_Restriction_Tag():
    global TagDic
    path_txt = os.getcwd() + '\BackUp.txt'
    path_txt_write = os.getcwd() + FileName_txt
    path_Picture = os.getcwd()
    getTags(path_txt)
    collectTags(path_Picture)
    Tag_Save(TagDic)
    TagDic = Sort_Dic(TagDic)
    TAGLIST = list(TagDic.keys())
    with open(path_txt_write, 'w') as file:
        print(path_txt_write)
        for tag in TAGLIST:
            print(tag, file=file)
    Test_TagOK(TAGLIST)
    return TAGLIST


def Test_TagOK_Check(List, Target):
    for tag in List:
        if tag in Target:
            return False
    return True


def Test_TagOK(List):
    namelist = os.listdir(os.getcwd())
    for name in namelist:
        if 'jpg' in name:
            name = name[:name.rfind('.jpg')]
            if Test_TagOK_Check(List, Dictionary_Tags[name]):
                print("Not Ok")
                return
    print("OK Yeah!")


def UpdateRestriction():
    ListRestrict = getRestriction_Tags('\Restriction_Tag.txt')
    ListSave = getRestriction_Tags('\Save_Tag.txt')
    for save in ListSave:
        if ListRestrict.count(save) >= 1:
            ListRestrict.remove(save)
    path_txt_write = os.getcwd() + FileName_txt
    with open(path_txt_write, 'w') as file:
        print(path_txt_write)
        for tag in ListRestrict:
            print(tag)
            print(tag, file=file)


def Welcome():
    print("请将下载下来且不合法的图片、所有的BackUp.txt放入该.py同一目录下。")
    print("接下来将获取到不合法的tags并按照数量制成txt文件，输出到本目录下")
    print("或者您可以将应该合法的tags放在Save_Tag.txt中，并选择2，这样可以对Restriction.txt进行更新\n")
    Status = input("1.开始程序\n")
    print("You have Chosen %s" % Status)
    if Status == '1':
        make_Restriction_Tag()
        return
    elif Status == '2':
        UpdateRestriction()
        return
    else:
        exit(0)


def getRestriction_Tags(SubFile):
    LIST = []
    path = os.getcwd() + SubFile
    print(path)
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


Welcome()
