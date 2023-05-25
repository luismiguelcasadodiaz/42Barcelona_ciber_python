#!/usr/bin/python3
kata = (0, 4, 132.42222, 10000, 12345.67)

if type(kata) is tuple:
    if len(kata) == 5:
        print("module_{:0>2}, ex_{:0>2} : {:.2f}, {:.2e}, {:.2e}".format(
            kata[0], kata[1], kata[2], kata[3], kata[4]))
    else:
        print(f"Kata {kata} does not fit in this template")
else:
    print(f"{kata} is not a tuple")
