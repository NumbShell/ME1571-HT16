from datetime import datetime
from datetime import datetime, timedelta
import sys

#if var name is equal to main (It has been called directly)
if __name__ == "__main__":

    #Grab the current time and store it in a var called now
    now = datetime.now()

    #Create a function
    def date_from_day(d):

        #print out the days from now based on the parameter d
        print("In " + str(d) + " days it will be " +  str(now + timedelta(days=d)))

    #Another function
    def date_from_date(y,m,d):

        #Grab the date that was specified by the user
        date = datetime(y,m,d)

        #Calc diff
        diff = now - date
        #Calc the time since then in days
        print("It has gone " + str(diff.days) + " days since " + str(date))

    #Grab the arguments that was provided in the cmd
    value = sys.argv

    #if length of value is less or equal to 2 then only one parameter was given
    if len(value) <= 2:
        date_from_day(int(value[1]))
    else:
        date_from_date(int(value[1]), int(value[2]), int(value[3]))
