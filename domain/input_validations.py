def is_empty(area:str):
    # Checks if the input is an empty string

    if not area or not area.strip():
        return None
    return area

def length(area:str):

    if len(area) < 2 or len(area) > 80:
        return None
    return area

def check_number(area:str):
    nums = 0
    for i in area:
        if i.isnumeric():
            nums+=1

    if len(area.strip()) == nums:
        return None

    return area