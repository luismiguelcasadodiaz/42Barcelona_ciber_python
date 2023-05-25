#!/usr/bin/python3
kata = (2019, 9, 25, 3, 30)
if type(kata) is tuple:
    if len(kata) == 5:
        print("{:0>2}/{:0>2}/{:4} {:0>2}:{:0>2}".format(
            kata[1], kata[2], kata[0], kata[3], kata[4]))
    else:
        print(f"Kata {kata} does not fit in this template")
else:
    print(f"{kata} is not a tuple")
