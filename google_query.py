import pycurl
import urllib
import sys
from StringIO import StringIO
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.nested_recording = False
        self.result = []
    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for name, value in attrs:           #extracted using blood, sweat and tears
                if name == 'class' and value in ["_Tgc", "_Tfc", "_m3b", "_Oke", "_Xbe", "_Nbe"]:
                    self.recording = True
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value in ["kltat", "_Mjf", "_eF"]:
                    self.nested_recording = True
    def handle_endtag(self, tag):
        if tag == 'span':
            self.recording = False
            self.nested_recording = False
        if tag == 'div' and self.nested_recording == True:
            self.nested_recording = False
    def handle_data(self, data):
        if self.recording == True:
            self.result.append(data)
        if self.nested_recording == True:
            self.result.append(data)
            self.result.append(' ')

def query(question):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")
    encoded_question = urllib.quote_plus(question,"?")
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, "https://www.google.cz/search?q="+encoded_question+"&hl=en")
    c.setopt(c.USERAGENT, "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1")
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    contents = buffer.getvalue()
    buffer.close()
    contents.decode("utf-8", "replace") 
    parser = MyHTMLParser()
    parser.feed(contents)
    if len(parser.result) == 0:
        return "answer not found"
    else:
        return (''.join(parser.result)).rstrip()

#the same as query, but dumps the website to a file for analysis
def queryAndDump(question):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")
    encoded_question = urllib.quote_plus(question,"?")
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, "https://www.google.cz/search?q="+encoded_question+"&hl=en")
    c.setopt(c.USERAGENT, "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1")
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    contents = buffer.getvalue()
    with open ("tmp.log", "w") as f:
        f.write(contents)
    buffer.close()
    contents.decode("utf-8", "replace") 
    parser = MyHTMLParser()
    parser.feed(contents)
    if len(parser.result) == 0:
        return "answer not found"
    else:
        return (''.join(parser.result)).rstrip()


def loadFromFile(filename):
    with open (filename, "r") as f:
        contents = f.read()
        contents.decode("utf-8", "replace") 
        parser = MyHTMLParser()
        parser.feed(contents)
        if len(parser.result) == 0:
            return "answer not found"
        else:
            return (''.join(parser.result)).rstrip()
