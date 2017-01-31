#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
import sys
import requests
import lxml.html
from time import sleep

N = 200

sett = set(line.strip() for line in sys.stdin.readlines())

for i in xrange(3):
    if i:
        sleep(1.1)
    sys.stderr.write('{}ページめをやります ... '.format(i+1))
    sys.stderr.flush()
    url = 'http://community.topcoder.com/tc?cc=392&sc=&sd=&cc=392&module=AlgoRank&nr={}&sr={}'.format(N, i*N+1)
    res = requests.get(url)
    if res.status_code != 200:
        sys.stderr.write('(ΦωΦ)＜not 200\n')
        exit(1)
    res0 = res.content.decode('utf-8')
    doc = lxml.html.fromstring(res0)
    ele = doc.xpath("//table[contains(@class, 'stat')]/tbody/tr/td[2]/a")
    for e in ele:
        sett.add(e.text)
    sys.stderr.write('完了\n')
    sys.stderr.flush()

print '\n'.join(sorted(sett))
