
import re


def clean_name(name) :
    specials = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"',"'",'<',',','>','.','?','/','’'}

    new_name = name\
        .replace(" ", "+")\
        .replace("ë", "e")\
        .replace("ä", "ae")\
        .replace("ü", "ue")\
        .replace("ö", "oe")
        
    
    for char in specials :
        new_name.replace(char, "")

    return new_name