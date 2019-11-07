#!/usr/bin/python3

from datetime import datetime

import os

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
        # print(reqtime)
        if ip in adict:
            adict[ip].append(line)
        else:
            adict[ip] = [line]

print(adict["63.143.42.252"])
print(adict["37.252.227.107"])

# 63.143.42.252 - - [29/Oct/2019:06:25:25 +0100] "HEAD /login HTTP/1.1" 200
# 0 "https://riskstarter.arengibox.com/login"
# "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
# 0.422 0.424 .
