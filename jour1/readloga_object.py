#!/usr/bin/python3

from datetime import datetime

import os


class Logline():
    def __init__(self, ip, login, passws, date, zone, reqtype,
                 url, httptype, status, size, referer,
                 uagent, timing):
        self.ip = ip
        self.login = login
        self.passws = passws
        self.date = date
        self.zone = zone
        self.reqtype = reqtype
        self.url = url
        self.httptype = httptype
        self.status = status
        self.size = size
        self.referer = referer
        self.uagent = uagent
        self.timing = timing


adict = {}
apath = os.path.expanduser("~/a.log")
print("chemin etendu en", apath)
with open(apath) as fd:
    for line in fd:
        ip, login, passws, date, zone, reqtype, \
        url, httptype, status, size, referer, \
        uagenttrash = line.split(None, 11)
        # print(ip)
        datetime_object = datetime.strptime(date[1:],
                                            '%d/%b/%Y:%H:%M:%S')
        # print(datetime_object)
        uagent = uagenttrash.split('"')[1]
        timing = uagenttrash.split('"')[2]
        # print(uagent)
        # print(timing.split())
        reqtime = timing.split()[0]
        alogline = Logline(ip, login, passws, datetime_object, zone, reqtype,
                 url, httptype, status, size, referer,
                 uagent, timing)
        # print(reqtime)
        if ip in adict:
            adict[ip].append(alogline)
        else:
            adict[ip] = [alogline]

# print(adict["63.143.42.252"])
print(adict["63.143.42.252"][0].uagent)
print(adict["63.143.42.252"][0].date)
print(adict["63.143.42.252"][0].ip)
print("nombre de ligne de log de cette ip", len(adict["63.143.42.252"]))
# print(adict["37.252.227.107"])

# 63.143.42.252 - - [29/Oct/2019:06:25:25 +0100] "HEAD /login HTTP/1.1" 200
# 0 "https://riskstarter.arengibox.com/login"
# "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
# 0.422 0.424 .
