import urllib.request	
import io
import re


def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part




def GetYtTagtoString(str):
    my_request = urllib.request.urlopen(str)
    my_HTML = my_request.read().decode("utf8")

    iostr = io.StringIO(my_HTML)

    currentline = 1
    funcon = True
    tlstring = ""

    while funcon == True:
    

        if currentline == 21:
        
            tlstring = (iostr.readline())
            funcon = False

        else:
         iostr.readline()
         currentline += 1
         funcon = True


    for x in range(tlstring.find('<meta name="keywords" content="') + 29):
     tlstring = (remove_char(tlstring, 1))

    tlstring = (remove_char(tlstring, 0))
    
    for x in range(len(tlstring) - tlstring.find('><link')):
     tlstring = (tlstring[:-1])
    return tlstring


def GetYtTagtoList(str):
    my_request = urllib.request.urlopen(str)
    my_HTML = my_request.read().decode("utf8")

    iostr = io.StringIO(my_HTML)

    currentline = 1
    funcon = True
    tlstring = ""

    while funcon == True:
    

        if currentline == 21:
        
            tlstring = (iostr.readline())
            funcon = False

        else:
         iostr.readline()
         currentline += 1
         funcon = True


    for x in range(tlstring.find('<meta name="keywords" content="') + 29):
     tlstring = (remove_char(tlstring, 1))

    tlstring = (remove_char(tlstring, 0))
    
    for x in range(len(tlstring) - tlstring.find('><link')):
     tlstring = (tlstring[:-1])
    return(re.split('\W+', tlstring))
 
 