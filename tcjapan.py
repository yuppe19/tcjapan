#!/usr/bin/python
# -*- coding: utf-8 -*-
# †
import sys
import requests
import lxml.html
from time import sleep

N = 200

sett = set(line.strip() for line in sys.stdin.readlines())

for i in xrange(3):
    url = 'http://community.topcoder.com/tc?cc=392&sc=&sd=&cc=392&module=AlgoRank&nr={}&sr={}'.format(N, i*N+1)
    res = requests.get(url)
    if res.status_code != 200:
        print '(ΦωΦ)＜not 200'
    res0 = res.content.decode('utf-8')
    doc = lxml.html.fromstring(res0)
    ele = doc.xpath("//table[contains(@class, 'stat')]/tbody/tr/td[2]/a")
    for e in ele:
        sett.add(e.text)
    sleep(1.1)

print '\n'.join(sorted(sett))
