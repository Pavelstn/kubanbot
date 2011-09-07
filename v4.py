# -*- coding: utf-8 -*-
#import re
import sys
import cookielib
from mechanize import Browser
reload(sys)
sys.setdefaultencoding("utf-8")
root_url = 'http://forums.kuban.ru/forum/viewtopic_new.php?t=2988999'
username = 'username'
password = 'password'
message = u"""Продаем"""
br = Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
home_page = br.open(root_url)
print  br.title()
br.select_form(nr=0)
br["username"] = username
br["password"] = password
br.submit()
br.select_form(nr=0)
br["message"] = message.decode('utf-8').encode('cp1251')
br.submit()