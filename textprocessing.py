#!/usr/bin/python
print "Content-Type: text/plain\n\n"
import urllib


def getpage(url):  #imports a page url and transforms the HTML it into a string to be parsed. 
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    return s

def getnextlink(s):  #gets returns the first link encountered in the parsed page, and the position in the string right after that link.
    startquote = s.find('href=') + 5
    endlink = startquote + 1
    if startquote == 4:
        return "",0
    if s[startquote] == '\'':
        endlink = s.find('\'',startquote+1)
    if s[startquote] == '"':
        endlink = s.find('"',startquote+1)
    return s[startquote+1: endlink], endlink
    
def getalllinks(url):  #returns all links from a url
    s = getpage(url)
    links = []
    while True:
        link,pos = getnextlink(s)
        if pos > 0:
            if link[0:4] == "http":
                links.append(link)
            s = s[pos:]
        else:
            break
    return links

def union(p,q): #unions two arrays
    for e in q:
        if e not in p:
            p.append(e)

			
def crawl_web(seed,maxdepth): #seed is the initial page the crawler starts on, max depth is the distance in pages the crawler can travel before it returns.
    tocrawl = [seed]
    crawled = []
    nextdepth = []
    depth = 0 
    while tocrawl and depth <= maxdepth:
        page = tocrawl.pop()
        if page not in crawled:
            union(nextdepth, getalllinks(page))
            crawled.append(page)
        if not tocrawl:
            tocrawl,nextdepth = nextdepth,[]
            depth = depth + 1
    return crawled

print crawl_web("http://www.cloudonshore.com",2) 