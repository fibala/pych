def ocr(webpage):
    import urllib
    webinfo=urllib.urlopen(webpage)
    return webinfo.read().translate(None,"[]{}()#$%^@+!*&_\n")


def main():
    #webpage="http://www.pythonchallenge.com/pc/def/ocr.html"
    webpage="ocr.html"
    print(ocr(webpage))

if __name__=="__main__":
    main()