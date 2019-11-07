#!/usr/bin/python3

from datetime import datetime

jour = datetime.now().day

if jour%2==0:
    print("Jour pair");
else:
    print("Jour impair");
