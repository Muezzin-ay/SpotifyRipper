
import urllib


def clean_name(name) :
    new_name = name\
        .replace(" ", "+")\
        .replace("ë", "e")\
        .replace("ä", "ae")\
        .replace("ü", "ue")\
        .replace("ö", "oe")\
        .replace(":", "")\
        .replace("<", "")\
        .replace(">", "")\
        .replace("/", "")
           
    new_name = urllib.parse.quote_plus(new_name)
    return new_name