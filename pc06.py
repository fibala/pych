#use python2
def linkedlist(num):
    import zipfile
    import re
    zfile=zipfile.ZipFile("channel.zip")
    content=zfile.read(num+".txt")
    info=zfile.getinfo(num+".txt").comment
    pattern=re.compile("Next nothing is (\d+)")
    match=pattern.search(content)
    print(content)
    if match==None:
        return ["Done",""]
    return [match.group(1),info]

def main():
    num="90052"
    comments=[]
    while num!="Done":
        num,info=linkedlist(num)
        comments.append(info)
    print("".join(comments))

if __name__=="__main__":
    main()