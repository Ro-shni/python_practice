#minutes to time in days,hours,minutes
def convert(sec):
    sec = sec % 24*3600
    day = sec //86400
    day %= 86400
    hour = sec//3600
    sec %= 3600
    minu = sec//60
    sec %= 60
    return "%d ,%d , %d , %d" % (day,hour, minu, sec)
print(convert(123456789)) 