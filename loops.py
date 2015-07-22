def bottles_lyrics():
    bottle = 9
    while bottle > 0:
        if bottle !=1:
            bottle_str = str (bottle) + " bottles"
        else:
            bottle_str = str (bottle) + " bottle"
        print(bottle_str + " of beer on the wall,")
        print(bottle_str + " of beer,")
        print("take one down, pass it around,")
        bottle -= 1
        print(str(bottle) + " bottles of beer on the wall!")
    return None
bottles_lyrics()
