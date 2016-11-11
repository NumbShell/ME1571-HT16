
"""file_ = open('test.txt', 'w')
file_.write('This is content from a variable! Actually no its not yet')
file_.close()"""

"""def convert(stn):
    #stn = input("Enter sentences...\n")

    return print("---------------\nYour message has been converted to the precious pirate lang!")"""


def message():
    txt = input("Type message to be converted in Pirate lang! \n").lower()
    return txt


def toPirate(stn):
    pirateDic={'hello':'avast', "the":"th'", }
    pirateSentence=''
    wordList=stn.split()
    for i in wordList:
        if i in pirateDic:
            i=pirateDic[i]
        pirateSentence=pirateSentence+' '+i
    return pirateSentence