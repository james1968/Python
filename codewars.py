def starting_mark(height):
    multiple = float((10.67 - 9.45)/(1.83 - 1.52))
    constant = (9.45 / (4*1.52))
    ans = float(height*multiple + (9.45 - (multiple*1.52)))
    print(ans, 2)


starting_mark(1.52)
starting_mark(1.83)
starting_mark(1.22)
starting_mark(2.13)
starting_mark(1.75)
