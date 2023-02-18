
import re


def clean_name(name) :
    new_name = name\
        .replace(" ", "+")\
        .replace("ë", "e")\
        .replace("ä", "ae")\
        .replace("ü", "ue")\
        .replace("ö", "oe")
        
    re.sub('[^A-Za-z0-9]+', '', new_name) 
    return new_name