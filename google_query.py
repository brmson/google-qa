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
        self.found_bold = False
        self.first = False
        self.merge = False
        self.result = []
    def handle_starttag(self, tag, attrs):
        if self.recording == True and tag == 'b':
            self.found_bold = True
            self.result.append('b')
        if tag == 'span' and self.first == True:
            self.merge = True
        if tag == 'span' and self.nested_recording == True:
            self.first = True
        if tag == 'span':
            for name, value in attrs:           #extracted using blood, sweat and tears
                if name == 'class' and value in ["_Tgc", "_Tfc", "_m3b", "_Oke", "_Xbe", "_Nbe"]:
                    self.recording = True
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value in ["kltat", "_Mjf", "_eF","_yXc"]:
                    self.nested_recording = True
    def handle_endtag(self, tag):
        if tag == 'span':
            if self.merge == True:
                self.merge = False                
            self.recording = False
        if tag == 'div' and self.nested_recording == True:
            self.nested_recording = False
            self.first = False
    def handle_data(self, data):
        if self.merge == True:
            self.result[-1] = self.result[-1] + data 
            return
        if self.recording == True:
            self.result.append(data)
        if self.nested_recording == True:
            self.result.append(data)

#we append 'b' to the list whenever we find a html bold tag, so now we parse it
def parseBoldStrings(result):
    result_list = []
    for x in range (0, len(result)):
            if result[x] == 'b':
                result_list.append(result[x+1])
    return result_list

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
    if parser.found_bold == True:
        return parseBoldStrings(parser.result)
    else:
        return parser.result

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
    if parser.found_bold == True:
        return parseBoldStrings(parser.result)
    else:
        return parser.result


def loadFromFile(filename):
    with open (filename, "r") as f:
        contents = f.read()
        contents.decode("utf-8", "replace") 
        parser = MyHTMLParser()
        parser.feed(contents)
        if parser.found_bold == True:
            return parseBoldStrings(parser.result)
        else:
            return parser.result

if __name__ == "__main__": print(loadFromFile("tmp.log"))