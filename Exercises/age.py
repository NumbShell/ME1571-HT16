from datetime import datetime
from datetime import datetime, timedelta

#Make a list to store the year, month and day values
list_date = []

#returnerar tiden som gått sedan du föddes i dagar och timmar
def time_alive(y, m, d):
    # Datumet du föddes
    born = datetime(y, m, d)

    # Tiden nu
    now = datetime.now()

    # konverterar datum till dagar
    diff = now - born

    if born > now:
        print("Are you from the future?")
    else:
        print ("You have been alive for " + str(diff.days) + " days or " + str(diff.days * 24) + " hours\n"
                                                                                                 "In thousand years it will be " + str(now + timedelta(days=1000)))


def assign_date(date):

    #date has been converted to something like this 19970601 without the /

    #assign [1997]0601 to _y
    _y = date[0:4]

    # assign 1997[06]01 to _y
    _m = date[4:6]

    # assign 199706[01] to _y
    _d = date[6:8]

    #Assign the values to the list_date list
    list_date.append(int(_y))
    list_date.append(int(_m))
    list_date.append(int(_d))

    #print(time_alive(int(_y), int(_m), int(_d)))


#Convert string and assign the values to variables
def dates():
    #Ask user for date
    _date = input("When were you born? (yyyy/mm/dd)\n")

    rpl = "/"
    for c in rpl:
        _date = _date.replace(c, "")
    return _date


#huvudfunktionen
def age():
    # 1. Ask user for date and convert it for easier manipulation and store it in a var
    date = dates()

    # 2. Add dates to _y, _m and _d from date
    assign_date(date)

    # 3. Run the time_alive function and give it the values of the list_date list
    time_alive(list_date[0], list_date[1], list_date[2])

if __name__ == "__main__":
    age()