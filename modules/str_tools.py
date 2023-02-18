
def clean_name(name) :
    new_name = name\
        .replace(" ", "+")\
        .replace("ë", "e")\
        .replace("ä", "ae")\
        .replace("ü", "ue")\
        .replace("ö", "oe")
    
    return new_name