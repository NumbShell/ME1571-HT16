import sys

"""new_file = open(sys.argv[1], 'r')
print(new_file.read())"""

<<<<<<< HEAD
def print():
    print("Welcome!")

printus()
=======
def fromPirate(sentence):
    pirateDic={'booty': 'butts', 'avast':'hello', 'proud beauty':"madam", "th'":"the"}
    pirateSentence=''
    wordList=sentence.split()
    for i in wordList:
        if i in pirateDic:
            i=pirateDic[i]
        pirateSentence=pirateSentence+' '+i
    return pirateSentence
>>>>>>> 45912551a6eb560034a27920aa17ff1e530e0410
