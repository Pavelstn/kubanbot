#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import cookielib
from mechanize import Browser
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class Senddata():
    def __init__(self):
        self.br = Browser()
        cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(cj)
        self.br.set_handle_equiv(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def auth(self,root_url,username,password):
        home_page = self.br.open(root_url)
        #print  self.br.title()
        self.br.select_form(nr=0)
        self.br["username"] = username
        self.br["password"] = password
        self.br.submit()

    def senddata(self,root_url, message):
        self.br.open(root_url)
        self.br.select_form(nr=0)
        self.br["message"] = message.decode('utf-8').encode('cp1251')
        self.br.submit()


root_url = 'http://forums.kuban.ru/forum/viewtopic_new.php?t=2988999'
username = 'username'
password = 'password'
message = u"""Продаем """

kubanspam= Senddata()
kubanspam.auth(root_url, username, password)


kubanspam.senddata("http://forums.kuban.ru/forum/viewtopic_new.php?t=2988999", message)
time.sleep(300) #пауза в 5 минут
kubanspam.senddata("http://forums.kuban.ru/forum/viewtopic_new.php?t=2979181", message)
time.sleep(300) #пауза в 5 минут
kubanspam.senddata("http://forums.kuban.ru/forum/viewtopic_new.php?t=2988999", message)
time.sleep(300) #пауза в 5 минут
kubanspam.senddata("http://forums.kuban.ru/forum/viewtopic_new.php?t=2979149", message)

