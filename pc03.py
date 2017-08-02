def equality(data):
    import re
    find=re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",data)
    return "".join(find)

def main():
    import urllib
    import re
    #webpage="http://www.pythonchallenge.com/pc/def/equality.html"
    webpage="equality.html"
    html=urllib.urlopen(webpage).read()
    #data=re.findall("<!--(.*?)-->",html,re.DOTALL)[0]
    data=html
    print(equality(data))

if __name__=="__main__":
    main()