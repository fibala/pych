import urllib
import pickle

peakhell=urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data=pickle.load(peakhell)
for line in data:
    print("".join([k * v for k, v in line]))

