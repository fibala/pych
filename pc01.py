def cipher1(words):
    cipher1_word=''
    for i in words:
        if i>='a' and i<='z':
            cipher1_word+=chr(((ord(i)+2-ord('a'))%26+ord('a')))
        else:
            cipher1_word+=i
    return cipher1_word
def cipher2(words):
    #use string.maketrans(python2), str.maketrans(python3)
    import string
    import sys
    if sys.version_info.major==2:
        trans=string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    elif sys.version_info.major==3:
        trans=str.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
    return words.translate(trans)

def main():
    the_string="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    the_map="map"
    print(cipher1(the_string))
    print(cipher2(the_map))

if __name__=="__main__":
    main()

