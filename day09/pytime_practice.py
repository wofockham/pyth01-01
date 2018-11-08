from pytime import pytime

def calendar():
    holidays = ['Halloween', 'Easter', 'Christmas']

    year = int(input("Please enter a year: "))

    print("Available holidays:", holidays)
    # TODO: validate
    holiday = input("Please enter a holiday: ")

    if holiday == 'Halloween':
        print("In", year, "Halloween was on", pytime.halloween(year))
    elif holiday == 'Easter':
        print("In", year, "Easter was on", pytime.easter(year))
    elif holiday == 'Christmas':
        print("In", year, "Christmas was on", pytime.christmas(year))

calendar()
