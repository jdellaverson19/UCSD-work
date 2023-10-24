def multiply(*list):
    # list here is actually a tuple
    total = 1
    for number in list:
        total *= number
    return total


multiply(2, 3, 4, 5)


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="admin")
# prints dictionary
# Python doesn't have block level scope -- variables accessible in fnct after they've been defined.
# Global outside of fnct
# can change global variable w global kword
# f9 brkpoint
# f5 debug, f10 step, f11 fnct shft f11 step out of fnct
# Windows tips: end key takes you to endl, begin use home key. cntrl home end for file
# for moving lines, press alt and then arrow keys while highlighted
# for duplication, select and hold shift alt down
# cntrl / for commenting.
# can do any letters in sequence for intellisense
