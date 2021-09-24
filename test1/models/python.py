import re
list = ["VIP_13", "VIP_98", "VIP_8" , "VIPP_10"]
for element in list:
    z = re.match("^VIP_([1-9]|[1-9][0-9]|0[1-9])$",element)
    if z:
        element = True
        print((element))
    else:
        element= False
        print((element))