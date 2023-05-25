#!/usr/bin/python3
kata = "The right format"
kata = ""
if len(kata) < 43:
    print("{:->42}".format(kata), end="")
else:
    print(f"Text '{kata}' is too long here")
