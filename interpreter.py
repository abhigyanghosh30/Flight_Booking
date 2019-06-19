import datetime

def inp_day():
    text = input("On what date do you want to go?")
    if 'today'.lower in text.lower:
        return datetime.datetime.today()
    if 'tomorrow'.lower in text.lower:
        return datetime.date.today() + datetime.timedelta(days=1)






