def linkedlist(num):
    import urllib
    import re
    webpage="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    pattern=re.compile("and the next nothing is (\d+)")
    websource=urllib.urlopen(webpage % num).read()
    match=pattern.search(websource)
    print(websource)
    if match==None:
        return "Done"
    return match.group(1)

def main():
    #num="12345"
    #num="9401"
    #num=str(16044/2)
    #num="87283"
    num="23298"
    while num!="Done":
        num=linkedlist(num)
    print(num)

if __name__=="__main__":
    main()