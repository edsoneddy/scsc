caso:str = input()

def validate(caso):

    if caso[-2:] == "00":
        dato:int = int(caso[:-2])
        if dato%4 == 0:
            return "si"
        else:
            return "no"
    if int(caso)%4 == 0:
        return "si"
    else:
        return "no"
print(validate(caso))
