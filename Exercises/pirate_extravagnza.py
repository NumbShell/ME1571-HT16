import pirate_lang
import pirate_read_lang
import sys

if __name__ == "__main__":

    #Call msg function from pirate_lang and save the text it returns in msg
    msg = pirate_lang.message()

    #convert the txt to pirate lang
    tp_msg = pirate_lang.toPirate(msg)
    print(tp_msg)

    fp_msg = pirate_read_lang.fromPirate(tp_msg)
    print(fp_msg)


"""%s" % (txt)"""