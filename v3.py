#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cookielib
import urllib
import urllib2
class Senddata():
    def __init__(self):
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    def postdata(self, theurl, body):
        try:
            txdata = urllib.urlencode(body)
            req = urllib2.Request(theurl, txdata, self.txheaders)
            handle = self.opener.open(req)
            HTMLSource = handle.read()
            print(HTMLSource)
        except IOError, e:
            print 'We failed to open "%s".' % theurl

    def loadpage(self,url):
        try:
            #page = opener.open('http://forums.kuban.ru/forum/').read()
            handle = self.opener.open(url)
            HTMLSource = handle.read()

           # handle = self.opener.send()

            return HTMLSource
        except IOError, e:
            print 'We failed to open "%s".' % theurl
            return ""


kubanspam= Senddata()

body={'username':'username','password':'password'}
theurl = 'http://forums.kuban.ru/forum/login_new.php'
kubanspam.postdata(theurl,body)

print (kubanspam.loadpage("http://forums.kuban.ru/forum/viewtopic_new.php?t=2979149"))

body={'add_post':'2979149','message':'UP'}
theurl = 'http://forums.kuban.ru/forum/posting_new.php?page=1'
kubanspam.postdata(theurl,body)

##cj = cookielib.CookieJar()
##opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#resp = opener.open('http://forums.kuban.ru/forum/login_new.php') # save a cookie
#
#theurl = 'http://forums.kuban.ru/forum/login_new.php'
## an example url that sets a cookie, try different urls here and see the cookie collection you can make !
#body={'username':'username','password':'password'}
#txdata = urllib.urlencode(body)
## if we were making a POST type request, we could encode a dictionary of values here - using urllib.urlencode
#txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
## fake a user agent, some websites (like google) don't like automated exploration

#
#try:
#    req = urllib2.Request(theurl, txdata, txheaders) # create a request object
#    handle = opener.open(req) # and open it to return a handle on the url
#    HTMLSource = handle.read()
#    f = file('test.html', 'w')
#    f.write(HTMLSource)
#    f.close()
#
#    page = opener.open('http://forums.kuban.ru/forum/').read()
#    f = file('body.html', 'w')
#    f.write(page)
#    f.close()
#    print(page)
#
#
#except IOError, e:
#    print 'We failed to open "%s".' % theurl
#    if hasattr(e, 'code'):
#        print 'We failed with error code - %s.' % e.code
#    elif hasattr(e, 'reason'):
#        print "The error object has the following 'reason' attribute :", e.reason
#        print "This usually means the server doesn't exist, is down, or we don't have an internet connection."
#        sys.exit()
#
#else:
#    print 'Here are the headers of the page :'
#    print handle.info() # handle.read() returns the page, handle.geturl() returns the true url of the page fetched (in case urlopen has followed any redirects, which it sometimes does)
#

## -*- coding: utf-8 -*-
#
#import urllib
##import urllib
#import urllib2
#import cookielib
#import re
#
#
#cj = cookielib.CookieJar()
##opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#
#opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.7) Gecko/20100106 Ubuntu/9.10 (karmic) Firefox/3.5.7'),
#('Referer', 'http://forums.kuban.ru/'), ('Accept-Charset', 'utf-8')]
#
#page = opener.open('http://forums.kuban.ru/').read().decode('cp1251')
#
#
##params = urllib.parse.urlencode({'from_name': 'NAME', 'prefix': 790892, 'phone_number': 12345, 'text_sms': 'Hello, world!', 'imgcc': c, 'cc': cc})
#
##page = opener.open('http://forums.kuban.ru/', params).read().decode('cp1251')
#print(page)

