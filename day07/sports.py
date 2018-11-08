sports = {
    "tennis": 2,
    "soccer": 75,
    "volleyball": 11,
    "chess": 2
}

for sport in sports:
    print("I like \"{0}\".".format(sport))
    print("There are usually {0} players in {1}.".format(sports[sport], sport))
