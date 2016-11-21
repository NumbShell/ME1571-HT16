
"""file_ = open('test.txt', 'w')
file_.write('This is content from a variable! Actually no its not yet')
file_.close()"""


def sentences():
    stn = input("Enter sentences...\n")


"""def convert(stn):
    #stn = input("Enter sentences...\n")

    return print("---------------\nYour message has been converted to the precious pirate lang!")"""


def message():
    txt = input("Type message to be converted in Pirate lang! \n").lower()
    return txt


def toPirate(msg):
    pirateDic={'hello':'avast', "the":"th'", }
    pirateSentence=msg
    wordList=pirateSentence.split()
    for i in wordList:
        if i in pirateDic:
            i=pirateDic[i]
        pirate_Sentence=pirateSentence+' '+i
    print(pirate_Sentence)
