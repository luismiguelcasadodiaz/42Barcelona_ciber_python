#!/usr/bin/python3
kata = (19, 42, 21)
if type(kata) is tuple:
    if len(kata) == 3:
        print("The 3 numbers are: {}, {}, {}".format(
            kata[0], kata[1], kata[2]))
    else:
        print(f"Kata {kata} does not fit in this template")
else:
    print(f"{kata} is not a tuple")
