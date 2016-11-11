import sys

"""new_file = open(sys.argv[1], 'r')
print(new_file.read())"""

def fromPirate(sentence):
    pirateDic={'booty': 'butts', 'avast':'hello', 'proud beauty':"madam", "th'":"the"}
    pirateSentence=''
    wordList=sentence.split()
    for i in wordList:
        if i in pirateDic:
            i=pirateDic[i]
        pirateSentence=pirateSentence+' '+i
    return pirateSentence